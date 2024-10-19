from pydantic import BaseModel, Field
from typing import Literal, Union, Optional, List

# --- Event follow-up classes ---

# Animal collected event
class AnimalCollectedEvent(BaseModel):
    type: Literal['animal collected']
    option: Literal['Yes', 'No']

# Recipient event
class RecipientEvent(BaseModel):
    type: Literal['recipient']
    option: Literal['Veterinary', 'Care center', 'Local Museum', 'National Museum', 'Other']

# Radiography event
class RadiographyEvent(BaseModel):
    type: Literal['radiography']
    option: Literal['Yes', 'No', 'Unknown']

# Given answer event
class GivenAnswerEvent(BaseModel):
    type: Literal['given answer']
    option: Literal[
        'Nothing', 
        'Complaint against X', 
        'Complaint', 
        'Police call', 
        'Discussion with the speaker', 
        'Press release', 
        'Unknown'
    ]

# Name of recipient/museum (open text field)
class NameOfRecipientEvent(BaseModel):
    type: Literal['name of recipient / museum']
    name: str  # Open text field for entering the name

# Collection reference (open text field)
class CollectionReferenceEvent(BaseModel):
    type: Literal['collection reference']
    reference: str  # Open text field for entering the reference

# Union of all possible follow-up event types
FollowUpEventType = Union[
    AnimalCollectedEvent,
    RecipientEvent,
    RadiographyEvent,
    GivenAnswerEvent,
    NameOfRecipientEvent,
    CollectionReferenceEvent
]

# Main class that logs multiple follow-up events
class FollowUpEvents(BaseModel):
    follow_up_events: List[FollowUpEventType]

