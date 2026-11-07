"""Georgian text → what a TTS voice should read (ka_speech). Ported from SiTech Shorts' normalize_ka.py.

Base-20 cardinals with the case on the noun (36%-ის → ოცდათექვსმეტი პროცენტის), a numeral before a dative or
postpositional noun loses its final ი (2012 წელს → ორი ათას თორმეტ წელს), ordinals მე-…-ე, versions
(Opus 4.7 → ოთხი წერტილი შვიდი), currencies and units. Latin names come from data/lexicon_ka.json (approved), then
the caller's own "say" map, then names learned earlier (lexicon_learned.json in the Kaeasy data dir); letter
acronyms are spelled (GPU → ჯი პი იუ). Screen text keeps the Latin name; only the voice gets Georgian letters.

This file is the source. SiTech Shorts vendors it unchanged as shorts/normalize_ka.py, with lexicon_ka.json and
latin_endings.json next to it (Shorts: tools/sync_kaeasy.py). Change it here, never in the copy.
"""
import json
import os
import pathlib
import re

SMALL = ("ნული", "ერთი", "ორი", "სამი", "ოთხი", "ხუთი", "ექვსი", "შვიდი", "რვა", "ცხრა", "ათი", "თერთმეტი",
         "თორმეტი", "ცამეტი", "თოთხმეტი", "თხუთმეტი", "თექვსმეტი", "ჩვიდმეტი", "თვრამეტი", "ცხრამეტი")
TWENTIES = {1: "ოცი", 2: "ორმოცი", 3: "სამოცი", 4: "ოთხმოცი"}
SCALES = ((1_000_000_000_000, "ტრილიონ"), (1_000_000_000, "მილიარდ"), (1_000_000, "მილიონ"), (1_000, "ათას"))
ORDINAL_SMALL = {1: "პირველი", 2: "მეორე", 3: "მესამე", 4: "მეოთხე", 5: "მეხუთე", 6: "მეექვსე", 7: "მეშვიდე",
                 8: "მერვე", 9: "მეცხრე", 10: "მეათე"}
DENOMINATORS = {1: "მეათედი", 2: "მეასედი", 3: "მეათასედი"}
LETTERS = {"A": "ეი", "B": "ბი", "C": "სი", "D": "დი", "E": "ი", "F": "ეფ", "G": "ჯი", "H": "ეიჩ", "I": "აი",
           "J": "ჯეი", "K": "ქეი", "L": "ელ", "M": "ემ", "N": "ენ", "O": "ოუ", "P": "პი", "Q": "ქიუ", "R": "არ",
           "S": "ეს", "T": "ტი", "U": "იუ", "V": "ვი", "W": "დაბლიუ", "X": "ექს", "Y": "უაი", "Z": "ზედ"}
HERE = pathlib.Path(__file__).resolve().parent
# Kaeasy keeps the JSON in data/; the vendored copy in SiTech Shorts keeps it next to this file.
DATA = HERE / "data" if (HERE / "data" / "lexicon_ka.json").exists() else HERE
WORDS = json.loads((DATA / "lexicon_ka.json").read_text(encoding="utf-8"))["words"]  # approved spoken forms
# Sound class of a Latin name's ending (latin-names.md). "i-sound" names keep their ი before an ending: სონიმ, სონის.
SOUND = json.loads((DATA / "latin_endings.json").read_text(encoding="utf-8"))["names"]
VOWELS = "აეიოუ"
CURRENCY = {"$": "დოლარ", "€": "ევრო", "₾": "ლარ", "£": "ფუნტ"}
UNITS = {"GB": "გიგაბაიტ", "TB": "ტერაბაიტ", "MB": "მეგაბაიტ", "GHz": "გიგაჰერც", "km": "კილომეტრ", "W": "ვატ",
         "nm": "ნანომეტრ"}
# Symbols and Georgian unit abbreviations written as their own word after a number (Kaeasy addition): 10 ₾, 5 კმ.
UNIT_WORDS = {"₾": "ლარი", "$": "დოლარი", "€": "ევრო", "£": "ფუნტი", "კმ/სთ": "კილომეტრი საათში",
              "მბ/წმ": "მეგაბაიტი წამში", "კმ": "კილომეტრი", "მ": "მეტრი", "სმ": "სანტიმეტრი", "მმ": "მილიმეტრი",
              "კგ": "კილოგრამი", "გ": "გრამი", "ლ": "ლიტრი", "მბ": "მეგაბაიტი", "გბ": "გიგაბაიტი", "ტბ": "ტერაბაიტი",
              "ჰც": "ჰერცი", "ვ": "ვოლტი", "°C": "გრადუსი", "°": "გრადუსი"}
