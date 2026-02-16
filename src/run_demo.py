# src/run_demo.py
import json
from pathlib import Path

from cwvs_engine import run_scan


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"

INPUT_FILE = EXAMPLES / "synthetic-input.json"
SCAN_OUT_FILE = EXAMPLES / "example-output-scan.json"
CARDS_OUT_FILE = EXAMPLES / "example-output-explainability-cards.json"


def main() -> None:
    payload = json.loads(INPUT_FILE.read_text(encoding="utf-8"))
    scan_out, cards = run_scan(payload)

    SCAN_OUT_FILE.write_text(json.dumps(scan_out, indent=2), encoding="utf-8")
    CARDS_OUT_FILE.write_text(json.dumps(cards, indent=2), encoding="utf-8")

    print("CWVS demo complete.")
    print(f"- Wrote: {SCAN_OUT_FILE.relative_to(ROOT)}")
    print(f"- Wrote: {CARDS_OUT_FILE.relative_to(ROOT)}")
    print(f"- Human review required: {scan_out['human_review_required']}")


if __name__ == "__main__":
    main()
