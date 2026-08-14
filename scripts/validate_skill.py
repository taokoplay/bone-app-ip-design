#!/usr/bin/env python3
"""Structural validation for bone-app-ip-design. Does not replace behavioral evals."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "SKILL.md"
errors: list[str] = []


def check(condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


text = SKILL.read_text(encoding="utf-8")
lines = text.splitlines()
check(text.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
check('name: bone-app-ip-design' in text, "frontmatter name mismatch")
check('version: "1.3.0"' in text, "version must be 1.3.0")
check(len(lines) <= 330, f"SKILL.md exceeds 330 lines: {len(lines)}")
check(text.count("```") % 2 == 0, "SKILL.md has unbalanced fenced code blocks")

refs = re.findall(r"\]\((references/[^)]+\.md)\)", text)
check(len(refs) >= 7, "SKILL.md should explicitly route to all reference files")
for rel in refs:
    check((ROOT / rel).exists(), f"missing reference: {rel}")

all_md = [SKILL, *sorted((ROOT / "references").glob("*.md"))]
for path in all_md:
    body = path.read_text(encoding="utf-8")
    check(body.count("```") % 2 == 0, f"unbalanced fenced code blocks: {path.relative_to(ROOT)}")

try:
    evals = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
    items = evals.get("evals", [])
    check(evals.get("skill_name") == "bone-app-ip-design", "eval skill_name mismatch")
    check(len(items) >= 15, f"expected at least 15 task evals, got {len(items)}")
    ids = [x.get("id") for x in items]
    check(len(ids) == len(set(ids)), "duplicate task eval ids")
    for item in items:
        check(len(item.get("expectations", [])) >= 3, f"eval {item.get('id')} lacks atomic expectations")
        for rel in item.get("files", []):
            check((ROOT / rel).exists(), f"eval {item.get('id')} missing fixture: {rel}")
except Exception as exc:
    errors.append(f"invalid evals.json: {exc}")

try:
    triggers = json.loads((ROOT / "evals/trigger-evals.json").read_text(encoding="utf-8"))
    positives = sum(1 for x in triggers if x.get("should_trigger") is True)
    negatives = sum(1 for x in triggers if x.get("should_trigger") is False)
    check(len(triggers) >= 20, f"expected at least 20 trigger evals, got {len(triggers)}")
    check(positives >= 10 and negatives >= 10, f"trigger eval balance too low: +{positives}/-{negatives}")
except Exception as exc:
    errors.append(f"invalid trigger-evals.json: {exc}")

for forbidden in [
    "正式母版：1024×1024 PNG、无 Alpha",
    "missed/error",
    "体积增加通常不超过角色宽度的 5–10%",
    "主色 60%+",
]:
    check(forbidden not in text, f"obsolete hard rule remains in SKILL.md: {forbidden}")

# Eval fixtures must state that they are synthetic and not real project data.
fixture_notice = "Synthetic eval"
for path in sorted((ROOT / "evals/fixtures").glob("*")):
    if path.is_file():
        body = path.read_text(encoding="utf-8")
        check(fixture_notice.lower() in body.lower() or "合成测试数据" in body,
              f"fixture lacks synthetic-data notice: {path.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    for err in errors:
        print(f"- {err}")
    sys.exit(1)

print("VALIDATION PASSED")
print(f"SKILL.md lines: {len(lines)}")
print(f"references routed: {len(set(refs))}")
print(f"task evals: {len(items)}")
print(f"trigger evals: {len(triggers)} (+{positives}/-{negatives})")
