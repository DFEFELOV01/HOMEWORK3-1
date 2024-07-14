from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index_page():
    return {"This is ": "homework3!"}


@app.get("/ping/")
def ping_page():
    return {"message": "pong"}