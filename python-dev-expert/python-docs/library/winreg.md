"winreg" --- Acesso aos registros do Windows
********************************************

**Source code:** PC/winreg.c

======================================================================

Essas funções expõem a API de registro do Windows ao Python. Em vez de
usar um inteiro como identificador de registro, um objeto
identificador é usado para garantir que os identificadores sejam
fechados corretamente, mesmo que o programador não os feche
explicitamente.

Disponibilidade: Windows.

Alterado na versão 3.3: Várias funções neste módulo costumavam
levantar um "WindowsError" , que agora é um apelido de "OSError".


Funções
=======

Este módulo oferece as seguintes funções:

winreg.CloseKey(hkey)

   Fecha uma chave de registro aberta anteriormente. O argumento
   *hkey* especifica uma chave aberta anteriormente.

   Nota:

     Se *hkey* não for fechado usando este método (ou via
     "hkey.Close()"), ele será fechado quando o objeto *hkey* for
     destruído pelo Python.

winreg.ConnectRegistry(computer_name, key)

   Estabelece uma conexão com um identificador de registro predefinido
   em outro computador e retorna um objeto identificador.

   *computer_name* é o nome do computador remoto, no formato
   "r"\\computername"". Se "None", o computador local será usado.

   *key* é o identificador predefinido para conexão.

   O valor de retorno é o identificador da chave aberta. Se a função
   falhar, uma exceção "OSError" será levantada.

   Levanta um evento de auditoria "winreg.ConnectRegistry" com os
   argumentos "computer_name", "key".

   Alterado na versão 3.3: Veja acima.

winreg.CreateKey(key, sub_key)

   Cria ou abre a chave especificada, retornando um objeto
   identificador.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *sub_key* é uma string que nomeia a chave que este método abre ou
   cria.

   Se *key* for uma das chaves predefinidas, *sub_key* poderá ser
   "None". Nesse caso, o identificador retornado será o mesmo
   identificador de chave passado para a função.

   Se a chave já existir, esta função abre a chave existente.

   O valor de retorno é o identificador da chave aberta. Se a função
   falhar, uma exceção "OSError" será levantada.

   Levanta um evento de auditoria "winreg.CreateKey" com os argumentos
   "key", "sub_key", "access".

   Levanta um evento de auditoria "winreg.OpenKey/result" com o
   argumento "key".

   Alterado na versão 3.3: Veja acima.

winreg.CreateKeyEx(key, sub_key, reserved=0, access=KEY_WRITE)

   Cria ou abre a chave especificada, retornando um objeto
   identificador.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *sub_key* é uma string que nomeia a chave que este método abre ou
   cria.

   *reserved* é um inteiro reservado e deve ser zero. O padrão é zero.

   *access* é um inteiro que especifica uma máscara de acesso que
   descreve o acesso de segurança desejado para a chave. O padrão é
   "KEY_WRITE". Consulte Direitos de acesso para outros valores
   permitidos.

   Se *key* for uma das chaves predefinidas, *sub_key* poderá ser
   "None". Nesse caso, o identificador retornado será o mesmo
   identificador de chave passado para a função.

   Se a chave já existir, esta função abre a chave existente.

   O valor de retorno é o identificador da chave aberta. Se a função
   falhar, uma exceção "OSError" será levantada.

   Levanta um evento de auditoria "winreg.CreateKey" com os argumentos
   "key", "sub_key", "access".

   Levanta um evento de auditoria "winreg.OpenKey/result" com o
   argumento "key".

   Adicionado na versão 3.2.

   Alterado na versão 3.3: Veja acima.

winreg.DeleteKey(key, sub_key)

   Exclui a chave especificada.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *sub_key* é uma string que deve ser uma subchave da chave
   identificada pelo parâmetro *key*. Este valor não pode ser "None",
   e a chave não pode ter subchaves.

   *Este método não pode excluir chaves com subchaves.*

   Se o método for bem-sucedido, a chave inteira, incluindo todos os
   seus valores, será removida. Se o método falhar, uma exceção
   "OSError" será levantada.

   Levanta um evento de auditoria "winreg.DeleteKey" com os argumentos
   "key", "sub_key", "access".

   Alterado na versão 3.3: Veja acima.

