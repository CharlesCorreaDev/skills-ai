# Recebe notificação assíncrona

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo-pgsql.getnotify.php

---

# Pdo\Pgsql::getNotify

(PHP 8 >= 8.4.0)

Pdo\Pgsql::getNotify — Recebe notificação assíncrona

### Descrição

public function **Pdo\Pgsql::getNotify**([int](language.types.integer.md) `$fetchMode` = **`PDO::FETCH_DEFAULT`**, [int](language.types.integer.md) `$timeoutMilliseconds` = 0): [array](language.types.array.md)|[false](language.types.singleton.md)

Retorna um conjunto de resultados que representa uma notificação assíncrona pendente.

### Parâmetros

`fetchMode`
:   O formato como o conjunto de resultados deve ser retornado,
    uma das seguintes constantes:

    - **`PDO::FETCH_DEFAULT`**
    - **`PDO::FETCH_BOTH`**
    - **`PDO::FETCH_ASSOC`**
    - **`PDO::FETCH_NUM`**

`timeoutMilliseconds`
:   O tempo de espera por uma resposta, em milissegundos.

### Valor Retornado

Se uma notificação estiver pendente, retorna uma única linha, caso contrário
retorna **`false`**. Alinha tem um campo `message` (o nome do canal)
e um campo `pid` (o ID do processo do backend que envia a notificação).
Se a notificação traz uma carga não vazia, a linha também tem um
campo `payload`. Com **`PDO::FETCH_NUM`**,
estes campos estão nos índices `0`, `1` e
`2`.

### Erros/Exceções

Uma exceção [ValueError](class.valueerror.md) será lançada se
`fetchMode` não for uma das constantes
**`PDO::FETCH_*`**
válidas.

Uma exceção [ValueError](class.valueerror.md) será lançada se
`timeoutMilliseconds` for menor que `0`.

Um **`E_WARNING`** é gerado quando
`timeoutMilliseconds` é maior que o valor
que pode estar contido em um inteiro com sinal de 32 bits; nesse caso, será o
valor máximo de um inteiro com sinal de 32 bits.

### Examples

**Exemplo #1 Exemplo de **Pdo\Pgsql::getNotify()****

Inscreva em um canal com `LISTEN` e então leia a próxima
notificação pendente com um tempo limite de um segundo.

```
<?php
$db = new Pdo\Pgsql('pgsql:dbname=test host=localhost', $user, $pass);
$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

$db->exec('LISTEN messages');
$db->exec("NOTIFY messages, 'hello'");

$notification = $db->getNotify(PDO::FETCH_ASSOC, 1000);
var_export($notification);
?>
```

O exemplo acima produzirá
algo semelhante a:

```
array (
  'message' => 'messages',
  'pid' => 1928,
  'payload' => 'hello',
)
```

### Veja também

- [PDO::query()](pdo.query.md) - Prepara e executa uma instrução SQL sem marcadores
- [PDOStatement::fetch()](pdostatement.fetch.md) - Busca a próxima linha de um resultado
- [PDOStatement::fetchAll()](pdostatement.fetchall.md) - Busca as linhas remanescentes de um conjunto de resultados

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
