# Instalação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.installation.php

---

## Instalação

Esta extensão está habilitada por padrão. Ela pode ser desabilitada usando a seguinte opção em tempo de compilação:
**--disable-pdo**

**Instalando o PDO em sistemas Unix**

1. O PDO e o driver [PDO\_SQLITE](ref.pdo-sqlite.md)
   estão habilitados por padrão.
   Pode ser preciso habilitar o driver PDO do banco de dados escolhido;
   consulte a documentação dos
   [drivers PDO de bancos de dados](pdo.drivers.md)
   para saber mais sobre isso.

   > **Nota**:
   >
   > Ao compilar o PDO como uma extensão compartilhada (*não
   > recomendado*), todos os drivers PDO *devem*
   > ser carregados *após* o próprio PDO.
2. Ao instalar o PDO como um módulo compartilhado, o arquivo php.ini precisa
   ser atualizado para que a extensão PDO seja carregada automaticamente quando o PHP for executado.
   Qualquer driver de banco de dados usado também precisará ser habilitado;
   certifique-se de que eles estejam listados após a linha extension=pdo, pois o PDO deve
   ser inicializado antes que as extensões específicas do banco de dados possam ser carregadas.
   Se o PDO e as extensões de banco de dados foram compilados estaticamente,
   esta etapa pode ser ignorada.

   ```
   extension=pdo
   ```

**Pessoas usuárias do Windows**

1. PDO é habilitado por padrão.
   Selecione os outros arquivos DLL e use a função
   [dl()](function.dl.md) para carregá-los em tempo de execução ou habilite-os no arquivo
   php.ini. Por exemplo, isto carrega o driver
   [PDO\_SQLITE](ref.pdo-sqlite.md) mas
   deixa o driver [PDO\_ODBC](ref.pdo-odbc.md) comentado:

   ```
   ;extension=pdo_odbc
   extension=pdo_sqlite
   ```

   Essas DLLs devem existir no diretório de extensões
   [extension\_dir](ini.core.md#ini.extension-dir) do sistema.

> **Nota**:
>
> Lembre-se que após fazer alterações no arquivo php.ini, será necessário
> reiniciar o PHP para que as novas diretivas de configuração entrem em vigor.

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