winreg.DeleteKeyEx(key, sub_key, access=KEY_WOW64_64KEY, reserved=0)

   Exclui a chave especificada.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *sub_key* é uma string que deve ser uma subchave da chave
   identificada pelo parâmetro *key*. Este valor não pode ser "None",
   e a chave não pode ter subchaves.

   *reserved* é um inteiro reservado e deve ser zero. O padrão é zero.

   *access* é um inteiro que especifica uma máscara de acesso que
   descreve o acesso de segurança desejado para a chave. O padrão é
   "KEY_WOW64_64KEY". No Windows de 32 bits, as constantes WOW64 são
   ignoradas. Consulte Direitos de acesso para outros valores
   permitidos.

   *Este método não pode excluir chaves com subchaves.*

   Se o método for bem-sucedido, a chave inteira, incluindo todos os
   seus valores, será removida. Se o método falhar, uma exceção
   "OSError" será levantada.

   Em versões do Windows sem suporte, "NotImplementedError" é
   levantada.

   Levanta um evento de auditoria "winreg.DeleteKey" com os argumentos
   "key", "sub_key", "access".

   Adicionado na versão 3.2.

   Alterado na versão 3.3: Veja acima.

winreg.DeleteTree(key, sub_key=None)

   Deletes the specified key and all its subkeys and values
   recursively.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *sub_key* is a string that names the subkey to delete. If "None",
   deletes all subkeys and values of the specified key.

   This function deletes a key and all its descendants. If *sub_key*
   is "None", all subkeys and values of the specified key are deleted.

   Raises an auditing event "winreg.DeleteTree" with arguments "key",
   "sub_key".

   Adicionado na versão 3.15.

winreg.DeleteValue(key, value)

   Remove um valor nomeado de uma chave de registro.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *value* é uma string que identifica o valor a ser removido.

   Levanta um evento de auditoria "winreg.DeleteValue" com os
   argumentos "key", "value".

winreg.EnumKey(key, index)

   Enumera subchaves de uma chave de registro aberta, retornando uma
   string.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *index* é um inteiro que identifica o índice da chave a ser
   recuperada.

   A função recupera o nome de uma subchave cada vez que é chamada.
   Normalmente, ela é chamada repetidamente até que uma exceção
   "OSError" seja levantada, indicando que não há mais valores
   disponíveis.

   Levanta um evento de auditoria "winreg.EnumKey" com os argumentos
   "key", "index".

   Alterado na versão 3.3: Veja acima.

winreg.EnumValue(key, index)

   Enumera valores de uma chave de registro aberta, retornando uma
   tupla.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *index* é um inteiro que identifica o índice do valor a ser
   recuperado.

   A função recupera o nome de uma subchave cada vez que é chamada.
   Normalmente, ela é chamada repetidamente, até que uma exceção
   "OSError" seja levantada, indicando que não há mais valores.

   O resultado é uma tupla de 3 itens:

   +---------+----------------------------------------------+
   | Índice  | Significado                                  |
   |=========|==============================================|
   | "0"     | Uma string que identifica o nome do valor    |
   +---------+----------------------------------------------+
   | "1"     | Um objeto que contém os dados de valor e     |
   |         | cujo tipo depende do tipo de registro        |
   |         | subjacente                                   |
   +---------+----------------------------------------------+
   | "2"     | Um inteiro que identifica o tipo dos dados   |
   |         | do valor (veja a tabela na documentação para |
   |         | "SetValueEx()")                              |
   +---------+----------------------------------------------+

   Levanta um evento de auditoria "winreg.EnumValue" com os argumentos
   "key", "index".

   Alterado na versão 3.3: Veja acima.

winreg.ExpandEnvironmentStrings(str)

   Expande os espaços reservados de posição de variáveis de ambiente
   "%NAME%" em strings como "REG_EXPAND_SZ":

      >>> ExpandEnvironmentStrings('%windir%')
      'C:\\Windows'

   Levanta um evento de auditoria "winreg.ExpandEnvironmentStrings"
   com o argumento "str".

winreg.FlushKey(key)

   Grava todos os atributos de uma chave no registro.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   Não é necessário chamar "FlushKey()" para alterar uma chave. As
   alterações do registro são descarregadas no disco pelo registro
   usando seu limpador lento. As alterações do registro também são
   descarregadas no disco no desligamento do sistema. Ao contrário de
   "CloseKey()", o método "FlushKey()" retorna somente quando todos os
   dados foram gravados no registro. Uma aplicação só deve chamar
   "FlushKey()" se precisar de certeza absoluta de que as alterações
   do registro estão no disco.

   Nota:

     Se você não sabe se uma chamada "FlushKey()" é necessária,
     provavelmente não é.

