# Suporte ao OCI8 Transparent Application Failover (TAF)

> **Fonte / Source:** https://www.php.net/manual/pt_BR/oci8.taf.php

---

# Suporte ao OCI8 Transparent Application Failover (TAF)

TAF é um recurso do Oracle Database que fornece alta disponibilidade.
Ele permite que apliações PHP OCI8 se reconectem automaticamente a um
banco de dados pré-configurado quando a conectividade do banco de dados falha devido a
uma falha na instância ou na rede.

Em um sistema Oracle Database configurado, o TAF ocorre quando a aplicação
PHP detecta que a instância do banco de dados está inativa
ou inacessível. Ele estabelece uma conexão com outro nó em uma
configuração Oracle [» RAC](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-DEF850F6-27E9-428E-B8FC-530230D78AD2),
em um banco de dados hot standby ou na própria instância
de banco
de dados. Consulte o [» Guia
do programador da Interface de Chamada Oracle](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-F7817CD2-4A2C-4D37-BD36-56DBABD4725F) para obter mais informações sobre
o OCI TAF.

Um retorno de chamada de aplicação pode ser registrado
com [oci\_register\_taf\_callback()](function.oci-register-taf-callback.md). Durante a recuperação
da falha, o processamento normal da aplicação é interrompido e o retorno de chamada
registrado é invocado. O retorno de chamada notifica a aplicação sobre os
eventos de falha. Se a recuperação for bem-sucedida, o processamento normal
será retomado. Se a recuperação abortar, quaisquer operações de banco de dados seguintes
na aplicação falharão devido à falta de conexão
disponível.

Quando uma conexão se recupera para um outro banco de dados, o retorno de chamada pode
redefinir qualquer estado de conexão necessário, por exemplo, reproduzindo quaisquer
comandos ALTER SESSION necessários se o serviço de banco de dados não tiver
-failover\_restore ativado.

Um retorno de chamada de aplicação pode ser removido chamando [oci\_unregister\_taf\_callback()](function.oci-unregister-taf-callback.md).

## Configurando o Transparent Application Failover

O TAF pode ser configurado no lado do PHP OCI8 ou na configuração
do banco de dados. Se ambos estiverem configurados, as configurações do lado do banco de dados
terão precedência.

Configure o TAF no PHP OCI8 (no lado do cliente) incluindo o
parâmetro FAILOVER\_MODE na parte CONNECT\_DATA de um
descritor de conexão. Consulte Configurando o Transparent Application
Failover no [» Guia
do Administrador de Serviços de Rede do Oracle Database](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-8F532535-C401-4B51-BE0B-04FD74BB0621) para
obter mais informações sobre a configuração do lado do cliente do TAF.

Um exemplo de tnsnames.ora para configurar o TAF para reconexão à
mesma instância do banco de dados:

```
    ORCL =
      (DESCRIPTION =
        (ADDRESS = (PROTOCOL = TCP)(HOST = 127.0.0.1)(PORT = 1521))
        (CONNECT_DATA =
          (SERVICE_NAME = orclpdb1)
          (FAILOVER_MODE =
            (TYPE = SELECT)
            (METHOD = BASIC)
            (RETRIES = 20)
            (DELAY = 15))))
```

Como alternativa, configure o TAF no lado do banco de dados
modificando o serviço de destino com
[» srvctl](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-8DC4D5E0-CA9D-47BC-BAD0-8769405AFEC5)
(para RAC) ou o procedimento empacotado
[» DBMS\_SERVICE.MODIFY\_SERVICE](https://www.oracle.com/pls/topic/lookup?ctx=dblatest&id=GUID-C11449DC-EEDE-4BB8-9D2C-0A45198C1928) (para
bancos de dados de instância
única).

## Usando Chamada de Retorno TAF no OCI8

Uma chamada de retorno TAF é uma função de aplicação que pode ser
registrada para ser chamada durante a recuperação de falha. Ela é chamada
diversas vezes ao restabelecer a conexão da aplicação.

A chamada de retorno ocorre primeiro quando uma perda de conexão é detectada.
Isso permite que a aplicação atue de acordo com o atraso
futuro da recuperação. Se a recuperação for bem-sucedida,
a chamada de retorno será invocada depois que a conexão for restabelecida
e utilizável. Neste momento, a aplicação pode ressincronizar
as configurações da sessão e executar ações como informar ao usuário
que ocorreu uma recuperação. Se ela não for bem-sucedida, ocorrerá
uma chamada de retorno para informar à aplicação que a recuperação não
ocorreu e que a conexão está inutilizável.

A interface de uma função de retorno TAF definida pelo usuário é
a seguinte:

function **userCallbackFn**([resource](language.types.resource.md) `$connection`, [int](language.types.integer.md) `$event`, [int](language.types.integer.md) `$type`): [int](language.types.integer.md)

`connection`
:   A conexão Oracle na qual a chamada de retorno TAF foi
    registrada por meio de [oci\_register\_taf\_callback()](function.oci-register-taf-callback.md).
    A conexão não é válida até que a
    recuperação seja concluída com êxito.

`event`
:   O evento de recuperação indica o status atual da
    recuperação.

    - **`OCI_FO_BEGIN`** indica que
      a recuperação detectou uma conexão perdida e a recuperação
      está iniciando.
    - **`OCI_FO_END`** indica conclusão
      de recuperação com sucesso.
    - **`OCI_FO_ABORT`** indica que
      a recuperação não foi bem-sucedida e que não há opção
      de uma nova tentativa.
    - **`OCI_FO_ERROR`** também indica
      que a recuperação não foi bem-sucedida mas dá à
      aplicação a oportunidade de lidar com o erro
      e retornar OCI\_FO\_RETRY para tentar a recuperação novamente.
    - **`OCI_FO_REAUTH`** indica
      que um usuário Oracle foi re-autenticado.

