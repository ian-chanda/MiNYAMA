"""
MiNYAMA Semantic Interface: Model Contracts

This module defines the core API for enforcing Active Inference principles 
across the models/ directory. It ensures that every Python entity is 
programmatically bound to its Phase 1 Schema.

Architectural Philosophy:
- Ontology-First: Models must inherit their structure from schemas.
- Sync-Aware: Entities must track their own synchronization state.
- Hardening-Ready: Classes must support metadata for hardening levels.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any, List, Optional

class ContractedEntity(ABC):
    """
    Base class for all schema-synchronized entities.
    Every class in models/baseline_models/ MUST inherit from this.
    """
    def __init__(self, entity_id: str, schema_path: str, version: str = "1.0.0"):
        self.entity_id = entity_id
        self.schema_path = schema_path
        self.version = version
        self.last_sync_timestamp: Optional[datetime] = None
        self.integrity_hash: Optional[str] = None

    @abstractmethod
    def validate_against_schema(self) -> bool:
        """
        Validates the instance's current attributes against the 
        mandatory fields defined in Phase 1.
        """
        pass

    @abstractmethod
    def calculate_surprise(self, observation: 'Observation') -> float:
        """
        Implements the Active Inference 'Surprise' calculation.
        Returns the prediction error (The Delta).
        """
        pass

class Zone(ContractedEntity):
    """
    Agriculture Sector Entity: The primary unit of management.
    Corresponds to Schema 3.1.
    """
    def __init__(self, zone_id: str, soil_model: Dict, moisture_model: Dict):
        super().__init__(zone_id, "schemas/agriculture/Agriculture_Sector_Schema.md")
        self.soil_model = soil_model
        self.moisture_model = moisture_model

    def validate_against_schema(self) -> bool:
        # Implementation logic to check against agriculture_sync.yaml
        return True

    def calculate_surprise(self, observation: 'Observation') -> float:
        # Delta between moisture_model (belief) and observation.data['moisture']
        return abs(self.moisture_model['level'] - observation.data['moisture'])

class Observation:
    """
    Semantic wrapper for evidence records.
    Corresponds to contracts/validation_specs/evidence_requirements.md.
    """
    def __init__(self, source_id: str, timestamp: datetime, data: Dict[str, Any], uncertainty: float = 0.05):
        self.source_id = source_id
        self.timestamp = timestamp
        self.data = data
        self.uncertainty = uncertainty  # Precision weighting

class Intervention:
    """
    Systemic Action record.
    Corresponds to Phase 4 and contracts/validation_specs/intervention_validation.md.
    """
    def __init__(self, intervention_id: str, type: str, target_ref: str, baseline_belief: Dict):
        self.intervention_id = intervention_id
        self.type = type
        self.target_ref = target_ref
        self.baseline_belief = baseline_belief  # The expected outcome
        self.actual_outcome: Optional[Dict] = None

class PredictionError:
    """
    The 'Surprise' record used to drive model updates.
    """
    def __init__(self, entity_ref: str, attribute: str, delta: float, timestamp: datetime):
        self.entity_ref = entity_ref
        self.attribute = attribute
        self.delta = delta
        self.timestamp = timestamp

class EvidenceRecord:
    """
    A persistent record of sensory input for auditability.
    """
    def __init__(self, file_path: str, schema_version: str):
        self.file_path = file_path
        self.schema_version = schema_version
        self.is_verified: bool = False

def schema_contract(schema_path: str):
    """
    Decorator to bind a model class to a specific technical schema.
    Used for automated drift detection.
    """
    def decorator(cls):
        cls.__minyama_schema__ = schema_path
        return cls
    return decorator
