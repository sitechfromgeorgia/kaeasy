# Disputed Points and Editorial Variations in Georgian Copy

This document tracks disputed points, regional/register variations, and stylistic edge cases in Georgian language guidelines across the `skills/` directory.

| file | current | proposed | why | confidence |
|---|---|---|---|---|
| `skills/georgian-grammar/references/cases.md` | `Meta-ს vs Meta-ის` marked as varying in press / fleet style | **Resolved**: Standardized on **`-ს`** for vowel-final foreign proper names ending in `-a`: `Meta-ს`, `Tesla-ს`, `NVIDIA-ს` in the genitive | Georgian quality media (**Forbes Georgia**, **Netgazeti**, **Publika**, **Interpressnews**) overwhelmingly and consistently use `-ს` (`Meta-ს შემოსავალი`, `Meta-ს პლატფორმები`, `Tesla-ს აქციები`, `Nvidia-ს CEO`). In Georgian grammar, foreign proper names ending in vowels (-ა, -ო, -უ) are treated as non-truncating vowel stems (like `შოთას`, `ტოკიოს`) where genitive and dative take `-ს`. Truncating `Meta` to `Met-ის` is artificial, non-phonetic, and virtually absent from modern quality newsrooms. | Resolved (High) |
| `skills/georgian-grammar/references/cases.md` | `needs-review: the instrumental of vowel-final names (NVIDIA-თი or NVIDIA-ით, GPU-თი or GPU-ით) varies in the press` | **Resolved**: Standardized on **`-თი`** for vowel-final names: `NVIDIA-თი`, `Meta-თი`, `Tesla-თი`, `GPU-თი` | In Georgian morphophonology, vowel stems strictly take the instrumental suffix `-თ / -თი` (`ტოკიოთი`, `მეტროთი`, `ანათი`), whereas `-ით` is reserved for consonant stems (`Google-ით`, `Microsoft-ით`). Suffixing `-ით` directly to a vowel stem (`NVIDIA-ით`, `Meta-ით`) causes a phonotactic vowel clash (`a-i`) and is considered an error in Georgian grammar. | Resolved (High) |
| `skills/georgian-grammar/references/cases.md` | `GPU-ს` in Genitive table (based on spoken `ჯი-პი-იუ`) | **Resolved**: Standardized on spoken final sound (`GPU-ს`, `GPU-თი`) in `latin-names.md` | Pronounced as English letters, `GPU` ends in vowel sound /u/ (`ჯი-პი-იუ`), hence non-truncating vowel stem taking `-ს` (`GPU-ს არქიტექტურა`). Codified deterministically across `latin-names.md` and `brands.md`. | Resolved (High) |
| `skills/georgian-names-numbers/references/brands.md` | Disputed `-ი` sound genitive (`OpenAI-ის` vs `OpenAI-ს`, `Spotify-ის` vs `Spotify-ს`) | **Resolved**: Standardized on **`-ს`** (genitive) and **`-თი`** (instrumental): `OpenAI-ს`, `Spotify-ს`, `Gemini-ს`, `Perplexity-ს`, `Sony-ს`, `Hyundai-ს` | Foreign loanwords and proper names ending in an `-ი` sound are non-truncating (უკვეცელი) root-inherent vowel stems (identical to `ტაქსი → ტაქსის`, `რაგბი → რაგბის`, `ჩაი → ჩაის`). In modern Georgian quality media (*Forbes Georgia*, *On.ge*, *Netgazeti*, *Publika*, *Interpressnews*), quality headlines overwhelmingly use `-ს` (`OpenAI-ს`, `Spotify-ს`, `Gemini-ს`). Adding `-ის` causes unnatural vowel hiatus (`OpenAI-ის`, `Sony-ის`). Fully documented in `latin-names.md` and `data/latin_endings.json`. | Resolved (High) |
| `skills/georgian-grammar/references/agreement.md` | `needs-review for ყველა მომხმარებელმა განაცხადა/განაცხადეს` | Standardize on **singular verb**: `ყველა მომხმარებელმა განაცხადა` | In standard literary and journalistic Georgian, `ყველა` with a singular noun is strictly singular in form and syntax, and requires a singular verb (`ყველა მომხმარებელმა განაცხადა`, `ყველა კომპანიამ დაადასტურა`). While plural verbs occur colloquially due to semantic agreement (synesis), copy editors in Georgian quality media treat `ყველა` + singular noun + plural verb as a grammatical error. | High |
| `skills/georgian-grammar/references/verbs.md` | `needs-review: edge cases (organizations as plural subjects, კომპანიებმა განაცხადეს is plural and correct)` | Retain plural verb for plural institutional/corporate agents: `კომპანიებმა განაცხადეს`, `ბანკებმა გაზარდეს` | Unlike purely inanimate plural nouns (which strictly take singular verbs in news style: `ფასები გაიზარდა`, `აქციები დაეცა`), organizations, banks, governments, and corporations in the plural acting as conscious agents (მოქმედი სუბიექტები) take plural verbs in quality media (`კომპანიებმა გააფორმეს შეთანხმება`). Singular `კომპანიამ განაცხადა` remains singular. | High |
| `skills/georgian-grammar/references/verbs.md` | `\| ჰაკერებმა სისტემა გატეხეს \| სისტემა გატყდა \|` | Replace `სისტემა გატყდა` with `სისტემა გატეხეს` (impersonal active) or `სისტემაში შეიჭრნენ`, or use a physical object (`მინა გატყდა`) | In Georgian, `გატყდა` is semantically restricted to physical, brittle objects snapping/shattering (glass, wood, bone). Saying `სისტემა გატყდა` or `სერვერი გატყდა` sounds comical or calqued from English slang. In Georgian IT journalism, unauthorized system access is rendered via active voice `სისტემა გატეხეს`, stative `სისტემა გატეხილია`, or `სისტემაში შეიჭრნენ`. | High |
| `skills/georgian-names-numbers/references/terms.md` | `\| encryption \| დაშიფვრა \| ❌ შიფრაცია in news copy (needs-review) \|` | Standardize on **`დაშიფვრა`**; drop `needs-review` | `დაშიფვრა` (verbal noun from `დაშიფრა`) is the standard, official, and universally accepted Georgian technical term for encryption. `შიფრაცია` is an unadapted Russian calque (шифрация) that has no standing in standard Georgian lexicography. | High |
| `skills/georgian-grammar/references/person-markers.md` | `needs-review: მოგწერეს vs მოგწერესთ` | In literary and news Georgian, standardize on **`მათ თქვენ მოგწერეს`** (no stacked `-თ`) | In spoken Georgian, `-თ` is colloquially appended to 3rd person plural verbs when addressing plural objects (`მათ თქვენ მოგწერესთ`), but the literary norm in standard Georgian strictly avoids stacking `-თ` onto the 3rd person plural subject suffix `-ეს`. | High |
| `skills/georgian-grammar/references/person-markers.md` | `needs-review: omission of ჰ- and ს- in modern news` | Preserve **`ჰ-`** and **`ს-`** in standard news copy (`ჰკითხა`, `სთხოვა`, `ჰგონია`, `სცადა`) | While colloquial Georgian and fast-paced web media frequently drop `ჰ-` and `ს-` (`კითხა`, `თხოვა`, `გონია`, `ცადა`), authoritative editorial styleguides and the State Language Department require preserving them where phonologically mandated by Shanidze's rule. | Medium |
| `skills/georgian-grammar/references/syntax.md` | `needs-review: comma before და connecting independent clauses` | Standardize on **no comma before `და`** in standard coordination unless contrastive or parenthetical | English and Russian punctuation rules require a comma before coordinating conjunctions separating independent clauses. Traditional Georgian syntax discourages a comma before a single `და` even between independent clauses with different subjects (`სერვერი გაითიშა და მომხმარებლებმა პრეტენზიები გამოთქვეს`), unless there is a strong semantic contrast or parenthetical interruption. | High |
| `skills/georgian-grammar/references/syntax.md` | `needs-review: single negation with negative pronouns` | Standardize on negative concord (**`არავინ არ იცის`**, **`არაფერი არ უთქვამს`**) as primary, while accepting single negation | In traditional literary Georgian, negative concord is the standard grammatical rule (`არავინ არ იცის`, `არაფერი არ ვიცი`). Single negation (`არავინ იცის`) has become common in contemporary news style under European influence and is acceptable, but full concord remains the most robust and natural Georgian form. | Medium |

