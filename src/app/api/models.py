from pydantic import BaseModel
from datetime import datetime
# from pydantic.dataclasses import dataclass

class NoteSchema(BaseModel):
    full_name: str
    job_title: str
    employment_date: datetime = None
    salary: int
    id_chief: int