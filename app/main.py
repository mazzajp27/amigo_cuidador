# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  
from app.api import routes_contratante
from app.database import Base, engine

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Criar tabelas no banco
Base.metadata.create_all(bind=engine)

# Incluir as rotas
app.include_router(routes_contratante.router, prefix="/api")
