# Speech Normalization for Dates, Numbers and Ordinals (TTS)

This reference defines how written numbers, dates, ordinals, time, percent, and currencies are normalized into spoken Georgian (`speech_text`) for TTS engines (Gemini TTS, Azure Speech, Edge-TTS, Piper).

Source: SiTech Shorts `normalize_ka.py` and Kaeasy `speech.py` specification.

---

## 1. Calendar Dates: Cardinals in Speech

In spoken Georgian text, calendar days (except the first) must be converted into **cardinals**, matching the case of the month:

| Written Form | Spoken Form (`speech_text`) | Case / Pattern |
|---|---|---|
| `1 იანვარი` | `პირველი იანვარი` | Ordinal (nominative) |
| `1 იანვარს` | `პირველ იანვარს` | Ordinal (dative stem) |
| `1 იანვრის` | `პირველი იანვრის` | Ordinal (genitive) |
| `1 იანვრამდე` | `პირველ იანვრამდე` | Ordinal (terminative stem) |
| `1 იანვრიდან` | `პირველი იანვრიდან` | Ordinal (ablative) |
| `22 ნოემბერი` | `ოცდაორი ნოემბერი` | Cardinal (nominative) |
| `22 ნოემბერს` | `ოცდაორ ნოემბერს` | Cardinal (dative stem) |
| `22 ნოემბრის` | `ოცდაორი ნოემბრის` | Cardinal (genitive) |
| `22 ნოემბრამდე` | `ოცდაორ ნოემბრამდე` | Cardinal (terminative stem) |
| `22 ნოემბრიდან` | `ოცდაორი ნოემბრიდან` | Cardinal (ablative) |
| `22-ე ნოემბერს` | `ოცდაორ ნოემბერს` | Normalized from errant ordinal notation |
| `10-14 ოქტომბერს` | `ათიდან თოთხმეტ ოქტომბრამდე` | Date range spoken with `-დან ... -მდე` |
| `2026 წლის 22 ნოემბერს` | `ორი ათას ოცდაექვსი წლის ოცდაორ ნოემბერს` | Full year + day dative |

---

## 2. Ordinals Above 100 in Speech

When reading articles, laws, floors, and ranks:

| Written Form | Spoken Form (`speech_text`) | Note |
|---|---|---|
| `მე-100` | `მეასე` | Even hundred |
| `101-ე` | `ას მეერთე` | `1` becomes `მეერთე` in compounds |
| `102-ე` | `ას მეორე` | Preceding hundred remains stem `ას` |
| `110-ე` | `ას მეათე` | `10` becomes `მეათე` |
| `120-ე` | `ას მეოცე` | `20` becomes `მეოცე` |
| `150-ე` | `ას ორმოცდამეათე` | `50` becomes `ორმოცდამეათე` |
| `180-ე მუხლი` | `ას მეოთხმოცე მუხლი` | Matsne verified: `180-ე (ას მეოთხმოცე)` |
| `180-ე მუხლს` | `ას მეოთხმოცე მუხლს` | `-ე` does not truncate before noun |
| `მე-200` | `მეორასე` | Even two hundred |
| `201-ე` | `ორას მეერთე` | `ორას` + `მეერთე` |
| `მე-300` | `მესამასე` | Even three hundred |
| `353-ე მუხლი` | `სამას ორმოცდამეცამეტე მუხლი` | `სამას` + `ორმოცდამეცამეტე` |
| `353¹-ე მუხლი` | `სამას ორმოცდამეცამეტე პრიმა მუხლი` | Prime article read with `პრიმა` |
| `მე-1000` | `მეათასე` | Even thousand |
| `1001-ე` | `ათას მეერთე` | `ათას` + `მეერთე` |
| `მე-2000` | `მეორიათასე` | Even two thousand |
| `2026-ე` | `ორი ათას ოცდამეექვსე` | `ორი ათას` + `ოცდამეექვსე` |

---

## 3. Clock Times, Percent and Currencies

- **Clock times**:
  - `15:30 საათზე` → `თხუთმეტ საათსა და ოცდაათ წუთზე`
  - `09:00 საათიდან` → `ცხრა საათიდან`
  - `18:00 საათამდე` → `თვრამეტ საათამდე`
- **Percent**:
  - `36%` → `ოცდათექვსმეტი პროცენტი`
  - `36%-ით` → `ოცდათექვსმეტი პროცენტით`
  - `40%-მდე` → `ორმოც პროცენტამდე`
- **Currency**:
  - `$50-ით` → `ორმოცდაათი დოლარით`
  - `$100-ად` → `ას დოლარად`
  - `₾200-მდე` → `ორას ლარამდე`
- **Decimals**:
  - `1,5` → `ერთნახევარი`
  - `2,5` → `ორნახევარი`
  - `3,5` → `სამნახევარი`
  - `4,2` → `ოთხი მთელი ორი მეათედი`
