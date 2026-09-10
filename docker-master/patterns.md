# Patterns & Architecture / Padrões e Arquitetura - Docker Master

## 🏛️ Padrões de Dockerfiles (Best Practices)

### 1. Multi-stage Builds (OBRIGATÓRIO PARA PRODUÇÃO)
Separe a fase de compilação/instalação (onde você precisa de compiladores, SDKs e ferramentas de build) da fase de execução.
- **Vantagem:** A imagem final contém apenas o binário compilado e as bibliotecas estritamente necessárias de runtime, diminuindo o tamanho e a superfície de ataque.

```dockerfile
# Estágio 1: Build
FROM golang:1.20 AS builder
WORKDIR /app
COPY . .
RUN go build -o meubinario main.go

# Estágio 2: Produção (Imagem limpa)
FROM alpine:latest
WORKDIR /app
COPY --from=builder /app/meubinario .
CMD ["./meubinario"]
```

### 2. Otimização do Cache de Camadas
A ordem das instruções no `Dockerfile` importa criticamente. O Docker invalida o cache de uma camada se a instrução atual ou os arquivos (`COPY` / `ADD`) mudarem.
- **Regra:** Execute cópias das dependências (ex: `package.json` ou `requirements.txt`) e as instale ANTES de copiar o código-fonte da aplicação inteira.

### 3. Evite o usuário Root (Rootless)
Sempre declare um usuário sem privilégios nas últimas camadas do seu Dockerfile para execução. Se o contêiner for comprometido, o atacante não terá privilégios de root no SO base do contêiner.

```dockerfile
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
```

### 4. Um Processo por Contêiner
O Docker não é uma máquina virtual completa. Contêineres devem ter foco único. Não rode o banco de dados, a aplicação web e o cronjob no mesmo contêiner. Separe-os em três contêineres e una-os via `docker compose`.
