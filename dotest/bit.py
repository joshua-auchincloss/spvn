from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def run_something():
    return "ok"