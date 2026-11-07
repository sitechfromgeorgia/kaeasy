# Dates, Numbers and Ordinals in Georgian

This reference documents the official rules for writing and declining numbers, dates, ordinals, time, currency, and quantities in standard Georgian.

Sources:
- Akaki Shanidze, *Fundamentals of Georgian Grammar* (საქართველოს მეცნიერებათა აკადემია)
- State Language Department of Georgia (სახელმწიფო ენის დეპარტამენტი: ენობრივი ნორმები და რეკომენდაციები)
- Legislative Herald of Georgia (*matsne.gov.ge*: ოფიციალური ნორმატიული ტექსტები და საერთაშორისო ხელშეკრულებები)
- *Explanatory Dictionary of the Georgian Language* (ქართული ენის განმარტებითი ლექსიკონი)

---

## 1. Calendar Dates: Cardinals, Not Ordinals

In Georgian, days of the month are expressed by **cardinal numbers** (რაოდენობითი რიცხვითი სახელი), **never ordinals** (რიგობითი რიცხვითი სახელი), with the sole exception of the first day of the month.

- **Only the 1st is an ordinal**:
  - ✅ `1 ნოემბერი` (spoken: `პირველი ნოემბერი`)
  - ✅ `1-ლი ნოემბერი` (spoken: `პირველი ნოემბერი`)
  - ✅ `1-ლ ნოემბერს` (spoken: `პირველ ნოემბერს`)
  - ❌ `1-ელი ნოემბერი` (flagged by linter; the first is written `1-ლი`)
- **All other days (2 to 31) are cardinals**:
  - ✅ `22 ნოემბერი` (spoken: `ოცდაორი ნოემბერი`)
  - ❌ `22-ე ნოემბერი` (flagged by linter)
  - ❌ `ოცდამეორე ნოემბერი` (flagged by linter)
  - ✅ `22 ნოემბერს` (spoken: `ოცდაორ ნოემბერს`)
  - ❌ `22-ე ნოემბერს`
  - ❌ `ოცდამეორე ნოემბერს`

### Word Order in Full Dates
In Georgian, the year always precedes the month, followed by the day:
- ✅ `2026 წლის 22 ნოემბერი` (or `2026 წლის 22 ნოემბერს`)
- ❌ `ნოემბერი 22, 2026` (English calque)
- ❌ `22 ნოემბერი 2026` (missing `წლის` and reversed order)

---

## 2. Declension of Dates Across All 12 Months

A numeral modifying a noun declines as an adjective:
- **Nominative**: Full form (`ოცდაორი ნოემბერი`, `ხუთი მარტი`)
- **Dative / Adverbial / with `-მდე`, `-ზე`, `-ში`**: Truncated stem (`ოცდაორ ნოემბერს`, `ხუთ მარტს`, `ოცდაორ ნოემბრამდე`, `ოცდაორ ნოემბერზე`)
- **Genitive / Ablative / with `-დან`, `-თვის`**: Full vowel-ending form (`ოცდაორი ნოემბრის`, `ხუთი მარტის`, `ოცდაორი ნოემბრიდან`, `ოცდაორი ნოემბრისთვის`)

### Stem Changes (კუმშვა/კვეცა) Across the 12 Months

1. **იანვარი** (syncopating: -არ- loses ა → იანვრ-)
   - Nom: `15 იანვარი` (`თხუთმეტი იანვარი`)
   - Dat: `15 იანვარს` (`თხუთმეტ იანვარს`)
   - Gen: `15 იანვრის` (`თხუთმეტი იანვრის`)
   - Term: `15 იანვრამდე` (`თხუთმეტ იანვრამდე`)
   - Abl: `15 იანვრიდან` (`თხუთმეტი იანვრიდან`)