UNIT_RE = re.compile("(?P<u>" + "|".join(re.escape(u) for u in sorted(UNIT_WORDS, key=len, reverse=True))
                     + r")(?:-(?P<suf>[ა-ჿ]+))?")
# A month in any case form. Whole forms, not prefixes: მარტივი and მაისური are not months.
MONTHS = re.compile(
    r"^(?:(?:იანვარ|თებერვალ|სექტემბერ|ოქტომბერ|ნოემბერ|დეკემბერ)(?:ი|ია|ს|ში|ზე)"
    r"|(?:იანვრ|თებერვლ|სექტემბრ|ოქტომბრ|ნოემბრ|დეკემბრ)(?:ის|ით|ად|ამდე|იდან|ისთვის)"
    r"|(?:მარტ|აპრილ|მაის|ივნის|ივლის)(?:ი|ია|ს|ის|ით|ად|ში|ზე|ამდე|იდან|ისთვის)"
    r"|აგვისტო(?:ა|ს|თი|დ|ში|ზე|მდე|დან|სთვის)?)$")
# Counted nouns that take the -მდე of a range (10-15 წუთი → ათიდან თხუთმეტ წუთამდე), as nominative → -მდე form.
RANGE_NOUNS = {"წამი": "წამამდე", "წუთი": "წუთამდე", "საათი": "საათამდე", "დღე": "დღემდე", "კვირა": "კვირამდე",
               "თვე": "თვემდე", "წელი": "წლამდე", "წლებში": "წლამდე", "პროცენტი": "პროცენტამდე", "ლარი": "ლარამდე",
               "დოლარი": "დოლარამდე", "ევრო": "ევრომდე", "ადამიანი": "ადამიანამდე", "კილომეტრი": "კილომეტრამდე",
               "მეტრი": "მეტრამდე", "კილოგრამი": "კილოგრამამდე", "ცალი": "ცალამდე"}

GEO = re.compile(r"[ა-ჿ]")


def cardinal(n):
    """Nominative cardinal, 0..999 trillion."""
    if n < 20:
        return SMALL[n]
    if n < 100:
        q, r = divmod(n, 20)
        return TWENTIES[q] if r == 0 else TWENTIES[q][:-1] + "და" + SMALL[r]
    if n < 1000:
        q, r = divmod(n, 100)
        stem = ("" if q == 1 else _drop_i(SMALL[q])) + "ას"
        return stem + "ი" if r == 0 else stem + " " + cardinal(r)
    for scale, stem in SCALES:
        if n >= scale:
            q, r = divmod(n, scale)
            head = ("" if scale == 1000 and q == 1 else cardinal(q) + " ") + stem
            return head + "ი" if r == 0 else head + " " + cardinal(r)
    raise ValueError(n)


def ordinal(n):
    if n in ORDINAL_SMALL:
        return ORDINAL_SMALL[n]
    if n < 20:
        return "მე" + _drop_i(SMALL[n]) + "ე"
    if n < 100:
        q, r = divmod(n, 20)
        if r == 0:
            return "მე" + _drop_i(TWENTIES[q]) + "ე"
        return TWENTIES[q][:-1] + "და" + ("მეერთე" if r == 1 else ordinal(r))
    if n < 1000:
        q, r = divmod(n, 100)
        head = ("" if q == 1 else _drop_i(SMALL[q])) + "ას"
        if r == 0:
            return "მე" + head + "ე"
        tail = "მეერთე" if r == 1 else ordinal(r)
        return head + " " + tail
    for scale, stem in SCALES:
        if n >= scale:
            q, r = divmod(n, scale)
            if scale == 1000 and q == 1:
                head = "ათას"
                if r == 0:
                    return "მეათასე"
            elif scale == 1000 and q == 2:
                head = "ორი ათას"
                if r == 0:
                    return "მეორიათასე"
            elif scale == 1000 and q < 20:
                head = cardinal(q) + " ათას"
                if r == 0:
                    return "მე" + _drop_i(cardinal(q)) + "ათასე"
            else:
                head = cardinal(q) + " " + stem
                if r == 0:
                    return "მე" + stem + "ე" if q == 1 else head + "ე"
            tail = "მეერთე" if r == 1 else ordinal(r)
            return head + " " + tail
    raise ValueError(n)


def _drop_i(word):
    return word.removesuffix("ი")


def stem(word):
    """Stem a phrase's last word takes before an ending: ხუთი → ხუთ, რვა/ცხრა (vowel stems) stay."""
    return _drop_i(word)


