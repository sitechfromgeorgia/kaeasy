# AGENTS.md

Guide for anyone (human or agent) changing this repo.

## What this repo is

A Hermes Agent plugin. The repo root **is** the plugin directory: `plugin.yaml`, `__init__.py` (register),
`lint.py` (deterministic linter), `fix.py` (mechanical fixer), `speech.py` (TTS text, a port of SiTech Shorts'
`normalize_ka.py`: keep the two in sync), `data/lexicon_ka.json` (approved spoken forms), `memory.py` (mistakes
memory), `skills/<name>/SKILL.md` with `references/` and `examples/`, `evals/`, `scripts/`. There is no build step.

## Commands

```bash
uv run --with pytest --with pyyaml python -m pytest -q   # all tests
uv run --with ruff ruff check .                          # lint
python lint.py --text "..." --strict                     # try the linter
uv run python evals/score.py --inspect news_001          # inspect an eval task
```

## Hard rules

- **No runtime cost.** No LLM calls, no network, no API keys in the plugin. Knowledge goes into skills.
- **No false positives in `STRICT`.** A strict rule must never fire on correct Georgian. Every ✅ line in
  `skills/*/examples/*.md` is linted in strict mode by the tests; if a new rule breaks one, the rule is wrong.
- **Skills stay small.** `SKILL.md` under 12 000 characters (tests enforce it); depth goes into `references/`
  and `examples/`, which the agent opens on demand.
- **Instructions in English, examples in Georgian.** Cheap models follow English instructions better.
- **Mark uncertainty.** A Georgian rule you are not sure about gets `needs-review` in the text. Do not guess.
- `ka_fix` only fixes what a strict rule flags and a machine can fix without judgment. It never changes
  grammar, and it leaves HTML, code and URLs untouched (tests in `tests/test_fix.py`).
- Handlers never raise; they return JSON with `error`.
- Nothing secret or personal in examples or in the memory (`memory.py` masks emails, phones, tokens).

## Adding knowledge

1. A new mistake pattern: add the wrong → right line to the right `examples/*.md` (format `- ❌ ... ✅ ...`).
2. A new rule: add it to the skill's `references/`; one line in `SKILL.md` only if it is among the most broken.
3. Mechanically detectable and zero-noise: add it to `lint.py` with tests for true positives and negatives.
4. Run the tests.

A rule taken from a book is written in your own words with its source, such as `(Peikrishvili §32)`. Never paste
book text: the books are in copyright.

## Change flow

Branch → PR → Louie merges. Code, comments and commits in English.
