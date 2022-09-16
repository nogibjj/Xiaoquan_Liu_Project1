from fastapi import FastAPI
import uvicorn
from dblib.querydb import querydb

app = FastAPI()

@app.get("/")
async def root():
    return {"This is my first project": "Welcome to the SQL query API"}

@app.get("/information/")
async def information():
    """information about the SQL query API"""

    return {"Datasets": "Health Indicators for Diabetes"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
