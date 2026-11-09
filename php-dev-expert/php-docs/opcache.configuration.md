# Configurações de Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/opcache.configuration.php

---

## Configurações de Execução

O comportamento destas funções é afetado pelas configurações do php.ini.

**Opções de configuração do OPcache**

| Nome | Padrão | Modificável | Registro de Alterações |
| --- | --- | --- | --- |
| [opcache.enable](opcache.configuration.md#ini.opcache.enable) | 1 | **`INI_ALL`** |  |
| [opcache.enable\_cli](opcache.configuration.md#ini.opcache.enable-cli) | 0 | **`INI_SYSTEM`** | Entre PHP 7.1.2 e 7.1.6 inclusive, o padrão era `1` |
| [opcache.memory\_consumption](opcache.configuration.md#ini.opcache.memory-consumption) | 128 | **`INI_SYSTEM`** |  |
| [opcache.interned\_strings\_buffer](opcache.configuration.md#ini.opcache.interned-strings-buffer) | 8 | **`INI_SYSTEM`** |  |
| [opcache.max\_accelerated\_files](opcache.configuration.md#ini.opcache.max-accelerated-files) | 10000 | **`INI_SYSTEM`** |  |
| [opcache.max\_wasted\_percentage](opcache.configuration.md#ini.opcache.max-wasted-percentage) | 5 | **`INI_SYSTEM`** |  |
| [opcache.use\_cwd](opcache.configuration.md#ini.opcache.use-cwd) | 1 | **`INI_SYSTEM`** |  |
| [opcache.validate\_timestamps](opcache.configuration.md#ini.opcache.validate-timestamps) | 1 | **`INI_ALL`** |  |
| [opcache.revalidate\_freq](opcache.configuration.md#ini.opcache.revalidate-freq) | 2 | **`INI_ALL`** |  |
| [opcache.revalidate\_path](opcache.configuration.md#ini.opcache.revalidate-path) | 0 | **`INI_ALL`** |  |
| [opcache.save\_comments](opcache.configuration.md#ini.opcache.save-comments) | 1 | **`INI_SYSTEM`** |  |
| [opcache.fast\_shutdown](opcache.configuration.md#ini.opcache.fast-shutdown) | 0 | **`INI_SYSTEM`** | Removido no PHP 7.2.0 |
| [opcache.enable\_file\_override](opcache.configuration.md#ini.opcache.enable-file-override) | 0 | **`INI_SYSTEM`** |  |
| [opcache.optimization\_level](opcache.configuration.md#ini.opcache.optimization-level) | 0x7FFEBFFF | **`INI_SYSTEM`** | Alterado de `0x7FFFBFFF` no PHP 7.3.0 |
| [opcache.inherited\_hack](opcache.configuration.md#ini.opcache.inherited-hack) | 1 | **`INI_SYSTEM`** | Removido no PHP 7.3.0 |
| [opcache.dups\_fix](opcache.configuration.md#ini.opcache.dups-fix) | 0 | **`INI_ALL`** |  |
| [opcache.blacklist\_filename](opcache.configuration.md#ini.opcache.blacklist-filename) | "" | **`INI_SYSTEM`** |  |
| [opcache.max\_file\_size](opcache.configuration.md#ini.opcache.max-file-size) | 0 | **`INI_SYSTEM`** |  |
| [opcache.consistency\_checks](opcache.configuration.md#ini.opcache.consistency-checks) | 0 | **`INI_ALL`** | Desativado a partir do 8.1.18 e 8.2.5. Removido a partir do PHP 8.3.0 |
| [opcache.force\_restart\_timeout](opcache.configuration.md#ini.opcache.force-restart-timeout) | 180 | **`INI_SYSTEM`** |  |
| [opcache.error\_log](opcache.configuration.md#ini.opcache.error-log) | "" | **`INI_SYSTEM`** |  |
| [opcache.log\_verbosity\_level](opcache.configuration.md#ini.opcache.log-verbosity-level) | 1 | **`INI_SYSTEM`** |  |
| [opcache.record\_warnings](opcache.configuration.md#ini.opcache.record-warnings) | 0 | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0 |
| [opcache.preferred\_memory\_model](opcache.configuration.md#ini.opcache.preferred-memory-model) | "" | **`INI_SYSTEM`** |  |
| [opcache.protect\_memory](opcache.configuration.md#ini.opcache.protect-memory) | 0 | **`INI_SYSTEM`** |  |
| [opcache.mmap\_base](opcache.configuration.md#ini.opcache.mmap-base) | **`null`** | **`INI_SYSTEM`** |  |
| [opcache.restrict\_api](opcache.configuration.md#ini.opcache.restrict-api) | "" | **`INI_SYSTEM`** |  |
| [opcache.file\_update\_protection](opcache.configuration.md#ini.opcache.file_update_protection) | 2 | **`INI_ALL`** |  |
| [opcache.huge\_code\_pages](opcache.configuration.md#ini.opcache.huge_code_pages) | 0 | **`INI_SYSTEM`** |  |
| [opcache.lockfile\_path](opcache.configuration.md#ini.opcache.lockfile_path) | "/tmp" | **`INI_SYSTEM`** |  |
| [opcache.opt\_debug\_level](opcache.configuration.md#ini.opcache.opt_debug_level) | 0 | **`INI_SYSTEM`** | Disponível a partir do PHP 7.1.0 |
| [opcache.file\_cache](opcache.configuration.md#ini.opcache.file-cache) | **`null`** | **`INI_SYSTEM`** |  |
| [opcache.file\_cache\_only](opcache.configuration.md#ini.opcache.file-cache-only) | 0 | **`INI_SYSTEM`** |  |
| [opcache.file\_cache\_consistency\_checks](opcache.configuration.md#ini.opcache.file-cache-consistency-checks) | 1 | **`INI_SYSTEM`** |  |
| [opcache.file\_cache\_fallback](opcache.configuration.md#ini.opcache.file-cache-fallback) | 1 | **`INI_SYSTEM`** | Somente Windows. |
| [opcache.validate\_permission](opcache.configuration.md#ini.opcache.validate-permission) | 0 | **`INI_SYSTEM`** | Disponível a partir do PHP 7.0.14 |
| [opcache.validate\_root](opcache.configuration.md#ini.opcache.validate-root) | 0 | **`INI_SYSTEM`** | Disponível a partir do PHP 7.0.14 |
| [opcache.preload](opcache.configuration.md#ini.opcache.preload) | "" | **`INI_SYSTEM`** | Disponível a partir do PHP 7.4.0 |
| [opcache.preload\_user](opcache.configuration.md#ini.opcache.preload-user) | "" | **`INI_SYSTEM`** | Disponível a partir do PHP 7.4.0 |
| [opcache.cache\_id](opcache.configuration.md#ini.opcache.cache-id) | "" | **`INI_SYSTEM`** | Somente Windows. Disponível a partir do PHP 7.4.0 |
| [opcache.jit](opcache.configuration.md#ini.opcache.jit) | "disable" | **`INI_ALL`** | Disponível a partir do PHP 8.0.0. Antes do PHP 8.4.0, o valor padrão era "tracing". |
| [opcache.jit\_buffer\_size](opcache.configuration.md#ini.opcache.jit-buffer-size) | 64M | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0. Antes do PHP 8.4.0, o valor padrão era 0. |
| [opcache.jit\_debug](opcache.configuration.md#ini.opcache.jit-debug) | 0 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_bisect\_limit](opcache.configuration.md#ini.opcache.jit-bisect-limit) | 0 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_prof\_threshold](opcache.configuration.md#ini.opcache.jit-prof-threshold) | 0.005 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_max\_root\_traces](opcache.configuration.md#ini.opcache.jit-max-root-traces) | 1024 | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_max\_side\_traces](opcache.configuration.md#ini.opcache.jit-max-side-traces) | 128 | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_max\_exit\_counters](opcache.configuration.md#ini.opcache.jit-max-exit-counters) | 8192 | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_hot\_loop](opcache.configuration.md#ini.opcache.jit-hot-loop) | 61 | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0, antes do PHP 8.5.0, o valor padrão era 64 |
| [opcache.jit\_hot\_func](opcache.configuration.md#ini.opcache.jit-hot-func) | 127 | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_hot\_return](opcache.configuration.md#ini.opcache.jit-hot-return) | 8 | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_hot\_side\_exit](opcache.configuration.md#ini.opcache.jit-hot-side-exit) | 8 | **`INI_SYSTEM`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_blacklist\_root\_trace](opcache.configuration.md#ini.opcache.jit-blacklist-root-trace) | 16 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_blacklist\_side\_trace](opcache.configuration.md#ini.opcache.jit-blacklist-side-trace) | 8 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_max\_loop\_unrolls](opcache.configuration.md#ini.opcache.jit-max-loop-unrolls) | 8 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_max\_recursive\_calls](opcache.configuration.md#ini.opcache.jit-max-recursive-calls) | 2 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_max\_recursive\_returns](opcache.configuration.md#ini.opcache.jit-max-recursive-return) | 2 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |
| [opcache.jit\_max\_polymorphic\_calls](opcache.configuration.md#ini.opcache.jit-max-polymorphic-calls) | 2 | **`INI_ALL`** | Disponível a partir do PHP 8.0.0 |

Para mais detalhes e definições dos modos
INI\_\*, consulte os [Onde uma configuração deve ser definida](configuration.changes.modes.md).

Aqui está uma breve explicação das
diretivas de configuração.

`opcache.enable` [bool](language.types.boolean.md)
:   Habilita o cache opcode. Quando desabilitado, o código não é otimizado ou
    armazenado em cache. A configuração `opcache.enable` não pode ser
    habilitada em tempo de execução através de [ini\_set()](function.ini-set.md), ela só pode
    ser desabilitada. Tentar ativá-lo em um script gerará um aviso.

`opcache.enable_cli` [bool](language.types.boolean.md)
:   Ativa o cache opcode para a versão CLI do PHP.

`opcache.memory_consumption` [int](language.types.integer.md)
:   O tamanho do armazenamento de memória compartilhada usado pelo OPcache, em megabytes.
    O valor mínimo permitido é `"8"`,
    que é aplicado se um valor menor for definido.

`opcache.interned_strings_buffer` [int](language.types.integer.md)
:   A quantidade de memória usada para armazenar strings internas, em megabytes.
    O valor máximo é de 32767 em arquiteturas de 64 bits.,
    e 4095 nas de 32 bits.

    > **Nota**:
    >
    > Antes do PHP 8.4.0, o valor máximo era de 4095 megabytes para todas
    > as arquiteturas.

`opcache.max_accelerated_files` [int](language.types.integer.md)
:   O número máximo de chaves (e, portanto, scripts) na tabela de hash do OPcache.
    O valor real usado será o primeiro número no conjunto de
    números primos
    `{ 223, 463, 983, 1979, 3907, 7963, 16229, 32531, 65407, 130987, 262237, 524521, 1048793 }`
    que é maior ou igual ao valor configurado. O valor mínimo é 200. O valor máximo
    é 1.000.000.
    Valores fora desta faixa são fixados na faixa permitida.

`opcache.max_wasted_percentage` [int](language.types.integer.md)
:   A porcentagem máxima de memória desperdiçada que é permitida antes de uma reinicialização
    ser planejada, se houver memória livre insuficiente.
    O valor máximo permitido é `"50"`,
    que é aplicado se um valor maior for definido.

`opcache.use_cwd` [bool](language.types.boolean.md)
:   Se ativado, o OPcache anexa o diretório de trabalho atual à chave de script,
    eliminando assim possíveis colisões entre arquivos com o mesmo nome de base.
    Desativar esta diretiva melhora o desempenho, mas pode interromper os
    aplicativos existentes.

`opcache.validate_timestamps` [bool](language.types.boolean.md)
:   Se ativado, o OPcache verificará os scripts atualizados a cada
    [opcache.revalidate\_freq](opcache.configuration.md#ini.opcache.revalidate-freq)
    segundos. Quando esta diretiva é desativada, você deve redefinir o OPcache
    manualmente via [opcache\_reset()](function.opcache-reset.md),
    [opcache\_invalidate()](function.opcache-invalidate.md) ou reiniciando o servidor Web
    para que as alterações no sistema de arquivos entrem em vigor.
    > **Nota**:
    >
    > O OPcache ainda pode validar o carimbo de data e hora de um arquivo durante o tempo de compilação se
    > as opções [opcache.file\_update\_protection](opcache.configuration.md#ini.opcache.file_update_protection) ou
    > [opcache.max\_file\_size](opcache.configuration.md#ini.opcache.max-file-size)
    > estiverem definidas com valores diferentes de zero.

`opcache.revalidate_freq` [int](language.types.integer.md)
:   Com que frequência verificar carimbos de data/hora do script para atualizações, em segundos.
    `0` resultará na verificação de atualizações do OPcache em
    cada solicitação.

    Esta diretiva de configuração será ignorada se
    [opcache.validate\_timestamps](opcache.configuration.md#ini.opcache.validate-timestamps)
    estiver desativado.

`opcache.revalidate_path` [bool](language.types.boolean.md)
:   Se desativado, os arquivos em cache existentes usando o mesmo
    [include\_path](ini.core.md#ini.include-path) serão reutilizados.
    Assim, se um arquivo com o mesmo nome estiver em outro lugar no include\_path,
    ele não será encontrado.

`opcache.save_comments` [bool](language.types.boolean.md)
:   Se desativado, todos os comentários da documentação serão descartados
    do cache do opcode para reduzir o tamanho do código otimizado. Desativar esta
    diretiva de configuração pode interromper aplicativos e frameworks que
    dependem da análise de comentários para anotações, incluindo Doctrine, Zend Framework 2
    e PHPUnit.

`opcache.fast_shutdown` [bool](language.types.boolean.md)
:   Se ativado, uma sequência de desligamento rápido é usada que não libera cada
    bloco alocado, mas depende do gerenciador de memória do Zend Engine para
    desalocar todo o conjunto de variáveis de solicitação em massa.

    Esta diretiva foi removida no PHP 7.2.0. Uma variante da sequência
    de desligamento rápido foi integrada ao PHP e será usada automaticamente,
    se possível.

`opcache.enable_file_override` [bool](language.types.boolean.md)
:   Quando ativado, o cache opcode será verificado para saber se um arquivo
    já foi armazenado em cache quando [file\_exists()](function.file-exists.md),
    [is\_file()](function.is-file.md) e [is\_readable()](function.is-readable.md) são
    chamados. Isso pode aumentar o desempenho em aplicativos que verificam
    a existência e legibilidade de scripts PHP, mas corre o risco de retornar dados desatualizados
    se
    [opcache.validate\_timestamps](opcache.configuration.md#ini.opcache.validate-timestamps)
    estiver desabilitado.

`opcache.optimization_level` [int](language.types.integer.md)
:   Uma máscara de bits que controla quais passos de otimização são executados.
    O valor padrão é `0x7FFEBFFF`, que habilita todas as
    otimizações seguras. Desabilitar otimizações ou habilitar otimizações inseguras
    é útil na maioria das vezes para depurar/desenvolver o otimizador.

    Cada bit da máscara habilita um passo específico da otimização:

    **Máscara de Bits de Passos da Otimização**

    | Bit | Nome do Passo | Descrição | Padrão |
    | --- | --- | --- | --- |
    | 0 | PASS\_1 | Otimizações simples de olho mágico | Ligado |
    | 1 | PASS\_2 | Não utilizado (mesclado ao PASS\_1) | Ligado |
    | 2 | PASS\_3 | Otimização de salto simples | Ligado |
    | 3 | PASS\_4 | Otimização de chamadas | Ligado |
    | 4 | PASS\_5 | Otimização baseada em grafo de fluxo de controle | Ligado |
    | 5 | PASS\_6 | Otimização baseada em análise de fluxo de dados | Ligado |
    | 6 | PASS\_7 | Se o grafo de chamadas deve ser usado para otimizações baseadas em SSA. | Ligado |
    | 7 | PASS\_8 | Propagação esparsa de constantes condicionais | Ligado |
    | 8 | PASS\_9 | Otimização de variáveis ​​temporárias | Ligado |
    | 9 | PASS\_10 | Remoção de opcodes NOP | Ligado |
    | 10 | PASS\_11 | Compactação literal | Ligado |
    | 11 | PASS\_12 | Pré-calcular o tamanho da pilha de chamadas | Ligado |
    | 12 | PASS\_13 | Remoção de variáveis ​​não utilizadas | Ligado |
    | 13 | PASS\_14 | Eliminação de código morto | Ligado |
    | 14 | PASS\_15 | Coletar e substituir declarações constantes (inseguro) | *Desligado* |
    | 15 | PASS\_16 | Inlining de função trivial (parte da otimização de chamadas) | Ligado |
    | 16 | (Flag) | Ignorar a possibilidade de sobrecarga do operador (inseguro) | *Desligado* |

    > **Nota**:
    > **Otimizações Seguras versus Inseguras**  
    >
    > *Otimizações Seguras* (habilitadas por padrão) preservam o comportamento
    > exato do código PHP enquanto melhora o desempenho. Elas incluem eliminação de código morto,
    > a redução de constantes e a otimização de saltos.
    >
    > *Otimizações Inseguras* (desabilitadas por padrão) podem alterar o comportamento
    > em casos extremos:
    >
    > - *Bit 14*: Coletando constantes. As constantes são substituídas
    >   no momento da compilação, ignorando a ordem de declaração do momento da execução:
    >
    >   ```
    >   <?php
    >   echo getA();         // Resultado: "hello" em vez de lançar um Error
    >   const A = "hello";
    >   function getA() { return A; }
    >   ```
    > - *Bit 16*: Ignorando a sobrecarga do operador.
    >   Inseguro ao usar classes com `do_operation`
    >   (ex.: [GMP](book.gmp.md),
    >   [BCMath](book.bc.md)) em operações aritméticas.
    >   Com declarações de tipo, o otimizador pode aplicar as mesmas otimizações de forma segura.

`opcache.inherited_hack` [bool](language.types.boolean.md)
:   Esta diretiva de configuração é ignorada.

`opcache.dups_fix` [bool](language.types.boolean.md)
:   Este hack só deve ser ativado para contornar os erros
    "Cannot redeclare class".

`opcache.blacklist_filename` [string](language.types.string.md)
:   A localização do arquivo de eliminação do OPcache. Um arquivo de eliminação
    é um arquivo de texto contendo os nomes dos arquivos que não devem ser acelerados, um por
    linha. Curingas(\*) são permitidos e prefixos também podem ser fornecidos.
    As linhas iniciadas com ponto e vírgula são ignoradas como comentários.

    Um arquivo de eliminação simples pode ter a seguinte aparência:

    ```
    ; Corresponde a um arquivo específico.
    /var/www/broken.php
    ; Um prefixo que corresponde a todos os arquivos que começam com x.
    /var/www/x
    ; Uma correspondência curinga.
    /var/www/*-broken.php
    ```

`opcache.max_file_size` [int](language.types.integer.md)
:   O tamanho máximo do arquivo que será armazenado em cache, em bytes. Se for
    `0`, todos os arquivos serão armazenados em cache.

`opcache.consistency_checks` [int](language.types.integer.md)
:   Se diferente de zero, o OPcache verificará a soma de verificação do cache a cada N solicitações,
    onde N é o valor desta diretiva de configuração. Isso só deve ser
    ativado durante a depuração, pois prejudicará o desempenho.

    > **Nota**:
    >
    > Desativado a partir do 8.1.18 e 8.2.5. Removido a partir do PHP 8.3.0.

`opcache.force_restart_timeout` [int](language.types.integer.md)
:   O tempo de espera para iniciar uma reinicialização agendada se o cache
    não estiver ativo, em segundos. Se o tempo limite for atingido, o OPcache assumirá
    que algo está errado e eliminará os processos que mantêm bloqueios no cache
    para permitir uma reinicialização.

    Se
    [opcache.log\_verbosity\_level](opcache.configuration.md#ini.opcache.log-verbosity-level)
    for definido como 2 ou superior, um aviso será registrado no log de erros quando
    isso ocorrer.

    Esta diretiva não é suportada no Windows.

`opcache.error_log` [string](language.types.string.md)
:   O log de erros para erros do OPcache. Uma string vazia é tratada da mesma forma que
    `stderr` e resultará no envio de logs para
    erro padrão (que será o log de erro do servidor Web na maioria dos casos).

`opcache.log_verbosity_level` [int](language.types.integer.md)
:   O nível de verbosidade do log. Por padrão, apenas erros fatais (nível 0) e
    erros (nível 1) são registrados. Outros níveis disponíveis são avisos (nível
    2), mensagens informativas (nível 3) e mensagens de depuração (nível 4).

`opcache.record_warnings` [bool](language.types.boolean.md)
:   Se ativado, o OPcache registrará avisos em tempo de compilação e os reproduzirá na
    próxima inclusão, mesmo que seja servido do cache.

`opcache.preferred_memory_model` [string](language.types.string.md)
:   O modelo de memória preferencial para uso do OPcache. Se deixado em branco, o OPcache
    escolherá o modelo mais adequado, que é o comportamento correto
    em praticamente todos os casos.

    Os valores possíveis incluem `mmap`, `shm`,
    `posix` e `win32`.

`opcache.protect_memory` [bool](language.types.boolean.md)
:   Protege a memória compartilhada contra gravações inesperadas durante a execução de scripts.
    Isso é útil apenas para depuração interna.

`opcache.mmap_base` [string](language.types.string.md)
:   A base usada para segmentos de memória compartilhada no Windows. Todos os processos PHP
    precisam mapear a memória compartilhada no mesmo espaço de endereço. O uso desta
    diretiva permite que os erros "Unable to reattach to base address" sejam
    corrigidos.

`opcache.restrict_api` [string](language.types.string.md)
:   Permite chamar funções da API do OPcache apenas de scripts PHP cujo caminho
    é iniciado a partir da string especificada. O padrão `""`
    significa nenhuma restrição.

`opcache.file_update_protection` [string](language.types.string.md)
:   Impede o armazenamento em cache de arquivos que tenham menos de um determinado número de segundos desde a última modificação.
    Isso protege contra o armazenamento em cache de arquivos que tenham sido atualizados de forma incompleta. Caso todas as
    atualizações forem atômicas, o desempenho pode ser aumentado definindo isso como `0`.
    Isso permitirá que os arquivos sejam armazenados em cache imediatamente.

`opcache.huge_code_pages` [bool](language.types.boolean.md)
:   Ativa ou desativa a cópia do código PHP (segmento de texto) em PÁGINAS ENORMES.
    Isso deve melhorar o desempenho, mas requer configuração de sistema operacional apropriada.
    Disponível no Linux a partir do PHP 7.0.0 e no FreeBSD a partir do PHP 7.4.0.

`opcache.lockfile_path` [string](language.types.string.md)
:   Caminho absoluto usado para armazenar arquivos de bloqueio compartilhados (somente para \* nix)

`opcache.opt_debug_level` [string](language.types.string.md)
:   Produz opcode dumps para depurar diferentes estágios de otimizações.
    0x10000 produzirá opcodes conforme o compilador os produziu antes que qualquer otimização ocorra,
    enquanto 0x20000 produzirá códigos otimizados.

`opcache.file_cache` [string](language.types.string.md)
:   Ativa e define o diretório de cache de segundo nível. Ele deve melhorar
    o desempenho quando a memória SHM estiver cheia, na reinicialização do servidor ou
    na reinicialização do SHM. O padrão `""` desativa o cache baseado em arquivo.

`opcache.file_cache_only` [bool](language.types.boolean.md)
:   Ativa ou desativa o armazenamento em cache opcode na memória compartilhada.

    > **Nota**:
    >
    > Antes do PHP 8.1.0, desabilitar esta diretiva com um cache de arquivo já preenchido
    > era necessário para limpar manualmente o cache de arquivo.

`opcache.file_cache_consistency_checks` [bool](language.types.boolean.md)
:   Ativa ou desativa a validação da soma de verificação quando o script é carregado do cache do arquivo.

`opcache.file_cache_fallback` [bool](language.types.boolean.md)
:   Implica em `opcache.file_cache_only=1` para um determinado processo que
    falhou ao se reconectar à memória compartilhada (somente para Windows). É necessário habilitar
    explicitamente o cache de arquivos.

    **Cuidado**

    Desativar esta opção de configuração pode impedir que os processos sejam iniciados
    e, portanto, é desencorajado.

`opcache.validate_permission` [bool](language.types.boolean.md)
:   Valida as permissões do arquivo em cache no usuário atual.

`opcache.validate_root` [bool](language.types.boolean.md)
:   Evita colisões de nomes em ambientes chroot'ed. Isso deve ser ativado em
    todos os ambientes chroot'ed para impedir o acesso a arquivos fora do chroot.

`opcache.preload` [string](language.types.string.md)
:   Especifica um script PHP que será compilado e executado na inicialização do servidor
    e que pode pré-carregar outros arquivos, seja por [include](function.include.md)ing ou usando
    a função [opcache\_compile\_file()](function.opcache-compile-file.md). Todas as entidades (por exemplo,
    funções e classes) definidas nesses arquivos estarão disponíveis para solicitações prontas
    para uso, até que o servidor seja desligado.

    > **Nota**:
    >
    > O pré-carregamento não é suportado no Windows.

`opcache.preload_user` [string](language.types.string.md)
:   Permite que o pré-carregamento seja executado como o usuário do sistema especificado. Isso é útil
    para servidores que inicializam como root antes de alternar para um usuário de sistema sem privilégios.
    O pré-carregamento como root não é permitido por padrão por motivos de segurança,
    a menos que esta diretiva seja explicitamente definida como `root`.
    A partir do PHP 8.3.0, esta diretiva não precisa ser definida para permitir pré-carregamento quando
    executado como root ao usar o CLI SAPI ou o [SAPI phpdbg](book.phpdbg.md).

`opcache.cache_id` [string](language.types.string.md)
:   No Windows, todos os processos executando o mesmo PHP SAPI
    na mesma conta de usuário com o mesmo ID de cache compartilham uma única instância do OPcache.
    O valor do cache ID pode ser escolhido livremente.

    **Dica**

    Para IIS, diferentes pools de aplicativos podem ter sua própria instância OPcache
    usando a variável de ambiente APP\_POOL\_ID como
    `opcache.cache_id`.

`opcache.jit` [string](language.types.string.md)|[int](language.types.integer.md)
:   Para uso típico, esta opção aceita um dos quatro valores de string:

    - `disable`: Completamente desativado, não pode ser ativado em tempo de execução.
    - `off`: Desativado, mas pode ser ativado em tempo de execução.
    - `tracing`/`on`:Use rastreamento JIT.
      Recomendado para a maioria dos usuários. Antes do PHP 8.4.0, este era o valor
      padrão; a partir do PHP 8.4.0, o padrão é `disable`.
    - `function`: Use function JIT.

    Para uso avançado, esta opção aceita um `CRTO` inteiro de 4 dígitos, onde os dígitos significam:

    `C` (CPU-sinalizadores de otimização específicos)
    :   - `0`: Desative a otimização específica da CPU.
        - `1`: Habilite o uso do AVX, se a CPU for compatível.

    `R` (alocação de registro)
    :   - `0`: Não execute alocação de registro.
        - `1`: Execute a alocação de registrador local de bloco.
        - `2`: Execute a alocação global de registradores.

    `T` (gatilho(trigger))
    :   - `0`: Compile todas as funções no carregamento do script.
        - `1`: Compile funções na primeira execução.
        - `2`: Funções de perfil no primeiro pedido e compilação das funções mais
          quentes depois.
        - `3`: Crie perfis em tempo real e compile funções importantes.
        - `4`: Atualmente sem uso.
        - `5`: Use tracing JIT. Crie perfis em tempo real e
          compile rastreamentos para segmentos de código dinâmico.

    `O` (nível de otimização)
    :   - `0`: Sem JIT.
        - `1`: JIT mínimo (chamada de manipuladores de VM padrão).
        - `2`: Manipuladores de VM embutidos.
        - `3`: Use inferência de tipo.
        - `4`: Usar gráfico de chamada.
        - `5`: Otimize todo o script.

    O modo `"tracing"` corresponde a `CRTO = 1254`,
    o modo `"function"` corresponde a `CRTO = 1205`.

    > **Nota**:
    >
    > A partiro do PHP 8.4.0, se o JIT estiver ativo, o PHP sai com um erro fatal
    > no início quando a inicialização do JIT falhar.

`opcache.jit_buffer_size` [int](language.types.integer.md)
:   A quantidade de memória compartilhada a ser reservada para o código JIT compilado. Um valor zero desativa o JIT.

    Quando um [int](language.types.integer.md) é usado, o
    valor é medido em bytes. A notação abreviada, como descrita
    [nesta FAQ](faq.using.md#faq.using.shorthandbytes), também pode ser usada.

`opcache.jit_debug` [int](language.types.integer.md)
:   Uma máscara de bits especificando qual saída de depuração JIT habilitar.
    Para possíveis valores, consulte
    [» zend\_jit.h](https://github.com/php/php-src/blob/master/ext/opcache/jit/zend_jit.h)
    (procure por definições de macro começando com `ZEND_JIT_DEBUG`).

`opcache.jit_bisect_limit` [int](language.types.integer.md)
:   Opção de depuração que desativa a compilação JIT após a compilação de um determinado número de funções.
    Isso pode ser útil para dividir a origem de um erro de compilação JIT. Observação: esta opção só funciona
    quando o gatilho JIT é definido como 0 (compilar no carregamento do script) ou 1 (compilar na primeira execução),
    por exemplo, `opcache.jit=1215`. Veja mais na opção [opcache.jit](opcache.configuration.md#ini.opcache.jit).

`opcache.jit_prof_threshold` [float](language.types.float.md)
:   Ao usar o modo de trigger "profile on first request", esse limite determina se uma
    função é considerada ativa. O número de chamadas para a função dividido pelo número de chamadas
    para todas as funções deve estar acima do limite. Por exemplo, um limite de 0,005 significa que as
    funções que representam mais de 0,5% de todas as chamadas serão compiladas por JIT.

`opcache.jit_max_root_traces` [int](language.types.integer.md)
:   Número máximo de root traces. O root trace é um fluxo de execução que percorre primeiro um
    caminho através do código, que é uma unidade de compilação JIT. O JIT não compilará o novo código se atingir esse limite.

`opcache.jit_max_side_traces` [int](language.types.integer.md)
:   Número máximo de side traces que um root trace pode ter. O side trace é outro fluxo de execução
    que não segue o caminho do root trace compilado. Os sides traces pertencentes ao mesmo
    root trace não serão compilados se atingirem esse limite.

`opcache.jit_max_exit_counters` [int](language.types.integer.md)
:   Número máximo de contadores de saída de side trace. Isso limita o número total de side traces
    que podem existir, em todos os root traces.

`opcache.jit_hot_loop` [int](language.types.integer.md)
:   Depois de quantas iterações um laço é considerado ativo.
    O intervalo de valores válidos é `[0,255]`; para qualquer configuração fora desse intervalo,
    por exemplo, `-1` ou `256`, o valor padrão será usado.
    O valor `0` desabilitará o JIT para rastrear ou compilar quaisquer laços.

    > **Nota**:
    >
    > É recomendado que este parâmetro seja definido para um número primo
    > para evitar que ele seja um múltiplo da contagem de laços de iteração.

`opcache.jit_hot_func` [int](language.types.integer.md)
:   Depois de quantas chamadas uma função é considerada ativa.
    O intervalo de valores válidos é `[0,255]`; para qualquer configuração fora desse intervalo,
    por exemplo, `-1` ou `256`, o valor padrão será usado.
    O valor `0` desabilitará o JIT para rastrear e compilar quaisquer funções.

`opcache.jit_hot_return` [int](language.types.integer.md)
:   Depois de quantos retornos, um retorno é considerado ativo.
    O intervalo de valores válidos é `[0,255]`; para qualquer configuração fora desse intervalo,
    por exemplo, `-1` ou `256`, o valor padrão será usado.
    O valor `0` desabilitará o JIT para rastrear e compilar quaisquer retornos.

`opcache.jit_hot_side_exit` [int](language.types.integer.md)
:   Depois de quantas saídas uma saída secundária é considerada ativa.
    O intervalo de valores válidos é `[0,255]`; para qualquer configuração fora desse intervalo,
    por exemplo, `-1` ou `256`, o valor padrão será usado.
    O valor zero `0` desabilitará o JIT para rastrear e compilar quaisquer saídas secundárias.

`opcache.jit_blacklist_root_trace` [int](language.types.integer.md)
:   Número máximo de vezes que a compilação de um root trace é tentada antes de ser incluída na blacklist.

`opcache.jit_blacklist_side_trace` [int](language.types.integer.md)
:   Número máximo de vezes que a compilação de um side trace é tentada antes de ser incluída na blacklist.

`opcache.jit_max_loop_unrolls` [int](language.types.integer.md)
:   Número máximo de tentativas de resolver um loop em um traço lateral,
    tentando alcançar o root trace e fechar o loop externo.

`opcache.jit_max_recursive_calls` [int](language.types.integer.md)
:   Número máximo de loops de chamada recursiva.

`opcache.jit_max_recursive_returns` [int](language.types.integer.md)
:   Número máximo de loops de retorno recursivos.

`opcache.jit_max_polymorphic_calls` [int](language.types.integer.md)
:   Número máximo de tentativas de chamadas polimórficas (dinâmicas ou de método) embutidas.
    As chamadas acima desse limite são tratadas como megamórficas e não são embutidas.

`↑` and `↓` to navigate •
`Enter` to select •
`Esc` to close • `/` to open

document.addEventListener("DOMContentLoaded", function() {
/\*{{{Search Modal\*/
const language = 'local';
initSearchModal();
initPHPSearch(language).then((searchCallback) => {
initSearchUI({language, searchCallback, limit: 30});
});
/\*}}}\*/
});
