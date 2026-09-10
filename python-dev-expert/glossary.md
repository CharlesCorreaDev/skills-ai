# Glossary / Glossário - Python Developer Expert

## 📖 Dicionário de Termos Técnicos

- **GIL (Global Interpreter Lock)**: Mecanismo no CPython que garante que apenas uma thread execute o bytecode Python por vez. Isso torna o Python thread-safe, mas impede o verdadeiro paralelismo em operações CPU-bound com threads (necessitando o uso de `multiprocessing`).
- **PEP 8**: O guia de estilo oficial para código Python (Python Enhancement Proposal 8). Define regras de formatação, nomenclatura de variáveis e boas práticas de legibilidade.
- **Dunder Methods (Magic Methods)**: Métodos que começam e terminam com dois underscores (ex: `__init__`, `__str__`, `__add__`). Eles permitem sobrecarregar operadores e integrar objetos customizados com as funções nativas da linguagem.
- **WSGI / ASGI**: 
  - **WSGI** (Web Server Gateway Interface): Padrão síncrono legado para comunicação entre servidores web e aplicações Python (ex: Gunicorn + Flask).
  - **ASGI** (Asynchronous Server Gateway Interface): O padrão moderno que suporta requisições assíncronas e WebSockets (ex: Uvicorn + FastAPI).
- **Duck Typing**: Conceito fundamental no Python: "Se anda como um pato e grasna como um pato, deve ser um pato". A checagem de tipos foca nos métodos e propriedades que o objeto possui, não na sua classe herdada.
- **Type Hinting**: Anotações opcionais de tipos introduzidas na PEP 484. Elas não são forçadas em tempo de execução, mas permitem checagem estática poderosa via ferramentas como `mypy`.
- **CPython / PyPy**: CPython é a implementação padrão e mais utilizada do Python (escrita em C). PyPy é uma implementação alternativa que usa JIT, focada em alta performance para código puro Python.
