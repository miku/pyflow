from pydantic import BaseModel
from typing import List

class Grade(BaseModel):
    points: int
    max_points: int
    percent: float
    agg_score: float
    mark: str

    def check_percent(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("not a percentage")
        return v

    def check_agg_score(cls, v):
        if not 0 <= v <= 24:
            raise ValueError("not an aggregation score")
        return v

    def check_mark(cls, v):
        valid_marks = (
            "A+",
            "A",
            "A-",
            "B+",
            "B",
            "B-",
            "C+",
            "C",
            "C-",
            "D+",
            "D",
            "D-",
            "F1",
            "F2",
            "F3",
            "F4",
        )
        if v not in valid_marks:
            raise ValueError("invalid mark")
        return v


class Feedback(BaseModel):
    did_well: str
    did_not_well: str
    improvements: str


class Assessment(BaseModel):
    """
    Validator for assessment data.
    """
    # Required to Table.
    surname: str
    first_name: str
    email: str

    # Required for feedback form.
    id: str
    date: str
    programme: str
    module_number: str
    assessment_type: str
    grade: Grade
    tutor: str
    signature: str
    feedback: Feedback


class Assessments(BaseModel):
    assessments: List[Assessment]


# schema
# print(Assessments.schema_json())

data = [
        {
            "surname": "First",
            "first_name": "Bob",
            "email": "a@b.com",
            "id": "123",
            "date": "2022-06-29",
            "programme": "Foundation",
            "module_number": "L1",
            "assessment_type": "Final Exam",
            "grade": {
                "points": 100,
                "max_points": 100,
                "percent": 100,
                "agg_score": 24,
                "mark": "A",    
            },
            "tutor": "Martin Czygan",
            "signature": "Martin Czygan",
            "feedback": {
                "did_well": "Overall good",
                "did_not_well": "formatting",
                "improvements": "",
            },
        },
        {
            "surname": "Second",
            "first_name": "Bob",
            "email": "a@b.com",
            "id": "123",
            "date": "2022-06-29",
            "programme": "Foundation",
            "module_number": "L1",
            "assessment_type": "Final Exam",
            "grade": {
                "points": 0.2,
                "max_points": 100,
                "percent": 80,
                "agg_score": 20,
                "mark": "B",    
            },
            "tutor": "Sample Tutor",
            "signature": "Sample Tutor",
            "feedback": {
                "did_well": "Overall good",
                "did_not_well": "formatting",
                "improvements": "",
            },
        },
    ]


# assessments = Assessments(assessments=[{}])
assessments = Assessments(assessments=data)
print(assessments)