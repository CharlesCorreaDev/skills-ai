"stat" --- Interpretando resultados de "stat()"
***********************************************

**Código-fonte:** Lib/stat.py

======================================================================

O módulo "stat" define constantes e funções para interpretar os
resultados de "os.stat()", "os.fstat()" e "os.lstat()" (se existirem).
Para detalhes completos sobre chamadas "stat()", "fstat()" e
"lstat()", consulte a documentação do seu sistema.

Alterado na versão 3.4: O módulo stat é apoiado por uma implementação
C.

O módulo "stat" define as seguintes funções para testar tipos de
arquivos específicos:

stat.S_ISDIR(mode)

   Retorna diferente de zero se o modo for de um diretório.

stat.S_ISCHR(mode)

   Retorna diferente de zero se o modo for de um arquivo de
   dispositivo especial de caractere.

stat.S_ISBLK(mode)

   Retorna diferente de zero se o modo for de um arquivo de
   dispositivo especial de bloco.

stat.S_ISREG(mode)

   Retorna diferente de zero se o modo for de um arquivo regular.

stat.S_ISFIFO(mode)

   Retorna diferente de zero se o modo for de um FIFO (encadeamento
   nomeado).

stat.S_ISLNK(mode)

   Retorna diferente de zero se o modo for de um link simbólico.

stat.S_ISSOCK(mode)

   Retorna diferente de zero se o modo for de um soquete.

stat.S_ISDOOR(mode)

   Retorna diferente de zero se o modo for de uma porta.

   Adicionado na versão 3.4.

stat.S_ISPORT(mode)

   Retorna diferente de zero se o modo for de uma porta de eventos.

   Adicionado na versão 3.4.

stat.S_ISWHT(mode)

   Retorna diferente de zero se o modo for de um apagamento.

   Adicionado na versão 3.4.

Duas funções adicionais são definidas para manipulação mais geral do
modo do arquivo:

stat.S_IMODE(mode)

   Retorna a parte do modo do arquivo que pode ser definido por
   "os.chmod()" --- ou seja, os bits de permissão do arquivo, mais os
   bits sticky bit, set-group-id e set-user-id (em sistemas que têm
   suporte a eles).

stat.S_IFMT(mode)

   Retorna a parte do modo do arquivo que descreve o tipo de arquivo
   (usado pelas funções "S_IS*()" acima).

Normalmente, você usaria as funções "os.path.is*()" para testar o tipo
de um arquivo; as funções aqui são úteis quando você está fazendo
vários testes do mesmo arquivo e deseja evitar a sobrecarga da chamada
de sistema "stat()" para cada teste. Eles também são úteis ao
verificar informações sobre um arquivo que não é manipulado por
"os.path", como os testes para dispositivos de blocos e caracteres.

