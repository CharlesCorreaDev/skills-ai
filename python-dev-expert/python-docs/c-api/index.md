Manual de referência da API C/Python
************************************

Este manual documenta a API usada por programadores C e C++ que
desejam escrever módulos de extensões ou embutir Python. É um
complemento para Estendendo e incorporando o interpretador Python, que
descreve os princípios gerais da escrita de extensões mas não
documenta as funções da API em detalhes.

* Introdução

  * Compatibilidade com a versão da linguagem

  * Padrões de codificação

  * Arquivos de inclusão

  * Macros úteis

  * Objetos, tipos e contagens de referências

  * Exceções

  * Incorporando Python

  * Compilações de depuração

  * Ferramentas de terceiros recomendadas

* C API and ABI Stability

  * API C Instável

  * Stable Application Binary Interfaces

  * Considerações da plataforma

  * ABI Checking

  * Conteúdo da API Limitada

* A camada de nível muito alto

  * Símbolos iniciais disponíveis

  * Stack Effects

* Contagem de referências

* Tratamento de exceções

  * Impressão e limpeza

  * Levantando exceções

  * Emitindo avisos

  * Consultando o indicador de erro

  * Tratamento de sinal

  * Classes de exceção

  * Objeto Exceção

  * Objetos de exceção Unicode

  * Controle de recursão

  * Exception and warning types

  * Tracebacks

* Definindo módulos de extensão

  * Extension export hook

  * Inicialização multifásica

  * Várias instâncias de módulo

  * "PyInit" function

* Slots de definição

  * Macros de conveniência

  * IDs de slot comuns

* Utilitários

  * Utilitários do sistema operacional

  * Funções de sistema

  * Controle de processos

  * Importando módulos

  * Suporte a *marshalling* de dados

  * Análise de argumentos e construção de valores

  * Conversão e formação de strings

  * Classificação e conversão de caracteres

  * API do PyHash

  * Reflexão

  * Registro de codec e funções de suporte

  * API C PyTime

  * Suporte a Mapas do Perf

  * API C do Expat

* Camada de Objetos Abstratos

  * Protocolo de objeto

  * Protocolo de chamada

  * Protocolo de número

  * Protocolo de sequência

  * Protocolo de mapeamento

  * Protocolo Iterador

  * Protocolo de buffer

* Camada de Objetos Concretos

  * Objetos Fundamentais

  * Objetos Numéricos

  * Objetos Sequência

  * Coleções

  * Objetos Função

  * Outros Objetos

  * API C para módulos de extensão

* Interpreter initialization and finalization

  * Before Python initialization

  * Variáveis de configuração global

  * Inicializando e encerrando o interpretador

  * Cautions regarding interpreter finalization

  * Interpreter views

  * Parâmetros de todo o processo

* Thread states and the global interpreter lock

  * Desvinculação do estado de thread do código de extensão

  * Using the C API from foreign threads

  * GIL-state APIs

  * Cuidados com o uso de fork()

  * APIs de alto nível

  * APIs de baixo nível

* Asynchronous notifications

* Operating system thread APIs

* Primitivas de sincronização

  * Python critical section API

  * Legacy locking APIs

* Thread-local storage support

  * Thread-specific storage API

  * Dynamic allocation

  * Métodos

  * Legacy APIs

* Multiple interpreters in a Python process

  * A per-interpreter GIL

  * Bugs and caveats

  * APIs de alto nível

  * APIs de baixo nível

  * Advanced debugger support

* Profiling and tracing

* Reference tracing

* Performance statistics

* Configuração de inicialização do Python

  * API C PyInitConfig

  * Opções de configuração

  * API de configuração Python em tempo de execução

  * API C PyConfig

  * Py_GetArgcArgv()

  * Multi-Phase Initialization Private Provisional API

* Gerenciamento de Memória

  * Visão Geral

  * Allocator Domains

  * Raw Memory Interface

  * Interface da Memória

  * Alocadores de objeto

  * Alocadores de memória padrão

  * Alocadores de memória

  * Debug hooks on the Python memory allocators

  * The pymalloc allocator

  * The mimalloc allocator

  * tracemalloc C API

  * Exemplos

* Suporte a implementação de Objetos

  * Alocando objetos na heap

  * Ciclo de vida do objeto

  * Estruturas comuns de objetos

  * Estruturas de objetos tipo

  * Suporte a Coleta Cíclica de Lixo

* API e Versionamento de ABI

  * Constantes de versão de tempo de construção

  * Versão de tempo de execução

  * Macros de empacotamento de bits

* API C de monitoramento

* Gerando eventos de execução

  * Gerenciando o Estado de um Monitoramento