winreg.LoadKey(key, sub_key, file_name)

   Cria uma subchave sob a chave especificada e armazena informações
   de registro de um arquivo especificado nessa subchave.

   *key* é um identificador retornado por "ConnectRegistry()" ou uma
   das constantes "HKEY_USERS" ou "HKEY_LOCAL_MACHINE".

   *sub_key* é uma string que identifica a subchave a ser carregada.

   *file_name* é o nome do arquivo do qual serão carregados os dados
   do registro. Este arquivo deve ter sido criado com a função
   "SaveKey()". No sistema de arquivos da tabela de alocação de
   arquivos (FAT), o nome do arquivo não pode ter extensão.

   Uma chamada para "LoadKey()" falhará se o processo de chamada não
   tiver o privilégio "SE_RESTORE_PRIVILEGE". Observe que privilégios
   são diferentes de permissões — consulte a documentação do
   RegLoadKey para mais detalhes.

   Se *key* for um identificador retornado por "ConnectRegistry()",
   então o caminho especificado em *file_name* será relativo ao
   computador remoto.

   Levanta um evento de auditoria "winreg.LoadKey" com os argumentos
   "key", "sub_key", "file_name".

winreg.OpenKey(key, sub_key, reserved=0, access=KEY_READ)
winreg.OpenKeyEx(key, sub_key, reserved=0, access=KEY_READ)

   Abre a chave especificada, retornando um objeto identificador.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *sub_key* é uma string que identifica a sub_key a ser aberta.

   *reserved* é um inteiro reservado e deve ser zero. O padrão é zero.

   *access* é um inteiro que especifica uma máscara de acesso que
   descreve o acesso de segurança desejado para a chave. O padrão é
   "KEY_READ". Consulte Direitos de acesso para outros valores
   permitidos.

   O resultado é um novo identificador para a chave especificada.

   Se a função falhar, "OSError" será levantada.

   Levanta um evento de auditoria "winreg.OpenKey" com os argumentos
   "key", "sub_key", "access".

   Levanta um evento de auditoria "winreg.OpenKey/result" com o
   argumento "key".

   Alterado na versão 3.2: Permite o uso de argumentos nomeados.

   Alterado na versão 3.3: Veja acima.

winreg.QueryInfoKey(key)

   Retorna informações sobre uma chave, como uma tupla.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   O resultado é uma tupla de 3 itens:

   +---------+-----------------------------------------------+
   | Índice  | Significado                                   |
   |=========|===============================================|
   | "0"     | Um inteiro que fornece o número de subchaves  |
   |         | que esta chave possui.                        |
   +---------+-----------------------------------------------+
   | "1"     | Um inteiro que fornece o número de valores    |
   |         | que esta chave possui.                        |
   +---------+-----------------------------------------------+
   | "2"     | Um número inteiro que indica quando a chave   |
   |         | foi modificada pela última vez (se            |
   |         | disponível) em centenas de nanossegundos      |
   |         | desde 1º de janeiro de 1601.                  |
   +---------+-----------------------------------------------+

   Levanta um evento de auditoria "winreg.QueryInfoKey" com o
   argumento "key".

winreg.QueryValue(key, sub_key)

   Recupera o valor sem nome de uma chave, como uma string.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *sub_key* é uma string que contém o nome da subchave à qual o valor
   está associado. Se este parâmetro for "None" ou estiver vazio, a
   função recupera o valor definido pelo método "SetValue()" para a
   chave identificada por *key*.

   Os valores no registro têm componentes de nome, tipo e dados. Este
   método recupera os dados do primeiro valor de uma chave que possui
   um nome "NULL". Mas a chamada de API subjacente não retorna o tipo,
   portanto, sempre use "QueryValueEx()" se possível.

   Levanta um evento de auditoria "winreg.QueryValue" com os
   argumentos "key", "sub_key", "value_name".

