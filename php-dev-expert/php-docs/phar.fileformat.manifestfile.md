# Definição de entrada do arquivo de manifesto Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.fileformat.manifestfile.php

---

## Definição de entrada do arquivo de manifesto Phar

Cada arquivo no manifesto contém as seguintes informações:

**Entrada no arquivo Phar Manifest**

| Tamanho em bytes | Descrição |
| --- | --- |
| 4 bytes | Comprimento do nome do arquivo em bytes |
| ?? | Nome do arquivo (comprimento especificado anteriormente) |
| 4 bytes | Tamanho do arquivo não compactado em bytes |
| 4 bytes | Timestamp Unix do arquivo |
| 4 bytes | Tamanho do arquivo compactado em bytes |
| 4 bytes | Soma de verificação CRC32 do conteúdo do arquivo não compactado |
| 4 bytes | Sinalizadores específicos de arquivo mapeados em bits |
| 4 bytes | Comprimento de metadados de arquivo serializado (`0` para nenhum) |
| ?? | Metadados de arquivo serializados, armazenados no formato [serialize()](function.serialize.md) |

Observe que, a partir da versão 1.1.1 da API, diretórios vazios são armazenados como nomes de arquivos
com uma barra final como `meu/diretorio/`.

Os valores reconhecidos de mapa de bits específicos para arquivo são:

**Valores reconhecidos de mapa de bits**

| Valor | Descrição |
| --- | --- |
| `0x000001FF` | Esses bits são reservados para definir permissões específicas de um arquivo. As permissões são usadas para [fstat()](function.fstat.md) e podem ser usadas para recriar as permissões desejadas na extração. |
| `0x00001000` | Se definido, este arquivo será compactado com DEFLATE zlib. |
| `0x00002000` | Se definido, este arquivo será compactado com bzip2. |

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
