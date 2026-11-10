"getopt" --- Analisador sintático no estilo C para opções de linha de comando
*****************************************************************************

**Código-fonte:** Lib/getopt.py

Nota:

  Este módulo é considerado completo em recursos. Uma alternativa mais
  declarativa e extensível para esta API é fornecida no módulo
  "optparse". Outros aprimoramentos funcionais para processamento de
  parâmetros de linha de comando são fornecidos como módulos de
  terceiros no PyPI ou como recursos no módulo "argparse".

======================================================================

Este módulo ajuda os scripts a analisar os argumentos da linha de
comando em "sys.argv". Ele suporta as mesmas convenções da função Unix
"getopt()" (incluindo os significados especiais de argumentos da forma
'"-"' e '"--"'). Longas opções semelhantes às suportadas pelo software
GNU também podem ser usadas por meio de um terceiro argumento
opcional.

Usuários que não estão familiarizados com a função Unix "getopt()"
devem considerar usar o módulo "argparse" em vez disso. Usuários que
estão familiarizados com a função Unix "getopt()", mas gostariam de
obter um comportamento equivalente enquanto escrevem menos código e
obtêm melhor ajuda e mensagens de erro devem considerar usar o módulo
"optparse". Veja Escolhendo uma biblioteca de análise de linha de
comando para detalhes adicionais.

Este módulo fornece duas funções e uma exceção:

getopt.getopt(args, shortopts, longopts=[])

   Analisa opções de linha de comando e lista de parâmetros. *args* é
   a lista de argumentos a ser analisada, sem a referência inicial
   para o programa em execução. Normalmente, isso significa
   "sys.argv[1:]". *shortopts* é a string de letras de opção que o
   script deseja reconhecer, com opções que requerem um argumento
   seguido por dois pontos ("':'") e opções que aceitam o argumento
   opcional seguido por dois caracteres de dois pontos ("'::'"); ou
   seja, o mesmo formato que Unix "getopt()" usa.

   Nota:

     Ao contrário do GNU "getopt()", após um argumento sem opção,
     todos os argumentos adicionais são considerados também sem opção.
     Isso é semelhante à maneira como os sistemas Unix não GNU
     funcionam.

   *longopts*, se especificado, deve ser uma lista de strings com os
   nomes das opções longas que devem ser suportadas. Os caracteres
   "'--'" no início não devem ser incluídos no nome da opção. Opções
   longas que requerem um argumento devem ser seguidas por um sinal de
   igual ("'='"). Opções longas que aceitam um argumento opcional
   devem ser seguidas por um sinal de igualdade e ponto de
   interrogação ("'=?'"). Para aceitar apenas opções longas,
   *shortopts* deve ser uma string vazia. Opções longas na linha de
   comando podem ser reconhecidas, desde que forneçam um prefixo do
   nome da opção que corresponda exatamente a uma das opções aceitas.
   Por exemplo, se *longopts* for "['foo', 'frob']", a opção "--fo"
   irá corresponder a "--foo", mas "--f" não corresponderá
   exclusivamente, então "GetoptError" será levantada.

   Se *longopts* for uma string, ela é tratada como uma lista de um
   único elemento.

   O valor de retorno consiste em dois elementos: o primeiro é uma
   lista de pares "(option, value)"; a segunda é a lista de argumentos
   de programa restantes depois que a lista de opções foi removida
   (esta é uma fatia ao final de *args*). Cada par de opção e valor
   retornado tem a opção como seu primeiro elemento, prefixado com um
   hífen para opções curtas (por exemplo, "'-x'") ou dois hifenes para
   opções longas (por exemplo, "'--long-option'"), e o argumento da
   opção como seu segundo elemento, ou uma string vazia se a opção não
   tiver argumento. As opções ocorrem na lista na mesma ordem em que
   foram encontradas, permitindo assim múltiplas ocorrências. Opções
   longas e curtas podem ser misturadas.

   Alterado na versão 3.14: Argumentos opcionais são suportados.

getopt.gnu_getopt(args, shortopts, longopts=[])

   This function works like "getopt()", except that GNU style scanning
   mode is used by default. This means that option and non-option
   arguments may be intermixed. The "getopt()" function stops
   processing options as soon as a non-option argument is encountered.

   Se o primeiro caractere da string de opção for "'+'", ou se a
   variável de ambiente "POSIXLY_CORRECT" estiver definida, então o
   processamento da opção para assim que um argumento não opcional for
   encontrado.

   Se o primeiro caractere da string de opção for "'-'", argumentos
   não opcionais seguidos por opções serão adicionados à lista de
   pares opção-valor como um par que tem "None" como primeiro elemento
   e a lista de argumentos não opcionais como segundo elemento. O
   segundo elemento do resultado "gnu_getopt()" é uma lista de
   argumentos do programa após a última opção.

   Alterado na versão 3.14: Suporte para retornar opções misturadas e
   argumentos não opcionais em ordem.