Exemplo:

   import os, sys
   from stat import *

   def walktree(top, callback):
       '''desce recursivamente a árvore de diretórios com raiz no topo,
        chamando a função de retorno de chamada para cada arquivo regular'''

       for f in os.listdir(top):
           pathname = os.path.join(top, f)
           mode = os.lstat(pathname).st_mode
           if S_ISDIR(mode):
               # É um diretório, percorre recursivamente nele
               walktree(pathname, callback)
           elif S_ISREG(mode):
               # É um arquivo, chama a função de retorno
               callback(pathname)
           else:
               # Tipo de arquivo desconhecido, imprime uma mensagem
               print('Pulando %s' % pathname)

   def visitfile(file):
       print('visitando, file)

   if __name__ == '__main__':
       walktree(sys.argv[1], visitfile)

Uma função utilitária adicional é fornecida para converter o modo de
um arquivo em uma string legível por humanos:

stat.filemode(mode)

   Converte o modo de um arquivo em uma string no formato
   '-rwxrwxrwx'.

   Adicionado na versão 3.3.

   Alterado na versão 3.4: A função tem suporte a "S_IFDOOR",
   "S_IFPORT" e "S_IFWHT".

Todas as variáveis abaixo são simplesmente índices simbólicos nas 10
tuplas retornadas por "os.stat()", "os.fstat()" ou "os.lstat()".

stat.ST_MODE

   Modo de proteção de nó-i.

stat.ST_INO

   Número de nó-i.

stat.ST_DEV

   Nó-i em que o dispositivo reside.

stat.ST_NLINK

   Número de links para o nó-i.

stat.ST_UID

   O ID de usuário para o proprietário.

stat.ST_GID

   O ID de grupo para o proprietário.

stat.ST_SIZE

   Tamanho em bytes de um arquivo simples; quantidade de dados
   aguardando em alguns arquivos especiais.

stat.ST_ATIME

   Hora do último acesso.

stat.ST_MTIME

   Hora da última modificação.

stat.ST_CTIME

   O "ctime" conforme relatado pelo sistema operacional. Em alguns
   sistemas (como Unix) é o horário da última alteração de metadados
   e, em outros (como Windows), é o horário de criação (consulte a
   documentação da plataforma para obter detalhes).

A interpretação do “tamanho do arquivo” muda de acordo com o tipo de
arquivo. Para arquivos simples, este é o tamanho do arquivo em bytes.
Para FIFOs e soquetes na maioria dos tipos de Unix (incluindo Linux em
particular), o "tamanho" é o número de bytes aguardando para serem
lidos no momento da chamada para "os.stat()", "os.fstat()" ou
"os.lstat()"; isso às vezes pode ser útil, especialmente para
pesquisar um desses arquivos especiais após uma abertura sem bloqueio.
O significado do campo de tamanho para outros dispositivos de
caracteres e blocos varia mais, dependendo da implementação da chamada
de sistema subjacente.

As variáveis abaixo definem os sinalizadores utilizadas no campo
"ST_MODE".

O uso das funções acima é mais portátil do que o uso do primeiro
conjunto de sinalizadores:

stat.S_IFSOCK

   Soquete.

stat.S_IFLNK

   Link simbólico.

stat.S_IFREG

   Arquivo regular.

stat.S_IFBLK

   Dispositivo de bloco.

stat.S_IFDIR

   Diretório.

stat.S_IFCHR

   Dispositivo de caracteres.

stat.S_IFIFO

   FIFO.

stat.S_IFDOOR

   Porta.

   Adicionado na versão 3.4.

stat.S_IFPORT

   Porta de eventos.

   Adicionado na versão 3.4.

stat.S_IFWHT

   Apagamento.

   Adicionado na versão 3.4.

Nota:

  "S_IFDOOR", "S_IFPORT" ou "S_IFWHT" são definidos como 0 quando a
  plataforma não possui suporte para os tipos de arquivo.

Os seguintes sinalizadores também podem ser usados no argumento *mode*
de "os.chmod()":

stat.S_ISUID

   Define o bit de UID.

stat.S_ISGID

   Bit de set-group-ID. Este bit tem vários usos especiais. Para um
   diretório, indica que a semântica BSD deve ser usada para esse
   diretório: os arquivos criados lá herdam seu ID de grupo do
   diretório, não do ID de grupo efetivo do processo de criação, e os
   diretórios criados lá também receberão o conjunto de bits
   "S_ISGID". Para um arquivo que não possui o bit de execução de
   grupo ("S_IXGRP") definido, o bit de set-group-ID indica trava
   obrigatória de arquivo/registro (veja também "S_ENFMT").

stat.S_ISVTX

   Sticky bit. Quando este bit é definido em um diretório, significa
   que um arquivo nesse diretório pode ser renomeado ou excluído
   apenas pelo proprietário do arquivo, pelo proprietário do diretório
   ou por um processo privilegiado.

stat.S_IRWXU

   Máscara para permissões de proprietário de arquivo.

stat.S_IRUSR

   Proprietário tem permissão de leitura.

stat.S_IWUSR

   Proprietário tem permissão de escrita.

stat.S_IXUSR

   Proprietário tem permissão de execução.

stat.S_IRWXG

   Máscara para permissões de grupo.

stat.S_IRGRP

   Grupo tem permissão de leitura.

stat.S_IWGRP

   Grupo tem permissão de escrita.

stat.S_IXGRP

   Grupo tem permissão de execução.

stat.S_IRWXO

   Máscara para permissões para outros (não no grupo).

stat.S_IROTH

   Outros têm permissão de leitura.

stat.S_IWOTH

   Outros têm permissão de escrita.

stat.S_IXOTH

   Outros têm permissão de execução.

stat.S_ENFMT

   Aplicação de trava de arquivo do System V. Este sinalizador é
   compartilhada com "S_ISGID": a trava de arquivo/registro é aplicada
   em arquivos que não possuem o bit de execução de grupo ("S_IXGRP")
   definido.

stat.S_IREAD

   Sinônimo Unix V7 para "S_IRUSR".

stat.S_IWRITE

   Sinônimo Unix V7 para "S_IWUSR".

stat.S_IEXEC

   Sinônimo Unix V7 para "S_IXUSR".

Os seguintes sinalizadores podem ser usados no argumento *flags* de
"os.chflags()":

stat.UF_SETTABLE

   Todos os sinalizadores definíveis pelo usuário

   Adicionado na versão 3.13.

stat.UF_NODUMP

   Não despeja o arquivo.

stat.UF_IMMUTABLE

   O arquivo não pode ser alterado.

stat.UF_APPEND

   O arquivo só pode sofrer acréscimos.

stat.UF_OPAQUE

   O diretório é opaco quando visualizado por meio de uma pilha de
   união.

stat.UF_NOUNLINK

   O arquivo não pode ser renomeado ou excluído.

stat.UF_COMPRESSED

   O arquivo é armazenado compactado (macOS 10.6+).

stat.UF_TRACKED

   Usado para manipular IDs de documentos (macOS)

   Adicionado na versão 3.13.

stat.UF_DATAVAULT

   O arquivo precisa de direito para leitura ou gravação (macOS
   10.13+)

   Adicionado na versão 3.13.

stat.UF_HIDDEN

   O arquivo não deve ser exibido em uma GUI (macOS 10.5+).

stat.SF_SETTABLE

   Todos os sinalizadores mutáveis de superusuário

   Adicionado na versão 3.13.

stat.SF_SUPPORTED

   Todos os sinalizadores válidos de superusuário

   Disponibilidade: macOS

   Adicionado na versão 3.13.

stat.SF_SYNTHETIC

   Todos os sinalizadores sintéticos de somente leitura de
   superusuário

   Disponibilidade: macOS

   Adicionado na versão 3.13.

stat.SF_ARCHIVED

   O arquivo não pode ser arquivado.

stat.SF_IMMUTABLE

   O arquivo não pode ser alterado.

stat.SF_APPEND

   O arquivo só pode sofrer acréscimos.

stat.SF_RESTRICTED

   O arquivo precisa de um direito para ser escrito (macOS 10.13+)

   Adicionado na versão 3.13.

stat.SF_NOUNLINK

   O arquivo não pode ser renomeado ou excluído.

stat.SF_SNAPSHOT

   O arquivo é um arquivo de captura (snapshot).

stat.SF_FIRMLINK

   O arquivo é um firmlink (macOS 10.15+)

   Adicionado na versão 3.13.

stat.SF_DATALESS

   O arquivo é um objeto sem dados (macOS 10.15+)

   Adicionado na versão 3.13.

Consulte a página man dos sistemas *BSD ou macOS *chflags(2)* para
obter mais informações.

No Windows, as seguintes constantes de atributos de arquivo estão
disponíveis para uso ao testar bits no membro "st_file_attributes"
retornado por "os.stat()". Consulte a documentação da API do Windows
para obter mais detalhes sobre o significado dessas constantes.

stat.FILE_ATTRIBUTE_ARCHIVE
stat.FILE_ATTRIBUTE_COMPRESSED
stat.FILE_ATTRIBUTE_DEVICE
stat.FILE_ATTRIBUTE_DIRECTORY
stat.FILE_ATTRIBUTE_ENCRYPTED
stat.FILE_ATTRIBUTE_HIDDEN
stat.FILE_ATTRIBUTE_INTEGRITY_STREAM
stat.FILE_ATTRIBUTE_NORMAL
stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED
stat.FILE_ATTRIBUTE_NO_SCRUB_DATA
stat.FILE_ATTRIBUTE_OFFLINE
stat.FILE_ATTRIBUTE_READONLY
stat.FILE_ATTRIBUTE_REPARSE_POINT
stat.FILE_ATTRIBUTE_SPARSE_FILE
stat.FILE_ATTRIBUTE_SYSTEM
stat.FILE_ATTRIBUTE_TEMPORARY
stat.FILE_ATTRIBUTE_VIRTUAL

   Adicionado na versão 3.5.

No Windows, as seguintes constantes estão disponíveis para comparação
com o membro "st_reparse_tag" retornado por "os.lstat()". Estas são
constantes bem conhecidas, mas não são uma lista exaustiva.

stat.IO_REPARSE_TAG_SYMLINK
stat.IO_REPARSE_TAG_MOUNT_POINT
stat.IO_REPARSE_TAG_APPEXECLINK

   Adicionado na versão 3.8.

No Linux, as seguintes constantes de atributo de arquivo estão
disponíveis para uso ao testar bits nos membros "stx_attributes" e
"stx_attributes_mask" retornados por "os.statx()". Consulte a página
man *statx(2)* para obter mais detalhes sobre o significado dessas
constantes.

stat.STATX_ATTR_COMPRESSED
stat.STATX_ATTR_IMMUTABLE
stat.STATX_ATTR_APPEND
stat.STATX_ATTR_NODUMP
stat.STATX_ATTR_ENCRYPTED
stat.STATX_ATTR_AUTOMOUNT
stat.STATX_ATTR_MOUNT_ROOT
stat.STATX_ATTR_VERITY
stat.STATX_ATTR_DAX
stat.STATX_ATTR_WRITE_ATOMIC

   Adicionado na versão 3.15.
