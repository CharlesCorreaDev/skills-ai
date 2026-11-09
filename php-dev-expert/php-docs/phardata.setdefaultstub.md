# Função fictícia (Phar::setDefaultStub não é válido para PharData)

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phardata.setdefaultstub.php

---

# PharData::setDefaultStub

(PHP 5 >= 5.3.0, PHP 7, PHP 8, PECL phar >= 2.0.0)

PharData::setDefaultStub — Função fictícia (Phar::setDefaultStub não é válido para PharData)

### Descrição

public function **PharData::setDefaultStub**([?](language.types.null.md)[string](language.types.string.md) `$index` = **`null`**, [?](language.types.null.md)[string](language.types.string.md) `$webIndex` = **`null`**): [bool](language.types.boolean.md)

Arquivos tar/zip não executáveis ​​não podem ter um stub, então esse método simplesmente
gera uma exceção.

### Parâmetros

`index`
:   Caminho relativo dentro do arquivo phar para execução se acessado na linha de comando

`webIndex`
:   Caminho relativo dentro do arquivo phar para ser executado se acessado por meio de um navegador da web

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha.

### Erros/Exceções

Lança [PharException](class.pharexception.md) em todas as chamadas do método

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0 | `webIndex` agora é anulável. |

### Veja também

- [Phar::setDefaultStub()](phar.setdefaultstub.md) - Usado para definir o carregador PHP ou o stub de bootstrap de um arquivo Phar para o carregador padrão

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