## Decisions (Louie, 2026-11-02)

All seven rows above are **accepted** and applied in `skills/` (the GPU-ს row keeps `GPU-ის` as an accepted
variant). The `needs-review` tags for them are removed.

## Correction (review, 2026-11-02)

The -ი sound row above said `-თი` for the instrumental (`OpenAI-თი`). Georgian ი-final loans take `-თ`, as in `ტაქსი → ტაქსით`, and `-თი` would read `ჩატჯიპიტითი`.
- **Applied:** `-ით` and `-ად`, written the way Georgian media writes them (`OpenAI-ით`, `ChatGPT-ით`), in `data/latin_endings.json`, `latin-names.md`, `brands.md`, `cases.md` and the examples.
- **Also correct:** `-თ` (`OpenAI-თ`). It is rare in the press.

## Open

| file | current | question | next step |
|---|---|---|---|
| `skills/georgian-names-numbers/references/brands.md`, `cases.md` | `OpenAI-ის`, `ChatGPT-ის`, `Spotify-ის` but `Gemini-ს`, `Perplexity-ს`, `Midjourney-ს` | Genitive of names ending in an -i sound: `-ის` or `-ს`? | Settled by P6: `-ს` (`OpenAI-ს`); instrumental `-ით` (see Correction). `ka_lint` flags neither form | done |
| `skills/georgian-natural-style/references/calques.md`, `lint.py` | `ბე-ემ-ვე` was both ✅ (brands.md) and ❌ (calques.md) | Settled: `ბე-ემ-ვე` is the established spoken form of BMW; `ka_lint` allows it | done |
| `skills/georgian-names-numbers/references/latin-names.md`, `speech.py` | `T` in letter table is `ტი`, but TBC is `თიბისი` | Letter `T` mapping in acronyms: should English `T` default to `თ` or `ტ` in acronyms? Evidence across 10+ acronyms shows `ტ` dominates in international tech acronyms (`TCP` → `ტი-სი-პი`, `TLS` → `ტი-ელ-ესი`, `TSMC` → `ტი-ეს-ემ-სი`, `TNT` → `ტი-ენ-ტი`, `TV` → `ტი-ვი`, `TB` → `ტი-ბი`), while `თ` is specific to local Georgian brands rooted in Georgian words (`TBC` → `თიბისი`, `Telasi` → `თელასი`, `TTC` → `თბილისის სატრანსპორტო კომპანია`). Recommendation: keep `T: ტი` in the global letter table and route local exceptions via `data/lexicon_ka.json` and `data/glossary/georgia-companies.json`. | for Louie |

