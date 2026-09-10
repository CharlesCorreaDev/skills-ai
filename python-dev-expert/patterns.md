# Patterns & Architecture / Padrões e Arquitetura - Python Developer Expert

## 🏛️ Padrões e Práticas "Pythonic"

### 1. EAFP (Easier to Ask for Forgiveness than Permission)
Em Python, é preferível tentar executar a operação e capturar a exceção (EAFP), ao invés de checar previamente se a operação é válida (LBYL - Look Before You Leap).
- **Ruim:** `if hasattr(obj, 'method'): obj.method()`
- **Bom:** `try: obj.method() except AttributeError: ...`

### 2. Context Managers (`with`)
Sempre use context managers para lidar com recursos (arquivos, conexões de banco, locks) para garantir que eles sejam liberados mesmo se uma exceção ocorrer.
- **Bom:** `with open('file.txt') as f: data = f.read()`

### 3. Decorators
Use decoradores para adicionar funcionalidades a funções de forma limpa (ex: retry logic, logging, authentication, caching via `functools.lru_cache`).

### 4. SOLID e Orientação a Objetos em Python
- **Composition over Inheritance:** Evite hierarquias de herança profundas. Como Python suporta Multiple Inheritance (com MRO), o uso indevido pode gerar código ilegível. Prefira injeção de dependências ou composição (`dataclasses` ajudam muito).
- **Single Responsibility & Interfaces:** Python usa "Duck Typing". Interfaces explícitas podem ser definidas via classe abstrata (`abc.ABC`) ou através de `typing.Protocol` (para checagem estrutural em vez de nominal).

### 5. Generators e Comprehensions
- Substitua loops pesados e criação de listas gigantescas na memória por geradores (`yield`) e generator expressions `(x for x in data)` quando possível.
- Use list/dict/set comprehensions para código mais idiomático e performático do que blocos `for` tradicionais.

### 6. Clean Architecture
Ao construir APIs (com FastAPI, por exemplo):
- **Routers/Controllers**: Apenas recebem a request Pydantic e chamam serviços.
- **Services/Use Cases**: Contêm a lógica de negócio principal. Não sabem que estão em uma API web.
- **Repositories**: Isolam a lógica de acesso a dados (SQLAlchemy).