`type`
:   O tipo da recuperação. Isto permite que a função de retorno saiba que
    tipo de recuperação a aplicação solicitou. Os
    valores usuais são os seguintes:

    - **`OCI_FO_SESSION`** indica que
      o usuário solicitou recuperação apenas de sessão. Por
      exemplo, se uma conexão de usuário é perdida, uma
      nova sessão é automaticamente criada para o usuário
      no backup. Este tipo de recuparação não tenta
      recuperar SELECTs.
    - **`OCI_FO_SELECT`** indica que
      o usuário também solicitou recuperação SELECT.
      Isto permite que usuários com cursores abertos continuem
      buscando dados após a falha.

`return value`
:   - `0` indica que os passos de
      recuperação devem continuar normalmente.
    - **`OCI_FO_RETRY`** indica que
      a recuperação deve ser tentada novamente pelo Oracle.
      No caso de um erro durante a recuperação para uma nova
      conexão, o TAF poderá tentar novamente a recuperação.
      Normalmente, o código da aplicação deve ficar inativo por
      um tempo antes de retornar OCI\_FO\_RETRY.

**Exemplo #1 Registrando uma chamada de retorno TAF**

```
<?php

// Define chamda de retorno no espaço de usuário
class MyClass {
    public static $retry_count;
    public static function TAFCallback($conn, $event, $type)
    {
        switch ($event) {
            case OCI_FO_BEGIN:
                printf(" Recuperando ... Por favor aguarde\n");
                printf(" Tipo de recuperação é %s \n",
                       (($type==OCI_FO_SESSION) ? "SESSION"
                        :(($type==OCI_FO_SELECT) ? "SELECT" : "DESCONHECIDA!")));
                self::$retry_count = 0;
                break;
            case OCI_FO_ABORT:
                // A aplicação não pode continuar usando o banco de dados
                printf(" Recuperação abortada. Recuperação não irá ocorrer.\n");
                break;
            case OCI_FO_END:
                // Recuperação conclui com sucesso. Informa usuários que uma recuperação aconteceu.
                printf(" Recuperação concluída ... retomando os serviços\n");
                break;
            case OCI_FO_REAUTH:
                printf(" Recuperando usuário ... retomando os serviços\n");
                // Reproduz qualquer comando ALTER SESSION associados com esta conexão
                // por exemplo, oci_parse($conn, ‘ALTER SESSION …’) ;
                break;
            case OCI_FO_ERROR:
                // Para de tentar se já foram feitas 20 tentativas.
                if (self::$retry_count >= 20)
                    return 0;
                printf(" Erro de recuperação recebido. Aguardando...\n");
                sleep(10);
                self::$retry_count++;
                return OCI_FO_RETRY; // tenta a recuperação novamente
                break;
            default:
                printf("Evento de recuperação desconhecido: %d.\n", $event);
                break;
        }
        return 0;
    }
}

$fn_name = 'MyClass::TAFCallback';

$conn = oci_connect('hr', 'welcome', 'orcl');
$sysconn = oci_connect('system', 'oracle', 'orcl');

// Usa uma conexão privilegiada para construir uma instrução SQL que iniciará a recuperação
$sql = <<< 'END'
select unique 'alter system disconnect session '''||sid||','||serial#||''''
from v$session_connect_info
where sid = sys_context('USERENV', 'SID')
END;

$s = oci_parse($conn, $sql);
oci_execute($s);
$r = oci_fetch_array($s);
$disconnectssql = $r[0];

oci_register_taf_callback($conn, $fn_name); // Registra TAFCallback para Oracle TAF

print "Analisando a consulta do usuário\n";
$sql = "select systimestamp from dual";
$stmt = oci_parse($conn, $sql);

// Por exemplo, se ocorrer uma perda de conexão neste ponto, oci_execute() detectará
// a perda e a recuperação será iniciada. Durante a recuperação, oci_execute() invocará
// a função de retorno de chamada do TAF diversas vezes. Se a recuperação for bem-sucedida,
// uma nova conexão será criada de forma transparente e oci_execute() continuará
// normalmente. As configurações da sessão de conexão podem ser redefinidas na função de
// retorno de chamada TAF. Se a recuperação for abortada, oci_execute() retornará um erro
// porque uma conexão válida não está disponível.

// Desconecta o usuário, o que inicia a recuperação
print "Desconectando o usuário\n";
$discsql = oci_parse($sysconn, $disconnectssql);
oci_execute($discsql);

print "Executando a consulta do usuário\n";
$e = oci_execute($stmt);
if (!$e) {
    $m = oci_error($stmt);
    trigger_error("Não foi possível executar a instrução: ". $m['message'], E_USER_ERROR);
}
$row = oci_fetch_array($stmt);
print $row[0] . "\n";

// executa outras instruções SQL com a nova conexão, se ainda for válida
// $stmt = oci_parse($conn,  . . .);

?>
```

## Veja também

- [oci\_register\_taf\_callback()](function.oci-register-taf-callback.md)
- [oci\_unregister\_taf\_callback()](function.oci-unregister-taf-callback.md)

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
