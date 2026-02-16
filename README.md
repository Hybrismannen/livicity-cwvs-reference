# Livicity CWVS / AWVS — Reference Package (Public)
Repository: https://github.com/Hybrismannen/livicity-cwvs-reference

Open, auditable child-impact toolkit (CWVS/AWVS) that converts mixed evidence into wellbeing vector scans with explainability artifacts and provenance. Includes an **NDC (neurodevelopmental conditions) accessibility filter**, human-review gates, and a transparency dashboard concept to strengthen accountability in public decisions.

This repository is a **public reference package**: schemas, governance artifacts, synthetic examples, and a minimal runnable reference demo. It is designed to support CIA/CRIA workflows with **inspectable outputs**, not opaque judgments.

## Contact
Barnombudet (Child Rights Organization, Sweden)  
Email: [hej@barnombudet.se, linus.fast@barnombudet.se]  
Website: [[ADD OFFICIAL URL](https://barnombudet.se/)]
Repository: https://github.com/Hybrismannen/livicity-cwvs-reference

---

## What’s in this repository (v0.1)

**Schema**
- `schema/cwvs.schema.json` — draft CWVS scan schema
- `schema/awvs.schema.json` — AWVS stub (extension planned)

**Governance & safety**
- `docs/system-card.md` — intended use, limits, safeguards
- `docs/misuse-boundaries.md` — non-negotiable misuse boundaries
- `docs/deployment-checklist.md` — early deployment readiness checklist
- `docs/contributing.md` — contribution guidelines

**Examples**
- `examples/synthetic-input.json` — synthetic input payload (no personal data)
- `examples/example-output-scan.json` — example scan output (generated or stub)
- `examples/example-output-explainability-cards.json` — explainability cards (generated or stub)

**Reference demo (Python)**
- `src/cwvs_engine.py` — minimal scan engine + explainability card generator
- `src/run_demo.py` — reads example input and writes example outputs
Input example: https://github.com/Hybrismannen/livicity-cwvs-reference/blob/main/examples/synthetic-input.json  
Scan output: https://github.com/Hybrismannen/livicity-cwvs-reference/blob/main/examples/example-output-scan.json  
Explainability cards: https://github.com/Hybrismannen/livicity-cwvs-reference/blob/main/examples/example-output-explainability-cards.json

## Demo (inspectable artifacts)
Because runtime execution may not be available in all environments, this repo includes **pre-generated synthetic outputs**:

- Input example: /examples/synthetic-input.json  
- Scan output: /examples/example-output-scan.json  
- Explainability cards: /examples/example-output-explainability-cards.json

---

## What this is NOT

- Not an automated decision system
- Not a diagnostic, predictive, or profiling tool
- Not a scoring/ranking tool for individual children or families
- Not a replacement for professional judgment or lawful procedures

This toolkit is designed for **decision-support and transparency**, with **mandatory human review** where flagged.

---

## Demo (project in action)

Run locally (Python 3.10+ recommended):

```bash
python -m src.run_demo

::contentReference[oaicite:0]{index=0}
