# Conecta a um banco de dados e retorna uma subclasse PDO para drivers que o suportam

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.connect.php

---

# PDO::connect

(PHP 8 >= 8.4.0)

PDO::connect — Conecta a um banco de dados e retorna uma subclasse PDO para drivers que o suportam

### Descrição

public static function **PDO::connect**(  
    [string](language.types.string.md) `$dsn`,  
    [?](language.types.null.md)[string](language.types.string.md) `$username` = **`null`**,  
    #[[\SensitiveParameter](class.sensitiveparameter.md)] [?](language.types.null.md)[string](language.types.string.md) `$password` = **`null`**,  
    [?](language.types.null.md)[array](language.types.array.md) `$options` = **`null`**  
): static

Cria uma instância de uma subclasse [PDO](class.pdo.md) para o
banco de dados sendo conectado, se existir,
caso contrário retorna uma instância genérica de [PDO](class.pdo.md).

### Parâmetros

`dsn`
:   O nome da fonte de dados, ou DSN, que contém a informação requerida para
    conexão ao banco de dados.

    Em geral, um DSN consiste no nome do driver PDO, seguido por dois-pontos,
    seguido pela sintaxe de conexão específica do driver PDO. Maiores
    informações estão disponíveis na [documentação
    específica do driver PDO](pdo.drivers.md).

    O parâmetro `dsn` suporta três
    métodos diferentes para especificar os argumentos requeridos para criação
    de uma conexão de banco de dados:

    Invocação do driver
    :   `dsn` contém o DSN completo.

    Invocação de URI
    :   `dsn` consiste em **`uri:`**
        seguido por uma URI que define a localização de um arquivo contendo
        a string DSN. A URI pode especificar um arquivo local ou uma URL remota.

        **`uri:file:///caminho/para/arquivodsn`**

    Criação de apelido
    :   `dsn` consiste em um nome
        (`name`) que é mapeado para
        `pdo.dsn.name` no php.ini
        definindo a string DSN.

        > **Nota**:
        >
        > O apelido deve ser definido no php.ini, e não no .htaccess ou no httpd.conf

`username`
:   O nome de usuário para a string DSN. Este parâmetro é opcional para
    alguns drivers PDO.

`password`
:   A senha para a srting DSN. Este parâmetro é opcional para
    alguns drivers PDO.

`options`
:   Um array de chave=>valor de opções de conexão específicas do driver.

### Valor Retornado

Retorna uma instância de uma subclasse [PDO](class.pdo.md) para o
driver PDO correspondente se existir,
ou uma instância genérica de [PDO](class.pdo.md).

### Erros/Exceções

Uma [PDOException](class.pdoexception.md) é lançada se a tentativa
de conexão ao banco de dados requisitado falhar,
independente de qual **`PDO::ATTR_ERRMODE`** estiver definido.

### Veja também

- [Pdo\Dblib](class.pdo-dblib.md)
- [Pdo\Firebird](class.pdo-firebird.md)
- [Pdo\Mysql](class.pdo-mysql.md)
- [Pdo\Odbc](class.pdo-odbc.md)
- [Pdo\Pgsql](class.pdo-pgsql.md)
- [Pdo\Sqlite](class.pdo-sqlite.md)
- [PDO::\_\_construct()](pdo.construct.md) - Cria uma instância PDO representando uma conexão a um banco de dados

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
