# Introdução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/oop5.intro.php

---

## Introdução

O PHP inclui uma modelagem a objetos completa.
Entre os recursos disponíveis há:
[visibilidade](language.oop5.visibility.md),
[classes e métodos abstratos](language.oop5.abstract.md) e
[finais](language.oop5.final.md),
[métodos mágicos](language.oop5.magic.md) adicionais,
[interfaces](language.oop5.interfaces.md) e
[clonagem](language.oop5.cloning.md).

O PHP trata objetos da mesma maneira que referências ou manipuladores, significando que
cada variável contém uma referência a um objeto ao invés de uma cópia
de todo o objeto. Veja
[Objetos e Referências](language.oop5.references.md)

**Dica**

Veja também o
[Guia de nomenclatura em espaço de usuário](userlandnaming.md).

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
