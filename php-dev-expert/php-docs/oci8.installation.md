# Instalação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/oci8.installation.php

---

## Instalação

## Configurando o PHP com o OCI8

Consulte a seção anterior
sobre [requisitos](oci8.requirements.md)
antes de configurar o OCI8.

Antes de inicializar o servidor web, o OCI8 tipicamente requer várias
variáveis de ambiente Oracle (veja abaixo) para localizar bibliotecas, apontar
para arquivos de configuração e definir algumas propriedades básicas como o
conjunto de caracteres utilizado pelas bibliotecas Oracle. As variáveis devem ser definidas
*antes* que qualquer processo PHP inicie.

O binário PHP deve ter sido construído com a mesma versão principal, ou mais recente, das
bibliotecas Oracle com as quais foi configurado. Por exemplo, se o OCI8 estiver utilizando
as bibliotecas Oracle versão 19, o PHP também deve ser construído e executado
com as bibliotecas Oracle 19. Aplicações PHP podem se conectar a outras
versões de banco de dados Oracle, já que a Oracle tem compatibilidade cliente-servidor com versões diferentes.

## Instalando OCI8 com PECL Usando o Comando pecl

A extensão OCI8 pode ser adicionada a uma instalação PHP existente usando
o repositório [» PECL](https://pecl.php.net/package/oci8).

- Se estiver por trás de um firewall, defina o proxy PEAR, por exemplo:

  ```
  pear config-set http_proxy http://my-proxy.example.com:80/
  ```
- Execute

  ```
  pecl install oci8
  ```

  Para o PHP 7, use `pecl install oci8-2.2.0`
- Quando solicitado, entre o valor de `$ORACLE_HOME` ou
  `instantclient,/caminho/para/biblioteca/instant/client`.

  Nota: Não use nomes de variáveis como `$ORACLE_HOME`
  ou `$HOME` porque o `pecl` não irá
  interpretá-las. Em vez disso, informa um caminho expandido, por
  exemplo `/opt/oracle/product/19c/dbhome_1`
  ou `instantclient,/Users/myname/Downloads/instantclient_19_8`.
- Se ocorrer um erro do tipo `oci8_dtrace_gen.h: No such file or
  directory`, significa que o PHP foi compilado com
  [Rastreamento Dinâmico DTrace](features.dtrace.md) habilitado.
  Instale usando:

  ```
  $ export PHP_DTRACE=yes
  $ pecl install oci8
  ```
- Edite o arquivo php.ini e adicione a linha:

  ```
  extension=oci8.so
  ```

  Certifique-se que a diretiva
  [extension\_dir](ini.core.md#ini.extension-dir) do php.ini esteja
  definida para o diretório onde o arquivo oci8.so tenha sido
  instalado.

## Instalando OCI8 com PECL Usando phpize

Para instalar o OCI8 em uma instalação PHP existente quando
o comando `pecl` não estiver disponível, baixe manualmente
o pacote OCI8 [» PECL](https://pecl.php.net/package/oci8),
ex.: oci8-3.0.0.tgz.

- Extraia o pacote:

  ```
  tar -zxf oci8-3.0.0.tgz
  cd oci8-3.0.0
  ```
- Prepare o pacote:

  ```
  phpize
  ```
- Configure o pacote,
  usando `$ORACLE_HOME` ou Instant Client

  ```
  ./configure -with-oci8=shared,$ORACLE_HOME
  ```

  ou

  ```
  ./configure -with-oci8=shared,instantclient,/caminho/para/biblioteca/instant/client
  ```
- Instale o pacote:

  ```
  make install
  ```
- Se ocorrer um erro do tipo `oci8_dtrace_gen.h: No such file or
  directory`, significa que o PHP foi compilado
  com [Rastreamento Dinâmico DTrace](features.dtrace.md) habilitado.
  Execute novamente os comandos `configure` e `make`
  depois de definir esta variável de ambiente:

  ```
  $ export PHP_DTRACE=yes
  ```
- Edite o arquivo php.ini e adicione a linha:

  ```
  extension=oci8.so
  ```

  Certifique-se que a diretiva
  [extension\_dir](ini.core.md#ini.extension-dir) do php.ini esteja
  definida para o diretório onde o arquivo oci8.so tenha sido
  instalado.

## Instalando o OCI8 como uma Extensão Compartilhada ao Compilar o PHP

Se o PHP está sendo compilado a partir do código-fonte, a opção
de configuração `shared` pode ser usada para construir o OCI8 como uma biblioteca
compartilhada que pode ser carregada dinamicamente no PHP. Construir uma extensão compartilhada permite que
o OCI8 seja atualizado facilmente sem impactar o restante do PHP.

Configure o OCI8 usando uma das opções de configuração a seguir.

- Se as bibliotecas gratuitas do [» Oracle Instant
  Client](https://www.oracle.com/database/technologies/instant-client.html) estiverem sendo usadas, execute:

  ```
  ./configure --with-oci8=shared,instantclient,/caminho/para/biblioteca/instant/client
  ```

  Se a Instant Client 12.2 (ou anterior) tiver sido instalada a partir de arquivos ZIP, certifique-se de
  criar as ligações simbólicas da biblioteca primeiro, por exemplo `ln -s
  libclntsh.so.12.1 libclntsh.so`.

  Se estiver sendo usada uma instalação baseada em RPM da Oracle Instant Client, a
  linha de configuração será parecida com:

  ```
  ./configure --with-oci8=shared,instantclient,/usr/lib/oracle/<version>/client/lib
  ```

  Por exemplo, **--with-oci8=shared,instantclient,/usr/lib/oracle/19.9/client/lib**
- Se um banco de dados Oracle ou uma instalação completa do Oracle Client estiverem sendo usados, execute:

  ```
  ./configure --with-oci8=shared,$ORACLE_HOME
  ```

  Certifique-se que o usuário sob o qual o servidor web esteja sendo executado
  (`nobody`, `www`) tenha acesso às
  bibliotecas, arquivos de inicialização
  e tnsnames.ora (se usado) no diretório
  `$ORACLE_HOME`. Com o Oracle
  10*g*R2, pode ser necessário executar
  o utilitário $ORACLE\_HOME/install/changePerm.sh
  para conceder acesso ao diretório.

Depois da configuração, siga o procedimento usual de compilação do PHP,
ex.: *make install*. A biblioteca da extensão
compartilhada OCI8 oci8.so será criada. Pode ser necessário
movê-la manualmente para o diretório das extensões PHP, especificado pela
opção [extension\_dir](ini.core.md#ini.extension-dir) no
arquivo php.ini.

Para completar a instalação do OCI8, edite o php.ini e adicione a linha:

```
extension=oci8.so
```

## Instalando o OCI8 como um Extensão Compilada Estaticamente ao Compilar o PHP

Se o PHP estiver sendo compilado a partir do código-fonte, pode-se configurá-lo para incluir
o OCI8 como uma extensão estática usando uma das seguintes opções de configuração.

- Se o Oracle Instant Client estiver sendo utilizado, execute:

  ```
  ./configure --with-oci8=instantclient,/caminho/para/biblioteca/instant/client
  ```
- Se um banco de dados Oracle ou uma instalação completa do Oracle Client estiverem sendo usados, execute:

  ```
  ./configure --with-oci8=$ORACLE_HOME
  ```

Depois da configuração, siga o procedimento usual de compilação do PHP,
ex.: *make install*. Após a compilação
bem sucedida, não é necessário incluir oci8.so ao
php.ini. Nenhum passo adicional de compilação é requerido.

## Instalando o OCI8 no Windows

A extensão OCI8 pode ser adicionada a uma instalação PHP existente usando as
DLLs do repositório [» PECL](https://pecl.php.net/package/oci8) ou
as bibliotecas no diretório `ext` da instalação do PHP.

Com as bibliotecas Oracle 12*c* (ou mais recentes), ative uma das
linhas `extension=php_oci8_12c.dll`,
`extension=php_oci8_11g.dll`
ou `extension=php_oci8.dll` do php.ini. Apenas uma dessas DLLs pode ser
habilitada de cada vez. DLLs com versões maiores podem conter mais
funcionalidades. Pode ser que nem todas as DLLs estejas disponíveis para todas as versões do PHP.
Certifique-se que [extension\_dir](ini.core.md#ini.extension-dir) esteja definido
para o diretório contendo as DLLs de extensões do PHP.

Se o Instant Client estiver sendo utilizado, defina a variável de ambiente do sistema PATH
para o diretório da biblioteca Oracle.

## Configurando o Ambiente Oracle

Antes de usar esta extensão, certifique-se que as variáveis de ambiente
Oracle estajam adequadamente definidas para o usuário sob o qual o servidor web esteja sendo executado.
Se o servidor web estiver sendo automaticamente iniciado quando o sistema é ligado, garanta que
o ambiente em tempo de inicialização também esteja configurado corretamente.

> **Nota**:
>
> Não defina as variáveis de ambiente Oracle
> usando [putenv()](function.putenv.md) em um script PHP porque as bilbiotecas
> Oracle podem estar carregadas e inicializadas antes que o script
> seja executado. Variáveis definidas com [putenv()](function.putenv.md) podem causar
> conflitos, travamentos ou comportamento imprevisível. Algumas funções podem
> funcionar mas outras podem dar erros sutis. As variáveis devem ser
> definidas *antes* que o servidor web seja iniciado.

No Linux Red Hat e variantes, exporte as variáveis no final do arquivo
/etc/sysconfig/httpd. Outros sistemas com
Apache 2 pode usar um script envvars no diretório
bin do Apache. Uma terceira opção, a
diretiva `SetEnv` do Apache
no arquivo httpd.conf, pode funcionar em alguns sistemas mas
é sabido que isto é insuficiente em outros.

Para verificar que as variáveis de ambiente estão definidas corretamente,
use [phpinfo()](function.phpinfo.md) e verifique se
a seção *Environment* (não a *Apache
Environment*) contém as variáveis esperadas.

As variáveis que devem ser necessárias estão incluídas na tabela
a seguir. Consulte a documentação da Oracle para mais informação sobre
todas as variáveis disponíveis.

**Variáveis de Ambiente Oracle Comuns**

| Nome | Propósito |
| --- | --- |
| ORACLE\_HOME | Contém o diretório da instalação completa do Banco de dados Oracle. Não defina esta variável ao usar o Oracle Instant Client pois é desnecessário e pode causar problemas de instalação. |
| ORACLE\_SID | Contém o nome do banco de dados na máquina local ao qual a ser conectado. Não há necessidade de definir esta variável se o Oracle Instant Client estiver sendo usado, ou passe sempre o parâmetro de conexão para a função [oci\_connect()](function.oci-connect.md). |
| LD\_LIBRARY\_PATH | Defina esta variável (ou sua equivalente dependendo da plataforma, como `LIBPATH` ou `SHLIB_PATH`) para a localização das bibliotecas Oracle libraries, por exemplo $ORACLE\_HOME/lib ou /usr/lib/oracle/18.5/client/lib. Note que com arquivos ZIP do Instant Client no Linux é mais confiável usar ldconfig, consulte as instruções de instalação do Instant Client. Com o Instant Client 19 (ou posterior) em arquivos RPM, `ldconfig` é executado automaticamente. Alguns usuários utilizam `LD_PRELOAD` no lugar de `LD_LIBRARY_PATH`. |
| NLS\_LANG | Esta é a variável primária para definir o conjunto de caracteres e informação de globalização usados pelas bibliotecas Oracle. |
| ORA\_SDTZ | Define o fuso horário da sessão Oracle. |
| TNS\_ADMIN | Contém o diretório onde os arquivos de configuração do Oracle Net Services como tnsnames.ora e sqlnet.ora são mantidos. Não é necessária se a string de conexão da função [oci\_connect()](function.oci-connect.md) usa a sintexe de nomes Easy Connect como `localhost/XE`. Não é necessária se os arquivos de configuração de rede estiverem em uma das localizações padrões como /usr/lib/oracle/VERSION/client/lib/network/admin, $ORACLE\_HOME/network/admin ou /etc. |

Variáveis de ambiente utilizadas com menor frequência incluem
`TWO_TASK`, `ORA_TZFILE` e as
várias configuração de globalização Oracle
como as variáveis `NLS*` e
`ORA_NLS_*`.

## Solução de Problemas

O problema mais comum na instalação do OCI8 é não ter o
ambiente Oracle definido corretamente. Isto tipicamente aparece como um
problema ao usar [oci\_connect()](function.oci-connect.md)
ou [oci\_pconnect()](function.oci-pconnect.md). O erro pode ser gerado pelo PHP,
como *Call to undefined function
oci\_connect()*, ou pelo Oracle, como ORA-12705, ou até
um travamento do Apache. Verifique se os arquivos de registro do Apache contêm erros de inicialização e
consulte as seções acima para resolver este problema.

Enquanto erros de rede como ORA-12154 ou ORA-12514 indicam um problema de
nome ou configuração de rede Oracle, a causa raiz pode ser o ambiente
PHP incorretamente configurado e a incapacidade das bibliotecas Oracle
em localizar o arquivo de configuração
tnsnames.ora.

No Windows, múltiplas versões do Oracle instaladas em uma máquina
pode facilmente gerar conflitos de bilbiotecas a menos que se tenha cuidado
garantindo que o PHP usa apenas a versão correta do Oracle.

Um utilitário para examinar que bibliotecas estão sendo procuradas e carregadas
pode ajudar a resolver problemas de bibliotecas ausentes ou conflitantes, particularmente no
Windows.

> **Nota**:
> **Se o servidor web não iniciar ou travar na
> inicialização**  
>
> Verifique que o Apache foi construído com a biblioteca pthread:
>
> ```
> # ldd /www/apache/bin/httpd
>   libpthread.so.0 => /lib/libpthread.so.0 (0x4001c000)
>   libm.so.6 => /lib/libm.so.6 (0x4002f000)
>   libcrypt.so.1 => /lib/libcrypt.so.1 (0x4004c000)
>   libdl.so.2 => /lib/libdl.so.2 (0x4007a000)
>   libc.so.6 => /lib/libc.so.6 (0x4007e000)
>   /lib/ld-linux.so.2 => /lib/ld-linux.so.2 (0x40000000)
> ```
>
> Se libpthread não estiver listada, reinstale o Apache:
>
> ```
> # cd /usr/src/apache_1.3.xx
> # make clean
> # LIBS=-lpthread ./config.status
> # make
> # make install
> ```
>
> Note que em alguns sistemas como UnixWare, o nome é libthread
> em vez de libpthread. PHP e Apache devem ser configurados com
> EXTRA\_LIBS=-lthread.

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
