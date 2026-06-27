from typing import TypedDict


class StudyState(TypedDict):
    name: str
    subjects: list[str]
    hours: int
    exam_days: int
    plan: str
    study_type: str
