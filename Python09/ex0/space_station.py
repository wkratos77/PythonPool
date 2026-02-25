from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(..., min_length=3, max_length=10)
    name: str = Field(..., min_length=1, max_length=50)
    crew_size: int = Field(..., ge=1, le=20)
    power_level: float = Field(..., ge=0.0, le=100.0)
    oxygen_level: float = Field(..., ge=0.0, le=100.0)
    last_maintenance: datetime = Field(...)
    is_operational: bool = True
    notes: Optional[str] = Field(None, max_length=200)


if __name__ == "__main__":
    print("Space Station Data Validation")
    print("========================================")
    station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance="2024-05-01 14:30:00",
        is_operational=True,
    )
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Last Maintenance: {station.last_maintenance}")
    print("Operational Status: "
          f"{'Operational' if station.is_operational else 'offline'}")
    if station.notes:
        print(f"Notes: {station.notes}")
    print("\n========================================")
    print("Expected validation error:")
    try:
        bad_station = SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=25,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance="2024-05-01 14:30:00",
            is_operational=True,
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"])
