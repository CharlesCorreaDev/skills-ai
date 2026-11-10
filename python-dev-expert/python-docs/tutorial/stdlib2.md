11. Um breve passeio pela biblioteca padrão --- parte II
********************************************************

Este segundo passeio apresenta alguns módulos avançados que atendem
necessidades de programação profissional. Estes módulos raramente
aparecem em scripts pequenos.


11.1. Formatando a saída
========================

O módulo "reprlib" fornece uma versão de "repr()" personalizado para
exibições abreviadas de contêineres grandes ou profundamente
aninhados:

   >>> import reprlib
   >>> reprlib.repr(set('supercalifragilisticexpialidoce'))
   "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

O módulo "pprint" oferece um controle mais sofisticado na exibição
tanto de objetos embutidos quanto aqueles criados pelo usuário de
maneira que fique legível para o interpretador. Quando o resultado é
maior que uma linha, o "pretty printer" acrescenta quebras de linha e
indentação para revelar as estruturas de maneira mais clara:

   >>> import pprint
   >>> t = [[[['preto', 'ciano'], 'branco', ['verde', 'vermelho']], [['magenta',
   ...     'amarelo'], 'azul']]]
   >>>
   >>> pprint.pprint(t, width=30)
   [[[['preto', 'ciano'],
      'branco',
      ['verde', 'vermelho']],
     [['magenta', 'amarelo'],
      'azul']]]

O módulo "textwrap" formata parágrafos de texto para que caibam em uma
dada largura de tela:

   >>> import textwrap
   >>> doc = """O método wrap() é como fill(), exceto que ele retorna
   ... uma lista de strings em vez de uma string grande com quebras
   ... de linha para separar as linhas quebradas."""
   ...
   >>> print(textwrap.fill(doc, width=40))
   O método wrap() é como fill(), exceto
   que ele retorna uma lista de strings em
   vez de uma string grande com quebras de
   linha para separar as linhas quebradas.

O módulo "locale" acessa uma base de dados de formatos específicos a
determinada cultura. O atributo de agrupamento da função "format"
oferece uma forma direta de formatar números com separadores de grupo:

   >>> import locale
   >>> locale.setlocale(locale.LC_ALL, 'English_United States.1252')
   'English_United States.1252'
   >>> conv = locale.localeconv()          # obtém mapeamento de convenções
   >>> x = 1234567.8
   >>> locale.format_string("%d", x, grouping=True)
   '1,234,567'
   >>> locale.format_string("%s%.*f", (conv['currency_symbol'],
   ...                      conv['frac_digits'], x), grouping=True)
   '$1,234,567.80'


11.2. Usando templates
======================

módulo "string" inclui a versátil classe "Template" com uma sintaxe
simplificada, adequada para ser editada por usuários finais. Isso
permite que usuários personalizem suas aplicações sem a necessidade de
alterar a aplicação.

Em um template são colocadas marcações indicando o local onde o texto
variável deve ser inserido. Uma marcação é formada por "$" seguido de
um identificador Python válido (caracteres alfanuméricos e
underscores). Envolvendo-se o identificador da marcação entre chaves,
permite que ele seja seguido por mais caracteres alfanuméricos sem a
necessidade de espaços. Escrevendo-se "$$" cria-se um único "$":

   >>> from string import Template
   >>> t = Template('O povo de ${vila} envia $$10 para $causa.')
   >>> t.substitute(vila='Nottingham', causa='o fundo de recuperação')
   'O povo de Nottingham envia $10 para o fundo de recuperação.'

O método "substitute()" levanta uma exceção "KeyError" quando o
identificador de uma marcação não é fornecido em um dicionário ou em
um argumento nomeado (*keyword argument*). Para aplicações que podem
receber dados incompletos fornecidos pelo usuário, o método
"safe_substitute()" pode ser mais apropriado --- deixará os marcadores
intactos se os dados estiverem faltando:

   >>> t = Template('Devolva $item para $dono.')
   >>> d = dict(item='a andorinha descarregada')
   >>> t.substitute(d)
   Traceback (most recent call last):
     ...
   KeyError: 'dono'
   >>> t.safe_substitute(d)
   'Devolva a andorinha descarregada para $dono.'

