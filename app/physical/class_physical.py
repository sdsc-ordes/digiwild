from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional

# Define common anomalies as a Literal type
CommonAnomalies = Literal[
    "blackened/burnt skin",
    "blood",
    "foreign body",
    "fracture",
    "injury",
    "parasite",
    "swelling",
    "warty or tumor-like growth, crusts",
]


# --- Beak-related Anomalies ---
class BeakAnomaly(BaseModel):
    """ Beak-related anomalies """
    type: Literal["beak"]
    anomaly_type: List[Literal["adhesion", "deformation", CommonAnomalies]]


# --- Body-related Anomalies ---
class BodyAnomaly(BaseModel):
    """ Body-related anomalies """
    type: Literal["body"]
    anomaly_type: List[
        Literal["emaciation", "fluffed up", "stained feathers", CommonAnomalies]
    ]


# --- Legs-related Anomalies ---
class LegAnomaly(BaseModel):
    """ Legs-related anomalies """
    type: Literal["legs"]
    anomaly_type: List[Literal["missing limb", "deformation", CommonAnomalies]]


# --- Feathers/Wings/Tail-related Anomalies ---
class FeathersWingsTailAnomaly(BaseModel):
    """ Feathers/Wings/Tail-related anomalies """
    type: Literal["feathers/wings/tail"]
    anomaly_type: List[
        Literal[
            "fluffed up",
            "feather abnormalities",
            "stained feathers",
            "abnormal wing posture",
            "missing limb",
            CommonAnomalies,
        ]
    ]


# --- Head-related Anomalies (including eyes) ---
class HeadAnomaly(BaseModel):
    """ Head-related anomalies """
    type: Literal["head incl. eyes"]
    anomaly_type: List[
        Literal["ear changes", "eye changes", "tilted head", CommonAnomalies]
    ]


# Union of all possible anomaly types for specific body parts
AnomalyType = Union[
    BeakAnomaly, BodyAnomaly, LegAnomaly, FeathersWingsTailAnomaly, HeadAnomaly
]


# Main PhysicalAnomaly class that logs anomalies across different body parts
class PhysicalAnomalies(BaseModel):
    """ Physical anomalies 
    Args:
        physical_radio: str
        physical_anomalies_type: Optional list of anomaly types
    """
    physical_radio: str
    physical_anomalies_type: Optional[List[AnomalyType]] = None
