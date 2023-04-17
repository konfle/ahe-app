from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from ..database import SQLALCHEMY_DATABASE_URL

router = APIRouter()


@router.get("/")
async def healthcheck():
    try:
        db_engine = create_engine(SQLALCHEMY_DATABASE_URL)
        db_conn = db_engine.connect()
        db_conn.close()
        return {"status": "ok"}
    except OperationalError:
        raise HTTPException(status_code=503, detail="Database connection error")
