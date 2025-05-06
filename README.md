# Amigo Cuidador
Criação de api com FastAPI 
### Para iniciar a aplicação digite o comando abaixo no diretório amigo_cuidador/
uvicorn app.main:app --reload

```bash

/amigo_cuidador/
│
├── app/
│   ├── __init__.py
│   ├── main.py        # Onde fica o app FastAPI e inicializa tudo
│   ├── crud/
│   │   ├── __init__.py
│   │   └── contratante.py   # Funções de banco: criar, listar, editar tênis
│   ├── models/
│   │   ├── __init__.py
│   │   └── contratante.py   # Model Contratante
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── contratante.py   # Pydantic BaseModel para validar entrada/saída
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes_contratante.py  # As rotas (endpoints) que chamam o CRUD
│   └── database.py    # Conexão e criação do banco
│   ├── testes/
│
├── env_exemplo.txt   # Exemplo para listar as variáveis de ambiente 
├── requirements.txt  # Dependências do projeto
├── .gitignore        # Arquivo que define o que o Git deve ignorar     
└── README.md         # Explicações

```

## database.py
- configura string de conexao ao banco

