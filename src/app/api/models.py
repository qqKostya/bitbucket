from typing import Optional

from sqlmodel import SQLModel, Field


class HeroBase(SQLModel):
    full_name: str = Field(index=True)
    job_title: str
    employment_date: str
    salary: int
    id_chief: Optional[int] = None


class Hero(HeroBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class HeroCreate(HeroBase):
    pass


class HeroRead(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    full_name: Optional[str] = None
    job_title: Optional[str] = None
    employment_date: Optional[str] = None
    salary: Optional[int] = None
    id_chief: Optional[int] = None
