"netrc" --- Arquivo de processamento netrc
******************************************

**Código-fonte:** Lib/netrc.py

======================================================================

A classe "netrc" analisa e encapsula o formato do arquivo netrc usado
pelo programa Unix **ftp** e outros clientes FTP.

class netrc.netrc([file])

   Uma instância ou instância de subclasse de "netrc" encapsula dados
   de um arquivo netrc. O argumento de inicialização, se presente,
   especifica o arquivo a ser analisado. Se nenhum argumento for
   fornecido, o arquivo ".netrc" no diretório inicial do usuário --
   conforme determinado por "os.path.expanduser()" -- será lido. Caso
   contrário, uma exceção "FileNotFoundError" será levantada. Os erros
   de análise levantam "NetrcParseError" com informações de
   diagnóstico, incluindo o nome do arquivo, o número da linha e o
   token final.

   Se nenhum argumento for especificado em um sistema POSIX, a
   presença de senhas no arquivo ".netrc" levantará um
   "NetrcParseError" se a propriedade ou as permissões do arquivo
   forem inseguras (pertencentes a um usuário que não seja o usuário
   executando o processo ou acessível para leitura ou gravação por
   qualquer outro usuário). Isso implementa um comportamento de
   segurança equivalente ao do ftp e de outros programas que usam
   ".netrc". Essas verificações de segurança não estão disponíveis em
   plataformas que não oferecem suporte a "os.getuid()".

   Alterado na versão 3.4: Adicionada a verificação de permissão
   POSIX.

   Alterado na versão 3.7: "os.path.expanduser()" é usado para
   encontrar a localização do arquivo ".netrc" quando *file* não é
   passado como argumento.

   Alterado na versão 3.10: "netrc" try UTF-8 encoding before using
   locale specific encoding. The entry in the netrc file no longer
   needs to contain all tokens.  The missing tokens' value default to
   an empty string.  All the tokens and their values now can contain
   arbitrary characters, like whitespace and non-ASCII characters. If
   the login name is anonymous, it won't trigger the security check.

exception netrc.NetrcParseError

   Exceção levantada pela classe "netrc" quando erros sintáticos são
   encontrados no texto fonte. As instâncias desta exceção fornecem
   três atributos interessantes:

   msg

      Explicação textual do erro.

   filename

      O nome do arquivo de origem.

   lineno

      O número da linha em que o erro foi encontrado.


Objetos netrc
=============

Uma instância da classe "netrc" tem os seguintes métodos:

netrc.authenticators(host)

   Retorna uma tupla de 3 elementos "(login, conta, senha)" dos
   autenticadores do *host*. Se o arquivo netrc não contém uma entrada
   para o host dado, retorna a tupla associada com a entrada padrão.
   Se não houver nenhum host correspondente nem uma entrada padrão
   estiver disponível, retorna "None".

netrc.__repr__()

   Despeja os dados da classe como uma string no formato de um arquivo
   netrc. (Isso descarta os comentários e pode reordenar as entradas.)

Instâncias de "netrc" possuem variáveis de instância públicas:

netrc.hosts

   Dicionário mapeando nomes de host para tuplas "(login, conta,
   senha)". A entrada *default*, se houver, é representada como um
   pseudo-host por esse nome.

netrc.macros

   Dicionário mapeando nomes de macros para listas de strings.
