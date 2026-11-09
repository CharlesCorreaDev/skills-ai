# Basic usage

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pgsql.examples-queries.php

---

## Basic usage

Estes exemplos contêm funções definidas pelo usuário similares às funções legadas
do MySQL.

**Exemplo #1 Exemplo de funções definidas pelo usuário no PostgreSQL**

```
<?php
// Este função deve ser necessária, já que o a conexão PostgreSQL vincula o banco de dados.
function pg_list_dbs($db)
{
    assert(is_resource($db));
    $query = '
SELECT
 d.datname as "Name",
 u.usename as "Owner",
 pg_encoding_to_char(d.encoding) as "Encoding"
FROM
 pg_database d LEFT JOIN pg_user u ON d.datdba = u.usesysid
ORDER BY 1;
';
    return pg_query($db, $query);
}

// Lista tabelas.
function pg_list_tables($db)
{
    assert(is_resource($db));
    $query = "
SELECT
 c.relname as \"Name\",
 CASE c.relkind WHEN 'r' THEN 'table' WHEN 'v' THEN 'view' WHEN 'i' THEN 'index' WHEN 'S' THEN 'sequence' WHEN 's' THEN 'special' END as \"Type\",
  u.usename as \"Owner\"
FROM
 pg_class c LEFT JOIN pg_user u ON c.relowner = u.usesysid
WHERE
 c.relkind IN ('r','v','S','')
 AND c.relname !~ '^pg_'
ORDER BY 1;
";
    return pg_query($db, $query);
}

// Veja também pg_meta_data(). Ela retorna definições de campo em um array.
function pg_list_fields($db, $table)
{
    assert(is_resource($db));
    $query = "
SELECT
 a.attname,
 format_type(a.atttypid, a.atttypmod),
 a.attnotnull,
 a.atthasdef,
 a.attnum
FROM
 pg_class c,
 pg_attribute a
WHERE
 c.relname = '".$table."'
 AND a.attnum > 0 AND a.attrelid = c.oid
ORDER BY a.attnum;
";
    return pg_query($db, $query);
}
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