def inflect(words, suffix):
    """A cardinal (independent use) + a Georgian case ending or postposition."""
    s = stem(words)
    vowel = not words.endswith("ი")  # რვა, ცხრა, ოცდარვა...
    if suffix in ("ჯერ",):
        return "ერთხელ" if words == "ერთი" else s + "ჯერ"
    table = {"ის": ("ის", "ის"), "ს": ("ს", "ს"), "მა": ("მა", "მ"), "მ": ("მა", "მ"), "ით": ("ით", "ით"),
             "ად": ("ად", "დ"), "დ": ("ად", "დ"), "მდე": ("ამდე", "მდე"), "ამდე": ("ამდე", "მდე"),
             "დან": ("იდან", "დან"), "იდან": ("იდან", "დან"), "ზე": ("ზე", "ზე"), "ში": ("ში", "ში"),
             "თან": ("თან", "სთან"), "ზეც": ("ზეც", "ზეც"), "ც": ("იც", "ც"), "იც": ("იც", "ც")}
    if suffix not in table:
        return words + suffix
    cons, vow = table[suffix]
    if vowel and suffix in ("ის", "ით", "იდან", "დან"):  # რვის, რვით, რვიდან (the final ა drops)
        return s[:-1] + {"ის": "ის", "ით": "ით", "იდან": "იდან", "დან": "იდან"}[suffix]
    return s + (vow if vowel else cons)


def attributive(words, next_word):
    """A numeral before a noun: dative/adverbial/postpositional nouns take the stem (ხუთ სერვერს)."""
    w = next_word.strip(".,;:!?„“\"()")
    if re.search(r"(ზე|ში|თან|ად|(?<=[აეიოუ])დ|ამდე|მდე)$", w) or (w.endswith("ს") and not w.endswith("ის")):
        return stem(words)
    if w.endswith("მა"):
        return stem(words) + "მა"
    return words


def spell(latin):
    return " ".join(LETTERS[c.upper()] for c in latin if c.upper() in LETTERS)


def spell_name(latin):
    """A spelled acronym used as a noun: a last letter ending in a consonant takes the nominative ი (ეს ემ ესი)."""
    s = spell(latin)
    return s + "ი" if s and s[-1] not in VOWELS else s


def root_i(latin):
    """Does the spoken name end in a root ი that stays before an ending (Sony, Gemini, AMD), not a nominative ი?"""
    if is_acronym(latin) and SOUND.get(latin) != "consonant":  # BOG → საქართველოს ბანკმა, not ბანკიმ
        return LETTERS[latin[-1].upper()][-1] == "ი"
    return SOUND.get(latin) == "i-sound" or latin[-1:].lower() in ("i", "y")


def attach(nominative, suf, keep_i=False):
    """A Georgian spoken name (nominative) + the case ending written after its hyphen.

    მაიკროსოფტი + მა → მაიკროსოფტმა (the nominative ი is an ending, it drops); ენვიდია + ის → ენვიდიას,
    + მა → ენვიდიამ, + ით → ენვიდიათი (vowel stems, like spelled acronyms: ეი აი + ს → ეი აის); a root ი after
    a vowel stays (ჰუავეი + მა → ჰუავეიმ), and so does one the Latin name ends in (keep_i: სონი + მა → სონიმ)."""
    last = nominative.split()[-1]
    if nominative.endswith("ი") and len(last) > 1 and last[-2] not in VOWELS and not keep_i:
        return nominative[:-1] + {"მდე": "ამდე", "დან": "იდან", "თვის": "ისთვის", "დ": "ად"}.get(suf, suf)  # ტამდე
    if nominative[-1] in VOWELS:  # research table: vowel stems don't truncate (ტესლამ, ტესლას, ენვიდიას)
        return nominative + {"ის": "ს", "მა": "მ", "ით": "თ" if nominative[-1] == "ი" else "თი", "ად": "დ",
                              "ი": ""}.get(suf, suf)  # AMD-ი → ეი ემ დი: a vowel stem has no nominative ი
    return nominative + suf


def number(text):
    """'1,500' / '2 250' / '3.5' / '36' → words (nominative)."""
    text = re.sub(r"[   ]", "", text)  # thousands grouped with a space ("2 250")
    text = text.replace(",", "") if re.fullmatch(r"\d{1,3}(,\d{3})+", text) else text
    if "." in text or ("," in text and not text.endswith(",")):
        whole, frac = re.split(r"[.,]", text, maxsplit=1)
        if frac == "5" and int(whole) < 20:  # 1,5 → ერთნახევარი, 0,5 → ნახევარი (Kaeasy addition)
            return (stem(cardinal(int(whole))) if int(whole) else "") + "ნახევარი"
        return f"{cardinal(int(whole))} მთელი {cardinal(int(frac))} {DENOMINATORS.get(len(frac), 'მეათასედი')}"
    return cardinal(int(text))


def version(text):
    """'4.7' after a product name, '23.0.1' → ოთხი წერტილი შვიდი (a version is not a decimal)."""
    return " წერტილი ".join(cardinal(int(p)) for p in text.split("."))


