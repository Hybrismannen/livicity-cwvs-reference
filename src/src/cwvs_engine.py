# src/cwvs_engine.py
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Dict, List, Tuple


@dataclass
class EvidenceItem:
    source_level: str
    source_ref: str | None
    summary: str
    uncertainty: str | None = None


@dataclass
class VectorResult:
    vector_id: str
    vector_name: str
    signal_level: str  # low/moderate/high/unknown
    evidence: List[EvidenceItem]


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def build_explainability_card(vector: VectorResult) -> Dict[str, Any]:
    """Generate a reviewer-friendly explainability card for a single vector."""
    evidence_summaries = []
    missing_refs = 0
    for e in vector.evidence:
        evidence_summaries.append(
            {
                "source_level": e.source_level,
                "source_ref": e.source_ref or "",
                "summary": e.summary,
                "uncertainty": e.uncertainty or "",
            }
        )
        if not e.source_ref:
            missing_refs += 1

    # Simple, transparent “human review required” heuristic:
    # - unknown signal OR missing references OR explicit high uncertainty => review required
    needs_review = (
        vector.signal_level == "unknown"
        or missing_refs > 0
        or any((e.uncertainty or "").lower().startswith("high") for e in vector.evidence)
    )

    missing_data_prompts = []
    if vector.signal_level == "unknown":
        missing_data_prompts.append(
            f"Clarify evidence to reduce uncertainty for '{vector.vector_name}'."
        )
    if missing_refs > 0:
        missing_data_prompts.append("Add source references for all evidence items.")
    if not vector.evidence:
        missing_data_prompts.append("Add at least one evidence item (L5–L1).")

    return {
        "vector_id": vector.vector_id,
        "vector_name": vector.vector_name,
        "signal_level": vector.signal_level,
        "claim": f"Current signal is '{vector.signal_level}' for '{vector.vector_name}'.",
        "based_on": evidence_summaries,
        "missing_data_prompts": missing_data_prompts,
        "human_review_required": needs_review,
        "notes": [
            "This is decision-support only.",
            "No automated decisions; human review is mandatory where flagged.",
        ],
    }


def run_scan(payload: Dict[str, Any]) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
    """
    Minimal reference scan:
    - Normalizes vectors
    - Produces scan JSON + per-vector explainability cards
    """
    scan_id = payload.get("scan_id", "cwvs-scan-unnamed")
    subject_scope = payload.get("subject_scope", "policy")
    vectors_in = payload.get("vectors", [])

    vector_results: List[VectorResult] = []
    for v in vectors_in:
        evidence_items = []
        for e in v.get("evidence", []) or []:
            evidence_items.append(
                EvidenceItem(
                    source_level=str(e.get("source_level", "L?")),
                    source_ref=e.get("source_ref"),
                    summary=str(e.get("summary", "")),
                    uncertainty=e.get("uncertainty"),
                )
            )
        vector_results.append(
            VectorResult(
                vector_id=str(v.get("vector_id", "")),
                vector_name=str(v.get("vector_name", "")),
                signal_level=str(v.get("signal_level", "unknown")),
                evidence=evidence_items,
            )
        )

    explain_cards = [build_explainability_card(v) for v in vector_results]

    # If ANY vector requires review -> overall review required
    overall_review_required = any(c["human_review_required"] for c in explain_cards)

    scan_out = {
        "scan_id": scan_id,
        "timestamp": _now_iso(),
        "subject_scope": subject_scope,
        "human_review_required": overall_review_required,
        "ve
