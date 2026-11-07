# Georgian Person Markers (პირის ნიშნები)

Georgian is a polypersonal language: a single verb form can cross-reference both the subject and the direct
or indirect object simultaneously. Cheap LLMs frequently stumble on polypersonal morphology, confusing subject
and object prefixes, dropping the plural marker `-თ`, or double-marking persons.

This reference provides the exact prefix/suffix distribution rules, prefix slot competition, and common pitfalls.

---

## 1. Subject vs Object Person Markers

Georgian distinguishes **Subject Person Markers** (სუბიექტური პირის ნიშნები) and **Object Person Markers**
(ობიექტური პირის ნიშნები):

| Person | Subject Marker (S) | Object Marker (O) | Subject Example | Object Example |
|---|---|---|---|---|
| **1st sg** (I / me) | `ვ-` | `მ-` | `ვწერ` (I write) | `მწერს` (He writes to me) |
| **1st pl** (we / us) | `ვ-...-თ` | `გვ-` | `ვწერთ` (We write) | `გვწერს` (He writes to us) |
| **2nd sg** (you) | `∅-` | `გ-` | `წერ` (You write) | `გწერს` (He writes to you) |
| **2nd pl** (you all) | `∅-...-თ` | `გ-...-თ` | `წერთ` (You all write) | `გწერთ` (He writes to you all: `მოგწერათ`) |
| **3rd sg** (he/she/it) | `-ს`, `-ა`, `-ო` | `ჰ-`, `ს-`, `∅-` | `წერს`, `დაწერა`, `თქვას` | `ჰკითხა`, `სთხოვა`, `მისწერა` |
| **3rd pl** (they) | `-ენ`, `-ან`, `-ეს`, `-ნენ` | `ჰ-`, `ს-`, `∅-` | `წერენ`, `დაწერეს` | `ჰკითხეს`, `სთხოვეს`, `მისწერეს` |

---

## 2. Prefix Slot Competition (პირის ნიშანთა შეწყობა)

A verb root in Georgian has only **one prefix slot** for person. When both the subject and the object require
a prefix, they cannot co-occur.

> [!IMPORTANT]
> **The Object Prefix Wins:** In any clash between a subject prefix (`ვ-`) and an object prefix (`მ-`, `გ-`, `გვ-`),
> the **object prefix takes the slot** and the subject prefix disappears entirely.

### 1st Person Subject + 2nd Person Object (მე შენ / მე თქვენ)
- `მე შენ გწერ` (I write to you) — The object prefix `გ-` displaces subject `ვ-`.
  ❌ `*ვგწერ` or `*გვწერ` (in the sense of "I write to you").
- `მე თქვენ გწერთ` (I write to you all) — `გ-` prefix + `-თ` suffix.
- `ჩვენ თქვენ გწერთ` (We write to you all) — `გ-` prefix + `-თ` suffix.

### 2nd Person Subject + 1st Person Object (შენ მე / თქვენ მე / შენ ჩვენ)
- `შენ მე მწერ` (You write to me) — Object prefix `მ-`.
- `თქვენ მე მწერთ` (You all write to me) — Object prefix `მ-` + plural suffix `-თ`.
- `შენ ჩვენ გვწერ` (You write to us) — Object prefix `გვ-`.
- `თქვენ ჩვენ გვწერთ` (You all write to us) — Object prefix `გვ-` + plural suffix `-თ`.

---

## 3. The Plural Suffix `-თ` and 3rd Person Subjects

The suffix `-თ` marks plurality for either the subject or the object in the 1st and 2nd persons.
When combined with 3rd person subjects (he/she/they), pay close attention to who is plural:

| Sentence | Subject | Object | Verb Form | Explanation |
|---|---|---|---|---|
| `მან მე მომწერა` | 3rd sg (`მან`) | 1st sg (`მე`) | `მომწერა` | 3rd sg aorist `-ა`, 1st sg object `მ-` |
| `მან ჩვენ მოგვწერა` | 3rd sg (`მან`) | 1st pl (`ჩვენ`) | `მოგვწერა` | 1st pl object `გვ-` is inherently plural; no `-თ` |
| `მან შენ მოგწერა` | 3rd sg (`მან`) | 2nd sg (`შენ`) | `მოგწერა` | 2nd sg object `გ-` |
| `მან თქვენ მოგწერათ` | 3rd sg (`მან`) | 2nd pl / formal (`თქვენ`) | `მოგწერათ` | `-თ` pluralizes the 2nd person object |
| `მათ მე მომწერეს` | 3rd pl (`მათ`) | 1st sg (`მე`) | `მომწერეს` | `-ეს` marks 3rd pl subject |
| `მათ ჩვენ მოგვწერეს` | 3rd pl (`მათ`) | 1st pl (`ჩვენ`) | `მოგვწერეს` | `გვ-` (us) + `-ეს` (they) |
| `მათ შენ მოგწერეს` | 3rd pl (`მათ`) | 2nd sg (`შენ`) | `მოგწერეს` | `გ-` (you) + `-ეს` (they) |
| `მათ თქვენ მოგწერეს` | 3rd pl (`მათ`) | 2nd pl (`თქვენ`) | `მოგწერეს` | Literary standard avoids stacking `-თ` on `-ეს` |

