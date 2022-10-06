# VANTAGENS
# Rápida de coloca uma API no ar
# Facilita criando documentação automaticamente
# gerenciamento de processos assincronos
# pip install fastapi 
# pip install uvicorn

from fastapi import FastAPI
#
#
#
minha_api = FastAPI()
# pra executar uma API, abra o terminal na pasta
#     uvicorn main:minha_api --reload
#

# criar rotas ( routes )
@minha_api.get("/")
def home():
    return "Minha API está no ar/on"
# automaticamente no caminho http://127.0.0.1:8000/docs  
# já contem uma documentação sobre a minha_api

# criando um dicionário para teste
vendas = {
    1: {"item": "lata", "preco-unitario": 4, "quantidade": 5 },
    2: {"item": "2l", "preco-unitario": 8, "quantidade": 15},
    3: {"item": "750ml", "preco-unitario": 6, "quantidade": 25},
    4: {"item": "lata-mini", "preco-unitario": 3, "quantidade": 105}
    }

@minha_api.get("/vendas")
def venda():
    return {"vendas": len(vendas)}


@minha_api.get("/consulta/{id_venda}")
# abaixo informar o tipo da variavel do argumento é necessário no fastAPI    
def consulta(id_venda:int):
    if id_venda in vendas:
        return vendas[id_venda]
    else: return {f"Erro: ID {id_venda} não existe"}
    
