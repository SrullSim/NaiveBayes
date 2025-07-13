import  uvicorn
from fastapi import FastAPI
from model.model import Model
from model.classify import ProbabilityCalculater
from model.trainer import Trainer
from model.inputs import Inputs
from model.manager import Manager


app = FastAPI()

@app.get('/{name}')
async  def root(name):
    return {"massage":name }

@app.get("/")
async def root():
    return {"hello": "sopkxcccc"}



if __name__ == "__main__":
    manager = Manager()
    manager.menu()
    uvicorn.run(app, host="127.0.0.1", port=8000)