> [!NOTE]
> `needs-review: მოგწერეს vs მოგწერესთ`
> In colloquial Georgian, `-თ` is sometimes added to 3rd person plural verbs when addressing a plural object
> (`მათ თქვენ მოგწერესთ`). In standard literary and news Georgian, the literary norm is `მათ თქვენ მოგწერეს`
> without stacking `-თ` onto the 3rd person plural suffix `-ეს`.

### The Crucial Distinction Table
Master these distinct forms:

- `მოგვწერა` = **He/she wrote to us** (`ჩვენ მოგვწერა`).
- `მოგწერათ` = **He/she wrote to you (plural/polite)** (`თქვენ მოგწერათ`).
- `მოგვწერეს` = **They wrote to us** (`მათ ჩვენ მოგვწერეს`).
- `მოგწერეს` = **They wrote to you** (`მათ თქვენ მოგწერეს`).
- `მოგწერეთ` = **We wrote to you / I wrote to you (plural/polite)** (`ჩვენ თქვენ მოგწერეთ`).
- `მოგწერე` = **I wrote to you (singular)** (`მე შენ მოგწერე`).

---

## 4. 3rd Person Indirect Object Markers: `ჰ-`, `ს-`, `∅-`

When the indirect object is 3rd person (`მას` / `მათ`), the verb marks it with `ჰ-`, `ს-`, or zero `∅-`.
The selection is strictly phonological based on the initial consonant of the verb stem (Shanidze's rule):

### `ჰ-` (Before labials and velars/uvulars)
Appears before: **ბ, ფ, პ, გ, ქ, კ, ყ**
- `ჰბაძავს` (imitates him)
- `ჰფარავს` (covers it)
- `ჰპასუხობს` (answers him)
- `ჰგონია` (thinks so)
- `ჰქონდა` (had it)
- `ჰკითხა` (asked him)
- `ჰყავს` (has him/them, animate)

### `ს-` (Before dentals, affricates, and sibilant stops)
Appears before: **დ, თ, ტ, ძ, ც, წ, ჯ, ჩ, ჭ**
- `სდევს` (chases him)
- `სთხოვა` (asked/requested of him)
- `სტყორცნა` (hurled at him)
- `სძულს` (hates him)
- `სცემს` (beats him / respects him: პატივს სცემს)
- `სცადა` (tried it)
- `სწერს` (writes to him)
- `სჭრის` (cuts for him)

### `∅-` (Zero Marker)
Appears:
1. Before spirants / sibilants: **ზ, ს, შ, ჟ, ხ** (to avoid unpronounceable clusters like `*სსწერს` or `*ჰხედავს`).
2. When a version vowel (`ი-`, `უ-`, `ე-`) is present:
   - `უთხრა` (told him, version vowel `უ-`)
   - `დაუწერა` (wrote for him)
   - `მისცა` (gave him, preverb `მი-` with root)
   - `აჩუქა` (gifted him)

> [!WARNING]
> **Direct Objects Never Take `ჰ-` / `ს-`!**
> `ჰ-` and `ს-` strictly mark **indirect objects** (მიცემითი ბრუნვის ირიბი ობიექტი).
> A 3rd person direct object (პირდაპირი ობიექტი) always takes **zero marker `∅-`**:
> - ✅ `მან წიგნი ნახა` (direct object: zero prefix)
> - ❌ `*მან წიგნი ჰნახა` (ungrammatical)
> - ✅ `მან მას წიგნი სთხოვა` (indirect object takes `ს-`)

> [!NOTE]
> `needs-review: omission of ჰ- and ს- in modern news`
> The classical grammatical standard mandates `ჰ-` and `ს-` (`ჰკითხა`, `სთხოვა`, `ჰგონია`, `სცადა`, `ჰპირდება`).
> In contemporary Georgian journalism and conversational speech, these markers are frequently dropped
> (`კითხა`, `თხოვა`, `გონია`, `ცადა`, `პირდება`).
> While colloquial text tolerates the omission, authoritative editorial styleguides and the State Language Department
> maintain that preserving `ჰ-` and `ს-` where phonetically required is the literary norm.

---

## 5. Common Anti-Patterns to Avoid

1. **Double Prefix Marking:**
   - ❌ `*ვგწერ` → ✅ `გწერ` (I write to you)
   - ❌ `*ვმალავთ` (when meaning "we hide you") → ✅ `გმალავთ`
2. **Double Plural with `გვ-`:**
   - `გვ-` already marks 1st person plural object ("us"). Do not append `-თ` for 1st person plural:
   - ❌ `*გვაქვსთ` → ✅ `გვაქვს`
   - ❌ `*გვინდათ` → ✅ `გვინდა`
   - ❌ `*გვწერსთ` → ✅ `გვწერს`
3. **Confusing `გვ-` (us) and `გ-` (you):**
   - ❌ `მომხმარებელმა მოგვწერა` (when informing a client "the user wrote to you") → ✅ `მომხმარებელმა მოგწერათ`
   - ❌ `ჩვენ მოგწერეთ` (when meaning "you wrote to us") → ✅ `თქვენ მოგვწერეთ`
4. **Missing `-თ` in Polite Direct Address:**
   - When addressing an audience, customer, or reader in the polite plural (`თქვენ`):
   - ❌ `გაცნობთ` / `გაცნობ` → ✅ `გაცნობებთ` / `გაგაცნობთ`
   - ❌ `შეგატყობინებ` → ✅ `შეგატყობინებთ`
   - ❌ `მოგწერა` (referring to a message to the client) → ✅ `მოგწერათ`

---

## 6. Book rules: subject sign ვ-

- Write the 1st-person subject sign ვ- even where it is not heard: it is not pronounced before the vowels უ and ო or before the consonant ვ, but it has to be written all the same. ✅ `ვუთხარი`, `ვოცნებობ`, `ვვარჯიშობ` (when the speaker is "I"). (Peikrishvili §79, point 1)
- In მოვედი and მოვალ the regular pattern would give a doubled ვ (მოვვედი, მოვვალ), but the 2nd person kept the Old Georgian marker ხ (მოხვედი, მოხვალ), so 1st and 2nd person are distinct anyway and the language easily lost the 1st-person ვ- prefix. ✅ `მოვედი`, `მოვალ`, `მოხვედი`, `მოხვალ`. The book records rare doubled forms in the written language (მოვვედი, შევვლე), for example in ვეფხისტყაოსანი. (Peikrishvili §77)
- The 1st person can be marked twice: once by the ვ- person sign and once by the auxiliary verb (the final -ვარ). These are regular forms and must not be "corrected": ✅ `ვშობილვარ`, `გავუგზავნივარ`, `ვზივარ`, `მივრბივარ`, `ვწერივარ`. This is not the "double prefix marking" of section 5, which is about two prefixes. (Peikrishvili §77)

## 7. Book rules: object prefixes that must not appear

- A 3rd-person direct object has no marker on the verb: ✅ `თქვა`, `გადაწყვიტა`, not `სთქვა`, `გადასწყვიტა`. The book calls such forms grammatically mistaken, and says they seem to come partly from analogy with the 3rd-person indirect object and partly from stylistic expressiveness. (Peikrishvili §79, point 7)
- Some one-person verbs are found with an object prefix on top of the subject marking; the book calls this incorrect: ✅ `შედგა`, `ჩანს`, `დუმს`, `ქუხს`, `ქრის`, not `შესდგა`, `სჩანს`, `სდუმს`, `ჰქუხს`, `ჰქრის`. It applies to the verbs the book lists and others like them, not to every one-person verb: verbs such as მძინავს and გღვიძავს are now one-person yet keep their two person signs. (Peikrishvili §79, point 2; §80 for the limit)
- A few verbs have only one person pattern (წყობა), subject or object: ვიცი only the subject pattern, მძინავს only the object pattern. In the object-only group the subject is always 3rd person (A. Shanidze), not the person the prefix shows. ✅ `მძინავს`, `გძინავს`, `სძინავს`, not `ვძინავარ`; ✅ `ვიცი`, `იცი`, `იცის`, not `მიცის`, `გიცის`. (Peikrishvili §80)

## 8. Book rules: aorist 3rd person plural

- In the aorist 3rd person plural, transitive verbs and the so-called defective verbs (no direct object, but a case-changing subject, as in იცხოვრა მან) end in -ეს, not -ენ. Intransitive verbs end in -ნენ, not -ენ. ✅ `გააკეთეს`, `იცხოვრეს`, `წავიდნენ`, not `გააკეთენ`, `იცხოვრენ`, `წავიდენ`. (Peikrishvili §115, points 2-3; defective verbs are described in §114)