## P11 review: still open (2026-11-04)

| Where | Question | Status |
|---|---|---|
| `georgia-companies.json`, `lexicon_ka.json` | BOG and GWP: full name or letters? No evidence found for how Georgians say them | for Louie |
| `georgia-companies.json` | `m²` read `ემ კვადრატი`; `ვენდუ` may no longer exist; `ვანილა სქაი` is not in the gcaa.ge register | to check |
| `speech.py` | `ასკ`: Administrative Procedure or Administrative Offences Code? It stays spelled as letters until a source settles it | to check |
| `speech.py`, `citations.md` | `144³` read `პრიმა სამი`: the law gives `პრიმ` plus a digit, usage in court was not checked | to check |
| `courts-institutions.md` | Bar association, appeal courts and Gurjaani court details: the sources could not be opened | not verified |


## Book review: for Louie (2026-11-07)

The rules added in v0.6.0 come from four books. Where a book disagreed with an existing Kaeasy rule, the rule stayed until Louie decided. All 14 rows are now decided (2026-11-07). Louie decided the four numeral rows and the `ჩვენთაგანი` row, and said that otherwise the books show what is correct, so the other rows follow the book.

| Where | Kaeasy said | The book says | Source | Decision (2026-11-07) |
|---|---|---|---|---|
| `syntax.md` §7 | Negative concord is primary | Doubling the negative is optional | Kvachadze §12 | Book: both correct, doubling the common form; lint flags neither |
| `syntax.md` §1 | `ნეტავ`, `ნეტა` | `ნეტავი`, `ნეტა` | Kvachadze §20 | Book: `ნეტავ`, `ნეტავი`, `ნეტა` all correct |
| `agreement.md` | `ყველა` may take a plural verb for "all of them" | Singular verb only | Kvachadze §55 | Book: `ყველა მოვიდა`; plural only with `ყველანი` |
| `syntax.md` §4 | Adjectives never take `-ებ-` | A following adjective may, as in poetry | Kvachadze §105 | Book: added as the postposed exception |
| `syntax.md` §5 | Subject-verb-object is an unresolved calque | One of three usual orders | Kvachadze §133-134 | Book: SVO is ✅; SOV stays the most neutral |
| `syntax.md` §1 | `თუ` + aorist is a calque | Normal when the aorist has a future meaning | Kvachadze §182 | Book: future `თუ` + aorist is ✅; the unreal-past ❌ stays |
| `syntax.md` §1 | Wish and necessity clauses need `რომ` | `რომ` is often dropped | Kvachadze §186 | Book: `რომ` optional |
| `syntax.md` §2 | Relayed `-თქო` uses the third-person optative | Its two examples use the second person | Kvachadze §194 | Book: second person added, third person kept |
| `agreement.md` | `ორ ათას ადამიანს` | `ორი ათას კაცს` | Peikrishvili §59 | Louie: `ორი ათას`; `ორ ათას` is a strict lint error |
| `dates-numbers.md` | `ერთნახევარი`, `ორნახევარი` | `ოთხ-ნახევარი`, `ტონა-ნახევარი` | Peikrishvili §56, §59 | Louie: numbers one word (`ოთხნახევარი`), units hyphenated (`კილო-ნახევარი`) |
| `dates-numbers.md` | `ას მეერთე`, spaced | `ასმეერთე`, one word | Peikrishvili §59 | Louie: spaced, as now |
| `dates-numbers.md`, `lint.py` | `1-ელი`, `100-ე` | `1-ლი`, `მე-100` | Peikrishvili §59 | Louie: `1-ლი`; `1-ელი` and `100-ე` are strict lint errors |
| not in Kaeasy | | `ჩვენთაგანი`, `თქვენთაგანი` are wrong, though common in print | Peikrishvili §41 | Louie: advice in `ka_lint` (`dated_form`), not strict |
| `noun-stems.md` §2 | Syncope before ი after რ, ლ, მ, ნ and a rare დ | Also rarely before other consonants: `ბეჭედი`, `ხოხობი`, `ნიჩაბი` | Peikrishvili §25 | Book: added |

Still open from the book: Peikrishvili writes `მე-` first when an ordinal's parts are joined without `და`, which could mean `მე-101` rather than `101-ე`. The book gives no example above 100, so Kaeasy keeps `101-ე`, `180-ე` as *matsne.gov.ge* writes them.

Applied, because they are errors of fact:
- `noun-stems.md`: the `-ა` of a stem drops before plural `-ებ-`; the file said it stays. The example forms were already right.
- `agreement.md`, `syntax.md`: no comma before `რომ` when it sits inside its own clause (`შენ რომ მოხვიდე, გავიხარებ`).

The rule cards that were left out because the modern norm is unclear are kept outside the repo, in `_rules/` next to the books.
