# Phars baseados em Tar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.fileformat.tar.php

---

## Phars baseados em Tar

Arquivos baseados no formato tar seguem o formato de arquivo USTAR
mais moderno. O design do cabeçalho do arquivo tar os torna mais eficientes
de acessar do que o formato zip e quase tão eficientes quanto o formato phar.
Os nomes de arquivo são limitados a 255 bytes, incluindo
o caminho completo dentro do arquivo phar. Não há limite para o número de arquivos
dentro de um arquivo phar baseado em tar. Esses arquivos podem ser totalmente compactados
no formato gzip ou bzip2 e ainda serem executados pela extensão Phar.

Há suporte limitado para leitura de tarballs no formato de intercâmbio pax,
mas todos os cabeçalhos pax reconhecidos (atualmente, typeflag `x` e
`g`) são ignorados silenciosamente.
Também há suporte limitado para Arquivos GNU Tar;
atualmente, os cabeçalhos `././@LongLink` são resolvidos.

Para compactar um arquivo inteiro, use [Phar::compress()](phar.compress.md).
Para descompactar um arquivo inteiro, use [Phar::decompress()](phar.decompress.md).

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
