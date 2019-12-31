from fastapi import FastAPI

app = FastAPI()


@app.get("/items/")
async def read_items(q: str = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q is not None:
        results.update({"q": q})
    return results
