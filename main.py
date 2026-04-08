from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Teste123"}

@app.get("/teste")
async def teste():
    return {"Teste": "123"}

