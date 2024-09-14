from fastapi import FastAPI
from script import get_draw_results

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/results")
def read_results():
    draw_results = get_draw_results()
    return {
        "stars": draw_results["stars"],
        "numbers": draw_results["numbers"]
    }