"urllib.robotparser" ---  Analisador sintático de robots.txt
************************************************************

**Código-fonte:** Lib/urllib/robotparser.py

======================================================================

Este módulo fornece uma única classe, "RobotFileParser", que responde
a perguntas sobre se um agente de usuário específico pode ou não
buscar uma URL no site que publicou o arquivo "robots.txt". Para mais
detalhes sobre a estrutura dos arquivos "robots.txt", consulte **RFC
9309**.

class urllib.robotparser.RobotFileParser(url='')

   Esta classe fornece métodos para ler, analisar e responder
   perguntas sobre o arquivo "robots.txt" em *url*.

   set_url(url)

      Define a URL referente a um arquivo "robots.txt".

   read()

      Lê o URL "robots.txt" e o alimenta para o analisador sintático.

   parse(lines)

      Analisa o argumento de linhas.

   can_fetch(useragent, url)

      Retorna "True" se o *useragent* tiver permissão para buscar a
      *url* de acordo com as regras contidas no arquivo "robots.txt"
      analisado.

   mtime()

      Retorna o horário em que o arquivo "robots.txt" foi buscado pela
      última vez. Isso é útil para web spiders de longa duração que
      precisam verificar novos arquivos "robots.txt" periodicamente.

   modified()

      Define a hora em que o arquivo "robots.txt" foi buscado pela
      última vez para a hora atual.

   crawl_delay(useragent)

      Retorna o valor do parâmetro "Crawl-delay" de "robots.txt" para
      o *useragent* em questão. Se não houver tal parâmetro ou se ele
      não se aplicar ao *useragent* especificado ou se a entrada
      "robots.txt" para este parâmetro tiver sintaxe inválida, retorna
      "None".

      Adicionado na versão 3.6.

   request_rate(useragent)

      Retorna o conteúdo do parâmetro "Request-rate" de "robots.txt"
      como uma *tupla nomeada* "RequestRate(requests, seconds)". Se
      não houver tal parâmetro ou se ele não se aplicar ao *useragent*
      especificado ou se a entrada "robots.txt" para este parâmetro
      tiver sintaxe inválida, retorna "None".

      Adicionado na versão 3.6.

   site_maps()

      Retorna o conteúdo do parâmetro "Sitemap" de "robots.txt" no
      formato de uma "list()". Se não houver tal parâmetro ou a
      entrada "robots.txt" para este parâmetro tiver sintaxe inválida,
      retorna "None".

      Adicionado na versão 3.8.

O exemplo a seguir demonstra o uso básico da classe "RobotFileParser":

   >>> import urllib.robotparser
   >>> rp = urllib.robotparser.RobotFileParser()
   >>> rp.set_url("http://www.pythontest.net/robots.txt")
   >>> rp.read()
   >>> rrate = rp.request_rate("*")
   >>> rrate.requests
   1
   >>> rrate.seconds
   1
   >>> rp.crawl_delay("*")
   6
   >>> rp.can_fetch("*", "http://www.pythontest.net/")
   True
   >>> rp.can_fetch("*", "http://www.pythontest.net/no-robots-here/")
   False
