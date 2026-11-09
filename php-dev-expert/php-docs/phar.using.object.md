# Usando Arquivos Phar: as classes Phar e PharData

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.using.object.php

---

## Usando Arquivos Phar: as classes Phar e PharData

A classe [Phar](class.phar.md) suporta leitura e manipulação
de arquivos Phar, bem como iteração por meio da funcionalidade herdada
da classe [RecursiveDirectoryIterator](class.recursivedirectoryiterator.md).
Com suporte à interface [ArrayAccess](class.arrayaccess.md),
os arquivos dentro de um arquivo Phar podem ser acessados ​​como se fossem
parte de um array associativo.

A classe [PharData](class.phardata.md) estende a classe [Phar](class.phar.md) e
permite criar e modificar arquivos tar e zip não executáveis ​​(de dados), mesmo que
`phar.readonly`=1 em php.ini. Dessa forma,
[PharData::setAlias()](phardata.setalias.md) e [PharData::setStub()](phardata.setstub.md)
estão desabilitados, pois os conceitos de alias e stub são exclusivos dos arquivos phar
executáveis.

É importante observar que, ao criar um arquivo Phar, o caminho completo
deve ser passado para o construtor do objeto [Phar](class.phar.md).
Caminhos relativos não serão inicializados.

Supondo que `$p` é um objeto Phar inicializado da seguinte maneira:

```
<?php
$p = new Phar('/caminho/para/meuphar.phar', 0, 'meuphar.phar');
?>
```

Um arquivo Phar vazio será criado em `/caminho/para/meuphar.phar`,
ou, se `/caminho/para/meuphar.phar` já existir, ele será aberto
novamente. O literal `meuphar.phar` demonstra o conceito de um apelido
que pode ser usado para referenciar `/caminho/para/meuphar.phar` em URLs como em:

```
<?php
// essas duas chamadas para file_get_contents() são equivalentes se
// /caminho/para/meuphar.phar tiver um apelido explícito de "meuphar.phar"
// em seu manifesto, ou se o phar foi inicializado com a
// configuração do objeto Phar do exemplo anterior
$f = file_get_contents('phar:///caminho/para/meuphar.phar/qualquercoisa.txt');
$f = file_get_contents('phar://meuphar.phar/qualquercoisa.txt');
?>
```

Com o objeto `$p` [Phar](class.phar.md) recém-criado,
o seguinte é possível:

- `$a = $p['arquivo.php']` cria uma classe [PharFileInfo](class.pharfileinfo.md)
  que se refere ao conteúdo de `phar://meuphar.phar/arquivo.php`
- `$p['arquivo.php'] = $v` cria um novo arquivo
  (`phar://meuphar.phar/arquivo.php`) ou sobrescreve
  um arquivo existente dentro de `meuphar.phar`. `$v`
  pode ser uma string ou um ponteiro para arquivo aberto, caso em que todo o
  conteúdo do arquivo será usado para criar o novo arquivo. Observe que
  `$p->addFromString('arquivo.php', $v)` é funcionalmente
  equivalente ao acima. Também é possível adicionar o conteúdo de um arquivo
  com `$p->addFile('/caminho/para/arquivo.php', 'arquivo.php')`.
  Por fim, um diretório vazio pode ser criado com
  `$p->addEmptyDir('empty')`.
- `isset($p['arquivo.php'])` pode ser usado para determinar
  se `phar://meuphar.phar/arquivo.php` existe dentro de
  `meuphar.phar`.
- `unset($p['arquivo.php'])` apaga
  `phar://meuphar.phar/arquivo.php` de
  `meuphar.phar`.

Além disso, o objeto [Phar](class.phar.md) é a única maneira de acessar
metadados específicos do Phar, por meio de
[Phar::getMetadata()](phar.getmetadata.md),
e a única maneira de definir ou recuperar o stub do carregador PHP de um arquivo Phar por meio de
[Phar::getStub()](phar.getstub.md) e
[Phar::setStub()](phar.setstub.md).
Além disso, a compactação de todo o arquivo Phar de uma só vez só pode ser manipulada
usando a classe [Phar](class.phar.md).

A lista completa de funcionalidades do objeto [Phar](class.phar.md) está documentada
abaixo.

A classe [PharFileInfo](class.pharfileinfo.md) estende a classe
[SplFileInfo](class.splfileinfo.md)
e adiciona vários métodos para manipular detalhes específicos de Phar de um arquivo
contido em um Phar, como manipular compactação e metadados.

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
