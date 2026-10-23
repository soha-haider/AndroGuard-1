"""Vulnerable-API dataset: every row of vuln_apis.csv becomes a rule, so a new API is detected by adding a row.
Columns: rule_id, category, title, severity, confidence, masvs (';'-separated), exploitability, exploit_reason,
pattern (regex over Java/Kotlin/manifest text), hint (lowercase substring the file must contain, optional),
example (a line the pattern must match, checked by tests/test_dataset.py), cause, description, remediation, source."""
import csv
import re
from pathlib import Path

CSV = Path(__file__).with_name("vuln_apis.csv")
LEVELS = ("CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO")


def load(path: Path = CSV):
    """Returns (kb, rules, hints, rows) in the same layout as the M1/M2 knowledge bases. Bad rows fail loudly."""
    kb, rules, hints, rows = {}, {}, {}, []
    with open(path, newline="", encoding="utf-8") as f:
        for n, row in enumerate(csv.DictReader(f), start=2):
            rid = row["rule_id"].strip()
            if rid in kb or row["severity"] not in LEVELS or row["exploitability"] not in ("HIGH", "MEDIUM", "LOW"):
                raise ValueError(f"{path.name} line {n}: duplicate rule_id or bad severity/exploitability ({rid})")
            masvs = [m.strip() for m in row["masvs"].split(";") if m.strip()]
            kb[rid] = (row["category"], row["title"], row["severity"], float(row["confidence"]), masvs, [],
                       row["cause"], row["description"], row["remediation"])
            rules[rid] = re.compile(row["pattern"])
            if row["hint"]:
                hints[rid] = (row["hint"].lower(),)
            rows.append(row)
    return kb, rules, hints, rows


KB, RULES, HINTS, ROWS = load()
EXPLOIT = {r["rule_id"]: (r["exploitability"], r["exploit_reason"]) for r in ROWS}
SOURCES = {r["rule_id"]: r["source"] for r in ROWS}
