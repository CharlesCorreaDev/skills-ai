# Cria uma instância PDO representando uma conexão a um banco de dados

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.construct.php

---

# PDO::\_\_construct

(PHP 5 >= 5.1.0, PHP 7, PHP 8, PECL pdo >= 0.1.0)

PDO::\_\_construct — 
Cria uma instância PDO representando uma conexão a um banco de dados

### Descrição

public function **PDO::\_\_construct**(  
    [string](language.types.string.md) `$dsn`,  
    [?](language.types.null.md)[string](language.types.string.md) `$username` = **`null`**,  
    #[[\SensitiveParameter](class.sensitiveparameter.md)] [?](language.types.null.md)[string](language.types.string.md) `$password` = **`null`**,  
    [?](language.types.null.md)[array](language.types.array.md) `$options` = **`null`**  
)

Cria uma instância PDO para representar uma conexão ao banco de dados
requisitado.

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

### Erros/Exceções

Uma [PDOException](class.pdoexception.md) é lançada se a tentativa
de conexão ao banco de dados requisitado falhar,
independente de qual **`PDO::ATTR_ERRMODE`** estiver definido.

### Examples

**Exemplo #1 Cria uma instância PDO através de invocação de driver**

```
<?php

$dsn = 'mysql:dbname=testdb;host=127.0.0.1';
$user = 'dbuser';
$password = 'dbpass';

$dbh = new PDO($dsn, $user, $password);

?>
```

**Exemplo #2 Cria uma instância PDO através de invocação de URI**

O exemplo a seguir assume que o arquivo
/usr/local/dbconnect existe com permissões
de leitura pelo PHP. O arquivo contém o DSN PDO para
conexão a um banco de dados DB2 através do driver PDO\_ODBC:

```
odbc:DSN=SAMPLE;UID=john;PWD=mypass
```

O script PHP pode então criar uma conexão ao banco de dados simplesmente
passando o parâmetro `uri:` e apontando para
a URI do arquivo:

```
<?php

$dsn = 'uri:file:///usr/local/dbconnect';
$user = '';
$password = '';

$dbh = new PDO($dsn, $user, $password);

?>
```

**Exemplo #3 Cria uma instância PDO usando um apelido**

O exemplo a seguir assume que o php.ini contém a seguinte
entrada para habilitar uma conexão ao banco de dados MySQL usando somente o
apelido `mydb`:

```
[PDO]
pdo.dsn.mydb="mysql:dbname=testdb;host=localhost"
```

```
<?php

$dsn = 'mydb';
$user = '';
$password = '';

$dbh = new PDO($dsn, $user, $password);

?>
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
