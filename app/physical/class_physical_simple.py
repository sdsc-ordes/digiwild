from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional

# Define common anomalies as a Literal type
CommonAnomaliesSimple = Literal["injury", "abnormal position"]


# --- Beak-related Anomalies ---
class BeakAnomaly(BaseModel):
    """ Beak-related anomalies """
    type: Literal["beak"]
    anomaly_type: List[Literal["adhesion/discharge", CommonAnomaliesSimple]]


# --- Body-related Anomalies ---
class BodyAnomaly(BaseModel):
    """ Body-related anomalies """
    type: Literal["body"]
    anomaly_type: List[Literal[CommonAnomaliesSimple]]


# --- Feathers/Wings/Tail-related Anomalies ---
class FeathersWingsTailAnomaly(BaseModel):
    """ Feathers/Wings/Tail-related anomalies """
    type: Literal["feathers/wings/tail"]
    anomaly_type: List[Literal["feather and skin change", CommonAnomaliesSimple]]


# --- Head-related Anomalies (including eyes) ---
class HeadAnomaly(BaseModel):
    """ Head-related anomalies """
    type: Literal["head incl. eyes"]
    anomaly_type: List[Literal["eye changes", CommonAnomaliesSimple]]


# --- Legs-related Anomalies ---
class LegAnomaly(BaseModel):
    """ Legs-related anomalies """
    type: Literal["legs"]
    anomaly_type: List[Literal[CommonAnomaliesSimple]]


# Union of all possible anomaly types for specific body parts
AnomalyTypeSimple = Union[
    BeakAnomaly, BodyAnomaly, LegAnomaly, FeathersWingsTailAnomaly, HeadAnomaly
]


# Main PhysicalAnomaly class that logs anomalies across different body parts
class PhysicalAnomaliesSimple(BaseModel):
    """ Physical anomalies 
    Args:
        physical_radio: str
        physical_anomalies_type: Optional list of anomaly types
    """
    physical_radio: str
    physical_anomalies_type: Optional[List[AnomalyTypeSimple]] = None
