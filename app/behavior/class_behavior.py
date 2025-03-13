from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional


class Behavior(BaseModel):
    """ Base class for behaviors """
    type: str
    description: Optional[str] = None  # Making the description field optional


# --- Specific Behavior classes ---
class AbnormalBreathing(Behavior):
    """ Class for the abnormal breathing behavior """
    type: Literal["abnormal breathing"]
    description: Optional[Literal["Problems breathing, breathing sounds"]] = None


class CrashFalling(Behavior):
    """ Class for the crash falling behavior """
    type: Literal["crash, falling from the sky"]
    description: Optional[Literal["Suddenly falling from the sky"]] = None


class Diarrhea(Behavior):
    """ Class for the diarrhea behavior """
    type: Literal["diarrhea"]
    description: Optional[Literal["Observed diarrhea"]] = None


class Lameness(Behavior):
    """ Class for the lameness behavior """
    type: Literal["lameness"]
    description: Optional[
        Literal["Apparent limping or not able to walk properly"]
    ] = None


class Neurological(Behavior):
    """ Class for the neurological behavior """
    type: Literal["neurological"]
    description: Optional[
        Literal["Circling, incoordination, tremors, convulsions, fast eye movements"]
    ] = None


class OtherAbnormalBehavior(Behavior):
    """ Class for other abnormal behavior """
    type: Literal["other abnormal behavior"]
    description: Optional[Literal["Other than weakness, other than neurologic"]] = None


class UnableToFly(Behavior):
    """ Class for the unable to fly behavior """
    type: Literal["unable to fly"]
    description: Optional[
        Literal["Animal alert and tries to fly but can not take off"]
    ] = None


class Vomiting(Behavior):
    """ Class for the vomiting behavior """
    type: Literal["vomiting"]
    description: Optional[Literal["Throwing up undigested food, regurgitating"]] = None


class Weakness(Behavior):
    """ Class for the weakness behavior """
    type: Literal["weakness"]
    description: Optional[
        Literal["Non responsive, does not fly away when approached, lethargy"]
    ] = None


class NoChanges(Behavior):
    """ Class for the no changes behavior """
    type: Literal["no changes"]
    description: Optional[Literal["Animal is acting normally"]] = None


# Union of all possible behaviors
BehaviorType = Union[
    AbnormalBreathing,
    CrashFalling,
    Diarrhea,
    Lameness,
    Neurological,
    OtherAbnormalBehavior,
    UnableToFly,
    Vomiting,
    Weakness,
    NoChanges,
]


# Main class that logs multiple behaviors
class Behaviors(BaseModel):
    """ Class for the behaviors
    Args:
        behaviors_radio: str
        behaviors_type: list of BehaviorType
    """
    behaviors_radio: str  # e.g., "Yes"
    behaviors_type: Optional[List[BehaviorType]] = None
