# Criando Arquivos Phar: Introdução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.creating.intro.php

---

## Criando Arquivos Phar: Introdução

Será escrito na íntegra em breve. Antes de ler isto, leia
[Como usar os Arquivos Phar](phar.using.md).

Um ótimo lugar para começar é lendo sobre [Phar::buildFromIterator()](phar.buildfromiterator.md),
e as especificações das opções de [formato de arquivo](phar.fileformat.md)
disponíveis para arquivos. Uma boa compreensão do que é e o que faz um stub é crucial
para a criação de arquivos phar, portanto, [Phar::setStub()](phar.setstub.md) e
[Phar::createDefaultStub()](phar.createdefaultstub.md) também são bons lugares para começar.
Se uma aplicação baseada na web estiver sendo distribuída, é crucial conhecer
[Phar::webPhar()](phar.webphar.md) e o método relacionado
[Phar::mungServer()](phar.mungserver.md). Qualquer aplicação que acesse
seus próprios arquivos também deve considerar o uso de [Phar::interceptFileFuncs()](phar.interceptfilefuncs.md).

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
