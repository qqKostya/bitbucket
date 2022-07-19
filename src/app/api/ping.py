from fastapi import APIRouter


router = APIRouter()

@router.get("/ping")
async def pong():
    # some async operation could happen here
    # example: `employee = await get_all_employee()`
    return {"ping": "pong!"}