from pydantic import BaseModel, Field
from typing import Literal, List, Union, Optional


class Longitude(BaseModel):
    """ Longitude value """
    type: Literal["longitude"]
    value: float


class Latitude(BaseModel):
    """ Latitude value """
    type: Literal["latitude"]
    value: float


class Geolocalisation(BaseModel):
    """ Geolocalisation 
    Args: 
        longitude: Longitude value
        latitude: Latitude value
        name: Optional name of the geolocalisation
    """
    longitude: Longitude
    latitude: Latitude
    name: Optional[str]
