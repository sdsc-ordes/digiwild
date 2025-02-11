from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional


class BehaviorSimple(BaseModel):
    type: str
    description: Optional[str] = None  # Making the description field optional


# --- Specific BehaviorSimple classes ---
class GeneralWeakness(BehaviorSimple):
    type: Literal["general weakness"]
    description: Optional[
        Literal[
            "Abnormal breathing (dyspnoea), sudden crash, apathy, lethargy, unable to fly but responsive"
        ]
    ] = None


class Vomiting(BehaviorSimple):
    type: Literal["vomiting"]
    description: Optional[Literal["Throwing up undigested food, regurgitating"]] = None


class AtypicalBehavior(BehaviorSimple):
    type: Literal["atypical behavior"]
    description: Optional[
        Literal["Circling, incoordination, tremors, convulsions"]
    ] = None


class NoChanges(BehaviorSimple):
    type: Literal["no changes"]
    description: Optional[Literal["Animal is acting normally"]] = None


# Union of all possible behaviors
BehaviorSimpleType = Union[GeneralWeakness, Vomiting, AtypicalBehavior, NoChanges]


# Main class that logs multiple behaviors
class BehaviorsSimple(BaseModel):
    behaviors_radio: str  # e.g., "Yes"
    behaviors_type: Optional[List[BehaviorSimpleType]] = None
