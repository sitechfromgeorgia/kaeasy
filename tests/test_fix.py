import json

import pytest
from kaeasy import fix, lint


@pytest.mark.parametrize("text,want", [
    ('მან თქვა "ჩვენ ვჩერდებით" და წავიდა.', "მან თქვა „ჩვენ ვჩერდებით“ და წავიდა."),
    ("Metaის შემოსავალი გაიზარდა.", "Meta-ის შემოსავალი გაიზარდა."),
    ("Microsoft -მა ახალი მოდელი წარადგინა.", "Microsoft-მა ახალი მოდელი წარადგინა."),
    ("Microsoft მა ახალი მოდელი წარადგინა.", "Microsoft-მა ახალი მოდელი წარადგინა."),
    ("GPUებს ყიდულობენ.", "GPU-ებს ყიდულობენ."),
    ("მაიკროსოფტმა ახალი მოდელი წარადგინა.", "Microsoft-მა ახალი მოდელი წარადგინა."),
    ("შემოსავალი 2.5 მილიარდი დოლარია.", "შემოსავალი 2,5 მილიარდი დოლარია."),
    ("ფასი 20 % -ით გაიზარდა.", "ფასი 20%-ით გაიზარდა."),
    ("კომპანია — ბაზრის ლიდერი.", "კომპანია - ბაზრის ლიდერი."),
    ("ფასები 2020–2024 წლებში გაიზარდა.", "ფასები 2020-2024 წლებში გაიზარდა."),
    ("და მერე...", "და მერე…"),
    ("ფასი  გაიზარდა , ძალიან.", "ფასი გაიზარდა, ძალიან."),
    ("შეხვედრა 22-ე ნოემბერს გაიმართება.", "შეხვედრა 22 ნოემბერს გაიმართება."),
    ("ვერცერთი არ შესრულდა.", "ვერცერთი შესრულდა."),
    ("არცერთი არ მოვიდა.", "არცერთი მოვიდა."),
])
def test_fixes(text, want):
    fixed, changes = fix.fix_text(text)
    assert fixed == want
    assert changes


@pytest.mark.parametrize("text", [
    "Microsoft-მა ახალი მოდელი წარადგინა.",
    "Python ის ენაა, რომელსაც ყველა იყენებს.",
    "May თვის ანგარიში გამოქვეყნდა.",
    'ნახეთ <a href="https://sitech.ge/a?x=1&y=2">ბმული</a> და `print("hi")` კოდი.',
    "საიტი https://example.com/path...end და მისამართი info@sitech.ge.",
    "```\nx = \"a\"  ...  — y\n```",
    "ვერსია 3.8 და iOS 18.1 გამოვიდა.",
    "1-ლი ნოემბერი ოფიციალური დღეა.",
    "მე-5 მუხლი ითვალისწინებს ჯარიმას.",
    "ვერცერთი შესრულდა.",
    "არცერთი მოვიდა.",
])
def test_leaves_correct_or_protected_text_alone(text):
    assert fix.fix_text(text) == (text, [])


def test_fixed_text_passes_strict_lint():
    text = 'Metaის და მაიკროსოფტმა "ახალი" მოდელი 2.5 მილიარდად შეაფასეს — 20 % -ით მეტად...'
    fixed, _ = fix.fix_text(text)
    assert lint.check_text(fixed, strict=True) == []


def test_check_json_uses_mode_per_field():
    script = {"title": "ახალი ჩიპი", "scenes": [{"text": "NVIDIA-მ 36%-ით გაზარდა.",
                                                  "say": "ენვიდიამ ოცდათექვსმეტი პროცენტით გაზარდა."},
                                                 {"text": "ok", "say": "Microsoft-მა 5 ჩიპი"}],
              "notes": "მაიკროსოფტმა"}
    found = lint.check_json(script, {"say": "speech", "notes": "skip", "*": "social"}, strict=True)
    assert {f.check for f in found} == {"latin_in_speech"}
    assert all(f.snippet.startswith("$.scenes[1].say") for f in found)


def test_tools(kaeasy):
    from test_plugin import FakeCtx
    ctx = FakeCtx()
    kaeasy.register(ctx)
    out = json.loads(ctx.tools["ka_fix"][1]({"text": "Metaის ფასი"}))
    assert out["text"] == "Meta-ის ფასი" and out["remaining"] == []
    out = json.loads(ctx.tools["ka_speech"][1]({"text": "Microsoft-მა 36%-ით გაზარდა."}))
    assert out["speech"] == "მაიკროსოფტმა ოცდათექვსმეტი პროცენტით გაზარდა." and out["remaining"] == []
    out = json.loads(ctx.tools["ka_lint"][1]({"text": json.dumps({"say": "GPU 5 ჩიპი"}), "fields": {"say": "speech"}}))
    assert not out["clean"]
    assert "error" in json.loads(ctx.tools["ka_lint"][1]({"text": "not json", "fields": {"*": "social"}}))
