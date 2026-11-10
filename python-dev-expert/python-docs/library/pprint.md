"pprint" --- Impressão bonita de dados
**************************************

**Código-fonte:** Lib/pprint.py

======================================================================

O módulo "pprint" fornece a capacidade de "imprimir de forma bonita"
estruturas de dados Python arbitrárias em um formato que pode ser
usado como entrada para o interpretador. Se as estruturas formatadas
incluírem objetos que não sejam tipos fundamentais do Python, a
representação poderá não ser carregável. Este pode ser o caso se
objetos como arquivos, soquetes ou classes forem incluídos, bem como
muitos outros objetos que não são representáveis como literais do
Python.

A representação formatada mantém os objetos em uma única linha, se
possível, e os divide em múltiplas linhas se eles não couberem na
largura permitida, ajustável pelo parâmetro *width* padrão para 80
caracteres.

Alterado na versão 3.9: Adicionado suporte para impressão bonita de
"types.SimpleNamespace".

Alterado na versão 3.10: Adicionado suporte para impressão bonita de
"dataclasses.dataclass".


Funções
=======

pprint.pp(object, stream=None, indent=1, width=80, depth=None, *, compact=False, expand=False, sort_dicts=False, underscore_numbers=False)

   Imprime a representação formatada de *object*, seguida por uma nova
   linha. Esta função pode ser usado no interpretador interativo em
   vez da função "print()" para inspecionar valores. Dica: você pode
   reatribuir "print = pprint.pp" para uso dentro de um escopo.

   Parâmetros:
      * **object** -- O objeto a ser impresso.

      * **stream** (*file-like object* | None) -- Um objeto arquivo ou
        similar no qual a saída será gravada chamando seu método
        "write()". Se "None" (o padrão), "sys.stdout" será usado.

      * **indent** (*int*) -- A quantidade de indentação adicionado
        para cada nível de aninhamento.

      * **width** (*int*) -- O número máximo desejado de caracteres
        por linha na saída. Se uma estrutura não puder ser formatada
        dentro da restrição de largura, será feito o melhor esforço.

      * **depth** (*int** | **None*) -- O número de níveis de
        aninhamento que podem ser impressos. Se a estrutura de dados
        que está sendo impressa for muito profunda, o próximo nível
        contido será substituído por "...". Se "None" (o padrão), não
        há restrição na profundidade dos objetos que estão sendo
        formatados.

      * **compact** (*bool*) -- Control the way long *sequences* are
        formatted. If "False" (the default), each item of a sequence
        will be formatted on a separate line, otherwise as many items
        as will fit within the *width* will be formatted on each
        output line. Incompatible with *expand*.

      * **expand** (*bool*) -- If "True", opening parentheses and
        brackets will be followed by a newline and the following
        content will be indented by one level, similar to pretty-
        printed JSON. Incompatible with *compact*.

      * **sort_dicts** (*bool*) -- Se "True", os dicionários serão
        formatados com suas chaves classificadas, caso contrário,
        serão exibidos na ordem de inserção (o padrão).

      * **underscore_numbers** (*bool*) -- Se "True", os números
        inteiros serão formatados com o caractere "_" para um
        separador de milhares, caso contrário, os sublinhados não
        serão exibidos (o padrão).

   >>> import pprint
   >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
   >>> stuff.insert(0, stuff)
   >>> pprint.pp(stuff)
   [<Recursion on list with id=...>,
    'spam',
    'eggs',
    'lumberjack',
    'knights',
    'ni']

   Adicionado na versão 3.8.

   Alterado na versão 3.10: Adicionado o parâmetro
   *underscore_numbers*.

   Alterado na versão 3.11: Não tenta mais escrever em "sys.stdout" se
   for "None".

   Alterado na versão 3.15: Added the *expand* parameter.

pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, expand=False, sort_dicts=True, underscore_numbers=False)

   Apelido para "pp()" com *sort_dicts* definido como "True" por
   padrão, o que classificaria automaticamente as chaves dos
   dicionários, você pode querer usar "pp()" em vez disso, onde é
   "False" por padrão.

pprint.pformat(object, indent=1, width=80, depth=None, *, compact=False, expand=False, sort_dicts=True, underscore_numbers=False)

   Return the formatted representation of *object* as a string.
   *indent*, *width*, *depth*, *compact*, *expand*, *sort_dicts* and
   *underscore_numbers* are passed to the "PrettyPrinter" constructor
   as formatting parameters and their meanings are as described in the
   documentation above.

