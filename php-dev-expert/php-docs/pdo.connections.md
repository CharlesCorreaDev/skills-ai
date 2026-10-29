# Conexões e gerenciamento de conexões

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.connections.php

---

# Conexões e gerenciamento de conexões

As conexões são estabelecidas criando instâncias da classe base PDO.
Não importa qual driver você deseja usar; você sempre usa o nome da
classe PDO. O construtor aceita parâmetros para especificar a
fonte do banco de dados (conhecida como DSN) e opcionalmente para o nome de usuário e
senha (se houver).

**Exemplo #1 Conectando-se ao MySQL**

```
<?php
$dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass);
?>
```

Se houver algum erro de conexão, um objeto `PDOException`
será lançado. Você pode capturar a exceção se quiser lidar com a
condição de erro, ou pode optar por deixá-la para um manipulador de exceção
global do aplicativo que você configurou via
[set\_exception\_handler()](function.set-exception-handler.md).

**Exemplo #2 Tratando erros de conexão**

```
<?php
try {
    $dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass);
} catch (PDOException $e) {
    // tentar reconectar após algum intervalo, por exemplo
}
```

**Aviso**

Assim como qualquer outra [exceção](language.error-handling.throwable.md#language.exceptions),
[PDOException](class.pdoexception.md) pode ser capturada explicitamente, via
uma instrução `catch`, ou implicitamente através de [set\_exception\_handler()](function.set-exception-handler.md).
Caso contrário, o comportamento padrão de converter uma exceção não capturada em um
**`E_FATAL_ERROR`** ocorrerá.
O erro fatal conterá uma rastreabilidade que pode vazar detalhes da conexão.
Portanto, a opção php.ini
[`display_errors`](errorfunc.configuration.md#ini.display-errors)
deve ser definida como `0` em um servidor de produção.

Após a conexão bem-sucedida com o banco de dados, uma instância da classe PDO
é retornada para seu script. A conexão permanece ativa pelo
tempo de vida desse objeto PDO. Para fechar a conexão, você precisa
destruir o objeto garantindo que todas as referências restantes a ele sejam
deletadas - você faz isso atribuindo **`null`** à variável que mantém o
objeto. Se você não fizer isso explicitamente, o PHP fechará automaticamente
a conexão quando seu script terminar.

> **Nota**:
>
> Se ainda houver outras referências a esta instância PDO (como de uma
> instância PDOStatement, ou de outras variáveis referenciando a mesma
> instância PDO), estas também devem ser removidas (por exemplo, atribuindo **`null`** à
> variável que referencia a instância PDOStatement).

**Exemplo #3 Fechando uma conexão**

```
<?php
$dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass);
// use a conexão aqui
$sth = $dbh->query('SELECT * FROM foo');

// e agora terminamos; feche-a
$sth = null;
$dbh = null;
?>
```

Muitas aplicações web se beneficiarão com a realização de conexões persistentes
com servidores de banco de dados. As conexões persistentes não são fechadas no final do
script, mas são armazenadas em cache e reutilizadas quando outro script solicita uma conexão
usando as mesmas credenciais. O cache de conexão persistente permite evitar a sobrecarga
de estabelecer uma nova conexão toda vez que um script precisa se comunicar com um banco de dados,
resultando em uma aplicação web mais
rápida.

**Exemplo #4 Conexões persistentes**

```
<?php
$dbh = new PDO('mysql:host=localhost;dbname=test', $user, $pass, array(
    PDO::ATTR_PERSISTENT => true
));
?>
```

O valor da opção **`PDO::ATTR_PERSISTENT`** é convertido para
[bool](language.types.boolean.md) (ativar/desativar conexões persistentes), a menos que seja uma
[string](language.types.string.md) não numérica, caso em que permite o uso de vários pools de conexões persistentes.
Isso é útil se diferentes conexões usam configurações incompatíveis, por exemplo,
valores diferentes de **`PDO::MYSQL_ATTR_USE_BUFFERED_QUERY`**.

> **Nota**:
>
> Se desejar usar conexões persistentes, você deve definir
> **`PDO::ATTR_PERSISTENT`** no array de opções do driver
> passadas para o construtor PDO. Se definir este atributo com
> [PDO::setAttribute()](pdo.setattribute.md) após a instanciação do
> objeto, o driver não usará conexões persistentes.

**Aviso**

O PDO não realiza nenhuma limpeza de conexões persistentes. Tabelas temporárias, bloqueios, transações e outras alterações de estado
podem permanecer do uso anterior da conexão, causando problemas inesperados. Consulte a seção
[Conexões de Banco de Dados Persistentes](features.persistent-connections.md) para obter mais informações.

> **Nota**:
>
> Se estiver usando o driver PDO ODBC e suas bibliotecas ODBC suportarem
> Pool de Conexões ODBC (unixODBC e Windows são duas que suportam; pode haver
> mais), então é recomendável que você não use conexões PDO
> persistentes e, em vez disso, deixe o cache de conexão para a camada de
> Pool de Conexões ODBC. O Pool de Conexões ODBC é compartilhado com outros
> módulos no processo; se o PDO for instruído a armazenar em cache a conexão,
> então essa conexão nunca seria retornada ao pool de conexões ODBC,
> resultando em conexões adicionais sendo criadas para atender a esses outros
> módulos.

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
