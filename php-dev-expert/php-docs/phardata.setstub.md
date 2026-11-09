# Função fictícia (Phar::setStub não é válido para PharData)

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.setstub.php

---

# PharData::setStub

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::setStub — Função fictícia (Phar::setStub não é válido para PharData)

### Descrição

public function **PharData::setStub**([resource](language.types.resource.md)|[string](language.types.string.md) `$stub`, [int](language.types.integer.md) `$length` = -1): [true](language.types.singleton.md)

Arquivos tar/zip não executáveis ​​não podem ter um stub, então esse método simplesmente
gera uma exceção.

### Parâmetros

`stub`
:   Formalmente, uma string ou um identificador de fluxo aberto para usar como stub executável para este
    arquivo phar. Este parâmetro é ignorado.

`length`
:   `stub` em bytes. Este parâmetro é ignorado.

### Valor Retornado

Sempre retorna **`true`**.

### Erros/Exceções

Lança [PharException](class.pharexception.md) em todas as chamadas do método

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.4.0 | O tipo do retorno agora é **`true`**; anteriormente, era [bool](language.types.boolean.md). |

### Veja também

- [Phar::setStub()](phar.setstub.md) - Usado para definir o carregador PHP ou o stub de inicialização de um arquivo Phar

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
