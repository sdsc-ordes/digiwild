from pydantic import BaseModel, Field
from typing import Literal, Union, Optional, List

# --- Event follow-up classes ---


class AnimalCollectedEvent(BaseModel):
    type: Literal["animal collected"]
    collected: Literal["yes", "no"]


class RecipientEvent(BaseModel):
    type: Literal["recipient"]
    recipient: Literal[
        "veterinary", "care center", "local museum", "national museum", "other"
    ]


class RadiographyEvent(BaseModel):
    type: Literal["radiography"]
    radiography: Literal["yes", "no", "unknown"]


class GivenAnswerEvent(BaseModel):
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
    type: Literal["recipient name"]
    name: str


class CollectionReferenceEvent(BaseModel):
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
    follow_up_events: Optional[List[FollowUpEventType]] = None