Subclasses de Template podem especificar um delimitador personalizado.
Por exemplo, um utilitário para renomeação em lote de fotos pode usar
o sinal de porcentagem para marcações como a data atual, número
sequencial da imagem ou formato do aquivo:

   >>> import time, os.path
   >>> arquivos_fotos = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
   >>> class RenomeiaEmLote(Template):
   ...     delimiter = '%'
   ...
   >>> formato = input('Informe o estilo de renomeação (%d-data %n-sequencia %f-formato):  ')
   Informe o estilo de renomeação (%d-data %n-sequencia %f-formato):  Ashley_%n%f

   >>> t = RenomeiaEmLote(formato)
   >>> data = time.strftime('%d%b%y')
   >>> for i, nome_arquivo in enumerate(arquivos_fotos):
   ...     base, extensão = os.path.splitext(nome_arquivo)
   ...     novo_nome = t.substitute(d=data, n=i, f=extensão)
   ...     print('{0} --> {1}'.format(nome_arquivo, novo_nome))

   img_1074.jpg --> Ashley_0.jpg
   img_1076.jpg --> Ashley_1.jpg
   img_1077.jpg --> Ashley_2.jpg

Outra aplicação para templates é separar a lógica da aplicação dos
detalhes de múltiplos formatos de saída. Assim é possível usar
templates personalizados para gerar arquivos XML, relatórios em texto
puro e relatórios web em HTML.


11.3. Trabalhando com formatos binários de dados
================================================

O módulo "struct" oferece as funções "pack()" e "unpack()" para
trabalhar com registros binários de tamanho variável. O exemplo a
seguir mostra como iterar através do cabeçalho de informação num
aquivo ZIP sem usar o módulo "zipfile". Os códigos de empacotamento
""H"" e ""I"" representam números sem sinal de dois e quatro bytes
respectivamente. O ""<"" indica que os números têm tamanho padrão e
são little-endian (bytes menos significativos primeiro):

   import struct

   with open('meuarquivo.zip', 'rb') as arq:
       dados = arq.read()

   inicio = 0
   for i in range(3):                      # mostra o cabeçalho dos 3 primeiros arquivos
       inicio += 14
       campos = struct.unpack('<IIIHH', dados[inicio:inicio+16])
       crc32, tamanho_comprimido, tamanho_descomprimido, tamanho_nome_arquivo, tamanho_extra = campos

       inicio += 16
       nome_arquivo = dados[inicio:inicio+tamanho_nome_arquivo]
       inicio += tamanho_nome_arquivo
       extra = dados[inicio:inicio+tamanho_extra]
       print(nome_arquivo, hex(crc32), tamanho_comprimido, tamanho_descomprimido)

       inicio += tamanho_extra + tamanho_comprimido     # pula para o próximo cabeçalho


11.4. Multi-threading
=====================

O uso de threads é uma técnica para desacoplar tarefas que não são
sequencialmente dependentes. Threads podem ser usadas para melhorar o
tempo de resposta de aplicações que aceitam entradas do usuário
enquanto outras tarefas são executadas em segundo plano. Um caso
relacionado é executar ações de entrada e saída (I/O) em uma thread
paralelamente a cálculos em outra thread.

O código a seguir mostra como o módulo de alto nível "threading" pode
executar tarefas em segundo plano enquanto o programa principal
continua a sua execução:

   import threading, zipfile

   class AsyncZip(threading.Thread):
       def __init__(self, arquivo_entrada, arquivo_saida):
           super().__init__()
           self.arquivo_entrada = arquivo_entrada
           self.arquivo_saida = arquivo_saida

       def run(self):
           with zipfile.ZipFile(self.arquivo_saida, 'w', zipfile.ZIP_DEFLATED) as f:
               f.write(self.arquivo_entrada)
           print('Finalizou compactação em background de:', self.arquivo_entrada)

   background = AsyncZip('meusdados.txt', 'meuarquivo.zip')
   background.start()
   print('O programa original continua a executar em primeiro plano.')

   background.join()    # Aguarda a tarefa em background finalizar
   print('Programa principal aguardou até a tarefa em background estar finalizada.')

