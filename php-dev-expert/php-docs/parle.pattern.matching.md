# Correspondência de padrões do Parle

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parle.pattern.matching.php

---

# Correspondência de padrões do Parle

O Parle suporta correspondência a expressões regulares semelhantes ao Flex.
Também são suportados os seguintes conjuntos de caracteres POSIX:
`[:alnum:]`, `[:alpha:]`, `[:blank:]`, `[:cntrl:]`, `[:digit:]`, `[:graph:]`, `[:lower:]`, `[:print:]`, `[:punct:]`, `[:space:]`, `[:upper:]`, `[:xdigit:]`.

As classes de caracteres Unicode não estão habilitadas por padrão. Use --enable-parle-utf32 para torná-las disponíveis.
Uma codificação específica pode ser mapeada com uma expressão regular construída corretamente.
Por exemplo, para corresponder ao símbolo EURO codificado em UTF-8, a expressão regular `[\xe2][\x82][\xac]` pode ser usada.
O padrão para uma string codificada em UTF-8 poderia ser `[ -\x7f]{+}[\x80-\xbf]{+}[\xc2-\xdf]{+}[\xe0-\xef]{+}[\xf0-\xff]+`.

## Representações de caracteres

**Representações de caracteres**

| Sequência | Descrição |
| --- | --- |
| \a | Alerta sonoro. |
| \b | Backspace. |
| \e | ESC, \x1b. |
| \n | Nova linha. |
| \r | Retorno de carro. |
| \f | Alimentação de formulário, \x0c. |
| \t | Tabulação horizontal, \x09. |
| \v | Tabulação vertical, \x0b. |
| \oct | Caractere especificado por um código octal de três dígitos. |
| \xhex | Caractere especificado por um código hexadecimal. |
| \cchar | Caractere de controle nomeado. |

## Classes de caracteres

**Classes de caracteres**

| Sequência | Descrição |
| --- | --- |
| [...] | Um único caractere listado ou contido em um intervalo listado. Intervalos podem ser combinados com os operadores `{+}` e `{-}`. Por exemplo, `[a-z]{+}[0-9]` é o mesmo que `[0-9a-z]` e `[a-z]{-}[aeiou]` é o mesmo que `[b-df-hj-np-tv-z]`. |
| [^...] | Um único caractere não listado e não contido em um intervalo listado. |
| . | Qualquer caractere, padrão `[^\n].` |
| \d | Caractere de dígito, `[0-9]`. |
| \D | Caractere não-dígito, `[^0-9]`. |
| \s | Caractere de espaço em branco, `[ \t\n\r\f\v]`. |
| \S | Caractere sem espaço em branco, `[^ \t\n\r\f\v]`. |
| \w | Caractere de palavra, `[a-zA-Z0-9_]`. |
| \W | Caractere que não é de palavra, `[^a-zA-Z0-9_]`. |

## Classes de caractere Unicode

**Classes de caractere Unicode**

| Sequência | Descrição |
| --- | --- |
| \p{C} | Outro. |
| \p{Cc} | Outro, controle. |
| \p{Cf} | Outro, formato. |
| \p{Co} | Outro, uso privado. |
| \p{Cs} | Outro, substituto. |
| \p{L} | Letra. |
| \p{LC} | Letra, capitalizada. |
| \p{Ll} | Letra, minúscula. |
| \p{Lm} | Letra, modificador. |
| \p{Lo} | Letra, outro. |
| \p{Lt} | Letra, de título. |
| \p{Lu} | Letra, maiúscula. |
| \p{M} | Marca. |
| \p{Mc} | Marca, combinação de espaço. |
| \p{Me} | Marca, delimitador. |
| \p{Mn} | Marca, sem espaçamento. |
| \p{N} | Número. |
| \p{Nd} | Número, dígito decimal. |
| \p{Nl} | Número, letra. |
| \p{No} | Número, outro. |
| \p{P} | Pontuação. |
| \p{Pc} | Pontuação, conector. |
| \p{Pd} | Pontuação, traço. |
| \p{Pe} | Pontuação, fechamento. |
| \p{Pf} | Pontuação, aspas de fechamento. |
| \p{Pi} | Pontuação, aspas de abertura. |
| \p{Po} | Pontuação, outro. |
| \p{Ps} | Pontuação, abertura. |
| \p{S} | Símbolo. |
| \p{Sc} | Símbolo, moeda. |
| \p{Sk} | Símbolo, modificador. |
| \p{Sm} | Símbolo, matemático. |
| \p{So} | Símbolo, outro. |
| \p{Z} | Separador. |
| \p{Zl} | Separador, linha. |
| \p{Zp} | Separador, parágrafo. |
| \p{Zs} | Separador, espaço. |

Essas classes de caracteres só estarão disponíveis se a opção --enable-parle-utf32 tiver sido passada no momento da compilação.

## Alternância e repetição

**Alternância e repetição**

| Sequência | Guloso | Descrição |
| --- | --- | --- |
| ...|... | - | Tenta subpadrões alternadamente. |
| \* | sim | Corresponde 0 ou mais vezes. |
| + | sim | Corresponde 1 ou mais vezes. |
| ? | sim | Corresponde 0 ou 1 vez. |
| {n} | no | Corresponde exatamente n vezes. |
| {n,} | sim | Corresponde pelo menos n vezes. |
| {n,m} | sim | Corresponde pelo menos n vezes mas não mais que m vezes. |
| \*? | não | Corresponde 1 ou mais vezes. |
| +? | não | Corresponde 1 ou mais vezes. |
| ?? | não | Corresponde 0 ou 1 vez. |
| {n,}? | não | Corresponde pelo menos n vezes. |
| {n,m}? | não | Corresponde pelo menos n vezes mas não mais que m vezes. |
| {MACRO} | - | Inclui a MACRO de expressão regular na expressão atual. |

## Âncoras

**Anchors**

| Sequência | Descrição |
| --- | --- |
| ^ | Início da string ou após uma nova linha. |
| $ | Fim da string ou antes de uma nova linha. |

## Agrupamento

**Agrupamento**

| Sequência | Descrição |
| --- | --- |
| (...) | Agrupa uma expressão regular para substituir a precedência do operador padrão. |
| (?r-s:pattern) | Aplica a opção r e omite a opção s ao interpretar o padrão. As opções podem ser zero ou mais dos caracteres i, s ou x.  `i` significa sem diferenciação de maiúsculas/minúsculas.  `-i` significa com diferenciação de maiúsculas/minúsculas.  `s` altera o significado de `.` para corresponder a qualquer caractere.  `-s` altera o significado de `.` para corresponder a qualquer caractere exceto `\n`.  `x` ignora comentários e espaços em branco em expressões. Espaços em branco são ignorados, a menos que sejam precedidos por barra invertida, estejam contidos entre `""s`, ou apareçam dentro de um intervalo de caracteres.  Essas opções podem ser aplicadas globalmente no nível de regras passando uma combinação de sinalizadores de bits para o analisador léxico. |
| (?# comment ) | Omite tudo dentro de (). O primeiro caractere ) encontrado encerra o padrão. Não é possível que o comentário contenha um caractere ). O comentário pode abranger várias linhas. |

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