2. **თებერვალი** (syncopating: -ალ- loses ა → თებერვლ-)
   - Nom: `20 თებერვალი` (`ოცი თებერვალი`)
   - Dat: `20 თებერვალს` (`ოც თებერვალს`)
   - Gen: `20 თებერვლის` (`ოცი თებერვლის`)
   - Term: `20 თებერვლამდე` (`ოც თებერვლამდე`)
   - Abl: `20 თებერვლიდან` (`ოცი თებერვლიდან`)

3. **მარტი** (vocalic root -ი)
   - Nom: `8 მარტი` (`რვა მარტი`)
   - Dat: `8 მარტს` (`რვა მარტს`)
   - Gen: `8 მარტის` (`რვა მარტის`)
   - Term: `8 მარტამდე` (`რვა მარტამდე`)
   - Abl: `8 მარტიდან` (`რვა მარტიდან`)

4. **აპრილი** (regular -ილ-)
   - Nom: `9 აპრილი` (`ცხრა აპრილი`)
   - Dat: `9 აპრილს` (`ცხრა აპრილს`)
   - Gen: `9 აპრილის` (`ცხრა აპრილის`)
   - Term: `9 აპრილამდე` (`ცხრა აპრილამდე`)
   - Abl: `9 აპრილიდან` (`ცხრა აპრილიდან`)

5. **მაისი** (regular)
   - Nom: `26 მაისი` (`ოცდაექვსი მაისი`)
   - Dat: `26 მაისს` (`ოცდაექვს მაისს`)
   - Gen: `26 მაისის` (`ოცდაექვსი მაისის`)
   - Term: `26 მაისამდე` (`ოცდაექვს მაისამდე`)
   - Abl: `26 მაისიდან` (`ოცდაექვსი მაისიდან`)

6. **ივნისი** (regular)
   - Nom: `1 ივნისი` (`პირველი ივნისი`)
   - Dat: `1 ივნისს` (`პირველ ივნისს`)
   - Gen: `1 ივნისის` (`პირველი ივნისის`)
   - Term: `1 ივნისამდე` (`პირველ ივნისამდე`)
   - Abl: `1 ივნისიდან` (`პირველი ივნისიდან`)

7. **ივლისი** (regular)
   - Nom: `10 ივლისი` (`ათი ივლისი`)
   - Dat: `10 ივლისს` (`ათ ივლისს`)
   - Gen: `10 ივლისის` (`ათი ივლისის`)
   - Term: `10 ივლისამდე` (`ათ ივლისამდე`)
   - Abl: `10 ივლისიდან` (`ათი ივლისიდან`)

8. **აგვისტო** (vowel-final -ო: does not truncate or drop stem vowel)
   - Nom: `12 აგვისტო` (`თორმეტი აგვისტო`)
   - Dat: `12 აგვისტოს` (`თორმეტ აგვისტოს`)
   - Gen: `12 აგვისტოს` (`თორმეტი აგვისტოს` / იშვიათად `აგვისტოსი`)
   - Term: `12 აგვისტომდე` (`თორმეტ აგვისტომდე`)
   - Abl: `12 აგვისტოდან` (`თორმეტი აგვისტოდან`)

9. **სექტემბერი** (syncopating: -ერ- loses ე → სექტემბრ-)
   - Nom: `15 სექტემბერი` (`თხუთმეტი სექტემბერი`)
   - Dat: `15 სექტემბერს` (`თხუთმეტ სექტემბერს`)
   - Gen: `15 სექტემბრის` (`თხუთმეტი სექტემბრის`)
   - Term: `15 სექტემბრამდე` (`თხუთმეტ სექტემბრამდე`)
   - Abl: `15 სექტემბრიდან` (`თხუთმეტი სექტემბრიდან`)

10. **ოქტომბერი** (syncopating: -ერ- loses ე → ოქტომბრ-)
    - Nom: `14 ოქტომბერი` (`თოთხმეტი ოქტომბერი`)
    - Dat: `14 ოქტომბერს` (`თოთხმეტ ოქტომბერს`)
    - Gen: `14 ოქტომბრის` (`თოთხმეტი ოქტომბრის`)
    - Term: `14 ოქტომბრამდე` (`თოთხმეტ ოქტომბრამდე`)
    - Abl: `14 ოქტომბრიდან` (`თოთხმეტი ოქტომბრიდან`)