GROUPED = r"\d{1,3}(?:[   ]\d{3})+(?!\d)"
NUM = rf"{GROUPED}|\d{{1,3}}(?:,\d{{3}})+|\d+(?:[.,]\d+)?"
TOKEN = re.compile(r"^(?P<pre>[„“\"(]*)(?P<core>.*?)(?P<post>[.,;:!?“\")]*)$")
ORD_CASE = "ის|ს|მა|ით|ად|მდე|ამდე|დან|იდან|ზე|ში|თან"  # case endings after an ordinal in digits
# Whitespace tokens, except that a number grouped with spaces ("2 250-ზე", "151 000") stays one token, so the
# voice reads one number and the caption shows it as one word.
TOKENS = re.compile(rf"(?<!\S)[„“\"(]*{GROUPED}\S*|\S+")
LATIN = re.compile(r"[A-Za-z]")
# What may follow a name's hyphen as a case ending; anything else is a compound ("AI-აგენტები").
ENDING = re.compile(r"ებ(?:ი|ს|ის|მა|ით|ზე|ში|თან|ისთვის)?|ის(?:ა|თვის|გან)?|ს(?:თან|თვის)?|მა|მ|ით|ად|დ|ზე|ში|თან|"
                    r"თვის|ზეც|შიც|იც|ც|ამდე|მდე|იდან|დან|კენ|ივით|ი|ელი|ელმა|ელს")


def tokens(text):
    return TOKENS.findall(text)


def learned_path():
    if os.environ.get("SHORTS_DATA"):
        return pathlib.Path(os.environ["SHORTS_DATA"]) / "lexicon_learned.json"
    try:
        from .memory import data_dir
    except ImportError:  # the vendored copy in SiTech Shorts: <repo>/data
        return HERE.parent / "data" / "lexicon_learned.json"
    return pathlib.Path(data_dir()) / "lexicon_learned.json"


def learned():
    """Names learned from earlier scripts' "say" maps: {name: spoken}. Approved entries live in lexicon_ka.json."""
    try:  # acronyms and IDs from older files are skipped: code spells them, learn() no longer keeps them
        return {k: v["say"] for k, v in json.loads(learned_path().read_text(encoding="utf-8")).items()
                if not is_acronym(k) and not is_id(k)}
    except (OSError, ValueError, KeyError, TypeError):
        return {}


def learn(say, slug):
    """Keeps a script's new spoken forms for later videos (status auto, for Louie to confirm). Returns the new names."""
    path = learned_path()
    try:
        known = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        known = {}
    import datetime as dt
    new = [k for k, v in (say or {}).items() if k not in WORDS and k not in known and not is_acronym(k)
           and not is_id(k) and isinstance(v, str) and v.strip()]  # letter acronyms stay spelled the same way everywhere
    for k in new:
        known[k] = {"say": say[k].strip(), "status": "auto", "first": dt.date.today().isoformat(), "slug": slug}
    if new:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(known, ensure_ascii=False, indent=1), encoding="utf-8")
    return new


def names(say=None):
    """Spoken forms for this narration, approved first: lexicon > the script's "say" > learned."""
    return {**learned(), **{k: v for k, v in (say or {}).items() if isinstance(v, str) and v.strip()}, **WORDS}


def is_id(word):
    """A one-off identifier, not a name to learn: CVE-2026-97631, KB5034441 (5+ digits; Storm-0940 and B300 are names)."""
    return sum(c.isdigit() for c in word) >= 5


def is_acronym(word):
    """Spelled letter by letter: AI, GPU, AWS, AAIF (up to 4 capitals). Longer all-caps words are names (ARTEX)."""
    return bool(re.fullmatch(r"[A-Z]{2,4}", word)) and word not in ("OK",)


# Noun endings after a time (საათ, წუთ) and whether the numeral before it keeps its ი (Kaeasy addition).
CLOCK = {"": ("ი", True), "ის": ("ის", True), "დან": ("იდან", True), "ით": ("ით", True), "ს": ("ს", False),
         "ზე": ("ზე", False), "მდე": ("ამდე", False), "ამდე": ("ამდე", False), "ში": ("ში", False),
         "თვის": ("ისთვის", True)}


def clock(h, minute, suf=""):
    """15:30-მდე → თხუთმეტ საათსა და ოცდაათ წუთამდე; 06:00-დან → ექვსი საათიდან; 14:05 → თოთხმეტი საათი და ხუთი წუთი."""
    ending, keep_i = CLOCK.get(suf, ("ი" + suf, True))

    def num(n):
        return cardinal(n) if keep_i else stem(cardinal(n))

    if minute == 0:
        return f"{num(h)} საათ{ending}"
    # In "X and Y" Georgian puts the shared ending on the last noun; the first takes -ი (nominative/genitive
    # group) or -სა (dative group): თხუთმეტი საათისა და ოცდაათი წუთიდან, თხუთმეტ საათსა და ოცდაათ წუთამდე.
    first = ("საათი" if suf == "" else "საათისა") if keep_i else "საათსა"
    return f"{num(h)} {first} და {num(minute)} წუთ{ending}"


