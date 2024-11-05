from pydantic import BaseModel, Field
from typing import Optional
import numpy as np
from PIL import Image
import io
import base64
import uuid

from behavior.class_behavior import Behaviors
from circumstances.class_circumstance import Circumstances
from physical.class_physical import PhysicalAnomalies
from follow_up.class_follow_up import FollowUpEvents
from geolocalisation.class_geolocalisation import Geolocalisation

class Wounded(BaseModel):
    circumstances: Circumstances
    behaviors: Behaviors
    physical_anomalies: PhysicalAnomalies
    follow_up_events: FollowUpEvents

class Dead(BaseModel):
    circumstances: Circumstances
    physical_anomalies: PhysicalAnomalies
    follow_up_events: FollowUpEvents

class ImageBase64(BaseModel):
    image: str  
    @classmethod
    def to_base64(cls, pixel_data: list):
        img_array = np.array(pixel_data, dtype=np.uint8)
        img = Image.fromarray(img_array)
        # Save the image to a bytes buffer
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        buffer.seek(0)
        base64_str = base64.b64encode(buffer.read()).decode('utf-8')
        return cls(image=base64_str)
    
class Report(BaseModel):
    identifier: str
    image: ImageBase64
    geolocalisation: Geolocalisation
    wounded_state: str
    wounded: Optional[Wounded] = None  
    dead_state: str
    dead: Optional[Dead] = None 
