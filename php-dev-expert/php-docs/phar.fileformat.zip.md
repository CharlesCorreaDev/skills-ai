# Phars baseados em Zip

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.fileformat.zip.php

---

## Phars baseados em Zip

Arquivos baseados no formato de arquivo zip suportam diversos recursos incorporados
ao formato de arquivo zip. Metadados por arquivo e de todo o arquivo são armazenados
no comentário do arquivo zip como uma string serializada. Comentários
zip pré-existentes serão lidos com sucesso como uma string. A leitura/gravação de compactação
por arquivo é suportada com a compactação DEFLATE do zlib, e o acesso de leitura é suportado
com a compactação bzip2. Não há limite para o número de arquivos
dentro de um arquivo phar baseado em zip. Diretórios vazios são armazenados no arquivo zip
como arquivos com uma barra final, como `meu/diretorio/`.

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
