from fastapi import FastAPI
from script import get_draw_results
from script import get_euromilhoes_results_message

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

@app.get("/formatted_myresults")
def read_results():
    return get_euromilhoes_results_message()