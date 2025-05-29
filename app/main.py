# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from app.api import routes_contratante, routes_auth, routes_endereco, routes_questionario, routes_hobbies
from app.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Libera acesso ao frontend (por exemplo: localhost ou outro)
origins = [
     "http://127.0.0.1:5500",  # Se estiver rodando o HTML local com Live Server (VS Code)
     "http://localhost:5500",  # Ou outra porta
     "http://127.0.0.1:8000",  # Se for consumir do Swagger
 ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou especifique origens: ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos: GET, POST, OPTIONS, etc.
    allow_headers=["*"],  # Permite todos os headers
)


# Criar tabelas no banco
Base.metadata.create_all(bind=engine)


# Incluir as rotas
app.include_router(routes_contratante.router, prefix="/api", tags=["contratante"])
app.include_router(routes_auth.router, prefix="/api", tags=["auth"])
app.include_router(routes_endereco.router, prefix="/api", tags=["endereco"])
app.include_router(routes_questionario.router, prefix="/api", tags=["questionario"])
app.include_router(routes_hobbies.router, prefix="/api", tags=["hobbies"])
