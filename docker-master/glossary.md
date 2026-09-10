# Glossary / Glossário - Docker Master

## 📖 Dicionário de Termos Técnicos e Infraestrutura

- **Docker Daemon (`dockerd`)**: O serviço de background que gerencia objetos Docker (imagens, contêineres, redes e volumes). O CLI do Docker se comunica com este daemon.
- **Image (Imagem)**: Um template imutável e de leitura. Contém o sistema operacional base, código, bibliotecas e dependências.
- **Container (Contêiner)**: Uma instância em execução de uma Imagem. Ele isola a aplicação do resto do sistema hospedeiro usando recursos do kernel (cgroups e namespaces).
- **Bind Mount**: Mapeia um arquivo ou diretório exato do sistema hospedeiro (sua máquina física) direto para dentro do contêiner. Geralmente usado para desenvolvimento local (para atualizar o código em tempo real).
- **Volume**: Espaço de armazenamento gerenciado integralmente pelo Docker. É a forma recomendada de persistir dados de banco de dados, sendo isolado do file system principal do usuário e muito mais performático (especialmente no Windows/Mac).
- **WSL2 (Windows Subsystem for Linux)**: Arquitetura da Microsoft que roda um kernel Linux real no Windows. O Docker Desktop usa o WSL2 para rodar os contêineres nativamente sem a pesada camada de VM antiga (Hyper-V).
- **Alpine / Distroless**: Imagens base conhecidas por serem microscópicas (frequentemente < 5MB). Elas não trazem ferramentas do SO (como `bash` ou `apt`), garantindo máxima segurança e tamanho mínimo.
- **Containerd**: Um runtime de contêiner de nível da indústria. O Docker usa o containerd por baixo dos panos para gerenciar o ciclo de vida completo do contêiner.
