from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Animal(BaseModel):
    nome: str
    cor: str
    ativo: bool


@app.get("/")
async def root():
    return {"message": "Teste123"}


@app.get("/teste")
async def teste():
    return {"Teste": "123"}


@app.post("/animais/criar/")
async def criarAnimal(animal: Animal):
    return animal


def calcular_calorias_feijao(gramas):
    return gramas * 0.76


def melhor_filme(filme):
    if filme == "Lago Mungo":
        return True
    else:
        return False