pprint.isreadable(object)

   Determina se a representação formatada de *object* é "legível" ou
   pode ser usada para reconstruir o valor usando "eval()". Isso
   sempre retorna "False" para objetos recursivos.

   >>> pprint.isreadable(stuff)
   False

pprint.isrecursive(object)

   Determina se *object* requer uma representação recursiva. Esta
   função está sujeita às mesmas limitações mencionadas em
   "saferepr()" abaixo e pode levantar uma exceção "RecursionError" se
   falhar em detectar um objeto recursivo.

pprint.saferepr(object)

   Retorna uma representação de string de *object*, protegida contra
   recursão em algumas estruturas de dados comuns, nomeadamente
   instâncias de "dict", "list" e "tuple" ou subclasses cujo
   "__repr__" não foi substituído. Se a representação do objeto expõe
   uma entrada recursiva, a referência recursiva será representada
   como "<Recursion on typename with id=number>". A representação não
   é formatada de outra forma.

   >>> pprint.saferepr(stuff)
   "[<Recursion on list with id=...>, 'spam', 'eggs', 'lumberjack', 'knights', 'ni']"


Objetos PrettyPrinter
=====================

class pprint.PrettyPrinter(indent=1, width=80, depth=None, stream=None, *, compact=False, expand=False, sort_dicts=True, underscore_numbers=False)

   Constrói uma instância "PrettyPrinter".

   Os argumentos têm o mesmo significado que para "pp()". Observe que
   eles estão em uma ordem diferente e que o padrão *sort_dicts* é
   "True".

   >>> import pprint
   >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
   >>> stuff.insert(0, stuff[:])
   >>> pp = pprint.PrettyPrinter(indent=4)
   >>> pp.pprint(stuff)
   [   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
       'spam',
       'eggs',
       'lumberjack',
       'knights',
       'ni']
   >>> pp = pprint.PrettyPrinter(width=41, compact=True)
   >>> pp.pprint(stuff)
   [['spam', 'eggs', 'lumberjack',
     'knights', 'ni'],
    'spam', 'eggs', 'lumberjack', 'knights',
    'ni']
   >>> pp = pprint.PrettyPrinter(width=41, expand=True, indent=3)
   >>> pp.pprint(stuff)
   [
      [
         'spam',
         'eggs',
         'lumberjack',
         'knights',
         'ni',
      ],
      'spam',
      'eggs',
      'lumberjack',
      'knights',
      'ni',
   ]
   >>> tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
   ... ('parrot', ('fresh fruit',))))))))
   >>> pp = pprint.PrettyPrinter(depth=6)
   >>> pp.pprint(tup)
   ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))

   Alterado na versão 3.4: Adicionado o parâmetro *compact*.

   Alterado na versão 3.8: Adicionado o parâmetro *sort_dicts*.

   Alterado na versão 3.10: Adicionado o parâmetro
   *underscore_numbers*.

   Alterado na versão 3.11: Não tenta mais escrever em "sys.stdout" se
   for "None".

   Alterado na versão 3.15: Added the *expand* parameter.

Instâncias "PrettyPrinter" contêm os seguintes métodos:

PrettyPrinter.pformat(object)

   Retorna a representação formatada de *object*. Isso leva em
   consideração as opções passadas para o construtor "PrettyPrinter".

PrettyPrinter.pprint(object)

   Exibe a representação formatada de *object* no fluxo configurado,
   seguida por uma nova linha.

Os métodos a seguir fornecem as implementações para as funções
correspondentes com os mesmos nomes. Usar esses métodos em uma
instância é um pouco mais eficiente já que novos objetos
"PrettyPrinter" não precisam ser criados.

PrettyPrinter.isreadable(object)

   Determina se a representação formatada do objeto é "legível" ou
   pode ser usada para reconstruir o valor usando "eval()". Observe
   que isso retorna "False" para objetos recursivos. Se o parâmetro
   *depth* de "PrettyPrinter" estiver definido e o objeto for mais
   profundo que o permitido, isso retornará "False".

PrettyPrinter.isrecursive(object)

   Determina se o objeto requer uma representação recursiva.

Este método é fornecido como um gancho para permitir que as subclasses
modifiquem a maneira como os objetos são convertidos em strings.  A
implementação padrão usa os componentes internos da implementação de
"saferepr()".