winreg.QueryValueEx(key, value_name)

   Recupera o tipo e os dados de um nome de valor especificado
   associado a uma chave de registro aberta.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *value_name* é uma string que indica o valor a ser consultado.

   O resultado é uma tupla de 2 itens:

   +---------+-------------------------------------------+
   | Índice  | Significado                               |
   |=========|===========================================|
   | "0"     | O valor do item do registro.              |
   +---------+-------------------------------------------+
   | "1"     | Um inteiro que fornece o tipo de registro |
   |         | para este valor (veja a tabela na         |
   |         | documentação para "SetValueEx()")         |
   +---------+-------------------------------------------+

   Levanta um evento de auditoria "winreg.QueryValue" com os
   argumentos "key", "sub_key", "value_name".

winreg.SaveKey(key, file_name)

   Salva a chave especificada e todas as suas subchaves no arquivo
   especificado.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *file_name* é o nome do arquivo para salvar os dados do registro.
   Este arquivo não pode existir. Se este nome de arquivo incluir uma
   extensão, ele não poderá ser usado em sistemas de arquivos FAT
   (tabela de alocação de arquivos) pelo método "LoadKey()".

   Se *key* representa uma chave em um computador remoto, o caminho
   descrito por *file_name* é relativo ao computador remoto. O
   chamador deste método deve possuir o privilégio de segurança
   **SeBackupPrivilege**. Observe que privilégios são diferentes de
   permissões — consulte a documentação Conflitos entre Direitos e
   Permissões do Usuário para obter mais detalhes.

   Esta função passa "NULL" para *security_attributes* para a API.

   Levanta um evento de auditoria "winreg.SaveKey" com os argumentos
   "key", "file_name".

winreg.SetValue(key, sub_key, type, value)

   Associa um valor a uma chave especificada.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *sub_key* é uma string que nomeia a subchave à qual o valor está
   associado.

   *type* é um inteiro que especifica o tipo dos dados. Atualmente,
   deve ser "REG_SZ", o que significa que apenas strings são
   suportadas. Use a função "SetValueEx()" para suporte a outros tipos
   de dados.

   *valor* é uma string que especifica o novo valor.

   Se a chave especificada pelo parâmetro *sub_key* não existir, a
   função SetValue a criará.

   O comprimento dos valores é limitado pela memória disponível.
   Valores longos (mais de 2048 bytes) devem ser armazenados como
   arquivos com os nomes dos arquivos armazenados no registro de
   configuração. Isso ajuda o registro a funcionar com eficiência.

   A chave identificada pelo parâmetro *key* deve ter sido aberta com
   acesso "KEY_SET_VALUE".

   Levanta um evento de auditoria "winreg.SetValue" com os argumentos
   "key", "sub_key", "type", "value".

winreg.SetValueEx(key, value_name, reserved, type, value)

   Armazena dados no campo de valor de uma chave de registro aberta.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   *value_name* é uma string que nomeia a subchave à qual o valor está
   associado.

   *reserved* pode ser qualquer coisa -- zero é sempre passado para a
   API.

   *type* é um inteiro que especifica o tipo dos dados. Consulte Tipos
   de valor para os tipos disponíveis.

   *valor* é uma string que especifica o novo valor.

   Este método também pode definir informações adicionais de valor e
   tipo para a chave especificada. A chave identificada pelo parâmetro
   key deve ter sido aberta com o acesso "KEY_SET_VALUE".

   Para abrir a chave, use os métodos "CreateKey()" ou "OpenKey()".

   O comprimento dos valores é limitado pela memória disponível.
   Valores longos (mais de 2048 bytes) devem ser armazenados como
   arquivos com os nomes dos arquivos armazenados no registro de
   configuração. Isso ajuda o registro a funcionar com eficiência.

   Levanta um evento de auditoria "winreg.SetValue" com os argumentos
   "key", "sub_key", "type", "value".

winreg.DisableReflectionKey(key)

   Desabilita a reflexão do registro para processos de 32 bits em
   execução em um sistema operacional de 64 bits.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   Geralmente levantará "NotImplementedError" se executado em um
   sistema operacional de 32 bits.

   Se a chave não estiver na lista de reflexão, a função será bem-
   sucedida, mas não terá efeito. Desabilitar a reflexão para uma
   chave não afeta a reflexão de nenhuma subchave.

   Levanta um evento de auditoria "winreg.DisableReflectionKey" com o
   argumento "key".

