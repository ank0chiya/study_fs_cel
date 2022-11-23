from app.worker import cel
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/celery")
def read_root():
    result = cel.send_task('add', (4, 4))
    result.get(timeout=1000)

    print(result.get(timeout=1000))
    return {"add function": result.get(timeout=1000)}
