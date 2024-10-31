from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional

from behavior.class_behavior import Behaviors
from circumstances.class_circumstance import Circumstances
from physical.class_physical import PhysicalAnomalies
from follow_up.class_follow_up import FollowUpEvents
from geolocalisation.class_geolocalisation import Geolocalisation

class Wounded(BaseModel):
    circumstances: Circumstances
    behaviors: List[Behaviors]
    physical_anomalies: List[PhysicalAnomalies]
    follow_up_events: List[FollowUpEvents]

class Dead(BaseModel):
    circumstances: List[Circumstances] 
    physical_anomalies: List[PhysicalAnomalies]
    follow_up_events: List[FollowUpEvents]

class Image(BaseModel):
    image: List[float]

class Report(BaseModel):
    image: Image
    geolocalisation: Geolocalisation
    wounded_state: bool
    wounded: Optional[Wounded] = None  
    dead_state: bool
    dead: Optional[Dead] = None 