O principal desafio para as aplicações que usam múltiplas threads é
coordenar as threads que compartilham dados ou outros recursos. Para
esta finalidade, o módulo threading oferece alguns mecanismos
primitivos de sincronização, como travas, eventos, variáveis de
condição e semáforos.

Ainda que todas essas ferramentas sejam poderosas, pequenos erros de
design podem resultar em problemas difíceis de serem diagnosticados.
Por isso, a abordagem preferida para a coordenação da tarefa é
concentrar todo o acesso a um recurso em um único tópico e, em
seguida, usar o módulo "queue" para alimentar esse segmento com
solicitações de outros tópicos. Aplicações que utilizam objetos
"Queue" para comunicação e coordenação inter-thread são mais fáceis de
serem projetados, mais legíveis e mais confiáveis.


11.5. Gerando logs
==================

O módulo "logging" oferece um completo e flexível sistema de log. Da
maneira mais simples, mensagens de log são enviadas para um arquivo ou
para "sys.stderr":

   import logging
   logging.debug('Depurando informações')
   logging.info('Mensagem informática')
   logging.warning('Alerta: arquivo de configuração  %s não encontrado', 'server.conf')
   logging.error('Ocorreu um erro')
   logging.critical('Erro crítico -- desligando')

Isso produz a seguinte saída:

   WARNING:root:Alerta:arquivo de configuração server.conf não encontrado
   ERROR:root:Ocorreu um erro
   CRITICAL:root:Erro crítico -- shutting down

Por padrão, mensagens informativas e de depuração são suprimidas e a
saída é enviada para a saída de erros padrão (stderr). Outras opções
de saída incluem envio de mensagens através de correio eletrônico,
datagramas, sockets ou para um servidor HTTP. Novos filtros podem
selecionar diferentes formas de envio de mensagens, baseadas na
prioridade da mensagem: "DEBUG", "INFO", "WARNING", "ERROR" e
"CRITICAL".

O sistema de log pode ser configurado diretamente do Python ou pode
ser carregado a partir de um arquivo de configuração editável pelo
usuário para logs personalizados sem a necessidade de alterar a
aplicação.


11.6. Referências fracas
========================

Python faz gerenciamento automático de memória (contagem de
referências para a maioria dos objetos e *coleta de lixo* para
eliminar ciclos). A memória ocupada por um objeto é liberada logo
depois da última referência a ele ser eliminada.

Essa abordagem funciona bem para a maioria das aplicações, mas
ocasionalmente surge a necessidade de rastrear objetos apenas enquanto
estão sendo usados por algum outro. Infelizmente rastreá-los cria uma
referência, e isso os fazem permanentes. O módulo "weakref" oferece
ferramentas para rastrear objetos sem criar uma referência. Quando o
objeto não é mais necessário, ele é automaticamente removido de uma
tabela de referências fracas e uma chamada (*callback*) é disparada.
Aplicações típicas incluem armazenamento em cache de objetos que são
muito custosos para criar:

   >>> import weakref, gc
   >>> class A:
   ...     def __init__(self, value):
   ...         self.value = value
   ...     def __repr__(self):
   ...         return str(self.value)
   ...
   >>> a = A(10)                   # cria a referência
   >>> d = weakref.WeakValueDictionary()
   >>> d['primário'] = a            # não cria a referência
   >>> d['primário']                #  obtém o objeto se ele ainda estiver vivo
   10
   >>> del a                       # remove a única referência
   >>> gc.collect()                # executa coleta de lixo imediatamente
   0
   >>> d['primário']                #  a entrada foi removida automaticamente
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
       d['primário']                # a entrada foi removida automaticamente
     File "C:/python315/lib/weakref.py", line 46, in __getitem__
       o = self.data[key]()
   KeyError: 'primário'


11.7. Ferramentas para trabalhar com listas
===========================================

Muitas necessidades envolvendo estruturas de dados podem ser
satisfeitas com o tipo embutido lista. Entretanto, algumas vezes há
uma necessidade por implementações alternativas que sacrificam algumas
facilidades em nome de melhor desempenho.

