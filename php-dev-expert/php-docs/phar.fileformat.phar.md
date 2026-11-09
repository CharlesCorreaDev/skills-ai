# Formato de arquivo phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.fileformat.phar.php

---

## Formato de arquivo phar

O formato do arquivo phar é literalmente definido como stub/manifesto/conteúdo/assinatura e
armazena as informações cruciais do que está incluído no arquivo phar em seu
`manifest`o.

O manifesto Phar é um formato altamente otimizado que permite a especificação por arquivo
da compactação, das permissões e até mesmo dos metadados
definidos pelo usuário, como usuário ou grupo do arquivo. Todos os valores maiores que 1 byte são armazenados
na ordem little-endian, com exceção da versão da API, que
por razões históricas é armazenada como 3 nibbles na ordem big-endian.

Todos os sinalizadores não utilizados são reservados para uso futuro e não devem ser usados
para armazenar informações personalizadas. Use o recurso de metadados por arquivo
para armazenar informações personalizadas sobre arquivos específicos.

O formato básico de arquivo de um manifesto de arquivo Phar é o seguinte:

**Formato global de manifesto Phar**

| Tamanho em bytes | Descrição |
| --- | --- |
| 4 bytes | Comprimento do manifesto em bytes (limite de 1 MB) |
| 4 bytes | Número de arquivos no Phar |
| 2 bytes | Versão da API do manifesto Phar (atualmente 1.0.0) |
| 4 bytes | Sinalizadores globais Phar em mapa de bits |
| 4 bytes | Comprimento do apelido Phar |
| ?? | Apelido Phar (comprimento com base no anterior) |
| 4 bytes | Comprimento dos metadados Phar (`0` para nenhum) |
| ?? | Metadados Phar serializados, armazenados no formato [serialize()](function.serialize.md) |
| pelo menos 24 \* número de bytes de entradas | entradas para cada arquivo |

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
