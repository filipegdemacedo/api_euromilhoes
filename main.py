from fastapi import FastAPI
from script import get_euromilhoes_results

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/results")
def read_results():
    return(get_euromilhoes_results())