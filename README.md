# Kaeasy

Georgian (ქართული) writing skills for AI agents. A [Hermes Agent](https://hermes-agent.nousresearch.com/docs)
plugin that helps cheap models (DeepSeek, GLM, gemma) write Georgian that a native editor would publish.

**Zero runtime cost.** No LLM calls, no API keys, no network. Knowledge lives in skills (rules +
`references/` + many wrong → right `examples/`); a deterministic linter checks the mechanical rules; a shared
mistakes memory feeds every correction back to all agents.

## What is inside

| Part | What it does |
|---|---|
| `skills/georgian-writing` | Entry point: workflow, the ten most-broken rules, which sibling to load |
| `skills/georgian-grammar` | Cases by verb series, numerals, adjectives, postpositions, verbs, agreement |
| `skills/georgian-natural-style` | Calques (EN/RU), AI filler, passive, rewrites |
| `skills/georgian-names-numbers` | Brands in Latin + hyphenated endings, countries, terms, numbers, dates, punctuation |
| `skills/georgian-news` | Articles and headlines (tbilisi.today, sitech.ge blog) |
| `skills/georgian-social` | Posts, ads, cards, on-screen video text |
| `skills/georgian-ui` | Buttons, statuses, errors, forms |
| `skills/georgian-speech` | `speech_text` for TTS: numbers in words, brands in Georgian letters |
| `skills/georgian-proofread` | Three-pass self-edit, review format, learning loop |
| `skills/georgian-business` | Commercial correspondence, invoices, B2B, email etiquette |
| `skills/georgian-marketing` | Hype-free copy, CTAs, landing pages, campaigns |
| `skills/georgian-official` | Official notices, legal citations, bureaucratic forms |
| `skills/georgian-legal` | Legal text: citations (prime articles), Constitution, 9 codes, courts, confusable terms, contracts |
| `skills/georgian-support` | Customer support, empathy, problem-resolution tone |
| `skills/georgian-translation` | Translation protocol, false friends, localization |
| `evals/` | 121 offline benchmark tasks (news rewrite, headline, Shorts hook, UI error) with mistake checklists & scoring |
| `ka_lint` tool | Mechanical checks, modes `article / social / ui / speech`, `strict` for publish gates, `fields` for JSON scripts (`{"say": "speech", "*": "social"}`) |
| `ka_fix` tool | Fixes what strict lint flags and a machine can fix: quotes, brand hyphens, transliterated brands, decimal comma, dashes, spacing. Never grammar |
| `ka_speech` tool | Written Georgian → TTS text: numbers with case, halves, times, ranges, money, units, phone numbers, versions, brands (`data/lexicon_ka.json`, endings by `data/latin_endings.json`), acronyms. Port of SiTech Shorts' `normalize_ka.py` |
| `ka_learn` / `ka_mistakes` tools | Shared memory of corrections (JSONL), most frequent first |
| `pre_llm_call` hook | One short hint per session so agents know the skills exist |

Skills are registered as `kaeasy:<name>` (`skill_view("kaeasy:georgian-writing")`). Plugin skills are read-only
and are not listed in `<available_skills>`, which is why the hook exists. Disable the hint with `KAEASY_HINT=0`.

## Install on a Hermes host

```bash
git clone https://github.com/sitechfromgeorgia/kaeasy /root/.hermes/shared-plugins/kaeasy
ln -s /root/.hermes/shared-plugins/kaeasy /root/.hermes/profiles/<profile>/plugins/kaeasy
# enable it for the profile (hermes plugins enable kaeasy, or plugins.enabled in config.yaml), then restart
# the gateway and check:  hermes plugins list
```

Shared learning across the fleet: set `KAEASY_DATA_DIR` to one directory for every profile (for example
`/root/.hermes/shared-knowledge/kaeasy`). Without it, each profile keeps its own memory in Hermes' plugin data dir.

## Linter outside Hermes

```bash
python lint.py --text "Microsoftმა 5 სტატიები გამოაქვეყნა" --strict
python lint.py --file draft.md --mode social --summary
```

## Evals ($0)

`evals/tasks.json` has 121 tasks; `evals/score.py` scores answers offline. `evals/run_opencode.py --n 5` runs 20
of them through a free opencode model with and without Kaeasy and writes `evals/RESULTS.md` (40 requests; it stops
when the free quota, shared with SiTech Shorts, is used up).

## Seed the memory

`python3 -m kaeasy.scripts.import_edits /root/sitech-shorts-lab/data/edits.jsonl` imports the language edits of
the Shorts review (with `KAEASY_DATA_DIR` set). Run it once per file.

## Develop

```bash
uv run --with pytest --with pyyaml python -m pytest -q
uv run --with ruff ruff check .
```

## Evals Benchmark

See [`evals/README.md`](evals/README.md) for the 121-task benchmark and zero-cost offline scoring utility:

```bash
# Inspect a task prompt, reference answer, and mistake checklist
uv run python evals/score.py --inspect news_001

# Score model output manually
uv run python evals/score.py --task news_001 --text "Microsoft-მა..."
```

See `AGENTS.md` for the rules of the repo (how to add a rule or an example without breaking anything).

## Credits

The linter and the first rules come from the SiTech fleet's `ge_ka_lint.py`, `GEORGIAN-STYLE.md` and the
`georgian-copy-quality` skill, plus the SiTech Shorts rulebook (K1-K22), `normalize_ka.py`, its lexicon and
review edits.

## Changelog

- **0.6.0**: Rules from four Georgian grammar books (Peikrishvili, Kvachadze, Chikobava, Khalvashi), in the writer's own words with the source. New references: `case-use`, `adjectives-pronouns`, `verb-forms`, `clauses`, `punctuation`, `particles-adverbs`. New checks: `wrong_form` (strict, exact forms from `data/wrong_forms.json`) and `dated_form` (advice). All 14 book-review points are decided (`docs/NEEDS-REVIEW.md`): the first is written `1-ლი`, whole hundreds `მე-100`, and `ორი ათას` keeps its nominative, all three strict; `ჩვენთაგანი` gets advice; `რომ` may be dropped after wish and necessity; subject-verb-object is a usual order. Speech now reads ordinals with case endings (`1-ლში`, `21-ეზე`).
- **0.5.3**: Added `negation` lint & auto-fix rule for `ვერცერთი`/`არცერთი` (inherent negation takes positive verb without `არ`/`ვერ`), `negation_split` warning for split spelling, grammar docs, and eval task `news_031`.
