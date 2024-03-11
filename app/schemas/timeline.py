import datetime
from typing import Literal

from pydantic import BaseModel


class Project(BaseModel):
    reference: str
    datetime_start: datetime.datetime
    datetime_end: datetime.datetime


class Location(BaseModel):
    type: Literal["Type 1", "Type 2", "Type 3"]
    reference: str
    projects: list[Project]


class Terminal(BaseModel):
    reference: str
    locations: list[Location]


class Period(BaseModel):
    reference: str
    time_start: datetime.time
    duration: datetime.timedelta


class Timeline(BaseModel):
    dates: list[datetime.date]
    periods: list[Period]
    terminals: list[Terminal]