PrettyPrinter.format(object, context, maxlevels, level)

   Retorna três valores: a versão formatada de *object* como uma
   string, um sinalizador indicando se o resultado é legível e um
   sinalizador indicando se a recursão foi detectada.  O primeiro
   argumento é o objeto a ser apresentado.  O segundo é um dicionário
   que contém o "id()" de objetos que fazem parte do contexto de
   apresentação atual (contêineres diretos e indiretos para *objects*
   que estão afetando a apresentação) como chaves; se for necessário
   apresentar um objeto que já esteja representado em *context*, o
   terceiro valor de retorno deverá ser "True".  Chamadas recursivas
   ao método "format()" devem adicionar entradas adicionais para
   contêineres neste dicionário.  O terceiro argumento, *maxlevels*,
   fornece o limite solicitado para recursão;  será "0" se não houver
   limite solicitado.  Este argumento deve ser passado sem
   modificações para chamadas recursivas. O quarto argumento, *level*,
   fornece o nível atual; chamadas recursivas devem receber um valor
   menor que o da chamada atual.


Exemplo
=======

Para demonstrar vários usos da função "pp()" e seus parâmetros, vamos
buscar informações sobre um projeto no PyPI:

   >>> import json
   >>> import pprint
   >>> from urllib.request import urlopen
   >>> with urlopen('https://pypi.org/pypi/sampleproject/1.2.0/json') as resp:
   ...     project_info = json.load(resp)['info']

Em sua forma básica, "pp()" mostra o objeto inteiro:

   >>> pprint.pp(project_info)
   {'author': 'The Python Packaging Authority',
    'author_email': 'pypa-dev@googlegroups.com',
    'bugtrack_url': None,
    'classifiers': ['Development Status :: 3 - Alpha',
                    'Intended Audience :: Developers',
                    'License :: OSI Approved :: MIT License',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.6',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.2',
                    'Programming Language :: Python :: 3.3',
                    'Programming Language :: Python :: 3.4',
                    'Topic :: Software Development :: Build Tools'],
    'description': 'A sample Python project\n'
                   '=======================\n'
                   '\n'
                   'This is the description file for the project.\n'
                   '\n'
                   'The file should use UTF-8 encoding and be written using '
                   'ReStructured Text. It\n'
                   'will be used to generate the project webpage on PyPI, and '
                   'should be written for\n'
                   'that purpose.\n'
                   '\n'
                   'Typical contents for this file would include an overview of '
                   'the project, basic\n'
                   'usage examples, etc. Generally, including the project '
                   'changelog in here is not\n'
                   'a good idea, although a simple "What\'s New" section for the '
                   'most recent version\n'
                   'may be appropriate.',
    'description_content_type': None,
    'docs_url': None,
    'download_url': 'UNKNOWN',
    'downloads': {'last_day': -1, 'last_month': -1, 'last_week': -1},
    'home_page': 'https://github.com/pypa/sampleproject',
    'keywords': 'sample setuptools development',
    'license': 'MIT',
    'maintainer': None,
    'maintainer_email': None,
    'name': 'sampleproject',
    'package_url': 'https://pypi.org/project/sampleproject/',
    'platform': 'UNKNOWN',
    'project_url': 'https://pypi.org/project/sampleproject/',
    'project_urls': {'Download': 'UNKNOWN',
                     'Homepage': 'https://github.com/pypa/sampleproject'},
    'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
    'requires_dist': None,
    'requires_python': None,
    'summary': 'A sample Python project',
    'version': '1.2.0'}

O resultado pode ser limitado a uma certa *depth* (reticências são
usadas para conteúdos mais profundos):

   >>> pprint.pp(project_info, depth=1)
   {'author': 'The Python Packaging Authority',
    'author_email': 'pypa-dev@googlegroups.com',
    'bugtrack_url': None,
    'classifiers': [...],
    'description': 'A sample Python project\n'
                   '=======================\n'
                   '\n'
                   'This is the description file for the project.\n'
                   '\n'
                   'The file should use UTF-8 encoding and be written using '
                   'ReStructured Text. It\n'
                   'will be used to generate the project webpage on PyPI, and '
                   'should be written for\n'
                   'that purpose.\n'
                   '\n'
                   'Typical contents for this file would include an overview of '
                   'the project, basic\n'
                   'usage examples, etc. Generally, including the project '
                   'changelog in here is not\n'
                   'a good idea, although a simple "What\'s New" section for the '
                   'most recent version\n'
                   'may be appropriate.',
    'description_content_type': None,
    'docs_url': None,
    'download_url': 'UNKNOWN',
    'downloads': {...},
    'home_page': 'https://github.com/pypa/sampleproject',
    'keywords': 'sample setuptools development',
    'license': 'MIT',
    'maintainer': None,
    'maintainer_email': None,
    'name': 'sampleproject',
    'package_url': 'https://pypi.org/project/sampleproject/',
    'platform': 'UNKNOWN',
    'project_url': 'https://pypi.org/project/sampleproject/',
    'project_urls': {...},
    'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
    'requires_dist': None,
    'requires_python': None,
    'summary': 'A sample Python project',
    'version': '1.2.0'}