# The law knows one word, პრიმ, plus a digit (organic law on normative acts, 16.11): 353¹, 144³.
PRIME_NAMES = {"¹": "პრიმა", "²": "პრიმა ორი", "³": "პრიმა სამი", "⁴": "პრიმა ოთხი"}

# 10-14 ოქტომბერს / ოქტომბრის → ათიდან თოთხმეტ ოქტომბრამდე.
MONTH_MDE = {
    **{full + e: short + "ამდე" for full, short in (("იანვარ", "იანვრ"), ("თებერვალ", "თებერვლ"),
                                                    ("სექტემბერ", "სექტემბრ"), ("ოქტომბერ", "ოქტომბრ"),
                                                    ("ნოემბერ", "ნოემბრ"), ("დეკემბერ", "დეკემბრ"))
       for e in ("ი", "ს")},
    **{short + "ის": short + "ამდე" for short in ("იანვრ", "თებერვლ", "სექტემბრ", "ოქტომბრ", "ნოემბრ", "დეკემბრ")},
    **{m + e: m + "ამდე" for m in ("მარტ", "აპრილ", "მაის", "ივნის", "ივლის") for e in ("ი", "ს", "ის")},
    "აგვისტო": "აგვისტომდე", "აგვისტოს": "აგვისტომდე",
}

GEO_EXPANSIONS = {
    "სზაკ": "საქართველოს ზოგადი ადმინისტრაციული კოდექსი",
    "სასკ": "საქართველოს ადმინისტრაციული საპროცესო კოდექსი",
    "შსს": "შინაგან საქმეთა სამინისტრო",
    "სუს": "სახელმწიფო უსაფრთხოების სამსახური",
    "სებ": "საქართველოს ეროვნული ბანკი",
}

GEO_ADJECTIVES = {"ეროვნული", "ზოგადი", "ადმინისტრაციული"}  # expand() makes these agree with the noun
# Read as letters. სსკ and სსსკ name different codes in civil and criminal decisions, ასკ is not settled either,
# so a guess could read out the wrong code. Text meant for speech writes the code's full name.
GEO_SPELLED = ("სსკ", "სსსკ", "ასკ", "შპს", "სს")

GEO_LETTERS = {
    "ა": "ა", "ბ": "ბე", "გ": "გე", "დ": "დე", "ე": "ე", "ვ": "ვე", "ზ": "ზე",
    "თ": "თე", "ი": "ი", "კ": "კა", "ლ": "ელ", "მ": "ემ", "ნ": "ენ", "ო": "ო",
    "პ": "პე", "ჟ": "ჟე", "რ": "ერ", "ს": "ეს", "ტ": "ტე", "უ": "უ", "ფ": "ფე",
    "ქ": "ქე", "ღ": "ღე", "ყ": "ყა", "შ": "შე", "ჩ": "ჩე", "ც": "ცე", "ძ": "ძე",
    "წ": "წე", "ჭ": "ჭე", "ხ": "ხა", "ჯ": "ჯე", "ჰ": "ჰე",
}


def month_day(n, next_word):
    """The day before a month is a cardinal, only the first is ordinal: ოცდაორ ნოემბერს, პირველ ნოემბერს."""
    word = ordinal(1) if n == 1 else cardinal(n)
    return attributive(word, next_word) if GEO.search(next_word or "") else word


def expand(abbr, suf):
    """სებ-მა → საქართველოს ეროვნულმა ბანკმა: an adjective agrees with the noun that takes the ending."""
    *head, noun = GEO_EXPANSIONS[abbr].split()
    form = "მა" if suf in ("მ", "მა") else "" if suf in ("ს", "ზე", "ში", "თან", "ად", "დ", "მდე", "ამდე") else None
    if form is not None:
        head = [w[:-1] + form if w in GEO_ADJECTIVES else w for w in head]
    return " ".join([*head, attach(noun, "მა" if suf == "მ" else suf)])


