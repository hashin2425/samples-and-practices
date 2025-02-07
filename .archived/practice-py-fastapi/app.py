import uvicorn

from fastapi import FastAPI

app = FastAPI()


# http://localhost:8000/docs
# FastAPI automatically generates the OpenAPI schema for the API


# http://localhost:8000/
@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    # python app.py
    uvicorn.run(app, host="localhost", port=8000, log_level="debug")