winreg.EnableReflectionKey(key)

   Restaura a reflexão do registro para a chave desabilitada
   especificada.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   Geralmente levantará "NotImplementedError" se executado em um
   sistema operacional de 32 bits.

   Restaura a reflexão de uma chave não afeta a reflexão de nenhuma
   subchave.

   Levanta um evento de auditoria "winreg.EnableReflectionKey" com o
   argumento "key".

winreg.QueryReflectionKey(key)

   Determina o estado de reflexão para a chave especificada.

   *key* é uma chave já aberta, ou uma das constantes predefinidas
   HKEY_*.

   Retorna "True" se a reflexão estiver desabilitada.

   Geralmente levantará "NotImplementedError" se executado em um
   sistema operacional de 32 bits.

   Levanta um evento de auditoria "winreg.QueryReflectionKey" com o
   argumento "key".


Constantes
==========

As seguintes constantes são definidas para uso em muitas funções do
módulo "winreg".


Constantes HKEY_*
-----------------

winreg.HKEY_CLASSES_ROOT

   Entradas de registro subordinadas a esta chave definem tipos (ou
   classes) de documentos e as propriedades associadas a esses tipos.
   Aplicações Shell e COM utilizam as informações armazenadas sob esta
   chave.

winreg.HKEY_CURRENT_USER

   As entradas de registro subordinadas a esta chave definem as
   preferências do usuário atual. Essas preferências incluem as
   configurações de variáveis de ambiente, dados sobre grupos de
   programas, cores, impressoras, conexões de rede e preferências de
   aplicações.

winreg.HKEY_LOCAL_MACHINE

   As entradas de registro subordinadas a esta chave definem o estado
   físico do computador, incluindo dados sobre o tipo de barramento,
   memória do sistema e hardware e software instalados.

winreg.HKEY_USERS

   As entradas de registro subordinadas a esta chave definem a
   configuração de usuário padrão para novos usuários no computador
   local e a configuração de usuário para o usuário atual.

winreg.HKEY_PERFORMANCE_DATA

   Entradas de registro subordinadas a esta chave permitem que você
   acesse dados de desempenho. Os dados não são armazenados no
   registro; as funções de registro fazem com que o sistema colete os
   dados de sua fonte.

winreg.HKEY_CURRENT_CONFIG

   Contém informações sobre o perfil de hardware atual do sistema de
   computador local.

winreg.HKEY_DYN_DATA

   Esta chave não é usada em versões do Windows posteriores à 98.


Direitos de acesso
------------------

Para obter mais informações, consulte Segurança e acesso a chaves do
registro.

winreg.KEY_ALL_ACCESS

   Combina os direitos de acesso STANDARD_RIGHTS_REQUIRED,
   "KEY_QUERY_VALUE", "KEY_SET_VALUE", "KEY_CREATE_SUB_KEY",
   "KEY_ENUMERATE_SUB_KEYS", "KEY_NOTIFY" e "KEY_CREATE_LINK".

winreg.KEY_WRITE

   Combina os direitos de acesso STANDARD_RIGHTS_WRITE,
   "KEY_SET_VALUE" e "KEY_CREATE_SUB_KEY".

winreg.KEY_READ

   Combina os valores STANDARD_RIGHTS_READ, "KEY_QUERY_VALUE",
   "KEY_ENUMERATE_SUB_KEYS" e "KEY_NOTIFY".

winreg.KEY_EXECUTE

   Equivalente a "KEY_READ".

winreg.KEY_QUERY_VALUE

   Necessário para consultar os valores de uma chave de registro.

winreg.KEY_SET_VALUE

   Necessário para criar, excluir ou definir um valor de registro.

winreg.KEY_CREATE_SUB_KEY

   Necessário para criar uma subchave de uma chave de registro.

winreg.KEY_ENUMERATE_SUB_KEYS

   Necessário para enumerar as subchaves de uma chave de registro.

winreg.KEY_NOTIFY

   Necessário para solicitar notificações de alteração para uma chave
   de registro ou para subchaves de uma chave de registro.

winreg.KEY_CREATE_LINK

   Reservado para uso pelo sistema.


Específico de 64 bits
~~~~~~~~~~~~~~~~~~~~~

Para obter mais informações, consulte Acessando uma exibição
alternativa do Registro.

