from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional

# Base class for CircumstanceType with a discriminator field 'type'
class CircumstanceTypeBase(BaseModel):
    type: str

# Collision with means of transport
class RoadVehicleCollision(CircumstanceTypeBase):
    type: Literal['road_vehicle']
    infrastructure_number: Optional[str] = None
    road_type: Literal['highway', 'main road', 'secondary road', 'local road/path/trail', 'parking lot', 'other', 'unknown']

class TrainCollision(CircumstanceTypeBase):
    type: Literal['train']
    infrastructure_number: str

class AircraftCollision(CircumstanceTypeBase):
    type: Literal['aircraft']

class BoatCollision(CircumstanceTypeBase):
    type: Literal['boat']

class OtherTransportCollision(CircumstanceTypeBase):
    type: Literal['other']

class UnknownTransportCollision(CircumstanceTypeBase):
    type: Literal['unknown']

# Destruction / Deliberately removed
class HuntingDestruction(CircumstanceTypeBase):
    type: Literal['hunting']
    method: Literal['shooting', 'bow', 'falconry', 'hounds hunting', 'digging up', 'other', 'unknown']

class TrapDestruction(CircumstanceTypeBase):
    type: Literal['trap']
    method: Literal['killing trap', 'pole trap', 'trap cage', 'corvids nasse', 'net', 'cage trap', 'fall-trap', 'glue trap', 'insect trap', 'other', 'unknown']

class PoisoningDestruction(CircumstanceTypeBase):
    type: Literal['poisoning']

class RemovalDestruction(CircumstanceTypeBase):
    type: Literal['removal or direct capture']
    method: Literal['gassing', 'raptor captured at nest', 'brood destruction', 'traffic/trade', 'capture accident', 'scientific sample', 'other', 'unknown']

class FishingDestruction(CircumstanceTypeBase):
    type: Literal['fishing']
    method: Literal['drowned/tangled', 'beached with capture indications', 'other', 'unknown']

class OtherDestruction(CircumstanceTypeBase):
    type: Literal['other']

class UnknownDestruction(CircumstanceTypeBase):
    type: Literal['unknown']

# Indirect destruction
class PylonElectricGridDestruction(CircumstanceTypeBase):
    type: Literal['pylone and electric grid']
    infrastructure: Literal['electric line', 'pole/pylon', 'other', 'unknown']
    cause: Literal['collision', 'electrocution', 'unknown']

class WindfarmDestruction(CircumstanceTypeBase):
    type: Literal['windfarm']

class OtherCollisionDestruction(CircumstanceTypeBase):
    type: Literal['other collision']
    object: Literal['window', 'building', 'lighthouse', 'cable', 'wire fence/barbed wire', 'other crash', 'unknown']

class FallDestruction(CircumstanceTypeBase):
    type: Literal['fall']
    location: Literal['chimney', 'empty pole', 'hole/well', 'other', 'unknown']

class DevelopmentWorkDestruction(CircumstanceTypeBase):
    type: Literal['development work']
    work_type: Literal['transport infrastructure', 'building', 'other', 'unknown']

class PollutionContaminationDestruction(CircumstanceTypeBase):
    type: Literal['pollution / contamination']
    pollution_type: Literal['oil pollution', 'chemical pollution', 'heavy metals', 'light', 'noise', 'plastic ingestion', 'other', 'unknown']

class AgriculturalNetProtectionDestruction(CircumstanceTypeBase):
    type: Literal['agricultural net protection']

class VegetalForestWorkDestruction(CircumstanceTypeBase):
    type: Literal['vegetal / forest work']
    work_type: Literal['clearing/mowing/plowing', 'tree felling/pruning', 'other', 'unknown']

class OtherIndirectDestruction(CircumstanceTypeBase):
    type: Literal['other']

class UnknownIndirectDestruction(CircumstanceTypeBase):
    type: Literal['unknown']

# Natural cause
class Predation(CircumstanceTypeBase):
    type: Literal['predation']
    predator: Literal['cat', 'dog', 'rooster/hen', 'other domestic animal', 'wild birds', 'wild mammal', 'other', 'unknown']

class Weather(CircumstanceTypeBase):
    type: Literal['weather']
    condition: Literal['cold wave', 'drought', 'hail', 'lightening', 'storm', 'other', 'unknown']

class NaturalDisaster(CircumstanceTypeBase):
    type: Literal['natural disaster']
    disaster: Literal['fire', 'avalanche', 'rock fall', 'mudslide', 'volcanic eruption/ashes', 'other', 'unknown']

class NestFall(CircumstanceTypeBase):
    type: Literal['nest fall']

class StrandingExhaustion(CircumstanceTypeBase):
    type: Literal['stranding due to exhaustion']

class DiseaseParasite(CircumstanceTypeBase):
    type: Literal['disease/parasite']

class AccidentalDrowning(CircumstanceTypeBase):
    type: Literal['accidental drowning']
    drowning_location: Literal['drinking trough', 'pool', 'storm pool', 'irrigation pool', 'natural pool', 'flood', 'other container', 'unknown']

class OtherNaturalCause(CircumstanceTypeBase):
    type: Literal['other']

class UnknownNaturalCause(CircumstanceTypeBase):
    type: Literal['unknown']

# Unknown cause
class UnknownCircumstance(CircumstanceTypeBase):
    type: Literal['unknown']

# Union of all possible CircumstanceTypes with 'type' as the discriminator
CircumstanceType = Union[
    RoadVehicleCollision,
    TrainCollision,
    AircraftCollision,
    BoatCollision,
    OtherTransportCollision,
    UnknownTransportCollision,
    HuntingDestruction,
    TrapDestruction,
    PoisoningDestruction,
    RemovalDestruction,
    FishingDestruction,
    OtherDestruction,
    UnknownDestruction,
    PylonElectricGridDestruction,
    WindfarmDestruction,
    OtherCollisionDestruction,
    FallDestruction,
    DevelopmentWorkDestruction,
    PollutionContaminationDestruction,
    AgriculturalNetProtectionDestruction,
    VegetalForestWorkDestruction,
    OtherIndirectDestruction,
    UnknownIndirectDestruction,
    Predation,
    Weather,
    NaturalDisaster,
    NestFall,
    StrandingExhaustion,
    DiseaseParasite,
    AccidentalDrowning,
    OtherNaturalCause,
    UnknownNaturalCause,
    UnknownCircumstance
]

# Main Circumstance class
class Circumstances(BaseModel):
    circumstance: str  # e.g., "COLLISION"
    circumstance_radio: str  # e.g., "Yes"
    circumstance_type: CircumstanceType = Field(..., discriminator='type')