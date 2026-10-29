# Testando

> **Fonte / Source:** https://www.php.net/manual/pt_BR/oci8.test.php

---

## Testando

A suíte de testes do OCI8 está em ext/oci8/tests.
Depois que os testes do OCI8 forem executados, este diretório também conterá registros de
falhas.

Antes de executar testes do PHP, edite o arquivo details.inc
e defina $user, $password e a string de conexão $dbase. A
suíte de testes do OCI8 foi desenvolvida usando a
conta `SYSTEM`. Alguns testes falharão se
o usuário de teste não tiver as permissões equivalentes.

Se o Oracle Database Resident Connection Pooling estiver sendo
testado, defina $test\_drcp para **`true`** e garanta que a
string de conexão use um servidor DRCP apropriado.

Uma alternativa para a edição de details.inc é
definir variáveis de ambiente, por exemplo:

```
    $ export PHP_OCI8_TEST_USER=system
    $ export PHP_OCI8_TEST_PASS=oracle
    $ export PHP_OCI8_TEST_DB=localhost/XE
    $ export PHP_OCI8_TEST_DRCP=FALSE
```

Observe que em alguns shells essas variáveis ​​não são propagadas corretamente
para o processo PHP e os testes falharão na conexão se este método
for usado.

A seguir, defina qualquer ambiente necessário para o banco de dados Oracle. Se o PHP
estiver sendo executado nas mesmas máquinas do Oracle Database, pode-se executar:

```
    $ . /usr/local/bin/oraenv
```

Com o Oracle 11*g*R2 XE, execute:

```
    $ . /u01/app/oracle/product/11.2.0/xe/bin/oracle_env.sh
```

Alguns shells exigem que php.ini tenham `E` no parâmetro
variables\_order, por exemplo:

```
    variables_order = "EGPCS"
```

Execute todos os testes PHP com:

```
    $ cd your_php_src_directory
    $ make test
```

ou execute somente os testes OCI8 com

```
    $ cd your_php_src_directory
    $ make test TESTS=ext/oci8
```

Quando os testes forem concluídos, revise quaisquer falhas de teste. Em sistemas
lentos, alguns testes podem demorar mais que o tempo
limite padrão em run-tests.php. Para corrigir isso,
defina a variável de ambiente `TEST_TIMEOUT` para
um número maior de segundos.

Em máquinas rápidas com um banco de dados local configurado para carga leve
(por exemplo, Oracle 11*g*R2 XE) alguns testes podem falhar com erros ORA-12516
ou ORA-12520. Para evitar isso, aumente o parâmetro
`PROCESSES` do banco de dados usando as seguintes etapas:

Conecte-se como o proprietário do software Oracle:

```
    $ su - oracle
```

Defina o ambiente Oracle necessário com oracle\_env.sh ou
oraenv, como descrito acima.

Inicie a ferramente de linha de comando SQL\*Plus e
aumente `PROCESSES`

```
    $ sqlplus / as sysdba
    SQL> alter system set processes=100 scope=spfile
```

Reinicie o banco de dados:

```
    SQL> startup force
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
