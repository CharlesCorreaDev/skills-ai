# Suporte à Notificação Rápida de Aplicação (FAN) do OCI8

> **Fonte / Source:** https://www.php.net/manual/pt_BR/oci8.fan.php

---

# Suporte à Notificação Rápida de Aplicação (FAN) do OCI8

O suporte ao FAN oferece recuperação rápida de falhas de conexão, um recurso de alta disponibilidade
do banco de dados Oracle. Isso permite que scripts PHP OCI8 sejam notificados quando uma
máquina de banco de dados ou instância de banco de dados ficar indisponível. Sem o
FAN, o OCI8 pode travar até que ocorra um tempo limite de TCP e um erro seja
retornado, o que pode levar vários minutos. A ativação do FAN no OCI8 pode
permitir que as aplicações detectem erros e se reconectem a uma instância
de banco de dados disponível sem que o usuário da web perceba uma interrupção.

O suporte ao FAN está disponível quando as bibliotecas cliente Oracle com as quais o PHP
se vincula e o banco de dados Oracle são da versão 10gR2 ou posterior.

O FAN beneficia os usuários da tecnologia de cluster (RAC) da Oracle porque
as conexões com as instâncias de banco de dados sobreviventes podem ser feitas
imediatamente. Os usuários do Data Guard da Oracle com um mediador verão os eventos
FAN gerados quando o banco de dados de reserva ficar online. Os bancos de dados
autônomos enviarão eventos FAN quando o banco de dados for reiniciado.

Para conexões ativas, quando uma máquina ou instância de banco de dados ficar
indisponível, um erro de falha de conexão será retornado pela
função da extensão OCI8 que está sendo chamada no momento. Em uma reconexão
subsequente do script PHP, será estabelecida uma conexão com uma instância de
banco de dados sobrevivente. A extensão OCI8 também
limpa de forma transparente quaisquer conexões ociosas afetadas por uma falha de máquina
ou de instância de banco de dados, para que as chamadas de conexão do PHP estabeleçam uma
nova conexão sem que o script esteja ciente de qualquer interrupção
do serviço.

Quando [oci8.events](oci8.configuration.md#ini.oci8.events)
for igual a `On`, a sugestão é
definir [oci8.ping\_interval](oci8.configuration.md#ini.oci8.ping-interval)
para -1 para desabilitar o ping, já que habilitar eventos FAN fornece
um gerenciamento proativo de conexões ociosas que se tornaram inválidas
por uma interrupção de serviço.

Para ativar o suporte FAN no PHP OCI8, compile o PHP OCI8 com bibliotecas Oracle 10gR2
ou posteriores e siga estas etapas:

- Como administrador de banco de dados privilegiado, use um programa como
  o SQL\*Plus para permitir que o serviço de banco de dados poste
  eventos FAN, por exemplo:

  ```
      SQL> execute dbms_service.modify_service(
                     SERVICE_NAME        => 'sales',
                     AQ_HA_NOTIFICATIONS => TRUE);
  ```
- Edite o php.ini e adicione

  ```
      oci8.events = On
  ```
- Se a aplicação ainda não lidar com condições de erro
  OCI8, modifique-a para detectar falhas e tomar as medidas
  apropriadas. Isso pode incluir a reconexão e a reexecução de
  instruções.
- Execute a aplicação conectando-se ao Oracle Database 10gR2 ou posterior.

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
