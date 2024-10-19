from pydantic import BaseModel, Field
from typing import Literal, List, Union


class Behavior(BaseModel):
    type: str
    description: str

# --- Specific Behavior classes ---
class AbnormalBreathing(Behavior):
    type: Literal['abnormal breathing']
    description: Literal["Problems breathing, breathing sounds"]

class CrashFalling(Behavior):
    type: Literal['crash, falling from the sky']
    description: Literal["Suddenly falling from the sky"]

class Diarrhea(Behavior):
    type: Literal['diarrhea']
    description: Literal["Observed diarrhea"]

class Lameness(Behavior):
    type: Literal['lameness']
    description: Literal["Apparent limping or not able to walk properly"]

class Neurological(Behavior):
    type: Literal['neurological']
    description: Literal["Circling, incoordination, tremors, convulsions, fast eye movements"]

class OtherAbnormalBehavior(Behavior):
    type: Literal['other abnormal behavior']
    description: Literal["Other than weakness, other than neurologic"]

class UnableToFly(Behavior):
    type: Literal['unable to fly']
    description: Literal["Animal alert and tries to fly but can not take off"]

class Vomiting(Behavior):
    type: Literal['vomiting']
    description: Literal["Throwing up undigested food, regurgitating"]

class Weakness(Behavior):
    type: Literal['weakness']
    description: Literal["Non responsive, does not fly away when approached, lethargy"]

class NoChanges(Behavior):
    type: Literal['no changes']
    description: Literal["Animal is acting normally"]

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
    NoChanges
]

# Main class that logs multiple behaviors
class Behaviors(BaseModel):
    observed_behaviors: List[BehaviorType]