11. **ნოემბერი** (syncopating: -ერ- loses ე → ნოემბრ-)
    - Nom: `22 ნოემბერი` (`ოცდაორი ნოემბერი`)
    - Dat: `22 ნოემბერს` (`ოცდაორ ნოემბერს`)
    - Gen: `22 ნოემბრის` (`ოცდაორი ნოემბრის`)
    - Term: `22 ნოემბრამდე` (`ოცდაორ ნოემბრამდე`)
    - Abl: `22 ნოემბრიდან` (`ოცდაორი ნოემბრიდან`)

12. **დეკემბერი** (syncopating: -ერ- loses ე → დეკემბრ-)
    - Nom: `31 დეკემბერი` (`ოცდათერთმეტი დეკემბერი`)
    - Dat: `31 დეკემბერს` (`ოცდათერთმეტ დეკემბერს`)
    - Gen: `31 დეკემბრის` (`ოცდათერთმეტი დეკემბრის`)
    - Term: `31 დეკემბრამდე` (`ოცდათერთმეტ დეკემბრამდე`)
    - Abl: `31 დეკემბრიდან` (`ოცდათერთმეტი დეკემბრიდან`)

---

## 3. Years, Decades, Centuries and Day Ranges

### Years
- `2026 წელი` (Nom)
- `2026 წელს` (Dat)
- `2026 წლის` (Gen)
- `2026 წლიდან` (Abl)
- `2026 წლამდე` (Term)

### Decades
- `90-იანი წლები` (Nom)
- `90-იან წლებში` (Dat/Inessive)
- `90-იანი წლების` (Gen)
- `2020-იანი წლები`
- ❌ `90-იანები` in formal prose; write `90-იანი წლები`.

### Centuries
In Georgian, centuries are predominantly written with Roman numerals without `-ე`:
- ✅ `XXI საუკუნე` (spoken: `ოცდამეერთე საუკუნე`)
- ✅ `XX საუკუნეში` (spoken: `მეოცე საუკუნეში`)
- ✅ `XIX საუკუნის` (spoken: `მეცხრამეტე საუკუნის`)
- ❌ `XXI-ე საუკუნე` (redundant; Roman numerals are ordinals already)
- If Arabic numerals are used: `21-ე საუკუნე` (acceptable, but Roman `XXI საუკუნე` preferred in literary style).

### Day Ranges
- Written: `10-14 ოქტომბერს` (with hyphen, no spaces)
- Spoken: `ათიდან თოთხმეტ ოქტომბრამდე`
- Do not write: `10-დან 14 ოქტომბრამდე` in compact headlines (in body copy both are valid, but avoid `10-14 ოქტომბრამდე` which mixes hyphen and suffix).

---

## 4. Where Ordinals ARE Correct

Ordinals (`მე-...-ე`) are correct whenever expressing sequence, rank, chapter, article, or hierarchical order:

- **Legal articles and sections**:
  - `მე-5 მუხლი` (`მეხუთე მუხლი`)
  - `180-ე მუხლი` (`ას მეოთხმოცე მუხლი`)
  - `353-ე მუხლი` (`სამას ორმოცდამეცამეტე მუხლი`)
  - `353¹-ე მუხლი` (`სამას ორმოცდამეცამეტე პრიმა მუხლი`)
- **Floors**:
  - `მე-2 სართული` (`მეორე სართული`)
  - `მე-5 სართულზე` (`მეხუთე სართულზე`)
- **Places and rankings**:
  - `1-ლი ადგილი` / `პირველი ადგილი`
  - `მე-2 ადგილი` (`მეორე ადგილი`)
  - `მე-3 ადგილი` (`მესამე ადგილი`)
- **School grades**:
  - `1-ლი კლასი` (`პირველი კლასი`)
  - `მე-7 კლასი` (`მეშვიდე კლასი`)
  - `მე-11 კლასი` (`მეთერთმეტე კლასი`)
