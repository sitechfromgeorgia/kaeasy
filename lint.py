"""Deterministic Georgian (ka) linter. No network, no LLM.

Ported from the fleet's ge_ka_lint.py (SiTech Hub, shared-knowledge/scripts/georgian-style/), without the
sitech.ge database modes. Every rule here must stay low-noise: a rule that fires on correct Georgian is worse
than no rule. The skills cover what a regex cannot (case government, verb agreement, word order).

Usage:
    python lint.py --text "ტექსტი" [--mode article|social|ui|speech] [--strict] [--json]
    python lint.py --file draft.md --summary
Exit code: 0 clean, 1 findings.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

MODES = ("article", "social", "ui", "speech")

# 1. Brands and acronyms written in Georgian letters (forbidden in written text, expected in speech text).
#    Word-start anchored so „მეტად" is not Meta and „გუბერნატორმა" is not Uber.
CASE_ENDINGS = r"(?:მ|მა|ის|ს|ით|ზე|ში|თვის|სა|ისა|ად)?"
TRANSLIT = {
    "ფბი": "FBI", "სიაიეი": "CIA", "ენესეი": "NSA", "ნასა": "NASA",
    "მეტა": "Meta", "გუგლ": "Google", "ამაზონ": "Amazon", "მაიკროსოფტ": "Microsoft",
    "ენვიდია": "NVIDIA", "ნვიდია": "NVIDIA", "ინტელი": "Intel", "ეიმდი": "AMD",
    "სამსუნგ": "Samsung", "ეპლი": "Apple", "ტესლა": "Tesla", "სპეისექსი": "SpaceX",
    "ოპენაი": "OpenAI", "ანთროპიკ": "Anthropic", "ჩატჯიპიტ": "ChatGPT",
    "ჯემინაი": "Gemini", "ვინდოუს": "Windows", "ლინუქს": "Linux",
    "ანდროიდ": "Android", "ნეტფლიქს": "Netflix", "იუთუბ": "YouTube",
    "ფეისბუქ": "Facebook", "ინსტაგრამ": "Instagram", "ტვიტერ": "Twitter",
    "ტიკტოკ": "TikTok", "სპოტიფაი": "Spotify", "უბერ": "Uber", "ფაიზერ": "Pfizer",
    "კლაუდფლერ": "Cloudflare", "გითჰაბ": "GitHub", "სტრაიპ": "Stripe",
}
TRANSLIT_RE = {
    ka: re.compile(r"(?<![ა-ჰ])" + re.escape(ka) + CASE_ENDINGS + r"(?![ა-ჰ])", re.IGNORECASE) for ka in TRANSLIT
}

# 2. Calques from English (word-for-word translation) → natural Georgian.
CALQUES = {
    r"\bმიიღოს ადგილი\b": "მოხდეს / შედგეს",
    r"\bადგილი მიიღო\b": "მოხდა / შედგა / გაიმართა",
    r"\bთამაშობს როლს\b": "მნიშვნელოვანია / როლს ასრულებს",
    r"\bგააკეთა გადაწყვეტილება\b": "მიიღო გადაწყვეტილება / გადაწყვიტა",
    r"\bიქნა (გაკეთებული|მიღებული|აღნიშნული|დადასტურებული|გამოყენებული|გამოქვეყნებული)\b":
        "აქტიური ფორმა: გაკეთდა / მიიღეს / აღნიშნა",
    r"\bარის საჭიროება\b": "საჭიროა",
    r"\bარსებობს საჭიროება\b": "საჭიროა",
    r"\bამ მომენტში\b": "ამჟამად / ახლა",
    r"\bდიდი რაოდენობით\b": "ბევრი",
    r"\bმიდის წინ\b": "შემდგომში",
    r"\bშედეგად იმისა, რომ\b": "იმის გამო, რომ",
    r"\bეს არის ის, რაც\b": "სწორედ ეს არის",
    r"\bყურადღების ქვეშ\b": "ყურადღების ცენტრში",
    r"\bმიმართულია იმისკენ, რომ\b": "მიზნად ისახავს",
    r"\bმიზნად ისახავს იმას, რომ\b": "მიზნად ისახავს",
    r"\bთამაშის შემცვლელი\b": "game changer: გარდამტეხი / რადიკალურად ცვლის",
}

AI_FILLER = {
    r"\bმნიშვნელოვანია აღინიშნოს,? რომ\b": "დაიწყე პირდაპირ ფაქტით",
    r"\bაღსანიშნავია,? რომ\b": "დაიწყე პირდაპირ ფაქტით",
    r"\bთანამედროვე სამყაროში\b": "ამოიღე ცარიელი შესავალი",
    r"\bროგორც ცნობილია\b": "მიუთითე წყარო ან ამოიღე",
    r"\bამ კონტექსტში\b": "ამოიღე, თუ ახალს არაფერს ამატებს",
}

# 3. Countries and cities must be written in Georgian.
COUNTRIES_LATIN = [
    "Germany", "France", "China", "Japan", "India", "Brazil", "Turkey", "Italy",
    "Spain", "Poland", "Netherlands", "Sweden", "Norway", "Finland", "Denmark",
    "Portugal", "Greece", "Egypt", "Israel", "Canada", "Mexico", "Australia",
    "Tokyo", "Paris", "Berlin", "London", "Beijing", "Shanghai", "Seoul", "Moscow",
]

# 4. Numeral + plural noun (Georgian uses the singular after a numeral).
PLURAL_AFTER_NUM = re.compile(
    r"\b\d[\d\s,.]*\s+(?:სტატიები|კომპანიები|მომხმარებლები|ადამიანები|წლები|დოლარები|"
    r"პროცენტები|მილიონები|მილიარდები|ექსპერტები|მკვლევრები|დეველოპერები|აპლიკაციები|"
    r"მოდელები|სერვერები|პროცესორები|აგენტები|ქვეყნები|თანამშრომლები|დღეები|საათები|წუთები)\b"
)
PLURAL_AFTER_WORD_NUM = re.compile(
    r"(?<![ა-ჰ])(?:ორი|სამი|ოთხი|ხუთი|ექვსი|შვიდი|რვა|ცხრა|ათი|ასი|ათასი|რამდენიმე|ბევრი|ყველა)\s+"
    r"(?:კომპანიები|მომხმარებლები|ადამიანები|წლები|ექსპერტები|მკვლევრები|აგენტები|ქვეყნები|მოდელები)"
    r"(?![ა-ჰ])"
)

CYRILLIC = re.compile(r"[а-яА-ЯёЁіІїЇєЄғҒқҚүҮұҰөӨһҺәӘ]")

POSTPOSITION_DATIVE = re.compile(
    r"(?<![A-Za-z0-9-])\b(ამას|იმას|რას|[ა-ჰ]{2,}ებს)\s+(შესახებ|გამო|მიხედვით)\b"
)

# Case endings of Latin names by their final sound (data/latin_endings.json, latin-names.md): a vowel sound takes
# -მ in the ergative (OpenAI-მ, Meta-მ), a consonant -მა (Microsoft-მა). Only names listed there are checked.
LATIN_CLASS: dict[str, str] = json.loads(
    (Path(__file__).resolve().parent / "data" / "latin_endings.json").read_text(encoding="utf-8"))["names"]
LATIN_NAME_ENDING = re.compile(
    r"(?<![A-Za-z0-9.\-])(" + "|".join(re.escape(n) for n in sorted(LATIN_CLASS, key=len, reverse=True))
    + r")-(მა|მ|ის|ით|თი)(?![ა-ჰ])")
# (sound class group, written ending) → right ending. Ergative mistakes are strict; the rest are advisories.
LATIN_ERGATIVE = {("consonant", "მ"): "მა", ("vowel", "მა"): "მ"}
LATIN_OTHER = {("consonant", "თი"): "ით", ("vowel", "ის"): "ს", ("i-sound", "თი"): "ით", ("a", "ით"): "თი",
               ("o-u", "ით"): "თი", ("e", "ით"): "თი"}

# Mechanical, near-zero false positives. A publish gate should block on these only.
STRICT = {"translit", "ending_hyphen", "quotes", "decimal", "ellipsis", "percent", "number_plural",
          "cyrillic", "space_punct", "double_space", "title_period", "dash", "latin_in_speech", "russian_letter",
          "postposition_dative", "latin_ergative", "numeral_compound", "legal_citation", "date_ordinal",
          "wrong_name", "negation", "wrong_form"}

COMPANIES_PATH =Path(__file__).resolve().parent / "data" / "glossary" / "georgia-companies.json"
# `wrong` lists spellings that are never right (ტიბისი, ტელასი). `avoid` is advice for the writer and stays out of
# the strict gate: it holds shortened forms and bare surnames that are correct when they name something else.
COMPANY_WRONG: dict[str, str] = {}
if COMPANIES_PATH.exists():
    for _entry in json.loads(COMPANIES_PATH.read_text(encoding="utf-8")):
        for _w in _entry.get("wrong", []):
            COMPANY_WRONG[_w] = _entry["preferred"]


def _name_pattern(wrong: str) -> str:
    """ტელასი → also ტელასმა, ტელასის; ტიბისი → also ტიბისიმ, ტიბისის."""
    tail = r"(?:მ|მა|ის|ს|ით|თ|ზე|ში|თან|ად|დ|ამდე|მდე|იდან|დან|თვის|სთვის|ისთვის)"
    forms = re.escape(wrong) + tail + "?"
    if wrong.endswith("ი"):
        forms += "|" + re.escape(wrong[:-1]) + tail
    return r"(?<![ა-ჰA-Za-z0-9])(?:" + forms + r")(?![ა-ჰA-Za-z0-9])"


COMPANY_WRONG_PATTERNS = [(re.compile(_name_pattern(w)), pref) for w, pref in
                          sorted(COMPANY_WRONG.items(), key=lambda x: len(x[0]), reverse=True)]

FORMS_PATH = Path(__file__).resolve().parent / "data" / "wrong_forms.json"
_FORMS = json.loads(FORMS_PATH.read_text(encoding="utf-8")) if FORMS_PATH.exists() else {}
WRONG_FORMS: dict[str, str] = _FORMS.get("error", {})  # never correct: strict
DATED_FORMS: dict[str, str] = _FORMS.get("warn", {})  # old or literary: advice only


def _forms_re(table: dict[str, str]) -> re.Pattern:
    """Whole words only. A space in an entry matches any run of spaces."""
    alts = sorted(table, key=len, reverse=True)
    forms = "|".join(re.escape(w).replace(r"\ ", r"\s+") for w in alts)
    return re.compile(rf"(?<![ა-ჰA-Za-z0-9-])(?:{forms})(?![ა-ჰA-Za-z0-9])")


WRONG_FORMS_RE = _forms_re(WRONG_FORMS)
DATED_FORMS_RE = _forms_re(DATED_FORMS)
QUOTED = re.compile(r"„[^“\n]*“")

# A month in any case form, the same forms as speech.MONTHS (a test keeps them equal). Whole forms, not prefixes:
# „მეორე მარტივი გზა“ and „მეორე მაისური“ are not dates.
MONTH_FORM = (r"(?:(?:იანვარ|თებერვალ|სექტემბერ|ოქტომბერ|ნოემბერ|დეკემბერ)(?:ი|ია|ს|ში|ზე)"
              r"|(?:იანვრ|თებერვლ|სექტემბრ|ოქტომბრ|ნოემბრ|დეკემბრ)(?:ის|ით|ად|ამდე|იდან|ისთვის)"
              r"|(?:მარტ|აპრილ|მაის|ივნის|ივლის)(?:ი|ია|ს|ის|ით|ად|ში|ზე|ამდე|იდან|ისთვის)"
              r"|აგვისტო(?:ა|ს|თი|დ|ში|ზე|მდე|დან|სთვის)?)")
MONTH_DAY = r"(?:[2-9]|[12]\d|3[01])"  # day 1 is ordinal („1-ლი ნოემბერი“), a year is not a day

ORDINAL_DATE_RE = re.compile(
    r"(?<![ა-ჰ0-9])(?<!ზედიზედ\s)"
    rf"(?:{MONTH_DAY}-ე|მე-{MONTH_DAY}(?:-ე)?|"
    r"მეორე|მესამე|მეოთხე|მეხუთე|მეექვსე|მეშვიდე|მერვე|მეცხრე|მეათე|"
    r"მეთერთმეტე|მეთორმეტე|მეცამეტე|მეთოთხმეტე|მეთხუთმეტე|მეთექვსმეტე|მეჩვიდმეტე|მეთვრამეტე|მეცხრამეტე|მეოცე|"
    r"ოცდამე\w+)"
    rf"\s+{MONTH_FORM}(?![ა-ჰ])"
)

# Rules that do not apply to a mode. Speech text is read aloud: brands are spelled in Georgian letters there.
MODE_SKIP = {
    "speech": {"translit", "ending_hyphen", "country"},
    "ui": {"title_period"},
}


@dataclass
class Finding:
    check: str
    severity: str  # error | warn
    message: str
    snippet: str
    start: int
    end: int

    def as_dict(self) -> dict:
        return asdict(self)


# Spans that are not prose: code (fenced, inline, <pre>/<code>) and HTML tags. Their content is never linted.
NOT_PROSE = re.compile(r"```.*?```|`[^`\n]*`|<(pre|code)\b[^>]*>.*?</\1>|<[^>]+>", re.DOTALL | re.IGNORECASE)


def strip_html(s: str) -> str:
    # Same length as the input so offsets stay valid: every masked character becomes a space (newlines stay).
    return NOT_PROSE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), s or "")


def _ctx(text: str, start: int, end: int, pad: int = 45) -> str:
    a, b = max(0, start - pad), min(len(text), end + pad)
    return ("…" if a else "") + text[a:b].replace("\n", "⏎") + ("…" if b < len(text) else "")


def check_text(text: str, mode: str = "article", title: str | None = None,
               strict: bool = False) -> list[Finding]:
    if mode not in MODES:
        raise ValueError(f"mode must be one of {MODES}")
    skip = MODE_SKIP.get(mode, set())
    body = strip_html(text)
    # Positions that were HTML tags or code: blanked to keep offsets, so whitespace rules must ignore them.
    in_tag = [False] * len(body)
    for t in NOT_PROSE.finditer(text or ""):
        in_tag[t.start():t.end()] = [True] * (t.end() - t.start())
    out: list[Finding] = []

    def on(check: str) -> bool:
        return check not in skip and (not strict or check in STRICT)

    def near_tag(m: re.Match) -> bool:
        return any(in_tag[max(0, m.start() - 1):m.end() + 1])

    def add(check: str, severity: str, message: str, m: re.Match) -> None:
        out.append(Finding(check, severity, message, _ctx(body, m.start(), m.end()), m.start(), m.end()))

    if on("translit"):
        for ka, rx in TRANSLIT_RE.items():
            for m in rx.finditer(body):
                add("translit", "error", f"„{m.group(0)}“ → {TRANSLIT[ka]} (ბრენდი ლათინურად)", m)

    if on("ending_hyphen"):
        # Latin word + Georgian case ending without a hyphen: Metaის, Amazonმა.
        for m in re.finditer(r"\b[A-Za-z][A-Za-z0-9.]*[ა-ჰ]{1,}", body):
            tok = m.group(0)
            if re.search(r"(მა|ის|ს|ით|ზე|ში|მ|თვის|ები|ად|დან|მდე)$", tok):
                fixed = re.sub(r"([A-Za-z0-9.])([ა-ჰ]+)$", r"\1-\2", tok)
                add("ending_hyphen", "error", f"„{tok}“ → „{fixed}“ (დეფისი სავალდებულოა)", m)
        for m in re.finditer(r"\b[A-Za-z][A-Za-z0-9.]*(?:\s+-\s*|-\s+)(მა|ის|ს|ით|ზე|ში)\b", body):
            add("ending_hyphen", "error", f"„{m.group(0)}“ → დეფისი გამოტოვების გარეშე", m)
        for m in re.finditer(r"\b([A-Za-z][A-Za-z0-9.]*)\s+(მა|მ|ს|ით|თი|ზე|ში|დან|მდე|ად|ები|ების|ებს|ებმა|ებით|ებად)\b", body):
            if not any(in_tag[m.start():m.end()]):
                add("ending_hyphen", "error", f"„{m.group(0)}“ → „{m.group(1)}-{m.group(2)}“ (დეფისი სავალდებულოა)", m)

    if on("quotes"):
        for m in re.finditer(r'"[^"\n]{2,80}"', body):
            add("quotes", "error", "ინგლისური ბრჭყალები → „…“", m)

    if on("ellipsis"):
        for m in re.finditer(r"\.\.\.", body):
            add("ellipsis", "warn", "„...“ → „…“", m)

    if on("dash"):
        # Edo's standing rule (2026-09-25): no em dash or en dash anywhere.
        for m in re.finditer(r"[—–]", body):
            add("dash", "error", "ტირე (— –) აკრძალულია: მძიმე, ორწერტილი ან დეფისი", m)

    if on("calque"):
        for pat, fix in CALQUES.items():
            for m in re.finditer(pat, body, re.IGNORECASE):
                add("calque", "error", f"კალკი: „{m.group(0)}“ → {fix}", m)

    if on("ai_filler"):
        for pat, fix in AI_FILLER.items():
            for m in re.finditer(pat, body, re.IGNORECASE):
                add("ai_filler", "error", f"ცარიელი AI ფრაზა: „{m.group(0)}“ → {fix}", m)

    if on("number_plural"):
        for rx in (PLURAL_AFTER_NUM, PLURAL_AFTER_WORD_NUM):
            for m in rx.finditer(body):
                pre = body[max(0, m.start() - 6):m.start() + 1]
                if re.search(r"\d\s*-\s*\d*$", pre):  # range such as 2020-2024
                    continue
                add("number_plural", "error", f"რიცხვის შემდეგ მხოლობითი: „{m.group(0)}“", m)

    if on("numeral_compound"):
        # Garbled year compounds such as „ოცდაოცდ ორი“ (2022) or „ოცდაოცის“ (2020): always an error.
        for m in re.finditer(r"ოცდაოც", body):
            add("numeral_compound", "error", "არასწორი რიცხვითი შენაერთი: „ოცდაოც...“ → „ორი ათას ოც...“", m)

    if on("date_ordinal"):
        # Dates take the cardinal day: „ორ ოქტომბერს“, not „მეორე ოქტომბერს“. Day 1 is ordinal: „პირველი“.
        for m in ORDINAL_DATE_RE.finditer(body):
            if any(in_tag[m.start():m.end()]):
                continue
            add("date_ordinal", "error", f"თარიღის დღე რიცხვითია, არა რიგითი: „{m.group(0)}“ → „ორ/სამ/... {m.group(0).split()[-1]}“", m)

    if on("legal_citation"):
        # Article number and its part must never collapse into "NNN პირველი მუხლი".
        # Prime articles (353¹) are a different offence from the base article (353).
        for pat in (r"\b\d+(?:-ე)?\s+პირველ[ი]?\s+მუხლ", r"\b\d+(?:-ე)?\s+მუხლის\s+პირველ[ი]?\s+მუხლ"):
            for m in re.finditer(pat, body):
                add("legal_citation", "error", f"მუხლი და ნაწილი აერია: „{m.group(0)}“ → „NNN-ე მუხლის პირველი ნაწილი“ (პრიმა მუხლი ცალკეა: „NNN-ე პრიმა მუხლის პირველი ნაწილი“)", m)

    if on("percent"):
        for m in re.finditer(r"\b\d+(?:[.,]\d+)?\s+%", body):
            add("percent", "error", f"„{m.group(0)}“ → {m.group(0).replace(' ', '')}", m)

    if on("decimal"):
        for m in re.finditer(r"\b\d+\.\d+\s*(?:მილიარდ|მილიონ|ათას|%)", body):
            add("decimal", "error", f"ათწილადი მძიმით: „{m.group(0).strip()}“", m)

    if on("space_punct"):
        for m in re.finditer(r"[ა-ჰ]\s+[,.;:!?](?=\s|$)", body):
            if not near_tag(m):
                add("space_punct", "error", "პუნქტუაციის წინ გამოტოვება", m)

    if on("double_space"):
        for m in re.finditer(r"(?<=\S)  +(?=\S)", body):
            if not near_tag(m):
                add("double_space", "warn", "ორმაგი გამოტოვება", m)

    if on("country"):
        for c in COUNTRIES_LATIN:
            for m in re.finditer(r"\b" + re.escape(c) + r"(?:-?[ა-ჰ]+)?\b", body):
                before = body[max(0, m.start() - 30):m.start()]
                if re.search(r"[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\s+$", before):  # part of an English name
                    continue
                add("country", "error", f"„{m.group(0)}“: ქვეყანა და ქალაქი ქართულად იწერება", m)

    if on("cyrillic"):
        for m in CYRILLIC.finditer(body):
            add("cyrillic", "error", "კირილიცას ასო ქართულ ტექსტში", m)

    if on("dup_word"):
        for m in re.finditer(r"(?<![ა-ჰ])([ა-ჰ]{2,})[ \t]+\1(?![ა-ჰ])", body, re.IGNORECASE):
            add("dup_word", "error", f"გამეორებული სიტყვა: „{m.group(0)}“", m)

    if on("no_space_after"):
        for m in re.finditer(r"([,;:!?.])([^\s\d)\"'»“”\-–—])", body):
            p, nxt = m.group(1), m.group(2)
            prev = body[m.start() - 1] if m.start() > 0 else ""
            if p == "." and prev.isalnum() and nxt.isalnum():  # domain, version, file name
                continue
            if p == "." and (prev == "" or prev.isspace()):
                continue
            if p in "?!" and nxt in "?!":
                continue
            if nxt in "”«»„“*_`":
                continue
            add("no_space_after", "error", f"„{p}{nxt}“: პუნქტუაციის შემდეგ გამოტოვება აკლია", m)

    if mode == "speech" and on("latin_in_speech"):
        for m in re.finditer(r"[A-Za-z]{2,}", body):
            add("latin_in_speech", "error", f"„{m.group(0)}“: ხმის ტექსტში მხოლოდ ქართული ასოები", m)
        for m in re.finditer(r"\d+", body):
            add("latin_in_speech", "error", f"„{m.group(0)}“: ხმის ტექსტში რიცხვი სიტყვებით", m)

    if mode == "speech" and on("russian_letter"):
        # Established forms, not Russian letter names for Latin ones: BMW, შპს, PSP, ტვ.
        allowed = [range(a.start(), a.end()) for a in re.finditer(r"ბე[\s-]+ემ[\s-]+ვე|შე[\s-]+პე[\s-]+ეს|პე[\s-]+ეს[\s-]+პე|ტე[\s-]+ვე", body)]
        for m in re.finditer(r"(?<![ა-ჰ])(ტე|პე|ბე)(?![ა-ჰ])", body):
            if any(m.start() in r for r in allowed):
                continue
            add("russian_letter", "error", f"„{m.group(0)}“: რუსული ასოს სახელი (გამოიყენე ტი, პი, ბი)", m)

    if on("postposition_dative"):
        for m in POSTPOSITION_DATIVE.finditer(body):
            if any(in_tag[m.start():m.end()]):
                continue
            word, postp = m.group(1), m.group(2)
            if word == "ამას":
                fix_word = "ამის"
            elif word == "იმას":
                fix_word = "იმის"
            elif word == "რას":
                fix_word = "რის"
            else:
                fix_word = re.sub(r"ებს$", "ების", word)
            add("postposition_dative", "error", f"„{m.group(0)}“ → „{fix_word} {postp}“ (თანდებული მოითხოვს ნათესაობით ბრუნვას)", m)

    if on("latin_ergative") or on("latin_case"):
        for m in LATIN_NAME_ENDING.finditer(body):
            if any(in_tag[m.start():m.end()]):
                continue
            name, suf = m.group(1), m.group(2)
            cls = LATIN_CLASS[name]
            group = "consonant" if cls == "consonant" else "vowel"
            right = LATIN_ERGATIVE.get((group, suf))
            if right and on("latin_ergative"):
                add("latin_ergative", "error", f"„{m.group(0)}“ → „{name}-{right}“ (მოთხრობითი ბოლო ბგერით: "
                    f"ხმოვანზე -მ, თანხმოვანზე -მა)", m)
                continue
            right = LATIN_OTHER.get((cls, suf)) or LATIN_OTHER.get((group, suf))
            if right and on("latin_case"):
                add("latin_case", "warn", f"„{m.group(0)}“ → „{name}-{right}“ (latin-names.md)", m)

    if on("wrong_name"):
        for rx, pref in COMPANY_WRONG_PATTERNS:
            for m in rx.finditer(body):
                if any(in_tag[m.start():m.end()]):
                    continue
                add("wrong_name", "error", f"არასწორი კომპანიის/ორგანიზაციის სახელი: „{m.group(0)}“ → „{pref}“", m)

    if on("negation"):
        for m in re.finditer(r"(?<![ა-ჰ])(ვერცერთ[ა-ჰ]*|არცერთ[ა-ჰ]*)([^,.;:!?\n\r]*?(?<![ა-ჰ])(არ|ვერ)(?![ა-ჰ]))", body):
            if any(in_tag[m.start():m.end()]):
                continue
            add("negation", "error", "ვერცერთი/არცერთი თავად უარყოფითია, ზმნას არ არ სჭირდება", m)

    if on("negation_split") or on("split_negation"):
        for m in re.finditer(r"(?<![ა-ჰ])(ვერც|არც)\s+ერთი(?![ა-ჰ])", body):
            if any(in_tag[m.start():m.end()]):
                continue
            after = body[m.end():m.end() + 30]
            # Exception: when ერთი is a numeral (e.g. contrasted with another number: არც ერთი და არც ორი)
            if re.match(r"^\s+(?:და|ან|თუ)\s+(?:(?:არც|ვერც)\s+)?(?:ორი|სამი|ოთხი)", after):
                continue
            add("negation_split", "warn", f"„{m.group(0)}“ → „{m.group(1)}ერთი“ (ერთად წერა)", m)

    if on("wrong_form") or on("dated_form"):
        # A quotation may keep an old form on purpose.
        quoted = [q.span() for q in QUOTED.finditer(body)]

        def forms(check: str, severity: str, rx: re.Pattern, table: dict[str, str], label: str) -> None:
            for m in rx.finditer(body):
                if any(in_tag[m.start():m.end()]) or any(a <= m.start() < b for a, b in quoted):
                    continue
                add(check, severity, f"{label}: „{m.group(0)}“ → „{table[' '.join(m.group(0).split())]}“", m)

        if on("wrong_form"):
            forms("wrong_form", "error", WRONG_FORMS_RE, WRONG_FORMS, "არასწორი ფორმა")
        if on("dated_form"):
            forms("dated_form", "warn", DATED_FORMS_RE, DATED_FORMS, "უმჯობესი ფორმა")

    if title is not None and on("title_period") and re.search(r"[.!]\s*$", title.strip()):
        t = title.strip()
        out.append(Finding("title_period", "warn", "სათაური წერტილით არ მთავრდება", t[:90], 0, len(t)))

    out.sort(key=lambda f: f.start)
    return out


def check_json(data, fields: dict[str, str], strict: bool = False) -> list[Finding]:
    """Lint every Georgian string in a JSON document in the mode its key maps to (a video script has "say" for
    the voice next to on-screen text). fields: {key: mode or "skip"}, "*" is the default (article if missing).
    Each finding's snippet starts with the JSON path; offsets are within that string."""
    out: list[Finding] = []

    def walk(x, path: str, key: str) -> None:
        if isinstance(x, dict):
            for k, v in x.items():
                walk(v, f"{path}.{k}", k)
        elif isinstance(x, list):
            for i, v in enumerate(x):
                walk(v, f"{path}[{i}]", key)
        elif isinstance(x, str) and re.search(r"[ა-ჰ]", x):
            mode = fields.get(key, fields.get("*", "article"))
            if mode == "skip":
                return
            for f in check_text(x, mode=mode, strict=strict):
                f.snippet = f"{path}: {f.snippet}"
                out.append(f)

    walk(data, "$", "")
    return out


