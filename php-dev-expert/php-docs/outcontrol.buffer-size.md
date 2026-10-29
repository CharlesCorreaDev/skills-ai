# Tamanho do Buffer

> **Fonte / Source:** https://www.php.net/manual/pt_BR/outcontrol.buffer-size.php

---

## Tamanho do Buffer

Os tamanhos dos buffers são expressos por números inteiros
e representam o número de bytes que o buffer pode armazenar sem descarregar.
Quando o tamanho da saída no buffer excede o tamanho do buffer,
o conteúdo do buffer é enviado para o manipulador de saída,
seu valor de retorno é descarregado e o buffer é limpo.

Com exceção de `"URL-Rewriter"`,
o tamanho dos buffers de saída pode ser definido quando o buffer é iniciado.
Se definido como `0`,
o buffer de saída será limitado apenas pela memória disponível para o PHP.
Se definido como `1`,
o buffer será descarregado após cada bloco de código produzir
qualquer saída de comprimento diferente de zero.

O tamanho dos buffers de saída pode ser recuperado chamando
[ob\_get\_status()](function.ob-get-status.md).

Buffers de saída iniciados com [ob\_start()](function.ob-start.md)
terão seus tamanhos de buffer definidos para o valor inteiro passado para
o segundo parâmetro `chunk_size` da função.
Se omitido, será definido como `0`.

O buffer de saída iniciado com
[output\_buffering](outcontrol.configuration.md#ini.output-buffering)
definido como `"On"` terá seu tamanho de buffer definido como 0.
Se definido como um número inteiro, o tamanho do buffer corresponderá a esse número.

O tamanho do buffer do `"URL-Rewriter"`está definido como `0`,
portanto ele é limitado apenas pela memória disponível para o PHP.

O tamanho do buffer de saída do `zlib` é controlado pela configuração
[zlib.output\_compression](zlib.configuration.md#ini.zlib.output-compression)
do php.ini.
Se definido como `"On"` o tamanho do buffer será
`"16K"`(`16384`).
Se definido como um número inteiro, o tamanho do buffer corresponderá a esse número em bytes.

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
