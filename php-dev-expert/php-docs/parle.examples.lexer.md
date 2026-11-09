# Exemplos de Lexer

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle.examples.lexer.php

---

## Exemplos de Lexer

**Exemplo #1 Tokenização de lista de inteiros separados por vírgula**

```
<?php

use Parle\Token;
use Parle\Lexer;
use Parle\LexerException;

/* name => id */
$token = array(
    "COMMA" => 1,
    "CRLF" => 2,
    "DECIMAL" => 3,
);
/* id => name */
$tokenIdToName = array_flip($token);

$lex = new Lexer;
$lex->push("[\x2c]", $token["COMMA"]);
$lex->push("[\r][\n]", $token["CRLF"]);
$lex->push("[\d]+", $token["DECIMAL"]);
$lex->build();

$in = "0,1,2\r\n3,42,5\r\n6,77,8\r\n";

$lex->consume($in);

do {
    $lex->advance();
    $tok = $lex->getToken();

    if (Token::UNKNOWN == $tok->id) {
        throw new LexerException("Token desconhecido '{$tok->value}' na posição {$lex->marker}.");
    }

    echo "TOKEN: ", $tokenIdToName[$tok->id], PHP_EOL;
} while (Token::EOI != $tok->id);
```

**Exemplo #2 Tokenização da instrução de atribuição**

```
<?php

use Parle\{Token, Lexer};

$lex = new Lexer;

$lex->push("\$[a-zA-Z_][a-zA-Z0-9_]*", 1);
$lex->push("=", 2);
$lex->push("\d+", 3);
$lex->push(";", 4);

$lex->build();

$lex->consume('$x = 42; $y = 24;');

do {
    $lex->advance();
    $tok = $lex->getToken();
    var_dump($tok);
} while (Token::EOI != $tok->id);
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
