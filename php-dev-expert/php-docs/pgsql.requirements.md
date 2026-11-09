# Dependências

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pgsql.requirements.php

---

## Dependências

Para usar usar as funções para PostgreSQL, é necessária a libpq (a biblioteca cliente C
do PostgreSQL).
A partir do PHP 8.0.0, libpq 9.1 ou posterior é requerida.
A partir do PHP 8.4.0, libpq 10.0 ou posterior é requerida.
PostgreSQL suporta vários tipos de codificação de caracteres incluindo
a codificação multibyte. Informação sobre a versão atual mais
detalhes sobre PostgreSQL estão disponíveis em
[» https://www.postgresql.org/](https://www.postgresql.org/) e na
[» Documentação do PostgreSQL](https://www.postgresql.org/docs/current/interactive/).

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