winreg.KEY_WOW64_64KEY

   Indica que uma aplicação no Windows 64 bits deve operar na
   visualização de registro de 64 bits. No Windows de 32 bits, esta
   constante é ignorada.

winreg.KEY_WOW64_32KEY

   Indica que uma aplicação no Windows 64 bits deve operar na
   visualização de registro de 32 bits. No Windows de 32 bits, esta
   constante é ignorada.


Tipos de valores
----------------

Para obter mais informações, consulte Tipos de valor do Registro.

winreg.REG_BINARY

   Dados binários em qualquer formato.

winreg.REG_DWORD

   Número de 32 bits.

winreg.REG_DWORD_LITTLE_ENDIAN

   Um número de 32 bits no formato little-endian. Equivalente a
   "REG_DWORD".

winreg.REG_DWORD_BIG_ENDIAN

   Um número de 32 bits no formato big-endian.

winreg.REG_EXPAND_SZ

   String terminada em nulo contendo referências a variáveis de
   ambiente ("%PATH%").

winreg.REG_LINK

   Um link simbólico Unicode.

winreg.REG_MULTI_SZ

   Uma sequência de strings terminadas em nulo, terminadas por dois
   caracteres nulos. (O Python lida com essa terminação
   automaticamente.)

winreg.REG_NONE

   Nenhum tipo de valor definido.

winreg.REG_QWORD

   Um número de 64 bits.

   Adicionado na versão 3.6.

winreg.REG_QWORD_LITTLE_ENDIAN

   Um número de 64 bits no formato little-endian. Equivalente a
   "REG_QWORD".

   Adicionado na versão 3.6.

winreg.REG_RESOURCE_LIST

   Uma lista de recursos de driver de dispositivo.

winreg.REG_FULL_RESOURCE_DESCRIPTOR

   Uma configuração de hardware.

winreg.REG_RESOURCE_REQUIREMENTS_LIST

   Uma lista de recursos de hardware.

winreg.REG_SZ

   Uma string terminada em nulo.


Objetos identificador de registro
=================================

Este objeto encapsula um objeto HKEY do Windows, fechando-o
automaticamente quando o objeto é destruído. Para garantir a limpeza,
você pode chamar o método "Close()" no objeto ou a função
"CloseKey()".

Todas as funções de registro neste módulo retornam um destes objetos.

Todas as funções de registro neste módulo que aceitam um objeto
identificador também aceitam um inteiro; no entanto, o uso do objeto
identificador é incentivado.

Objetos identificador fornecem semântica para "__bool__()" -- portanto

   if handle:
       print("Sim")

vai exibir "Sim" se o identificador for válido no momento (não foi
fechado ou desanexado).

The object also support equality comparison semantics, so handle
objects will compare equal if they both reference the same underlying
Windows handle value. Closed handle objects (those with a handle value
of zero) always compare equal.

Objetos identificador podem ser convertidos em um inteiro (por
exemplo, usando a função embutida "int()"), caso em que o valor do
identificador do Windows subjacente é retornado. Você também pode usar
o método "Detach()" para retornar o identificador inteiro e também
desconectar o identificador do Windows do objeto identificador.

PyHKEY.Close()

   Fecha o identificador subjacente do Windows.

   Se o identificador já estiver fechado, nenhum erro será levantado.

PyHKEY.Detach()

   Separa o identificador do Windows do objeto identificador.

   O resultado é um inteiro que contém o valor do identificador antes
   de ser destacado. Se o identificador já estiver destacado ou
   fechado, isso retornará zero.

   Após chamar esta função, o identificador é efetivamente invalidado,
   mas não é fechado. Você chamaria esta função quando precisasse que
   o identificador subjacente de Win32 existisse além do tempo de vida
   do objeto identificador.

   Levanta um evento de auditoria "winreg.PyHKEY.Detach" com o
   argumento "key".

PyHKEY.__enter__()
PyHKEY.__exit__(*exc_info)

   O objeto HKEY implementa "__enter__()" e "__exit__()" e, portanto,
   oferece suporte ao protocolo de contexto para a instrução "with":

      with OpenKey(HKEY_LOCAL_MACHINE, "foo") as key:
          ...  # trabalha com a chave "key"

   vai fechar automaticamente *key* quando o controle sair do bloco
   "with".

Alterado na versão 3.15: Handle objects are now compared by their
underlying Windows handle value instead of object identity for
equality comparisons.