def summary(findings: list[Finding]) -> str:
    if not findings:
        return "სუფთაა (0)"
    counts: dict[str, int] = {}
    for f in findings:
        counts[f.check] = counts.get(f.check, 0) + 1
    return f"{len(findings)} შენიშვნა: " + ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))


def _load_file(path: str) -> str:
    with open(path, encoding="utf-8") as fh:
        raw = fh.read()
    if path.endswith(".json"):
        try:
            data = json.loads(raw)
        except json.JSONDecodeError:
            return raw
        parts: list[str] = []

        def walk(x):
            if isinstance(x, str):
                parts.append(x)
            elif isinstance(x, dict):
                for v in x.values():
                    walk(v)
            elif isinstance(x, list):
                for v in x:
                    walk(v)

        walk(data)
        return "\n".join(parts)
    return raw


def main(argv: list[str] | None = None) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        # Windows console encoding safeguard
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    ap = argparse.ArgumentParser(description="Georgian (ka) linter")
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--text")
    src.add_argument("--file")
    ap.add_argument("--title")
    ap.add_argument("--mode", default="article", choices=MODES)
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--summary", action="store_true")
    a = ap.parse_args(argv)
    text = a.text if a.text is not None else _load_file(a.file)
    findings = check_text(text, mode=a.mode, title=a.title, strict=a.strict)
    if a.json:
        print(json.dumps([f.as_dict() for f in findings], ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"[{f.severity}] {f.check}: {f.message}\n    {f.snippet}")
        if a.summary or not findings:
            print(summary(findings))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
