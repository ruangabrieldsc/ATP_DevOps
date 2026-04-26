from src.main import *
import pytest
import pytest_asyncio


@pytest.mark.asyncio
async def test_teste():
    resultado = await teste()
    assert resultado == {"número1": 1}


@pytest.mark.asyncio
async def test_root():
    resultado = await root()
    assert resultado == {"message": "Teste123"}


@pytest.mark.asyncio
async def test_create_animal(animal: Animal):
    animal_teste = Animal(nome="Pikachu", cor="Amarelho", ativo=True)
    resultado = await criarAnimal(animal_teste)
    assert animal_teste == resultado


def test_calcular_calorias_feijao(gramas):
    assert calcular_calorias_feijao(500) == 380


def melhor_filme(filme):
    assert filme("GTA 6") == False
