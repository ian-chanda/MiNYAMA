"""
MiNYAMA Surprise Calculator
===========================

Calculates prediction error ("surprise") between prior beliefs stored in
evidence/environmental_priors/ and sensory observations stored in
evidence/observations/.

This script is intentionally simple and schema-aware for the Manufacturing
sector. It can be extended for other sectors by adding sector-specific
parsers and surprise metrics.

Usage:
    python surprise_calculator.py \
        --priors evidence/environmental_priors/manufacturing_zambia_population.json \
        --observations evidence/observations/manufacturing_zambia_observations.json \
        --output evidence/prediction_error_logs/manufacturing_zambia_surprise_log.json
"""

import argparse
import json
import math
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional


def parse_iso8601_duration(duration: str) -> float:
    """
    Convert an ISO 8601 duration string to total seconds.
    Supports PT#H#M#S format.
    """
    if not duration:
        return 0.0

    pattern = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?")
    match = pattern.match(duration)
    if not match:
        raise ValueError(f"Unsupported ISO 8601 duration format: {duration}")

    hours = float(match.group(1) or 0)
    minutes = float(match.group(2) or 0)
    seconds = float(match.group(3) or 0)
    return hours * 3600 + minutes * 60 + seconds


def format_seconds(seconds: float) -> str:
    """Format seconds as an ISO 8601 duration string."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = seconds % 60
    result = "PT"
    if hours:
        result += f"{hours}H"
    if minutes:
        result += f"{minutes}M"
    if secs or (hours == 0 and minutes == 0):
        result += f"{secs:.1f}S" if secs != int(secs) else f"{int(secs)}S"
    return result


def parse_days(value: Any) -> Optional[float]:
    """Parse a string like '2d' or '2.5d' into a float number of days."""
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        match = re.match(r"(\d+(?:\.\d+)?)d", value.strip())
        if match:
            return float(match.group(1))
    return None


def find_entity_record(priors: Dict[str, Any], entity_type: str, entity_id: str) -> Optional[Dict[str, Any]]:
    """Locate a single entity record in the prior population data."""
    entity_list = priors.get(entity_type, [])

    id_field_map = {
        "PhysicalAsset": "asset_id",
        "Material": "material_id",
        "WorkOrder": "order_id",
        "Process": "process_id",
        "SupplyChainLink": "link_id",
    }

    id_field = id_field_map.get(entity_type)
    if id_field:
        return next((r for r in entity_list if r.get(id_field) == entity_id), None)
    return None


def extract_prior_value(priors: Dict[str, Any], entity_ref: str, metric: str) -> Optional[Any]:
    """
    Extract a predicted/baseline value from the prior population data.

    entity_ref format: EntityType.entity_id (e.g., WorkOrder.WO-ZMB-2026-001)

    Handles schema-specific mappings for the Manufacturing sector:
      - PhysicalAsset telemetry metrics -> latest reading from telemetry_feed
      - WorkOrder.actual_duration -> WorkOrder.expected_duration
      - SupplyChainLink.delivery_lead_time -> lead_time_model.parameters.mean
      - Process quality metrics -> matching quality_checkpoints threshold
    """
    parts = entity_ref.split(".")
    if len(parts) != 2:
        return None

    entity_type, entity_id = parts
    record = find_entity_record(priors, entity_type, entity_id)
    if record is None:
        return None

    # Sector-specific mappings (take precedence over direct attribute lookup)
    if entity_type == "PhysicalAsset" and metric in ("vibration_ms2", "temperature_c"):
        telemetry = record.get("telemetry_feed", {})
        readings = telemetry.get("readings", [])
        if readings:
            latest = max(readings, key=lambda r: r.get("timestamp", ""))
            return latest.get(metric)

    if entity_type == "WorkOrder" and metric == "actual_duration":
        return record.get("expected_duration")

    if entity_type == "SupplyChainLink" and metric == "delivery_lead_time":
        lead_time_model = record.get("lead_time_model", {})
        params = lead_time_model.get("parameters", {})
        return parse_days(params.get("mean"))

    if entity_type == "Process":
        for checkpoint in record.get("quality_checkpoints", []):
            if checkpoint.get("check") == metric:
                return checkpoint.get("threshold")

    # Direct attribute lookup
    if metric in record:
        return record[metric]

    # Generic nested lookup (e.g., lead_time_model.parameters.mean)
    if "." in metric:
        keys = metric.split(".")
        value = record
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return None
        return value

    return None


def compute_surprise(expected: Any, observed: Any, metric: str) -> Dict[str, Any]:
    """
    Compute prediction error and a normalized surprise score.

    Returns a dict with expected_value, observed_value, raw_delta,
    normalized_surprise_score, and p_value.
    """
    result = {
        "expected_value": expected,
        "observed_value": observed,
        "raw_delta": None,
        "normalized_surprise_score": 0.0,
        "p_value": None,
    }

    if metric == "actual_duration":
        expected_s = parse_iso8601_duration(str(expected)) if expected else 0.0
        observed_s = parse_iso8601_duration(str(observed)) if observed else 0.0
        raw_delta = observed_s - expected_s
        surprise = abs(raw_delta) / expected_s if expected_s else 0.0
        result["expected_seconds"] = expected_s
        result["observed_seconds"] = observed_s
        result["raw_delta_seconds"] = raw_delta
        result["raw_delta"] = raw_delta
        result["normalized_surprise_score"] = round(min(surprise, 1.0), 3)
        # Rough p-value heuristic: assumes exponential decay with surprise
        result["p_value"] = round(math.exp(-5 * surprise), 3)

    elif isinstance(expected, (int, float)) and isinstance(observed, (int, float)):
        raw_delta = observed - expected
        denominator = abs(expected) if expected != 0 else 1.0
        surprise = abs(raw_delta) / denominator
        result["raw_delta"] = raw_delta
        result["normalized_surprise_score"] = round(min(surprise, 1.0), 3)
        result["p_value"] = round(math.exp(-3 * surprise), 3)

    else:
        result["raw_delta"] = "N/A"
        result["normalized_surprise_score"] = 0.0 if expected == observed else 0.5

    return result


def severity_from_score(score: float) -> str:
    if score < 0.05:
        return "LOW"
    if score < 0.15:
        return "MEDIUM"
    return "HIGH"


def build_surprise_record(
    observation: Dict[str, Any],
    priors: Dict[str, Any],
    log_index: int,
    schema_ref: str,
) -> Optional[Dict[str, Any]]:
    """
    Build a single surprise record from an observation and the prior population.
    """
    entity_ref = observation.get("entity_ref", "")
    metric = observation.get("metric", "")
    observed_value = observation.get("value")

    expected_value = extract_prior_value(priors, entity_ref, metric)
    if expected_value is None:
        return None

    inference_data = compute_surprise(expected_value, observed_value, metric)
    if inference_data["normalized_surprise_score"] == 0.0 and inference_data.get("raw_delta") == 0:
        return None  # No surprise

    entity_type, entity_id = entity_ref.split(".", 1)
    log_id = f"SURPRISE-ZMB-MFG-{log_index:03d}"
    timestamp = observation.get("timestamp", datetime.utcnow().isoformat() + "Z")

    return {
        "inference_metadata": {
            "log_id": log_id,
            "timestamp": timestamp,
        },
        "context": {
            "region": "Zambia",
            "entity": entity_id,
            "entity_type": entity_type,
            "metric": metric,
        },
        "inference_data": inference_data,
        "analytical_insight": {
            "explanation": f"Observed {metric} ({observed_value}) differs from prior belief ({expected_value}).",
            "severity": severity_from_score(inference_data["normalized_surprise_score"]),
            "intervention_recommendation": "Review prior model and update parameters.",
            "sync_update_target": f"schemas/manufacturing/{entity_type}.{metric}",
        },
        "audit_trail": {
            "calculated_by": "models/prediction_engines/surprise_calculator.py",
            "input_integrity_hash": "placeholder",
            "traceability_id": f"trace-{log_id}-{timestamp[:10].replace('-', '')}",
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description="Calculate prediction error between priors and observations."
    )
    parser.add_argument(
        "--priors",
        default="evidence/environmental_priors/manufacturing_zambia_population.json",
        help="Path to the prior/population JSON file.",
    )
    parser.add_argument(
        "--observations",
        default="evidence/observations/manufacturing_zambia_observations.json",
        help="Path to the observations JSON file.",
    )
    parser.add_argument(
        "--output",
        default="evidence/prediction_error_logs/manufacturing_zambia_surprise_log.json",
        help="Path to write the surprise log JSON file.",
    )
    args = parser.parse_args()

    priors_path = Path(args.priors)
    observations_path = Path(args.observations)
    output_path = Path(args.output)

    if not priors_path.exists():
        print(f"ERROR: Priors file not found: {priors_path}", file=sys.stderr)
        sys.exit(1)
    if not observations_path.exists():
        print(f"ERROR: Observations file not found: {observations_path}", file=sys.stderr)
        sys.exit(1)

    with priors_path.open("r", encoding="utf-8") as f:
        priors = json.load(f)

    with observations_path.open("r", encoding="utf-8") as f:
        observations_doc = json.load(f)

    observations = observations_doc.get("observations", [])
    schema_ref = observations_doc.get("schema_ref", "schemas/manufacturing/Manufacturing_Sector_Schema.md")

    surprises: List[Dict[str, Any]] = []
    log_index = 1
    for obs in observations:
        record = build_surprise_record(obs, priors, log_index, schema_ref)
        if record:
            surprises.append(record)
            log_index += 1

    output_doc = {
        "surprise_log_id": f"SURPRISE-ZMB-MFG-{datetime.utcnow().strftime('%Y%m%d')}",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "schema_ref": schema_ref,
        "prior_ref": str(priors_path).replace("\\", "/"),
        "observation_ref": str(observations_path).replace("\\", "/"),
        "confidence_level": 0.88,
        "governance_status": "pending_review",
        "surprises": surprises,
    }

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(output_doc, f, indent=2, ensure_ascii=False)

    print(f"Wrote {len(surprises)} surprise records to {output_path}")


if __name__ == "__main__":
    main()