def speak_token(core, next_word="", prev_word="", known=None):
    """One token without surrounding punctuation → spoken form (None = keep as is).
    known: name → spoken nominative (names()); prev_word tells a version ("Opus 4.7") from a decimal."""
    if not core:
        return None
    known = WORDS if known is None else known
    if core in known:
        return known[core]
    m = re.fullmatch(r"(?P<sign>[+−-])(?P<rest>\d.*)", core)  # -1-დან, +1-მდე (Kaeasy addition)
    if m:
        rest = speak_token(m["rest"], next_word, prev_word, known)
        return rest and ("პლუს " if m["sign"] == "+" else "მინუს ") + rest
    m = re.fullmatch(r"(?P<h>[01]?\d|2[0-3]):(?P<min>[0-5]\d)(?:-(?P<suf>[ა-ჿ]+))?", core)  # 06:00-დან, 15:30-მდე
    if m:
        return clock(int(m["h"]), int(m["min"]), m["suf"] or "")
    m = re.fullmatch(r"(?P<w>.*[A-Za-z0-9.])-(?P<suf>[ა-ჿ]+)", core)  # NVIDIA-ს, AI-ს, GPU-ები, Storm-0940-მა
    if m and LATIN.search(m["w"]) and not UNIT_RE.fullmatch(core) and "°" not in core:
        w, suf = m["w"], m["suf"]
        base = known.get(w) or (spell_name(w) if is_acronym(w) else speak_token(w, prev_word=prev_word, known=known))
        if not base:
            return None
        return attach(base, suf, root_i(w)) if ENDING.fullmatch(suf) else base + " " + suf  # AI-აგენტები: compound
    m = re.fullmatch(r"v(?P<n>\d+(?:\.\d+)+)", core)  # v3.8 → ვერსია სამი წერტილი რვა (Kaeasy addition)
    if m:
        return "ვერსია " + version(m["n"])
    m = re.fullmatch(r"(?P<a>[A-Z])2(?P<b>[A-Z])", core)  # B2B → ბი თუ ბი
    if m:
        return f'{spell(m["a"])} თუ {spell_name(m["b"])}'
    m = UNIT_RE.fullmatch(core)  # 10 ₾, 500 ₾-ით, 5 კმ: a unit word after a number
    if m and re.fullmatch(rf"[+−-]?(?:{NUM})", prev_word or ""):
        head, _, rest = UNIT_WORDS[m["u"]].partition(" ")
        return (attach(head, m["suf"]) if m["suf"] else head) + (" " + rest if rest else "")
    m = re.fullmatch(r"(?P<n>\d+(?:\.\d+){2,})(?:-(?P<suf>[ა-ჿ]+))?", core)  # 23.0.1, 23.0.1-ზე
    if m or (prev_word and LATIN.search(prev_word) and re.fullmatch(r"\d+\.\d+(?:-[ა-ჿ]+)?", core)):  # Opus 4.7
        n, _, suf = core.partition("-")
        v = version(n)
        return inflect(v, suf) if suf else v
    m = re.fullmatch(r"(?P<a>\d+)[–-](?P<b>\d+)", core)  # 10–15 (not a model name like GPT-5)
    if m:
        return inflect(cardinal(int(m["a"])), "დან") + " " + inflect(cardinal(int(m["b"])), "მდე")
    m = re.fullmatch(rf"(?P<cur>[$€₾£])(?P<n>{NUM})(?:-(?P<suf>[ა-ჿ]+))?", core)
    if m:
        unit = CURRENCY[m["cur"]]
        tail = next_word.strip(".,;:!?")
        if tail in ("მილიონი", "მილიარდი", "ათასი", "million", "billion") and not m["suf"]:
            return number(m["n"])  # the scale word follows; the currency is spoken after it by the writer
        noun = unit + ("ი" if not unit.endswith("ო") else "")
        if m["suf"]:  # $50-ით → ორმოცდაათი დოლარით, $100-ად → ას დოლარად
            noun = attach(noun, m["suf"])
            return attributive(number(m["n"]), noun) + " " + noun
        return number(m["n"]) + " " + noun
    m = re.fullmatch(rf"(?P<n>{NUM})\s?°C?(?:-(?P<suf>[ა-ჿ]+))?", core)  # 25°C, 25°C-მდე
    if m:
        noun = attach("გრადუსი", m["suf"]) if m["suf"] else "გრადუსი"
        return attributive(number(m["n"]), noun) + " " + noun
    m = re.fullmatch(rf"(?P<n>{NUM})%(?:-(?P<suf>[ა-ჿ]+))?", core)  # 36%, 36%-ის
    if m:
        n, suf = number(m["n"]), m["suf"]
        if not suf:
            return n + " პროცენტი"
        if suf in ("ს", "ზე", "ში", "მდე", "ამდე", "თან"):
            return stem(n) + " პროცენტ" + {"მდე": "ამდე", "ამდე": "ამდე"}.get(suf, suf)
        if suf in ("მა", "მ"):
            return stem(n) + "მა პროცენტმა"
        return n + " პროცენტ" + {"ის": "ის", "ით": "ით", "დან": "იდან", "იდან": "იდან", "ად": "ად", "ც": "იც"}.get(suf, suf)
    m = re.fullmatch(rf"(?P<n>{NUM})\s?(?P<u>GB|TB|MB|GHz|km|W|nm)", core)
    if m:
        return number(m["n"]) + " " + UNITS[m["u"]] + "ი"
    m = re.fullmatch(r"(?P<n>\d+)(?P<p>[¹²³⁴])(?:-(?P<suf>[ა-ჿ]+))?", core)  # 353¹-ე მუხლი
    if m:
        n_val = int(m["n"])
        p_name = PRIME_NAMES[m["p"]]
        suf = m["suf"]
        if suf in ("ე", "ელი", "ლი", "ელ", "ლ") or (not suf and next_word.startswith("მუხლ")):
            ord_word = ordinal(n_val)
            return f"{ord_word} {p_name}"
        if suf:
            return f"{ordinal(n_val)} {attach(p_name, suf)}"
        return f"{cardinal(n_val)} {p_name}"
    m = re.fullmatch(r"(?P<n>\d+)-(?P<o>ე|ელი|ლი|ელ|ლ)", core)  # 21-ე, 1-ლი, 1-ლ იანვარს (old 1-ელი too)
    if m:
        n_val = int(m["n"])
        after = TOKEN.match(next_word or "")["core"]
        if MONTHS.match(after):
            return month_day(n_val, next_word)
        return ordinal(n_val) if m["o"] in ("ე", "ელი", "ლი") else _drop_i(ordinal(n_val))
    # An ordinal with a case ending: 1-ლში, 21-ეზე, მე-5-ში, მე-5-ის.
    m = re.fullmatch(rf"(?:(?P<n>\d+)-(?:ე|ელ|ლ)|მე-(?P<m>\d+)-)(?P<suf>{ORD_CASE})", core)
    if m:
        return inflect(ordinal(int(m["n"] or m["m"])), m["suf"])
    m = re.fullmatch(r"მე-(?P<n>\d+)(?:-ე)?", core)  # მე-2
    if m:
        n_val = int(m["n"])
        after = TOKEN.match(next_word or "")["core"]
        if MONTHS.match(after):
            return month_day(n_val, next_word)
        return ordinal(n_val)
    m = re.fullmatch(rf"(?P<n>{NUM})-(?P<suf>[ა-ჿ]+)", core)  # 4-ჯერ, 2012-ში, 5-მა
    if m:
        return inflect(number(m["n"]), m["suf"])
    m = re.fullmatch(rf"(?P<n>{NUM})", core)
    if m:
        words = number(m["n"])
        after = TOKEN.match(next_word or "")["core"]
        if words == "ერთი" and MONTHS.match(after):  # 1 ივნისს → პირველ ივნისს
            words = ordinal(1)
        unit = UNIT_RE.fullmatch(after) and speak_token(after, prev_word=m["n"], known=known)
        if unit:  # 100 ₾-ად → ას ლარად
            return attributive(words, unit.split()[0])
        return attributive(words, next_word) if GEO.search(next_word or "") else words
    m = re.fullmatch(r"(?P<w>[A-Za-z]+)-?(?P<n>\d+)(?P<rest>[A-Za-z]*)", core)  # B300, GPT-5, M4
    if m and m["w"].isupper():
        return f'{spell(m["w"])} {cardinal(int(m["n"]))}' + (f' {spell(m["rest"])}' if m["rest"] else "")
    if is_acronym(core):  # AI, GPU, AMD, TSMC; SMS → ეს ემ ესი, but a following word keeps the bare letters:
        # RTX 5090 → არ ტი ექს, VPN დანამატი → ვი პი ენ დანამატი (usually a modifier; a subject takes ი in writing)
        return spell(core) if next_word and re.match(r"[\dა-ჰ]", TOKEN.match(next_word)["core"]) else spell_name(core)
    m = re.fullmatch(r"(?P<w>[ა-ჰ]{2,6})-(?P<suf>[ა-ჿ]+)", core)  # სზაკ-ის, შსს-ს, სსკ-ის
    if m:
        w, suf = m["w"], m["suf"]
        if w in GEO_EXPANSIONS:
            return expand(w, suf)
        if w in GEO_SPELLED:
            return attach(" ".join(GEO_LETTERS.get(c, c) for c in w), suf)
    if core in GEO_EXPANSIONS:
        return GEO_EXPANSIONS[core]
    if core in GEO_SPELLED:
        return " ".join(GEO_LETTERS.get(c, c) for c in core)
    return None