Além disso, a largura *width* máxima do caractere pode ser sugerida.
Se um objeto longo não puder ser dividido, a largura especificada será
excedida:

   >>> pprint.pp(project_info, depth=1, width=60)
   {'author': 'The Python Packaging Authority',
    'author_email': 'pypa-dev@googlegroups.com',
    'bugtrack_url': None,
    'classifiers': [...],
    'description': 'A sample Python project\n'
                   '=======================\n'
                   '\n'
                   'This is the description file for the '
                   'project.\n'
                   '\n'
                   'The file should use UTF-8 encoding and be '
                   'written using ReStructured Text. It\n'
                   'will be used to generate the project '
                   'webpage on PyPI, and should be written '
                   'for\n'
                   'that purpose.\n'
                   '\n'
                   'Typical contents for this file would '
                   'include an overview of the project, '
                   'basic\n'
                   'usage examples, etc. Generally, including '
                   'the project changelog in here is not\n'
                   'a good idea, although a simple "What\'s '
                   'New" section for the most recent version\n'
                   'may be appropriate.',
    'description_content_type': None,
    'docs_url': None,
    'download_url': 'UNKNOWN',
    'downloads': {...},
    'home_page': 'https://github.com/pypa/sampleproject',
    'keywords': 'sample setuptools development',
    'license': 'MIT',
    'maintainer': None,
    'maintainer_email': None,
    'name': 'sampleproject',
    'package_url': 'https://pypi.org/project/sampleproject/',
    'platform': 'UNKNOWN',
    'project_url': 'https://pypi.org/project/sampleproject/',
    'project_urls': {...},
    'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
    'requires_dist': None,
    'requires_python': None,
    'summary': 'A sample Python project',
    'version': '1.2.0'}

Lastly, we can format like pretty-printed JSON with the *expand*
parameter. Best results are achieved with a higher *indent* value:

   >>> pprint.pp(project_info, indent=4, expand=True)
   {
      'author': 'The Python Packaging Authority',
      'author_email': 'pypa-dev@googlegroups.com',
      'bugtrack_url': None,
      'classifiers': [
         'Development Status :: 3 - Alpha',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: MIT License',
         'Programming Language :: Python :: 2',
         'Programming Language :: Python :: 2.6',
         'Programming Language :: Python :: 2.7',
         'Programming Language :: Python :: 3',
         'Programming Language :: Python :: 3.2',
         'Programming Language :: Python :: 3.3',
         'Programming Language :: Python :: 3.4',
         'Topic :: Software Development :: Build Tools',
      ],
      'description': 'A sample Python project\n'
      '=======================\n'
      '\n'
      'This is the description file for the project.\n'
      '\n'
      'The file should use UTF-8 encoding and be written using ReStructured '
      'Text. It\n'
      'will be used to generate the project webpage on PyPI, and should be '
      'written for\n'
      'that purpose.\n'
      '\n'
      'Typical contents for this file would include an overview of the project, '
      'basic\n'
      'usage examples, etc. Generally, including the project changelog in here '
      'is not\n'
      'a good idea, although a simple "What\'s New" section for the most recent '
      'version\n'
      'may be appropriate.',
      'description_content_type': None,
      'docs_url': None,
      'download_url': 'UNKNOWN',
      'downloads': {'last_day': -1, 'last_month': -1, 'last_week': -1},
      'dynamic': None,
      'home_page': 'https://github.com/pypa/sampleproject',
      'keywords': 'sample setuptools development',
      'license': 'MIT',
      'license_expression': None,
      'license_files': None,
      'maintainer': None,
      'maintainer_email': None,
      'name': 'sampleproject',
      'package_url': 'https://pypi.org/project/sampleproject/',
      'platform': 'UNKNOWN',
      'project_url': 'https://pypi.org/project/sampleproject/',
      'project_urls': {
         'Download': 'UNKNOWN',
         'Homepage': 'https://github.com/pypa/sampleproject',
      },
      'provides_extra': None,
      'release_url': 'https://pypi.org/project/sampleproject/1.2.0/',
      'requires_dist': None,
      'requires_python': None,
      'summary': 'A sample Python project',
      'version': '1.2.0',
      'yanked': False,
      'yanked_reason': None,
   }
