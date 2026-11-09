# Buffer de Saída

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.output-buffering.php

---

# Buffer de Saída

O buffer de saída é o buffer (armazenamento temporário) da saída
antes de ela ser descarregada (enviada e descartada) para o navegador (em um contexto da web)
ou para o shell (na linha de comando).
Enquanto o buffer de saída estiver ativo, nenhuma saída será enviada do script;
em vez disso, a saída será armazenada em um buffer interno.

## Buffer Afetando o PHP

O PHP depende da infraestrutura de software/hardware subjacente
ao descarregar a saída.
O buffer implementado por consoles na linha de comando (por exemplo, buffer de linha)
ou servidores web e navegador em um contexto web (por exemplo, totalmente bufferizado)
afeta quando a saída é exibida para o usuário final.
Alguns desses efeitos podem ser eliminados ajustando as configurações do servidor
e/ou alinhando os tamanhos dos buffers das diversas camadas.

## Controle de Buffer de Saída no PHP

O PHP fornece um buffer de saída em nível de usuário totalmente armazenado em buffer
com funções para iniciar, manipular e desligar o buffer
(a maioria das funções [ob\_\*](ref.outcontrol.md))
e duas funções para descarregar os buffers subjacentes do sistema
([flush()](function.flush.md) e [ob\_implicit\_flush()](function.ob-implicit-flush.md)).
Algumas dessas funcionalidades podem ser definidas e/ou configuradas
usando também as configurações apropriadas do php.ini.

## Casos de Uso

O buffer de saída geralmente é útil em situações em que a saída armazenada em buffer
é modificada ou inspecionada ou é usada mais de uma vez em uma solicitação;
ou quando a descarga controlada da saída é desejada.
Os casos de uso específicos incluem:

- Armazenar em cache o resultado de scripts com uso intensivo de tempo/computação,
  por exemplo, gerando páginas `HTML` estáticas.
- Reutilizar a saída gerada exibindo-a, salvando-a em um arquivo
  e/ou enviando-a por e-mail.
- Enviar a tag `head` de uma página `HTML`,
  antes da tag `body` permite que os navegadores
  carreguem recursos externos enquanto o script executa
  processos potencialmente mais demorados
  (por exemplo, acesso a banco de dados e arquivos, conexão de rede externa).
  Isto só é útil se o código de status `HTTP`
  não puder ser alterado após o envio dos cabeçalhos.
- Extrair informações de funções que de outra forma produziriam saída
  (por exemplo, [phpinfo()](function.phpinfo.md)).
- Controlar a saída de código de terceiros modificando/usando partes
  (por exemplo, extraindo dados, substituindo palavras/frases,
  adicionando tags `HTML` ausentes)
  ou descartando-o inteiramente sob certas condições (por exemplo, erros).
- Preenchendo certas funcionalidades indisponíveis do servidor web
  (por exemplo, compactação ou codificação de saída)

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
