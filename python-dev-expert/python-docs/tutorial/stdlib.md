10. Um breve passeio pela biblioteca padrão
*******************************************


10.1. Interface com o sistema operacional
=========================================

O módulo "os" fornece dúzias de funções para interagir com o sistema
operacional:

   >>> import os
   >>> os.getcwd()      # Retorna o diretório de trabalho atual
   'C:\\Python315'
   >>> os.chdir('/server/accesslogs')   # Altera o diretório de trabalho atual
   >>> os.system('mkdir today')   # Executa o comando mkdir na shell do sistema
   0

Certifique-se de usar a forma "import os" ao invés de "from os import
*". Isso evitará que "os.open()" oculte a função "open()" que opera de
forma muito diferente.

As funções embutidas "dir()" e "help()" são úteis como um sistema de
ajuda interativa para lidar com módulos grandes como "os":

   >>> import os
   >>> dir(os)
   <retorna uma lista de todas as funções do módulo>
   >>> help(os)
   <retorna uma página de manual extensa criada a partir das docstrings do módulo>

Para tarefas de gerenciamento cotidiano de arquivos e diretórios, o
módulo "shutil" fornece uma interface de nível mais alto que é mais
simples de usar:

   >>> import shutil
   >>> shutil.copyfile('dados.db', 'arquivo.db')
   'arquivo.db'
   >>> shutil.move('/build/executáveis', 'dir_instal')
   'dir_instal'


10.2. Caracteres curinga
========================

O módulo "glob" fornece uma função para criar listas de arquivos a
partir de buscas em diretórios usando caracteres curinga:

   >>> import glob
   >>> glob.glob('*.py')
   ['primos.py', 'aleatorizar.py', 'aspas.py']


10.3. Argumentos de linha de comando
====================================

Scripts geralmente precisam processar argumentos passados na linha de
comando. Esses argumentos são armazenados como uma lista no atributo
*argv* do módulo "sys". Por exemplo, consideremos o arquivo "demo.py"
a seguir:

   # Arquivo demo.py
   import sys
   print(sys.argv)