O módulo "array" oferece uma classe "array", semelhante a uma lista,
mas que armazena apenas dados homogêneos e de maneira mais compacta. O
exemplo a seguir mostra um vetor de números armazenados como números
binários de dois bytes sem sinal (código de tipo ""H"") ao invés dos
16 bytes usuais para cada item em uma lista de "int":

   >>> from array import array
   >>> a = array('H', [4000, 10, 700, 22222])
   >>> sum(a)
   26932
   >>> a[1:3]
   array('H', [10, 700])

O módulo "collections" oferece um objeto "deque" que comporta-se como
uma lista mas com *appends* e *pops* pela esquerda mais rápidos, porém
mais lento ao percorrer o meio da sequência. Esses objetos são
adequados para implementar filas e buscas em amplitude em árvores de
dados:

   >>> from collections import deque
   >>> d = deque(["tarefa1", "tarefa2", "tarefa3"])
   >>> d.append("tarefa4")
   >>> print("Tratando", d.popleft())
   Tratando tarefa1

   nao_pesquisada = deque([no_inicial])
   def busca_em_profundidade(nao_pesquisada):
       no = nao_pesquisada.popleft()
       for m in gen_moves(no):
           if eh_o_alvo(m):
               return m
           nao_pesquisada.append(m)

Além de implementações alternativas de listas, a biblioteca também
oferece outras ferramentas como o módulo "bisect" com funções para
manipulação de listas ordenadas:

   >>> import bisect
   >>> notas = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
   >>> bisect.insort(notas, (300, 'ruby'))
   >>> notas
   [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

O módulo "heapq" oferece funções para implementação de *heaps*
baseadas em listas normais. O valor mais baixo é sempre mantido na
posição zero. Isso é útil para aplicações que acessam repetidamente o
menor elemento, mas não querem reordenar a lista toda a cada acesso:

   >>> from heapq import heapify, heappop, heappush
   >>> dados = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
   >>> heapify(dados)                      # reorganiza a lista como um heap
   >>> heappush(dados, -5)                 # adiciona o valor -5 ao heap
   >>> [heappop(dados) for i in range(3)]  # encontra as 3 menores entradas
   [-5, 0, 1]


11.8. Aritmética decimal com ponto flutuante
============================================

O módulo "decimal" oferece o tipo "Decimal" para aritmética decimal
com ponto flutuante. Comparado a implementação embutida "float" que
usa aritmética binária de ponto flutuante, a classe é especialmente
útil para:

* aplicações financeiras que requerem representação decimal exata,

* controle sobre a precisão,

* controle sobre arredondamento para satisfazer requisitos legais,

* rastreamento de casas decimais significativas, ou

* aplicações onde o usuário espera que os resultados sejam os mesmos
  que os dos cálculos feitos à mão.

Por exemplo, calcular um imposto de 5% sobre uma chamada telefônica de
70 centavos devolve diferentes resultados com aritmética de ponto
flutuante decimal ou binária. A diferença torna-se significativa se os
resultados são arredondados para o centavo mais próximo:

   >>> from decimal import *
   >>> round(Decimal('0.70') * Decimal('1.05'), 2)
   Decimal('0.74')
   >>> round(.70 * 1.05, 2)
   0.73

O resultado de "Decimal" considera zeros à direita, automaticamente
inferindo quatro casas decimais a partir de multiplicandos com duas
casas decimais. O módulo Decimal reproduz a aritmética como fazemos à
mão e evita problemas que podem ocorrer quando a representação binária
do ponto flutuante não consegue representar quantidades decimais com
exatidão.

A representação exata permite à classe "Decimal" executar cálculos de
módulo e testes de igualdade que não funcionam bem em ponto flutuante
binário:

   >>> Decimal('1.00') % Decimal('.10')
   Decimal('0.00')
   >>> 1.00 % 0.10
   0.09999999999999995

   >>> sum([Decimal('0.1')]*10) == Decimal('1.0')
   True
   >>> 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 == 1.0
   False

O módulo "decimal" implementa a aritmética com tanta precisão quanto
necessária:

   >>> getcontext().prec = 36
   >>> Decimal(1) / Decimal(7)
   Decimal('0.142857142857142857142857142857142857')