- **Editions, sessions, and conferences**:
  - `მე-3 გამოცემა` (`მესამე გამოცემა`)
  - `მე-10 სესია` (`მეათე სესია`)

---

## 5. Ordinals Above 100: Morphology and Rules

In Georgian grammar (Shanidze, *Grammar of Georgian*, §151; confirmed by *matsne.gov.ge*):
- When forming compound ordinals, **only the final component** receives the circumfix `მე-...-ე`.
- Preceding components (hundreds, thousands, millions) remain in their bare cardinal stem form (`ას`, `ორას`, `სამას`, `ათას`, `ორი ათას`).
- If the final unit is 1 in a compound, it becomes **`მეერთე`** (never `პირველი`): `21-ე` is `ოცდამეერთე`, `101-ე` is `ას მეერთე`, `1001-ე` is `ათას მეერთე`.
- Tens and twenties: 80 is `ოთხმოცი`, its ordinal is `მეოთხმოცე`. Therefore, `180-ე` is **`ას მეოთხმოცე`** (never `ას ოთხმოცი` or `ას ოთხმოცე`).
- **Ordinals in digits** (Peikrishvili §59): if the spoken word starts with `მე-`, write `მე-` and then the digits:
  `მე-5`, `მე-40`, `მე-100`, `მე-1000`. Otherwise write the digits and then `-ე`: `21-ე`, `30-ე`, `101-ე`, `180-ე`.
  The first is `1-ლი`, and its case forms keep the hyphen: `1-ლ ნოემბერს`, `1-ლში`. `ka_lint` flags `1-ელი` and
  `100-ე` (Louie confirmed `1-ლი`, 2026-11-07).
- **Spacing**: Peikrishvili writes a compound ordinal as one word (`ასმეერთე`). Kaeasy keeps it spaced, like the
  cardinals and *matsne.gov.ge*: `ას მეერთე`, `ორი ათას ოცდამეექვსე` (decided by Louie, 2026-11-07).
- **The multiplier of ათასი stays nominative** in every case (Peikrishvili §59): `ორი ათასი კაცი`,
  `ორი ათას კაცს`, `სამი ათასმა კაცმა`. ❌ `ორ ათას კაცს` (flagged by `ka_lint`; Louie confirmed, 2026-11-07).

### Reference Table: Ordinals from 100 to 2000+

| Digits | Ordinal Spoken Form | Note / Source |
|---|---|---|
| `მე-100` | `მეასე` | The word starts with `მე-`, so the digits follow `მე-` |
| `101-ე` | `ას მეერთე` | Compound 1 becomes `მეერთე` |
| `102-ე` | `ას მეორე` | Preceding hundred is stem `ას` |
| `110-ე` | `ას მეათე` | `ათი` → `მეათე` |
| `120-ე` | `ას მეოცე` | `ოცი` → `მეოცე` |
| `150-ე` | `ას ორმოცდამეათე` | `ორმოცდაათი` → `ორმოცდამეათე` |
| `180-ე` | `ას მეოთხმოცე` | Confirmed by matsne.gov.ge: `180-ე (ას მეოთხმოცე)` |
| `მე-200` | `მეორასე` | `ორასი` → `მეორასე` |
| `201-ე` | `ორას მეერთე` | Preceding hundred is stem `ორას` |
| `მე-300` | `მესამასე` | `სამასი` → `მესამასე` |
| `353-ე` | `სამას ორმოცდამეცამეტე` | `300` (`სამას`) + `53` (`ორმოცდამეცამეტე`) |
| `მე-400` | `მეოთხასე` | `ოთხასი` → `მეოთხასე` |
| `მე-500` | `მეხუთასე` | `ხუთასი` → `მეხუთასე` |
| `მე-600` | `მეექვსასე` | `ექვსასი` → `მეექვსასე` |
| `მე-700` | `მეშვიდასე` | `შვიდასი` → `მეშვიდასე` |
| `მე-800` | `მერვაასე` | `რვაასი` → `მერვაასე` |
| `მე-900` | `მეცხრაასე` | `ცხრაასი` → `მეცხრაასე` |
| `მე-1000` | `მეათასე` | `ათასი` → `მეათასე` |
| `1001-ე` | `ათას მეერთე` | `1000` (`ათას`) + `1` (`მეერთე`) |
| `1180-ე` | `ათას ას მეოთხმოცე` | Stem + stem + ordinal |
| `მე-2000` | `მეორიათასე` | Even two thousand: `მეორიათასე` |
| `2026-ე` | `ორი ათას ოცდამეექვსე` | `2000` (`ორი ათას`) + `26` (`ოცდამეექვსე`) |

