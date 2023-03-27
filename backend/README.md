### Commands

###### Start the PostgreSQL Docker container <br>
``docker-compose up --ddetach``

###### Stop the PostgreSQL Docker container <br>
``docker-compose down``

###### Start the FastAPI server with Uvicorn <br>
``uvicorn backend.main:app --host localhost --port 8000 --reload``
