# Configurações de Execução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.configuration.php

---

## Configurações de Execução

O comportamento destas funções é afetado pelas configurações do php.ini.

**Opções de configuração de sistema de arquivos e fluxos**

| Nome | Padrão | Modificável | Registro de Alterações |
| --- | --- | --- | --- |
| [phar.readonly](phar.configuration.md#ini.phar.readonly) | "1" | **`INI_ALL`** |  |
| [phar.require\_hash](phar.configuration.md#ini.phar.require-hash) | "1" | **`INI_ALL`** |  |
| [phar.cache\_list](phar.configuration.md#ini.phar.cache-list) | "" | **`INI_SYSTEM`** |  |

Aqui está uma breve explicação das
diretivas de configuração.

`phar.readonly` [bool](language.types.boolean.md)
:   Esta opção desabilita a criação ou modificação de arquivos Phar
    usando o fluxo `phar` ou o suporte de gravação do objeto [Phar](class.phar.md).
    Esta configuração deve estar sempre habilitada em
    máquinas de produção, pois o suporte conveniente de gravação da extensão phar
    pode permitir a criação direta de um vírus baseado em PHP quando combinado
    com outras vulnerabilidades de segurança comuns.

    > **Nota**:
    >
    > Esta configuração só pode ser desativada no arquivo php.ini por motivos de segurança.
    > Se `phar.readonly` estiver desabilitado no arquivo php.ini, o
    > usuário poderá habilitar `phar.readonly` em um script
    > ou desabilitá-lo posteriormente. Se `phar.readonly` estiver
    > habilitado no arquivo php.ini, um script poderá "reabilitar"
    > a variável INI sem causar danos, mas não poderá desabilitá-la.

`phar.require_hash` [bool](language.types.boolean.md)
:   Esta opção forçará todos os arquivos Phar abertos a conter algum
    tipo de assinatura (atualmente MD5, SHA1, SHA256, SHA512 e OpenSSL são suportados) e
    se recusará a processar qualquer arquivo Phar que não contenha uma assinatura.

    > **Nota**:
    >
    > Esta configuração só pode ser desativada em php.ini.
    > Se `phar.require_hash` estiver desabilitado em php.ini, o
    > usuário poderá habilitar `phar.require_hash` em um script
    > ou desabilitá-lo posteriormente. Se `phar.require_hash` estiver
    > habilitado em php.ini, um script poderá "reabilitar"
    > a variável INI sem causar danos, mas não poderá desabilitá-la.
    >
    > Esta configuração não afeta a leitura de arquivos tar simples com a classe
    > [PharData](class.phardata.md).

    **Cuidado**

    `phar.require_hash` não fornece nenhuma segurança por si só,
    é apenas uma medida contra a execução acidental de arquivos Phar corrompidos,
    porque qualquer um que conseguisse adulterar o Phar poderia facilmente consertar
    a assinatura posteriormente.

`phar.cache_list` [string](language.types.string.md)
:   Permite que o mapeamento de arquivos phar seja pré-analisado na inicialização do servidor web,
    proporcionando uma melhoria de desempenho que aproxima a execução de arquivos de um
    arquivo phar da velocidade de execução desses arquivos de uma
    instalação tradicional baseada em disco.

    **Exemplo #1 Exemplo de uso de phar.cache\_list**

    ```
    no php.ini (windows):
    phar.cache_list =C:\caminho\para\phar1.phar;C:\caminho\para\phar2.phar
    no php.ini (unix):
    phar.cache_list =/caminho/para/phar1.phar:/caminho/para/phar2.phar
    ```

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
