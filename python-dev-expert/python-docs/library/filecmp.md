"filecmp" --- Comparações de arquivos e diretórios
**************************************************

**Código-fonte:** Lib/filecmp.py

======================================================================

O módulo "filecmp" define funções para comparar arquivos e diretórios,
com várias compensações opcionais de tempo/correção. Para comparar
arquivos, veja também o módulo "difflib".

O módulo "filecmp" define as seguintes funções:

filecmp.cmp(f1, f2, shallow=True)

   Compara os arquivos chamados *f1* e *f2*, retornando "True" se eles
   parecerem iguais, "False" caso contrário.

   Se *shallow* for verdadeiro e as assinaturas de "os.stat()" (tipo
   de arquivo, tamanho e hora de modificação) de ambos os arquivos
   forem idênticas, os arquivos serão considerados iguais.

   Caso contrário, os arquivos serão tratados como diferentes se seus
   tamanhos ou conteúdos forem diferentes.

   Observe que nenhum programa externo é chamado a partir desta
   função, o que lhe confere portabilidade e eficiência.

   Esta função usa um cache para comparações passadas e os resultados,
   com entradas de cache invalidadas se as informações de "os.stat()"
   para o arquivo mudarem. O cache inteiro pode ser limpo usando
   "clear_cache()".

filecmp.cmpfiles(a, b, common, shallow=True)

   Compara os arquivos nos dois diretórios *a* e *b* cujos nomes são
   dados por *common*.

   Retorna três listas de nomes de arquivos: *match*, *mismatch*,
   *errors*. *match* contém a lista de arquivos que correspondem,
   *mismatch* contém os nomes daqueles que não correspondem e *errors*
   lista os nomes dos arquivos que não puderam ser comparados. Os
   arquivos são listados em *errors* se não existirem em um dos
   diretórios, o usuário não tiver permissão para lê-los ou se a
   comparação não puder ser feita por algum outro motivo.

   O parâmetro *shallow* tem o mesmo significado e valor padrão que
   "filecmp.cmp()".

   Por exemplo, "cmpfiles('a', 'b', ['c', 'd/e'])" comparará "a/c" com
   "b/c" e "a/d/e" com "b/d/e". "'c'" e "'d/e'" estarão cada um em uma
   das três listas retornadas.

filecmp.clear_cache()

   Limpa o cache do filecmp. Isso pode ser útil se um arquivo for
   comparado tão rapidamente após ser modificado que ele esteja dentro
   da resolução de mtime do sistema de arquivos subjacente.

   Adicionado na versão 3.4.


A classe "dircmp"
=================

class filecmp.dircmp(a, b, ignore=None, hide=None, *, shallow=True)

   Constrói um novo objeto de comparação de diretórios para comparar
   os diretórios *a* e *b*. *ignore* é uma lista de nomes a serem
   ignorados e o padrão é "filecmp.DEFAULT_IGNORES". *hide* é uma
   lista de nomes a serem ocultados e o padrão é "[os.curdir,
   os.pardir]".

   A classe "dircmp" compara arquivos fazendo comparações rasas, isto
   é, *shallow* conforme descrito para "filecmp.cmp()" por padrão
   usando o parâmetro *shallow*.

   Alterado na versão 3.13: Adicionado o parâmetro *shallow*.

   A classe "dircmp" fornece os seguintes métodos:

   report()

      Exibe (para "sys.stdout") uma comparação entre *a* e *b*.

   report_partial_closure()

      Exibe uma comparação entre *a* e *b* e subdiretórios imediatos
      comuns.

   report_full_closure()

      Exibe uma comparação entre *a* e *b* e subdiretórios comuns
      (recursivamente).

   A classe "dircmp" oferece uma série de atributos interessantes que
   podem ser usados para obter várias informações sobre as árvores de
   diretórios que estão sendo comparadas.

   Observe que, por meio dos ganchos "__getattr__()", todos os
   atributos são computados preguiçosamente, portanto, não há perda de
   velocidade se apenas os atributos que são leves para computar forem
   usados.

   left

      O diretório *a*.

   right

      O diretório *b*.

   left_list

      Arquivos e subdiretórios em *a*, filtrados por *hide* e
      *ignore*.

   right_list

      Arquivos e subdiretórios em *b*, filtrados por *hide* e
      *ignore*.

   common

      Arquivos e subdiretórios em *a* e *b*.

   left_only

      Arquivos e subdiretórios em apenas *a*.

   right_only

      Arquivos e subdiretórios em apenas *b*.

   common_dirs

      Subdiretórios em *a* e *b*.

   common_files

      Arquivos em *a* e *b*.

   common_funny

      Nomes em *a* e *b*, de modo que o tipo difere entre os
      diretórios, ou nomes para os quais "os.stat()" relata um erro.

   same_files

      Arquivos que são idênticos em *a* e *b*, usando o operador de
      comparação de arquivos da classe.

   diff_files

      Arquivos que estão em *a* e *b*, cujos conteúdos diferem de
      acordo com o operador de comparação de arquivos da classe.

   funny_files

      Arquivos que estão em *a* e *b*, mas não puderam ser comparados.

   subdirs

      Um dicionário que mapeia nomes em "common_dirs" para instâncias
      "dircmp" (ou instâncias MyDirCmp se esta instância for do tipo
      MyDirCmp, uma subclasse de "dircmp").

      Alterado na versão 3.10: Anteriormente, as entradas eram sempre
      instâncias de "dircmp". Agora, as entradas são do mesmo tipo que
      *self*, se *self* for uma subclasse de "dircmp".

filecmp.DEFAULT_IGNORES

   Adicionado na versão 3.4.

   Lista de diretórios ignorados por "dircmp" por padrão.

Aqui está um exemplo simplificado do uso do atributo "subdirs" para
pesquisar recursivamente em dois diretórios para mostrar arquivos
diferentes em comum:

   >>> from filecmp import dircmp
   >>> def print_diff_files(dcmp):
   ...     for name in dcmp.diff_files:
   ...         print("diff_file %s found in %s and %s" % (name, dcmp.left,
   ...               dcmp.right))
   ...     for sub_dcmp in dcmp.subdirs.values():
   ...         print_diff_files(sub_dcmp)
   ...
   >>> dcmp = dircmp('dir1', 'dir2')
   >>> print_diff_files(dcmp)
