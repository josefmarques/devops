# pip install fastapi uvicorn sqlalchemy passlib\[bcrypt\] python-jose\[criptography\] python-dotenv python-multipart
# pip install sqlalchemy_utils
# pip install alembic
# alembic init alembic 
# alterar sqlalchemy.url = sqlite://banco.db
#alembic revision --autogenerate -m "Initial Migration"
# executar a migração: alembic upgrade head
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
from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app = FastAPI()

bccrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)