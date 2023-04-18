# Third-party imports
import psutil
from fastapi import APIRouter, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Local application imports
from ..database import SQLALCHEMY_DATABASE_URL

router = APIRouter()


@router.get("/ping", summary="API availability check")
async def ping_pong():
    """
    Check API availability by sending a ping request.

    Returns:
        A dictionary with a single key "ping" and the value "pong".
    """
    return {"ping": "pong"}


@router.get("/db", summary="Database health check")
async def database_health_check():
    """
       Check the health of the database by attempting to create a connection.

       Returns:
           A dictionary with a single key "status" and the value "ok" if the connection was successful.

       Raises:
           HTTPException: If there was an error connecting to the database.
       """
    try:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        with engine.connect() as conn:
            conn.close()
        return {"status": "ok"}
    except OperationalError:
        raise HTTPException(status_code=503, detail="Database connection error")


@router.get("/status", summary="Server health check")
async def healthcheck():
    """
    Check the health of the server by returning a simple response.

    Returns:
        A dictionary with a single key "status" and the value "ok".
    """
    return {"status": "ok"}


@router.get("/system", summary="System resource health check")
async def check_system_resources():
    """
    Check the health of the system resources (CPU, memory, disk).

    Returns:
        A dictionary with three keys "cpu", "memory", and "disk", each containing a boolean value indicating whether
        the corresponding resource is available or not.
    """
    cpu = psutil.cpu_percent() < 80  # Check CPU usage (<80%)
    memory = psutil.virtual_memory().available / (1024 ** 2) > 100  # Check available memory (>100 MB)
    disk = psutil.disk_usage("/").free / (1024 ** 3) > 5  # Check available disk space (>5 GB)

    return {"cpu": cpu, "memory": memory, "disk": disk}
