"""OWApp benchmark: python -m eval.owapp   (APKs in data/apks/owapp/<test>.apk, see eval/owapp.json for the method)
Needs apktool and jadx (run it inside the Docker image); reports are cached in data/eval/owapp/."""
import json
from pathlib import Path
from app.pipeline import scan

ROOT = Path(__file__).resolve().parents[1]
APKS, CACHE = ROOT / "data" / "apks" / "owapp", ROOT / "data" / "eval" / "owapp"

if __name__ == "__main__":
    gt = json.loads((ROOT / "eval" / "owapp.json").read_text(encoding="utf-8"))
    CACHE.mkdir(parents=True, exist_ok=True)
    rows, out = [], []
    for app, expected in gt["apps"].items():
        if not isinstance(expected, list):
            out.append(f"| {app} | {expected['out_of_scope']} |")
            continue
        path = CACHE / f"{app}.json"
        if not path.exists():
            print(f"scanning {app}...", flush=True)
            path.write_text(json.dumps(scan(str(APKS / f"{app}.apk"), progress=lambda m: None), indent=1), encoding="utf-8")
        found = {f["category"] for f in json.loads(path.read_text(encoding="utf-8"))["findings"]}
        rows.append((app, expected, bool(found & set(expected))))
    hits = sum(r[2] for r in rows)
    lines = [f"# AndroGuard on OWApp ({len(rows)} in-scope apps)", "",
             f"Detected **{hits} of {len(rows)}** (recall {hits / len(rows):.3f}). OWApp has no fixed versions, so false "
             f"alarms are not measured. {len(out)} apps are out of scope (no rule for that MASTG test).", "",
             "| App (MASTG test) | Expected category | Result |", "|---|---|---|"]
    lines += [f"| {a} | {' or '.join(c)} | {'detected' if d else 'missed'} |" for a, c, d in rows]
    lines += ["", "## Out of scope", "", "| App | Why |", "|---|---|"] + out + ["", "## Method", "", gt["_method"]]
    (ROOT / "eval" / "results_owapp.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:3]))
