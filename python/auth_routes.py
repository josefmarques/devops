from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao
from main import bccrypt_context


auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticaçào do nosso sistema.
    """
    return {"mensagem": "Você acessou a rota padrão de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    if usuario:
        # já existe um usuario com esse email
        return {"mensagem": "Já existe um usuário com esse email"}
    else:
        senha_criptografada = bccrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuário cadastrado com sucesso!"}

    