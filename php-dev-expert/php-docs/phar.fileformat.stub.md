# Stub de arquivo Phar

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.fileformat.stub.php

---

## Stub de arquivo Phar

Um stub de Phar é um arquivo PHP simples. O menor stub possível é o seguinte:

```
<?php __HALT_COMPILER();
```

Um stub deve conter, no mínimo, o token `__HALT_COMPILER();`
em sua conclusão. Normalmente, um stub conterá a funcionalidade do carregador
como a seguir:

```
<?php
Phar::mapPhar();
include 'phar://meuphar.phar/index.php';
__HALT_COMPILER();
```

Não há restrições quanto ao conteúdo de um stub Phar, exceto pelo requisito
de que ele termine com `__HALT_COMPILER();`. A tag PHP de fechamento
```` ```
?>
``` ```` pode ser incluída ou omitida, mas não pode haver
mais de 1 espaço entre `;` e a tag de fechamento
```` ```
?>
``` ```` ou a extensão phar não conseguirá
processar o manifesto do arquivo Phar.

Em um arquivo Phar baseado em tar ou zip, o stub é armazenado no arquivo
`.phar/stub.php`. O stub padrão para arquivos Phar
baseados em Phar contém aproximadamente 7k de código para extrair o conteúdo
do Phar e executá-lo. Consulte [Phar::createDefaultStub()](phar.createdefaultstub.md)
para mais detalhes.

O apelido phar é armazenado em um arquivo phar tar ou zip no arquivo
`.phar/alias.txt` como texto simples.

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
