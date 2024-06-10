import azure.functions as func
import fastapi


# initialize
app = fastapi.FastAPI()


@app.get("/")
async def hello_world(req: fastapi.Request):
    return {
        "message": "Hello World! This API has enabled.",
    }

