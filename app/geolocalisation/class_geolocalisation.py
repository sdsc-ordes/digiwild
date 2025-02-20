from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional


class Longitude(BaseModel):
    type: Literal["longitude"]
    value: float


class Latitude(BaseModel):
    type: Literal["latitude"]
    value: float


class Geolocalisation(BaseModel):
    longitude: Longitude
    latitude: Latitude
    name: Optional[str]
