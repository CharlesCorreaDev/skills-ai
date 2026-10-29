# Obtém as informações do esquema solicitadas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/pdo.cubrid-schema.php

---

# PDO::cubrid\_schema

(PECL PDO\_CUBRID >= 8.3.0.0001)

PDO::cubrid\_schema — Obtém as informações do esquema solicitadas

### Descrição

public function **PDO::cubrid\_schema**([int](language.types.integer.md) `$schema_type`, [string](language.types.string.md) `$table_name` = ?, [string](language.types.string.md) `$col_name` = ?): [array](language.types.array.md)

Esta função é usada para obter as informações do esquema solicitadas do
banco de dados. Deve ser informado o nome da tabela em `table_name`, se
for necessário obter informações sobre determinada tabela e o nome da coluna em `col_name`,
se a intenção for obter informações sobre determinada coluna (pode ser usado apenas com
PDO:: CUBRID\_SCH\_COL\_PRIVILEGE).

O resultado desta função é retornado como um array bidimensional (coluna
(array associativo) \* linha (array numérico)). As tabelas a seguir mostram os tipos
de esquema e a estrutura de colunas do array de resultados a ser retornada com base
no tipo de esquema.

**Composição de Resultado para Cada Tipo**

| Esquema | Número da Coluna | Nome da Coluna | Valor |
| --- | --- | --- | --- |
| PDO::CUBRID\_SCH\_TABLE | 1 | NAME |  |
|  | 2 | TYPE | 0:system table 1:view 2:table |
| PDO::CUBRID\_SCH\_VIEW | 1 | NAME |  |
|  | 2 | TYPE | 1:view |
| PDO::CUBRID\_SCH\_QUERY\_SPEC | 1 | QUERY\_SPEC |  |
| PDO::CUBRID\_SCH\_ATTRIBUTE / PDO::CUBRID\_SCH\_TABLE\_ATTRIBUTE | 1 | ATTR\_NAME |  |
|  | 2 | DOMAIN |  |
|  | 3 | SCALE |  |
|  | 4 | PRECISION |  |
|  | 5 | INDEXED | 1:indexed |
|  | 6 | NOT NULL | 1:not null |
|  | 7 | SHARED | 1:shared |
|  | 8 | UNIQUE | 1:unique |
|  | 9 | DEFAULT |  |
|  | 10 | ATTR\_ORDER | base:1 |
|  | 11 | CLASS\_NAME |  |
|  | 12 | SOURCE\_CLASS |  |
|  | 13 | IS\_KEY | 1:key |
| PDO::CUBRID\_SCH\_METHOD / PDO::CUBRID\_SCH\_TABLE\_METHOD | 1 | NAME |  |
|  | 2 | RET\_DOMAIN |  |
|  | 3 | ARG\_DOMAIN |  |
| PDO::CUBRID\_SCH\_METHOD\_FILE | 1 | METHOD\_FILE |  |
| PDO::CUBRID\_SCH\_SUPER\_TABLE / PDO::CUBRID\_SCH\_DIRECT\_SUPER\_TABLE / PDO::CUBRID\_SCH\_SUB\_TABLE | 1 | CLASS\_NAME |  |
|  | 2 | TYPE | 0:system table 1:view 2:table |
| PDO::CUBRID\_SCH\_CONSTRAINT | 1 | TYPE | 0:unique 1:index 2:reverse unique 3:reverse index |
|  | 2 | NAME |  |
|  | 3 | ATTR\_NAME |  |
|  | 4 | NUM\_PAGES |  |
|  | 5 | NUM\_KEYS |  |
|  | 6 | PRIMARY\_KEY | 1:primary key |
|  | 7 | KEY\_ORDER | base:1 |
| PDO::CUBRID\_SCH\_TRIGGER | 1 | NAME |  |
|  | 2 | STATUS |  |
|  | 3 | EVENT |  |
|  | 4 | TARGET\_CLASS |  |
|  | 5 | TARGET\_ATTR |  |
|  | 6 | ACTION\_TIME |  |
|  | 7 | ACTION |  |
|  | 8 | PRIORITY |  |
|  | 9 | CONDITION\_TIME |  |
|  | 10 | CONDITION |  |
| PDO::CUBRID\_SCH\_TABLE\_PRIVILEGE / PDO::CUBRID\_SCH\_COL\_PRIVILEGE | 1 | CLASS\_NAME / ATTR\_NAME |  |
|  | 2 | PRIVILEGE |  |
|  | 3 | GRANTABLE |  |
| PDO::CUBRID\_SCH\_PRIMARY\_KEY | 1 | CLASS\_NAME |  |
|  | 2 | ATTR\_NAME |  |
|  | 3 | KEY\_SEQ | base:1 |
|  | 4 | KEY\_NAME |  |
| PDO::CUBRID\_SCH\_IMPORTED\_KEYS / PDO::CUBRID\_SCH\_EXPORTED\_KEYS / PDO::CUBRID\_SCH\_CROSS\_REFERENCE | 1 | PKTABLE\_NAME |  |
|  | 2 | PKCOLUMN\_NAME |  |
|  | 3 | FKTABLE\_NAME | base:1 |
|  | 4 | FKCOLUMN\_NAME |  |
|  | 5 | KEY\_SEQ | base:1 |
|  | 6 | UPDATE\_ACTION | 0:cascade 1:restrict 2:no action 3:set null |
|  | 7 | DELETE\_ACTION | 0:cascade 1:restrict 2:no action 3:set null |
|  | 8 | FK\_NAME |  |
|  | 9 | PK\_NAME |  |