exception getopt.GetoptError

   Isso é levantado quando uma opção não reconhecida é encontrada na
   lista de argumentos ou quando uma opção que requer um argumento não
   é fornecida. O argumento para a exceção é uma string que indica a
   causa do erro. Para opções longas, um argumento dado a uma opção
   que não requer uma também fará com que essa exceção seja levantada.
   Os atributos "msg" e "opt" fornecem a mensagem de erro e a opção
   relacionada; se não houver uma opção específica à qual a exceção se
   relaciona, "opt" é uma string vazia.

exception getopt.error

   Apelido para "GetoptError"; para compatibilidade reversa.

Um exemplo usando apenas opções de estilo Unix:

   >>> import getopt
   >>> args = '-a -b -cfoo -d bar a1 a2'.split()
   >>> args
   ['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']
   >>> optlist, args = getopt.getopt(args, 'abc:d:')
   >>> optlist
   [('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', 'bar')]
   >>> args
   ['a1', 'a2']

Usar nomes de opções longos é igualmente fácil:

   >>> s = '--condition=foo --testing --output-file abc.def -x a1 a2'
   >>> args = s.split()
   >>> args
   ['--condition=foo', '--testing', '--output-file', 'abc.def', '-x', 'a1', 'a2']
   >>> optlist, args = getopt.getopt(args, 'x', [
   ...     'condition=', 'output-file=', 'testing'])
   >>> optlist
   [('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x', '')]
   >>> args
   ['a1', 'a2']

Argumentos opcionais devem ser especificados explicitamente:

   >>> s = '-Con -C --color=off --color a1 a2'
   >>> args = s.split()
   >>> args
   ['-Con', '-C', '--color=off', '--color', 'a1', 'a2']
   >>> optlist, args = getopt.getopt(args, 'C::', ['color=?'])
   >>> optlist
   [('-C', 'on'), ('-C', ''), ('--color', 'off'), ('--color', '')]
   >>> args
   ['a1', 'a2']

A ordem dos argumentos opcionais e não opcionais pode ser preservada:

   >>> s = 'a1 -x a2 a3 a4 --long a5 a6'
   >>> args = s.split()
   >>> args
   ['a1', '-x', 'a2', 'a3', 'a4', '--long', 'a5', 'a6']
   >>> optlist, args = getopt.gnu_getopt(args, '-x:', ['long='])
   >>> optlist
   [(None, ['a1']), ('-x', 'a2'), (None, ['a3', 'a4']), ('--long', 'a5')]
   >>> args
   ['a6']

Em um script, o uso típico é algo assim:

   import getopt, sys

   def main():
       try:
           opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
       except getopt.GetoptError as err:
           # print help information and exit:
           print(err)  # will print something like "option -a not recognized"
           usage()
           sys.exit(2)
       output = None
       verbose = False
       for o, a in opts:
           if o == "-v":
               verbose = True
           elif o in ("-h", "--help"):
               usage()
               sys.exit()
           elif o in ("-o", "--output"):
               output = a
           else:
               assert False, "unhandled option"
       process(args, output=output, verbose=verbose)

   if __name__ == "__main__":
       main()

Observe que uma interface de linha de comando equivalente pode ser
produzida com menos código e mais mensagens de erro de ajuda e erro
informativas usando o módulo "optparse":

   import optparse

   if __name__ == '__main__':
       parser = optparse.OptionParser()
       parser.add_option('-o', '--output')
       parser.add_option('-v', dest='verbose', action='store_true')
       opts, args = parser.parse_args()
       process(args, output=opts.output, verbose=opts.verbose)

Uma interface de linha de comando aproximadamente equivalente para
este caso também pode ser produzida usando o módulo "argparse":

   import argparse

   if __name__ == '__main__':
       parser = argparse.ArgumentParser()
       parser.add_argument('-o', '--output')
       parser.add_argument('-v', dest='verbose', action='store_true')
       parser.add_argument('rest', nargs='*')
       args = parser.parse_args()
       process(args.rest, output=args.output, verbose=args.verbose)

Veja Escolhendo uma biblioteca de análise de linha de comando para
detalhes sobre como a versão "argparse" deste código difere em
comportamento da versão "optparse" (e "getopt").

Ver também:

  Módulo "optparse"
     Análise de opções de linha de comando declarativa.

  Módulo "argparse"
     Opção de linha de comando e biblioteca de análise de argumentos
     mais opinativa.
