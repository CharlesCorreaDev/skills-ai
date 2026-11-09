# Altera o estado atual do buffer para o objeto grande

> **Fonte / Source:** https://www.php.net/manual/pt_BR/ocilob.setbuffering.php

---

# OCILob::setBuffering

(PHP 5, PHP 7, PHP 8, PECL OCI8 >= 1.1.0)

OCILob::setBuffering — Altera o estado atual do buffer para o objeto grande

### Descrição

public function **OCILob::setBuffering**([bool](language.types.boolean.md) `$mode`): [bool](language.types.boolean.md)

Define o buffer para o objeto grande, dependendo do valor do
modo informado no parâmetro `mode`.

O uso desta função pode fornecer melhorias de desempenho ao armazenar em buffer
pequenas leituras e gravações de LOBs, reduzindo o número de
viagens de ida e volta da rede e versões de LOB.
[OCILob::flush()](ocilob.flush.md)
deve ser usado para liberar buffers, quando tiver terminado o trabalho
com o objeto grande.

### Parâmetros

`mode`
:   **`true`** para ligado e **`false`** para desligado.

### Valor Retornado

Retorna **`true`** em caso de sucesso ou **`false`** em caso de falha. Chamadas repetidas para este método com o mesmo sinalizador retornarão
**`true`**.

### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 8.0.0, PECL OCI8 3.0.0 | A classe **OCI-Lob** foi renomeada para [OCILob](class.ocilob.md) para se alinhar aos padrões de nomenclatura PHP. |

### Veja também

- [OCILob::getBuffering](ocilob.getbuffering.md)

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