### Declension Before Nouns
Ordinals ending in `-ე` are vocalic stems that do **not** drop `-ე` before nouns:
- `180-ე მუხლი` (Nom: `ას მეოთხმოცე მუხლი`)
- `180-ე მუხლს` (Dat: `ას მეოთხმოცე მუხლს`)
- `180-ე მუხლის` (Gen: `ას მეოთხმოცე მუხლის`)
- `180-ე მუხლით` (Inst: `ას მეოთხმოცე მუხლით`)
- `180-ე მუხლამდე` (Term: `ას მეოთხმოცე მუხლამდე`)

Exception: `პირველი` ends in consonant stem `-ელ-` + `-ი`:
- `პირველი მუხლი` (Nom)
- `პირველ მუხლს` (Dat: drops `-ი`)
- `პირველი მუხლის` (Gen)
- `პირველმა მუხლმა` (Erg: drops `-ი` before `-მა`)

---

## 6. Base-20 (Vigesimal) Cardinal System and Case Declension

Georgian numbers from 20 to 99 are counted in twenties:
- `20` = `ოცი`
- `30` = `20 + 10` = `ოცდაათი`
- `40` = `2 × 20` = `ორმოცი`
- `50` = `2 × 20 + 10` = `ორმოცდაათი`
- `60` = `3 × 20` = `სამოცი`
- `70` = `3 × 20 + 10` = `სამოცდაათი`
- `80` = `4 × 20` = `ოთხმოცი`
- `90` = `4 × 20 + 10` = `ოთხმოცდაათი`
- `100` = `ასი`
- `1000` = `ათასი`

### Cardinal Declension Modifying a Noun

| Case | Standalone Cardinal | Preceding a Noun (e.g. დღე) |
|---|---|---|
| **სახელობითი** (Nom) | `ოცი`, `ორმოცდაათი`, `ასი` | `ოცი დღე`, `ორმოცდაათი დღე`, `ასი დღე` |
| **მოთხრობითი** (Erg) | `ოცმა`, `ორმოცდაათმა`, `ასმა` | `ოცმა დღემ`, `ორმოცდაათმა დღემ`, `ასმა დღემ` |
| **მიცემითი** (Dat) | `ოცს`, `ორმოცდაათს`, `ასს` | `ოც დღეს`, `ორმოცდაათ დღეს`, `ას დღეს` (stem) |
| **ნათესაობითი** (Gen) | `ოცის`, `ორმოცდაათის`, `ასის` | `ოცი დღის`, `ორმოცდაათი დღის`, `ასი დღის` (ends in -ი) |
| **მოქმედებითი** (Inst) | `ოცით`, `ორმოცდაათით`, `ასით` | `ოცი დღით`, `ორმოცდაათი დღით`, `ასი დღით` |
| **ვითარებითი** (Adv) | `ოცად`, `ორმოცდაათად`, `ასად` | `ოც დღედ`, `ორმოცდაათ დღედ`, `ას დღედ` (stem) |
| **თანდებული `-მდე`** | `ოცამდე`, `ორმოცდაათამდე`, `ასამდე` | `ოც დღემდე`, `ორმოცდაათ დღემდე`, `ას დღემდე` (stem) |
| **თანდებული `-დან`** | `ოციდან`, `ორმოცდაათიდან`, `ასიდან` | `ოცი დღიდან`, `ორმოცდაათი დღიდან`, `ასი დღიდან` |
| **თანდებული `-ზე`** | `ოცზე`, `ორმოცდაათზე`, `ასზე` | `ოც დღეზე`, `ორმოცდაათ დღეზე`, `ას დღეზე` (stem) |
| **თანდებული `-ში`** | `ოცში`, `ორმოცდაათში`, `ასში` | `ოც დღეში`, `ორმოცდაათ დღეში`, `ას დღეში` (stem) |

