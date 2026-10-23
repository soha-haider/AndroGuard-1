"""Ghera benchmark: python -m eval.ghera   (Ghera checked out in data/ghera, see eval/ghera.json for the method)
Scans each benchmark's vulnerable (Benign/) and fixed (Secure/) source project once; reports are cached in data/eval/ghera/."""
import json
from pathlib import Path
from app.pipeline import scan_source

ROOT = Path(__file__).resolve().parents[1]
GHERA, CACHE = ROOT / "data" / "ghera", ROOT / "data" / "eval" / "ghera"


def categories(name: str, version: str) -> set[str] | None:
    project = GHERA / name / version
    if not project.is_dir():
        return None
    path = CACHE / f"{name.replace('/', '__')}__{version}.json"
    if not path.exists():
        print(f"scanning {name} {version}...", flush=True)
        path.write_text(json.dumps(scan_source(project, progress=lambda m: None), indent=1), encoding="utf-8")
    return {f["category"] for f in json.loads(path.read_text(encoding="utf-8"))["findings"]}


if __name__ == "__main__":
    gt = json.loads((ROOT / "eval" / "ghera.json").read_text(encoding="utf-8"))
    CACHE.mkdir(parents=True, exist_ok=True)
    rows, skipped, out = [], [], []
    for name, expected in gt["benchmarks"].items():
        if not isinstance(expected, str):
            out.append(f"| {name} | {expected['out_of_scope']} |")
            continue
        vuln, fixed = categories(name, "Benign"), categories(name, "Secure")
        if vuln is None or fixed is None:
            skipped.append(name)
            continue
        rows.append((name, expected, expected in vuln, expected in fixed))
    scored, found = len(rows), sum(r[2] for r in rows)
    alarms = sum(r[3] for r in rows)
    lines = [f"# AndroGuard on Ghera ({scored} in-scope benchmarks scanned as source)", "",
             f"Detected **{found} of {scored}** (recall {found / scored:.3f}). The fixed version was still flagged in the "
             f"same category in **{alarms} of {scored}** (false-alarm rate on fixed apps {alarms / scored:.3f}). "
             f"{len(out)} benchmarks are out of scope (no rule for that weakness).", "",
             "| Benchmark | Expected category | Vulnerable app | Fixed app |", "|---|---|---|---|"]
    lines += [f"| {n} | {c} | {'detected' if v else 'missed'} | {'still flagged' if s else 'clean'} |" for n, c, v, s in rows]
    if skipped:
        lines += ["", "Not scanned (no source project for both versions): " + ", ".join(skipped)]
    lines += ["", "## Out of scope", "", "| Benchmark | Why |", "|---|---|"] + out
    lines += ["", "## Method", "", gt["_method"]]
    (ROOT / "eval" / "results_ghera.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:3]))
