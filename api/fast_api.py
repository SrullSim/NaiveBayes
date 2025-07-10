import  uvicorn
from fastapi import FastAPI


app = FastAPI()

@app.get('/{name}')
async  def root(name):
    return {"massage":name }

@app.get("/")
async def root():
    return {"hello": "sopkxcccc"}



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
