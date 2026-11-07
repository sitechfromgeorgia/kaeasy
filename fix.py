"""Mechanical Georgian fixes: only what ka_lint's strict rules flag and a machine can fix without judgment.

Ported from the hub's ge_ka_fix.py fix_text() (no database parts). Grammar, word choice and case endings are
never touched: those need the writer. HTML tags, `code`, fenced code blocks and URLs are left as they are.
"""
from __future__ import annotations

import re

from .lint import MONTH_DAY, MONTH_FORM, TRANSLIT, TRANSLIT_RE

# Spans the fixer must not change: HTML tags, fenced code, inline code, <pre>/<code> blocks, URLs and e-mails.
PROTECTED = re.compile(r"```.*?```|`[^`\n]*`|<(pre|code)\b[^>]*>.*?</\1>|<[^>]+>|https?://\S+|www\.\S+|[\w.+-]+@[\w-]+\.[\w.]+", re.DOTALL)


def fix_text(text: str) -> tuple[str, list[str]]:
    """Return (fixed text, list of applied fixes)."""
    if not text:
        return text, []
    changes: list[str] = []
    kept: list[str] = []

    def stash(m: re.Match) -> str:
        kept.append(m.group(0))
        return f"\x00{len(kept) - 1}\x00"

    out = PROTECTED.sub(stash, text)

    def sub(pattern: str, repl, name: str, flags: int = 0) -> None:
        nonlocal out
        out, n = re.subn(pattern, repl, out, flags=flags)
        if n:
            changes.append(f"{name}×{n}")

    # English quotes → „…“ (a „ opened with a straight closing quote first, then plain pairs).
    sub(r'„([^"“”\n\x00]{1,200}?)"', r"„\1“", "quotes")
    sub(r'"([^"“”„\n\x00]{1,200}?)"', r"„\1“", "quotes")
    sub(r"(?<!\.)\.\.\.(?!\.)", "…", "ellipsis")
    sub(r"(?<=\S)  +(?=\S)", " ", "double_space")
    sub(r"(?<=[ა-ჰA-Za-z0-9»“)]) +([,;:!?])", r"\1", "space_punct")
    sub(r"(\d)\s+%", r"\1%", "percent")
    sub(r"%\s+-\s*([ა-ჰ])", r"%-\1", "percent")
    sub(r"(\d)\.(\d+)(\s*(?:მილიარდ|მილიონ|ათას|%))", r"\1,\2\3", "decimal")
    # Latin word + Georgian case ending: glued (Metaის) or spaced (Meta -ის, Meta- ის) → Meta-ის.
    sub(r"\b([A-Za-z][A-Za-z0-9.]*[A-Za-z0-9])((?:მა|მ|ის|ს|ით|ზე|ში|თვის|ებ|დან|მდე|ად|თან)[ა-ჰ]*)", r"\1-\2",
        "ending_hyphen")
    sub(r"\b([A-Za-z][A-Za-z0-9.]*)(?:\s+-\s*|-\s+)(მა|ის|ს|ით|ზე|ში|მ)(?![ა-ჰ])", r"\1-\2", "ending_hyphen")
    sub(r"\b([A-Za-z][A-Za-z0-9.]*[A-Za-z0-9]) (მა|მ|ს|ით|ზე|ში|დან|მდე|ად|ები)(?![ა-ჰ])", r"\1-\2", "ending_hyphen")
    # Dashes are banned in Georgian copy (Edo's rule, 2026-09-25): ranges get a hyphen, asides a spaced hyphen.
    sub(r"(?<=\d)[–—](?=\d)", "-", "dash")
    sub(r"\s*[–—]\s*", " - ", "dash")
    # Ordinal day of month: 22-ე ნოემბრის, მე-22 ნოემბერს → 22 ნოემბერს. Day 1 stays 1-ლი.
    sub(rf"(?<![\w-])(?:მე-)?({MONTH_DAY})-ე\s+({MONTH_FORM})(?![ა-ჰ])", r"\1 \2", "ordinal_date")
    sub(rf"(?<![\w-])მე-({MONTH_DAY})\s+({MONTH_FORM})(?![ა-ჰ])", r"\1 \2", "ordinal_date")
    # Forms ვერცერთი and არცერთი inherently contain negation; remove redundant არ or ვერ before the verb.
    sub(r"(?<![ა-ჰ])(ვერცერთ[ა-ჰ]*|არცერთ[ა-ჰ]*)([^,.;:!?\n\r]*?)\s+(?:არ|ვერ)\s+", r"\1\2 ", "negation")

    for ka, rx in TRANSLIT_RE.items():
        def latin(m: re.Match, ka: str = ka) -> str:
            ending = m.group(0)[len(ka):]
            changes.append(f"translit: {m.group(0)} → {TRANSLIT[ka]}{'-' + ending if ending else ''}")
            return TRANSLIT[ka] + ("-" + ending if ending else "")
        out = rx.sub(latin, out)

    out = re.sub(r"\x00(\d+)\x00", lambda m: kept[int(m.group(1))], out)
    return out, changes
