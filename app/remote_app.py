from worker import cel
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str


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


@app.post("/folder")
async def read_root(item: Item):
    # use id
    task_name = "post.folder"
    task = cel.send_task(task_name, args=[item.name])
    return dict(id=task.id, url=f'localhost:8000/folder/{task.id}')


@app.get("/folder/{id}")
def read_root(id: str):
    # use id
    task = cel.AsyncResult(id)
    response = {
        "state": task.state,
        "result": task.result,
        "task_id": task.id
    }
    return response