def pairs(text, say=None):
    """[(display token, spoken text)] for every token of the narration (tokens()). say: the script's own
    spoken forms for names the lexicon doesn't know ({"ARTEX": "არტექსი"})."""
    toks, known = tokens(text), names(say)
    multi = {**joined(toks), **multiword(toks, known)}
    out = []
    for i, tok in enumerate(toks):
        m = TOKEN.match(tok)
        nxt = toks[i + 1] if i + 1 < len(toks) else ""
        prev = TOKEN.match(toks[i - 1])["core"] if i else ""
        spoken = multi.get(i) or speak_token(m["core"], "" if m["post"] else nxt, prev, known)  # a comma ends the phrase
        out.append((tok, tok if spoken is None else m["pre"] + spoken + m["post"]))
    return out


CLOCK_NOUN = {ending: suf for suf, (ending, _) in CLOCK.items()}  # საათ + ზე → "ზე"
PHONE_GROUP = re.compile(r"\d{2,3}")


def _digits(group):
    return " ".join(SMALL[int(d)] for d in group)


def joined(toks):
    """{token index: spoken} where a number and the next word are read together (Kaeasy addition): a time before
    საათი (18:30 საათზე → თვრამეტ საათსა და ოცდაათ | წუთზე), a range before a counted noun (10-15 წუთი →
    ათიდან თხუთმეტ | წუთამდე) and a +995 phone number read in groups. The next token keeps its own slot."""
    cores = [TOKEN.match(t) for t in toks]
    out = {}
    for i, m in enumerate(cores):
        core = m["core"]
        nxt = cores[i + 1] if i + 1 < len(toks) else None
        t = re.fullmatch(r"(?P<h>[01]?\d|2[0-3]):(?P<min>[0-5]\d)", core)
        if t and nxt and nxt["core"].startswith("საათ") and nxt["core"][4:] in CLOCK_NOUN:
            head, _, last = clock(int(t["h"]), int(t["min"]), CLOCK_NOUN[nxt["core"][4:]]).rpartition(" ")
            out[i], out[i + 1] = head, last
        r = re.fullmatch(r"(?P<a>\d+)[–-](?P<b>\d+)", core)
        if r and nxt and nxt["core"] in RANGE_NOUNS:
            end = r["a"][:2] + r["b"] if len(r["a"]) == 4 and len(r["b"]) == 2 else r["b"]  # 2025-26 წლებში
            out[i] = inflect(cardinal(int(r["a"])), "დან") + " " + stem(cardinal(int(end)))
            out[i + 1] = RANGE_NOUNS[nxt["core"]]
        elif r and nxt and nxt["core"] in MONTH_MDE:
            out[i] = inflect(cardinal(int(r["a"])), "დან") + " " + stem(cardinal(int(r["b"])))
            out[i + 1] = MONTH_MDE[nxt["core"]]
        if core == "+995":
            groups = []
            for c in cores[i + 1:i + 5]:
                if not PHONE_GROUP.fullmatch(c["core"]):
                    break
                groups.append(c)
            if len(groups) >= 3:
                out[i] = "პლუს " + cardinal(995) + ","
                for j, c in enumerate(groups, i + 1):
                    g = c["core"]
                    said = _digits(g) if len(g) == 3 or g.startswith("0") else cardinal(int(g))
                    out[j] = said + ("," if j < i + len(groups) else "")
    return out