Aqui está a saída da execução "python demo.py um dois três" na linha
de comando:

   ['demo.py', 'um', 'dois, 'três']

O módulo "argparse" fornece um mecanismo mais sofisticado para
processar argumentos de linha de comando. O script seguinte extrai e
exibe um ou mais nomes de arquivos e um número de linhas opcional:

   import argparse

   parser = argparse.ArgumentParser(
       prog='topo',
       description='Mostra as primeiras linhas de cada arquivo')
   parser.add_argument('arquivos, nargs='+')
   parser.add_argument('-l', '--linhas', type=int, default=10)
   args = parser.parse_args()
   print(args)

Quando executada na linha de comando "python topo.py --linhas=5
alfa.txt beta.txt", o script define "args.linhas" para "5" e
"args.arquivos" para "['alfa.txt', 'beta.txt']".


10.4. Redirecionamento de erros e encerramento do programa
==========================================================

O módulo "sys" também possui atributos para *stdin*, *stdout* e
*stderr*. O último é usado para emitir avisos e mensagens de erros
visíveis mesmo quando *stdout* foi redirecionado:

   >>> sys.stderr.write('Aviso, arquivo log não encontrado, iniciando um novo\n')
   Aviso, arquivo log não encontrado, iniciando um novo

A forma mais direta de encerrar um script é usando "sys.exit()".


10.5. Reconhecimento de padrões em strings
==========================================

O módulo "re" fornece ferramentas para lidar com processamento de
strings através de expressões regulares. Para reconhecimento de
padrões complexos, expressões regulares oferecem uma solução sucinta e
eficiente:

   >>> import re
   >>> re.findall(r'\br[a-z]*', 'o rato roeu a roupa do rei de roma')
   ['rato', 'roeu', 'roupa', 'rei', 'roma']
   >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'o gato de de chapéu')
   'o gato de chapéu'

Quando as exigências são simples, métodos de strings são preferíveis
por serem mais fáceis de ler e depurar:

   >>> 'xá para dois'.replace('xá', 'chá')
   'chá para dois'


10.6. Matemática
================

O módulo "math" oferece acesso às funções da biblioteca C para
matemática de ponto flutuante:

   >>> import math
   >>> math.cos(math.pi / 4)
   0.70710678118654757
   >>> math.log(1024, 2)
   10.0

O módulo "random" fornece ferramentas para gerar seleções aleatórias:

   >>> import random
   >>> random.choice(['maçã', 'pera', 'banana'])
   'maçã'
   >>> random.sample(range(100), 10)   # amostragem sem reposição
   [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
   >>> random.random()    # ponto flutuante aleatório do intervalo [0.0, 1.0)
   0.17970987693706186
   >>> random.randrange(6)    # inteiro aleatório escolhido de range(6)
   4

O módulo "statistics" calcula as propriedades estatísticas básicas (a
média, a mediana, a variação, etc.) de dados numéricos:

   >>> import statistics
   >>> dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
   >>> statistics.mean(dados)
   1.6071428571428572
   >>> statistics.median(dados)
   1.25
   >>> statistics.variance(dados)
   1.3720238095238095

O projeto SciPy <https://scipy.org> tem muitos outros módulos para
cálculos numéricos.


10.7. Acesso à internet
=======================

Há diversos módulos para acesso e processamento de protocolos da
internet. Dois dos mais simples são "urllib.request" para efetuar
download de dados a partir de URLs e "smtplib" para enviar mensagens
de correio eletrônico:

   >>> from urllib.request import urlopen
   >>> with urlopen('https://docs.python.org/3/') as response:
   ...     for line in response:
   ...         line = line.decode()             # Converte bytes para um str
   ...         if 'updated' in line:
   ...             print(line.rstrip())         # Remove nova linha ao final
   ...
         Last updated on Nov 11, 2025 (20:11 UTC).

   >>> import smtplib
   >>> server = smtplib.SMTP('localhost')
   >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
   ... """To: jcaesar@example.org
   ... From: soothsayer@example.org
   ...
   ... Cuidado com os Idos de Março.
   ... """)
   >>> server.quit()

(Note que o segundo exemplo precisa de um servidor de email rodando em
localhost.)


10.8. Data e hora
=================

O módulo "datetime" fornece classes para manipulação de datas e horas
nas mais variadas formas. Apesar da disponibilidade de aritmética com
data e hora, o foco da implementação é na extração eficiente dos
membros para formatação e manipulação. O módulo também oferece objetos
que levam os fusos horários em consideração.

   >>> # datas são facilmente construídas e formatadas
   >>> import datetime as dt
   >>> now = dt.date.today()
   >>> now
   datetime.date(2003, 12, 2)
   >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
   '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

   >>> # datas têm suporte a matemática de calendário
   >>> birthday = date(1964, 7, 31)
   >>> age = now - birthday
   >>> age.days
   14368


10.9. Compressão de dados
=========================

Formatos comuns de arquivamento e compressão de dados estão
disponíveis diretamente através de alguns módulos, entre eles: "zlib",
"gzip", "bz2", "lzma", "zipfile" and "tarfile".

   >>> import zlib
   >>> s = b'A vaca malhada foi molhada por outra vaca molhada e malhada.'
   >>> len(s)
   60
   >>> t = zlib.compress(s)
   >>> len(t)
   47
   >>> zlib.decompress(t)
   b'A vaca malhada foi molhada por outra vaca molhada e malhada.'
   >>> zlib.crc32(s)
   2444551089


10.10. Medição de desempenho
============================

Alguns usuários de Python desenvolvem um interesse profundo pelo
desempenho relativo de diferentes abordagens para o mesmo problema.
Python oferece uma ferramenta de medição que esclarece essas dúvidas
rapidamente.

Por exemplo, pode ser tentador usar o empacotamento e desempacotamento
de tuplas ao invés da abordagem tradicional de permutar os argumentos.
O módulo "timeit" rapidamente mostra uma modesta vantagem de
desempenho:

   >>> from timeit import Timer
   >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
   0.57535828626024577
   >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
   0.54962537085770791

Em contraste com a granularidade fina do módulo "timeit", os módulos
"profile" e "pstats" oferecem ferramentas para identificar os trechos
mais críticos em grandes blocos de código.


10.11. Controle de qualidade
============================

Uma das abordagens usadas no desenvolvimento de software de alta
qualidade é escrever testes para cada função à medida que é
desenvolvida e executar esses testes frequentemente durante o processo
de desenvolvimento.

O módulo "doctest" oferece uma ferramenta para realizar um trabalho de
varredura e validação de testes escritos nas strings de documentação
(docstrings) de um programa. A construção dos testes é tão simples
quanto copiar uma chamada típica juntamente com seus resultados e
colá-los na docstring. Isto aprimora a documentação, fornecendo ao
usuário um exemplo real, e permite que o módulo doctest verifique se o
código continua fiel à documentação:

   def average(values):
       """Calcula a média aritmética da lista de números.

       >>> print(average([20, 30, 70]))
       40.0
       """
       return sum(values) / len(values)

   import doctest
   doctest.testmod()   # valida automaticamente os testes incorporados

O módulo "unittest" não é tão simples de usar quanto o módulo
"doctest", mas permite que um conjunto muito maior de testes seja
mantido em um arquivo separado:

   import unittest

   class TestStatisticalFunctions(unittest.TestCase):

       def test_average(self):
           self.assertEqual(average([20, 30, 70]), 40.0)
           self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
           with self.assertRaises(ZeroDivisionError):
               average([])
           with self.assertRaises(TypeError):
               average(20, 30, 70)

   unittest.main()  # Chamar a partir da linha de comando invoca todos os testes


10.12. Baterias incluídas
=========================

Python tem uma filosofia de "baterias incluídas". Isso fica mais
evidente através da sofisticação e robustez dos seus maiores pacotes.
Por exemplo:

* Os módulos "xmlrpc.client" e "xmlrpc.server" tornam a implementação
  de chamadas remotas (remote procedure calls) em uma tarefa quase
  trivial. Apesar dos nomes dos módulos, nenhum conhecimento direto ou
  manipulação de XML é necessário.

* O pacote "email" é uma biblioteca para gerenciamento de mensagens de
  correio eletrônico, incluindo MIME e outros baseados no **RFC
  5322**. Diferente dos módulos "smtplib" e "poplib" que apenas enviam
  e recebem mensagens, o pacote de email tem um conjunto completo de
  ferramentas para construir ou decodificar a estrutura de mensagens
  complexas (incluindo anexos) e para implementação de protocolos de
  codificação e cabeçalhos.

* O pacote "json" oferece um suporte robusto para analisar este
  popular formato para troca de dados. O módulo "csv" oferece suporte
  para leitura e escrita direta em arquivos no formato Comma-Separated
  Value, comumente suportado por bancos de dados e planilhas. O
  processamento XML é fornecido pelos pacotes "xml.etree.ElementTree",
  "xml.dom" e "xml.sax". Juntos, esses módulos e pacotes simplificam
  muito a troca de informações entre aplicativos Python e outras
  ferramentas.

* O módulo "sqlite3" é um wrapper para a biblioteca de banco de dados
  SQLite, fornecendo um banco de dados persistente que pode ser
  atualizado e acessado usando sintaxe SQL ligeiramente fora do
  padrão.

* Internacionalização está disponível através de diversos módulos,
  como "gettext", "locale", e o pacote "codecs".
