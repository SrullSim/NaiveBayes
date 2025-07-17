import  uvicorn
from fastapi import FastAPI
from model.model import Model
from model.probabilityCalculater import ProbabilityCalculater
from model.inputs import Inputs
from model.trainer import Trainer
from model.manager import Manager


app = FastAPI()

@app.get('/{name}')
async  def root(name):
    return {"massage":name }

@app.get("/{path}")
async def display():
    return {"hello": ""}

@app.get("/{path}/")
async def display():
    res =manager.main()
    return res
















if __name__ == "__main__":
    manager = Manager()
    manager.main()
    uvicorn.run(app, host="127.0.0.1", port=8000)