def multiword(toks, known):
    """{token index: spoken} for names of several words ("Hugging Face": "ჰაგინგ ფეისი"), one spoken word per
    written word (the last one takes any extra words and the case ending: "Hugging Face-ზე")."""
    out = {}
    for name, said in known.items():
        parts, words = name.split(), said.split()
        if len(parts) < 2 or len(words) < len(parts):
            continue
        spoken = words[:len(parts) - 1] + [" ".join(words[len(parts) - 1:])]
        for i in range(len(toks) - len(parts) + 1):
            cores = [TOKEN.match(t)["core"] for t in toks[i:i + len(parts)]]
            last, suf = cores[-1], ""
            m = re.fullmatch(r"(?P<w>.*[A-Za-z0-9.])-(?P<suf>[ა-ჿ]+)", last)
            if m and m["w"] == parts[-1]:
                last, suf = m["w"], m["suf"]
            if cores[:-1] + [last] == parts:
                tail = spoken[-1] if not suf else attach(spoken[-1], suf) if ENDING.fullmatch(suf) else spoken[-1] + " " + suf
                out.update({i + j: w for j, w in enumerate(spoken[:-1] + [tail])})
    return out


def speech(text, say=None):
    return " ".join(s for _, s in pairs(text, say))


def unspoken(text, say=None):
    """Latin words the voice would get in Latin letters (no lexicon entry, no "say", not a letter acronym)."""
    out = [re.sub(r"-[ა-ჿ]+$", "", TOKEN.match(tok)["core"]) for tok, said in pairs(text, say) if LATIN.search(said)]
    return list(dict.fromkeys(out))
