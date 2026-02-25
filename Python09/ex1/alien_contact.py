from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import Optional
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    PHYSICAL = "physical"
    VISUAL = "visual"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(..., min_length=5, max_length=15)
    timestamp: datetime = Field(...)
    location: str = Field(..., min_length=3, max_length=100)
    contact_type: ContactType = Field(...)
    signal_strength: float = Field(..., ge=0.0, le=10.0)
    duration_minutes: int = Field(..., ge=1, le=1440)
    witness_count:  int = Field(..., ge=1, le=100)
    message_received: Optional[str] = Field(None, max_length=500)
    is_verified: bool = False

    @model_validator(mode='after')
    def validate(self) -> "AlienContact":
        ID = self.contact_id
        if not ID.startswith("AC"):
            raise ValueError("contact_id must start with 'AC'")
        contact_type = self.contact_type
        witness = self.witness_count
        if contact_type == ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact must be verified")
        if contact_type == ContactType.TELEPATHIC and witness < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        signal = self.signal_strength
        message = self.message_received
        if signal > 7.0 and (message is None or message.strip() == ""):
            raise ValueError("High signal strength requires a message")
        return self


if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    print("Valid contact report:")
    contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-06-01 12:00:00",
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
        )
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Localion: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    print(f"Message: {contact.message_received}")
    print("\n======================================")
    print("Expected validation error:")
    try:
        bad_contact = AlienContact(
            contact_id="AC_2024_002",
            timestamp="2024-06-01 12:00:00",
            location="Area 51, Nevada",
            contact_type="telepathic",
            signal_strength=5.0,
            duration_minutes=30,
            witness_count=2,
            message_received=None,
            is_verified=False,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
