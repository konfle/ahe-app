### Commands

###### Start the PostgreSQL Docker container
``docker-compose up --detach``

###### Stop the PostgreSQL Docker container
``docker-compose down``

###### Start the FastAPI server with Uvicorn
``uvicorn backend.main:app --host localhost --port 8000 --reload``

###### Database access via docker
Step 1:
``docker exec -it postgres bash``

Step 2:
``psql -U <psql_user> <psql_db>``
