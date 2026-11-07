---
name: georgian-grammar
description: Georgian (ka) grammar for writers - which case the subject and object take (ergative -მა, dative -ს), verb agreement, numerals, adjectives, postpositions. Load when writing or checking any Georgian sentence.
---

# Georgian grammar for writers

The errors weak models make are systematic. Check every sentence against these four questions, in order:

1. **What is the verb's tense group (series)?** That decides the subject and object cases (table below).
2. **Is the subject a number + noun?** Then noun and verb are singular.
3. **Does every adjective agree** with its noun's case (and stay singular in form)?
4. **Does every postposition get the case it governs?**

## Subject and object case by series

| Series | Typical forms | Subject (transitive) | Direct object | Example |
|---|---|---|---|---|
| I: present / future | აცხადებს, გამოუშვებს | nominative | dative | `კომპანია ახალ მოდელს უშვებს` |
| II: aorist / optative | გამოუშვა, გამოუშვას | **ergative -მა/-მ** | **nominative** | `კომპანიამ ახალი მოდელი გამოუშვა` |
| III: perfect (evidential) | გამოუშვია | **dative -ს** | nominative | `კომპანიას ახალი მოდელი გამოუშვია` |

- Ergative ending: **-მა** after a consonant stem (`სტუდენტმა`, `Microsoft-მა`), **-მ** after a vowel stem
  (`კომპანიამ`, `OpenAI-მ`, `ChatGPT-მ`).
- Many intransitive-looking "activity" verbs also take the ergative in series II: `იმუშავა`, `ითამაშა`,
  `იცეკვა`, `იტირა`, `იფიქრა`: ✅ `გუნდმა კარგად ითამაშა`.
- True intransitives (become, grow, close, arrive) keep the nominative: ✅ `კომპანია გაიზარდა`,
  `სერვისი დაიხურა`, `მომხმარებლები მოვიდნენ`.
- Verbs of feeling, wanting, having take a **dative subject** in every tense: ✅ `მომხმარებელს სჭირდება`,
  `კომპანიას აქვს`, `მკითხველს მოეწონა`, `ედოს უნდა`.

## Numerals

- Number + **singular** noun: `5 სერვერი`, `ათი ქვეყანა`, `რამდენიმე კომპანია`, `ბევრი ადამიანი`.
- The verb agrees with the singular: ✅ `ხუთმა ექსპერტმა განაცხადა` ❌ `ხუთმა ექსპერტმა განაცხადეს`.
- The case ending goes on the numeral too: `ხუთმა ექსპერტმა`, `სამ ქვეყანაში`, `ორი კომპანიის`.

## Adjectives

A consonant-stem adjective (`ახალი`, `დიდი`, `ქართული`) changes with the noun, but **never takes plural**:

| Case | Form | Example |
|---|---|---|
| nominative | ახალი | `ახალი მოდელი / მოდელები` |
| ergative | ახალმა | `ახალმა მოდელმა / მოდელებმა` |
| dative | ახალ | `ახალ მოდელს` ❌ `ახალს მოდელს` |
| genitive | ახალი | `ახალი მოდელის` ❌ `ახალის მოდელის` |
| instrumental | ახალი | `ახალი მოდელით` |
| adverbial | ახალ | `ახალ მოდელად` |

Vowel-stem adjectives (`მწვანე`, `ფართო`, `ახლო`) do not change at all: `მწვანე ენერგიას`,
`ფართო აუდიტორიისთვის`, `ახლო მომავალში`.

## Postpositions (most common)

| Takes | Postposition | Example |
|---|---|---|
| dative stem (suffix) | -ში, -ზე, -თან, -ვით | `კომპანიაში`, `სერვერზე`, `მთავრობასთან` |
| genitive (suffix) | -თვის, -გან, -კენ | `მომხმარებლისთვის`, `კომპანიისგან`, `ქალაქისკენ` |
| instrumental (suffix) | -დან | `სერვერიდან`, `2024 წლიდან` |
| adverbial (suffix) | -მდე | `ქალაქამდე`, `2030 წლამდე`, `40%-მდე` |
| genitive (separate word) | შესახებ, გამო, მიხედვით, შემდეგ, წინ, დროს, მიერ, ნაცვლად, გარდა, მიუხედავად, მიმართ | `კვლევის მიხედვით`, `ამის მიუხედავად` |

## More

- `references/cases.md`: all seven cases with endings and stem changes.
- `references/verb-classes.md`: four verb classes, series case alignment, and 40 frequent news verbs table.
- `references/noun-stems.md`: syncope and truncation rules with genitive, instrumental and plural for 60 nouns.
- `references/verbs.md`: series, preverbs, version vowels, person agreement, common verb pairs.
- `references/person-markers.md`: polypersonal agreement, prefixes მ-/გ-/გვ-, plural -თ, and 3rd person ჰ-/ს-/∅.
- `references/agreement.md`: plural subjects, collective nouns, "ის / ისინი", relative `რომელიც`.
- `references/syntax.md`: conditionals, subjunctive, reported speech, active vs passive, word order, commas, negation.
- `references/case-use.md`: which case or postposition each object and adverbial takes.
- `references/adjectives-pronouns.md`: degrees, declining a modifier with its noun, pronoun and numeral forms.
- `references/verb-forms.md`: preverbs, voice, version, contact, thematic markers, verbal noun, participles.
- `references/clauses.md`: compound and subordinate clauses, conjunctions, reported speech.
- `references/punctuation.md`: each mark, set-off phrases, direct address, parenthetical words.
- `references/particles-adverbs.md`: adverbs and their spelling, postpositions, conjunctions, particles.
- `examples/grammar-fixes.md`: 200+ wrong → right sentences from news, tech and social copy. Read before writing.
