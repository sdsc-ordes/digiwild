from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional

# Define common anomalies as a Literal type
CommonAnomalies = Literal[
    'blackened/burnt skin',
    'blood',
    'foreign body',
    'fracture',
    'injury',
    'parasite',
    'swelling',
    'warty or tumor-like growth, crusts'
]

# --- Beak-related Anomalies ---
class BeakAnomaly(BaseModel):
    type: Literal['beak']
    anomaly_type: Literal[
        'adhesion',
        'deformation',
        CommonAnomalies
    ]

# --- Body-related Anomalies ---
class BodyAnomaly(BaseModel):
    type: Literal['body']
    anomaly_type: Literal[
        'emaciation',
        'fluffed up',
        'stained feathers',
        CommonAnomalies
    ]

# --- Legs-related Anomalies ---
class LegAnomaly(BaseModel):
    type: Literal['legs']
    anomaly_type: Literal[
        'missing limb',
        'deformation',
        CommonAnomalies
    ]

# --- Feathers/Wings/Tail-related Anomalies ---
class FeathersWingsTailAnomaly(BaseModel):
    type: Literal['feathers/wings/tail']
    anomaly_type: Literal[
        'fluffed up',
        'feather abnormalities',
        'stained feathers',
        'abnormal wing posture',
        'missing limb',
        CommonAnomalies
    ]

# --- Head-related Anomalies (including eyes) ---
class HeadAnomaly(BaseModel):
    type: Literal['head']
    anomaly_type: Literal[
        'ear changes',
        'eye changes',
        'tilted head',
        CommonAnomalies
    ]


# Union of all possible anomaly types for specific body parts
AnomalyType = Union[
    BeakAnomaly,
    BodyAnomaly,
    LegAnomaly,
    FeathersWingsTailAnomaly,
    HeadAnomaly
]

# Main PhysicalAnomaly class that logs anomalies across different body parts
class PhysicalAnomaly(BaseModel):
    body_part_anomalies: List[AnomalyType]  # List of anomalies across different body parts
