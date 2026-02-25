from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from typing import List
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=2, max_length=50)
    rank: Rank
    age: int = Field(..., ge=18, le=80)
    specialization: str = Field(..., min_length=3, max_length=30)
    years_experience: int = Field(..., ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(..., min_length=5, max_length=15)
    mission_name: str = Field(..., min_length=3, max_length=100)
    destination: str = Field(..., min_length=3, max_length=50)
    launch_date: datetime = Field(...)
    duration_days: int = Field(..., ge=1, le=3650)
    crew: List[CrewMember] = Field(..., min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(..., ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validate(self) -> "SpaceMission":

        if not self.mission_id.startswith("M"):
            raise ValueError("mission_id must start with 'M'")

        if not any(member.rank in {Rank.CAPTAIN, Rank.COMMANDER}
                   for member in self.crew):
            raise ValueError(
                "Mission must have at least one Commander or Captain")

        if self.duration_days > 365:
            experienced_count = sum(
                1 for member in self.crew
                if member.years_experience >= 5
            )
            required = (len(self.crew) + 1) // 2
            if experienced_count < required:
                raise ValueError(
                    "Long missions (>365 days) require at least 50% "
                    "experienced crew"
                )

        for member in self.crew:
            if not member.is_active:
                raise ValueError(f"Crew member {member.name} is not active")
        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2025-07-15 09:00:00",
        duration_days=900,
        crew=[
            CrewMember(
                member_id="C001",
                name="Alice Smith",
                rank="commander",
                age=45,
                specialization="pilot",
                years_experience=20,
                is_active=True,
            ),
            CrewMember(
                member_id="C002",
                name="Bob Johnson",
                rank="captain",
                age=38,
                specialization="engineer",
                years_experience=12,
                is_active=True,
            ),
            CrewMember(
                member_id="C003",
                name="Charlie Lee",
                rank="officer",
                age=30,
                specialization="scientist",
                years_experience=6,
                is_active=True,
            ),
        ],
        mission_status="planned",
        budget_millions=2500.0,
    )
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print("Crew Members:")
    for member in mission.crew:
        role = (
            "Mission Command" if member.rank == Rank.COMMANDER
            else "Navigation" if member.rank == Rank.CAPTAIN
            else "Engineering" if member.rank == Rank.OFFICER
            else "Support"
        )
        print(f" - {member.name} ({member.rank.value}) - {role}")
    print("\n=========================================")
    print("Expected validation error:")
    try:
        bad_mission = SpaceMission(
            mission_id="MARS2024",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date="2025-07-15 09:00:00",
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Alice Smith",
                    rank="officer",
                    age=45,
                    specialization="pilot",
                    years_experience=20,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C002",
                    name="Bob Johnson",
                    rank="officer",
                    age=38,
                    specialization="engineer",
                    years_experience=12,
                    is_active=True,
                ),
                CrewMember(
                    member_id="C003",
                    name="Charlie Lee",
                    rank="officer",
                    age=30,
                    specialization="scientist",
                    years_experience=6,
                    is_active=True,
                ),
            ],
            mission_status="planned",
            budget_millions=2500.0,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