---

## 7. Quantities, Money, Percent, Decimals, Time and Other Traps

### Percent
- Written glued: `25%`, `36%-ით`, `40%-მდე`. ❌ `25 %`.
- Range: `20-30%`. ❌ `20%-დან 30%-მდე`.
- Spoken with case:
  - `36%` → `ოცდათექვსმეტი პროცენტი`
  - `36%-ს` → `ოცდათექვსმეტ პროცენტს` (stem)
  - `36%-ის` → `ოცდათექვსმეტი პროცენტის`
  - `36%-ით` → `ოცდათექვსმეტი პროცენტით`
  - `40%-მდე` → `ორმოც პროცენტამდე` (stem)
  - `50%-ზე` → `ორმოცდაათ პროცენტზე` (stem)

### Decimals and Halves
- Decimal comma: `3,5%`, `2,5 მილიარდი`. ❌ `3.5%`.
- `.5` values up to 20 use `...ნახევარი`:
  - `0,5` → `ნახევარი`
  - `1,5` → `ერთნახევარი`
  - `2,5` → `ორნახევარი`
  - `3,5` → `სამნახევარი`
  - `10,5` → `ათნახევარი`
- A number and `ნახევარი` are one word (`ოთხნახევარი`), though Peikrishvili hyphenates them (`ოთხ-ნახევარი`).
  A unit word takes a hyphen: `კილო-ნახევარი`, `ტონა-ნახევარი`, `საათ-ნახევარი` (Peikrishvili §56; decided by
  Louie, 2026-11-07).
- Higher decimals use `მთელი`:
  - `25,4` → `ოცდახუთი მთელი ოთხი მეათედი`
  - `12,75` → `თორმეტი მთელი სამოცდათხუთმეტი მეასედი`

### Money
- Currency sign placed before: `$50`, `€100`, `₾500`.
- Case suffix attached to digits: `$50-ით` (`ორმოცდაათი დოლარით`), `$100-ად` (`ას დოლარად`), `₾200-მდე` (`ორას ლარამდე`).
- Written prose: `100 მილიონი დოლარი` or `$100 მლნ`.

### Time of Day
- Written: `15:30 საათზე`, `09:00 საათიდან`, `18:00 საათამდე`.
- Spoken:
  - `15:30 საათზე` → `თხუთმეტ საათსა და ოცდაათ წუთზე`
  - `09:00 საათიდან` → `ცხრა საათიდან`
  - `18:00 საათამდე` → `თვრამეტ საათამდე`

### Temperature
- Written: `25°C`, `-5°C`, `30°C-მდე`.
- Spoken:
  - `25°C` → `ოცდახუთი გრადუსი`
  - `-5°C` → `მინუს ხუთი გრადუსი`
  - `30°C-მდე` → `ოცდაათ გრადუსამდე`

### Phone Numbers
- Written: `+995 599 12 34 56`
- Spoken in standard groupings: `პლუს ცხრაას ოთხმოცდათხუთმეტი, ხუთი ცხრა ცხრა...`

### Versions and Document Numbers
- Versions: `v3.8` (spoken: `ვერსია სამი წერტილი რვა`), `Opus 4.7` (spoken: `ოპუს ოთხი წერტილი შვიდი`).
- Document numbers: `№123 ბრძანება` / `N123 დადგენილება` (spoken: `ნომერი ას ოცდასამი დადგენილება`).
