from pydantic import BaseModel, Field
from typing import Literal, Union, Optional, List

# --- Event follow-up classes ---


class AnimalCollectedEvent(BaseModel):
    """ Class for the event of an animal being collected """
    type: Literal["animal collected"]
    collected: Literal["yes", "no"]


class RecipientEvent(BaseModel):
    """ Class for the recipient of the collection """
    type: Literal["recipient"]
    recipient: Literal[
        "veterinary", "care center", "local museum", "national museum", "other"
    ]


class RadiographyEvent(BaseModel):
    """ Class for if a radiography was performed on the animal """
    type: Literal["radiography"]
    radiography: Literal["yes", "no", "unknown"]


class GivenAnswerEvent(BaseModel):
    """ Class for the given answer of the speaker """
    type: Literal["given answer"]
    answer: Literal[
        "nothing",
        "complaint against x",
        "complaint",
        "police call",
        "discussion with the speaker",
        "press release",
        "unknown",
    ]


class NameOfRecipientEvent(BaseModel):
    """ Class for the name of the recipient of the collection """
    type: Literal["recipient name"]
    name: str


class CollectionReferenceEvent(BaseModel):
    """ Class for the reference of the collection """
    type: Literal["collection reference"]
    reference: str


FollowUpEventType = Union[
    AnimalCollectedEvent,
    RecipientEvent,
    RadiographyEvent,
    GivenAnswerEvent,
    NameOfRecipientEvent,
    CollectionReferenceEvent,
]


class FollowUpEvents(BaseModel):
    """ Class for the follow-up events """
    follow_up_events: Optional[List[FollowUpEventType]] = None
