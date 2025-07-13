# pip install fastapi uvicorn sqlalchemy passlib\[bcrypt\] python-jose\[criptography\] python-dotenv python-multipart
# pip install sqlalchemy_utils
# pip install alembic
# alembic init alembic 
# alterar sqlalchemy.url = sqlite://banco.db
#alembic revision --autogenerate -m "Initial Migration"
## para rodar o código, executar no terminal: uvicorn main:app --reload
# endpoint: meusite.com 
# rota: /orders (caminho/path)

# Rest APIS
# Get -> leitura/pegar 
# Post -> enviar/criar
# Put/Patch -> edição
# Delete -> deletar

from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bccrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)