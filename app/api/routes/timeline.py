import datetime
from fastapi import APIRouter
from app.schemas.timeline import Timeline

router = APIRouter(prefix="/timeline", tags=["Timeline"])


@router.get("/", response_model=Timeline)
def get_timeline_data():
    """Get all projects for timeline

    A basic endpoint that takes in dates, disregards these dates, and
    returns a static list of projects in the format necessary for the timeline.
    """

    dates = [
        datetime.datetime.strptime("2024-12-14", "%Y-%m-%d").date()
        + datetime.timedelta(days=x)
        for x in range(7)
    ]

    periods = [
        {"reference": "D", "time_start": "08:00", "duration": "12:00"},
        {"reference": "N", "time_start": "18:00", "duration": "12:00"},
    ]

    terminals = [
        {
            "reference": "Terminal 1",
            "locations": [
                {
                    "type": "Type 1",
                    "reference": "SB1",
                    "projects": [
                        {
                            "reference": "Project 1",
                            "datetime_start": "2024-12-13T12:00:00Z",
                            "datetime_end": "2024-12-15T21:59:00Z",
                        }
                    ],
                },
                {
                    "type": "Type 1",
                    "reference": "SB3",
                    "projects": [
                        {
                            "reference": "Project 3",
                            "datetime_start": "2024-12-18T01:00:00Z",
                            "datetime_end": "2024-12-26T23:59:00Z",
                        }
                    ],
                },
                {
                    "type": "Type 2",
                    "reference": "WH1",
                    "projects": [
                        {
                            "reference": "Project 2",
                            "datetime_start": "2024-12-15T22:00:00Z",
                            "datetime_end": "2024-12-17T11:00:00Z",
                        }
                    ],
                },
                {"type": "Type 2", "reference": "WH2", "projects": []},
            ],
        },
        {
            "reference": "Terminal 2",
            "locations": [
                {
                    "type": "Type 3",
                    "reference": "R1",
                    "projects": [
                        {
                            "reference": "Project 5",
                            "datetime_start": "2024-12-15T09:00:00Z",
                            "datetime_end": "2024-12-18T23:00:00Z",
                        }
                    ],
                },
                {
                    "type": "Type 3",
                    "reference": "R2",
                    "projects": [
                        {
                            "reference": "Project 4",
                            "datetime_start": "2024-12-14T15:00:00Z",
                            "datetime_end": "2024-12-15T17:00:00Z",
                        }
                    ],
                },
                {"type": "Type 1", "reference": "SB5", "projects": []},
                {
                    "type": "Type 1",
                    "reference": "SB6",
                    "projects": [
                        {
                            "reference": "Project 6",
                            "datetime_start": "2024-12-16T23:59:00Z",
                            "datetime_end": "2024-12-19T22:00:00Z",
                        }
                    ],
                },
            ],
        },
    ]

    return {"dates": dates, "periods": periods, "terminals": terminals}
