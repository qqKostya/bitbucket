from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy import select
from sqlmodel import Session
from typing import List

from .db import get_session, create_db_and_tables
from .api.models import HeroRead, Hero, HeroCreate, HeroUpdate

app = FastAPI()


# @app.on_event("startup")
# def on_startup():
#     create_db_and_tables()


@app.post("/heroes/", response_model=HeroRead)
async def create_hero(*, session: Session = Depends(get_session), hero: HeroCreate):
    db_hero = Hero.from_orm(hero)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@app.get("/heroes/", response_model=List[Hero])
def get_songs(session: Session = Depends(get_session)):
    result = session.execute(select(Hero))
    heros = result.scalars().all()
    return [
        Hero(
            full_name=hero.full_name,
            job_title=hero.job_title,
            employment_date=hero.employment_date,
            salary=hero.salary,
            id_chief=hero.id_chief,
            id=hero.id,
        )
        for hero in heros
    ]


@app.get("/heroes/{hero_id}", response_model=HeroRead)
def read_hero(*, session: Session = Depends(get_session), hero_id: int):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero


@app.patch("/heroes/{hero_id}", response_model=HeroRead)
def update_hero(
    *, session: Session = Depends(get_session), hero_id: int, hero: HeroUpdate
):
    db_hero = session.get(Hero, hero_id)
    if not db_hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    hero_data = hero.dict(exclude_unset=True)
    for key, value in hero_data.items():
        setattr(db_hero, key, value)
    session.add(db_hero)
    session.commit()
    session.refresh(db_hero)
    return db_hero


@app.delete("/heroes/{hero_id}")
def delete_hero(*, session: Session = Depends(get_session), hero_id: int):

    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(hero)
    session.commit()
    return {"ok": True}
