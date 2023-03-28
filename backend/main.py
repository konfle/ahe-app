from fastapi import FastAPI

app = FastAPI()


@app.get('/api/health')
def root():
    return {'status': 'available'}