### Parâmetros

`schema_type`
:   Tipo de esquema a ser conhecido.

`table_name`
:   Tabela cujo esquema deseja-se conhecer.

`col_name`
:   Coluna cujo esquema deseja-se conhecer.

### Valor Retornado

Array contendo informações do esquema, em caso de sucesso;

FALSE, em caso de falha.

### Examples

**Exemplo #1 Um exemplo de **PDO::cubrid\_schema()****

Este exemplo mostra como obter a chave primária e as chaves estrangeiras da tabela 'game'.

```
<?php
$pk_list = $dbh->cubrid_schema(PDO::CUBRID_SCH_PRIMARY_KEY, "game");
print_r($pk_list);

$fk_list = $dbh->cubrid_schema(PDO::CUBRID_SCH_IMPORTED_KEYS, "game");
print_r($fk_list);
?>
```

O exemplo acima produzirá:

```
Resultado:
Array
(
    [0] => Array
        (
            [CLASS_NAME] => game
            [ATTR_NAME] => athlete_code
            [KEY_SEQ] => 3
            [KEY_NAME] => pk_game_host_year_event_code_athlete_code
        )

    [1] => Array
        (
            [CLASS_NAME] => game
            [ATTR_NAME] => event_code
            [KEY_SEQ] => 2
            [KEY_NAME] => pk_game_host_year_event_code_athlete_code
        )

    [2] => Array
        (
            [CLASS_NAME] => game
            [ATTR_NAME] => host_year
            [KEY_SEQ] => 1
            [KEY_NAME] => pk_game_host_year_event_code_athlete_code
        )

)
Array
(
    [0] => Array
        (
            [PKTABLE_NAME] => athlete
            [PKCOLUMN_NAME] => code
            [FKTABLE_NAME] => game
            [FKCOLUMN_NAME] => athlete_code
            [KEY_SEQ] => 1
            [UPDATE_RULE] => 1
            [DELETE_RULE] => 1
            [FK_NAME] => fk_game_athlete_code
            [PK_NAME] => pk_athlete_code
        )

    [1] => Array
        (
            [PKTABLE_NAME] => event
            [PKCOLUMN_NAME] => code
            [FKTABLE_NAME] => game
            [FKCOLUMN_NAME] => event_code
            [KEY_SEQ] => 1
            [UPDATE_RULE] => 1
            [DELETE_RULE] => 1
            [FK_NAME] => fk_game_event_code
            [PK_NAME] => pk_event_code
        )

)
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
