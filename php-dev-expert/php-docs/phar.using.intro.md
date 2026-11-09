# Usando Arquivos Phar: Introdução

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.using.intro.php

---

## Usando Arquivos Phar: Introdução

Os arquivos Phar são semelhantes em conceito aos arquivos JAR do Java, mas são adaptados
às necessidades e à flexibilidade de aplicações PHP. Um arquivo Phar é
usado para distribuir uma aplicação ou biblioteca PHP completa em um único arquivo.
Uma aplicação de arquivo Phar é usada exatamente como qualquer outra aplicação PHP:

```
php aplicacaoincrivel.phar
```

Usar uma biblioteca de arquivo Phar é idêntico ao uso de qualquer outra biblioteca PHP:

```
<?php
include 'bibliotecafantastica.phar';
?>
```

O empacotador de fluxo `phar` fornece o núcleo da extensão phar e
é explicado em detalhes [aqui](phar.using.stream.md).
O empacotador de fluxo phar permite acessar os arquivos dentro de um arquivo phar usando
as funções de arquivo padrão do PHP [fopen()](function.fopen.md), [opendir()](function.opendir.md) e
outras que funcionam em arquivos comuns. O empacotador de fluxo `phar` suporta todas as
operações de leitura/gravação em arquivos e diretórios.

```
<?php
include 'phar://bibliotecafantastica.phar/interno/arquivo.php';
header('Content-type: image/jpeg');
// phars pode ser acessado pelo caminho completo ou por apelido
echo file_get_contents('phar:///caminhocompleto/para/bibliotecafantastica.phar/imagens/uau.jpg');
?>
```

A classe [Phar](class.phar.md) implementa funcionalidades avançadas para acessar
arquivos e criar arquivos phar. A classe Phar é explicada em detalhes
[aqui](phar.using.object.md).

```
<?php
try {
    // abre um phar existente
    $p = new Phar('bibliotecafantastica.phar', 0);
    // Phar estende a classe DirectoryIterator do SPL
    foreach (new RecursiveIteratorIterator($p) as $file) {
        // $file é uma classe PharFileInfo e herda de SplFileInfo
        echo $file->getFileName() . "\n";
        echo file_get_contents($file->getPathName()) . "\n"; // exibir conteúdo;
    }
    if (isset($p['internal/file.php'])) {
        var_dump($p['internal/file.php']->getMetadata());
    }

    // cria um novo phar - phar.readonly deve ser 0 em php.ini
    // phar.readonly é habilitado por padrão por motivos de segurança.
    // Em servidores de produção, Phars nunca precisam ser criados,
    // apenas executados.
    if (Phar::canWrite()) {
        $p = new Phar('novophar.tar.phar', 0, 'novophar.tar.phar');
        // faz deste um arquivo phar baseado em tar, compactado com compressão gzip (.tar.gz)
        $p = $p->convertToExecutable(Phar::TAR, Phar::GZ);

        // cria transação - nada é escrito em novophar.phar
        // até que stopBuffering() seja chamado, embora seja necessário armazenamento temporário
        $p->startBuffering();
        // adiciona todos os arquivos em /caminho/para/projeto, salvando no phar com o prefixo "projeto"
        $p->buildFromIterator(new RecursiveIteratorIterator(new RecursiveDirectoryIterator('/caminho/para/projeto')), '/caminho/para/');

        // adiciona um novo arquivo por meio da API de acesso a array
        $p['arquivo1.txt'] = 'Informação';
        $fp = fopen('arquivogigante.dat', 'rb');
        // copia todos os dados do fluxo
        $p['dados/arquivogigante.dat'] = $fp;

        if (Phar::canCompress(Phar::GZ)) {
            $p['dados/arquivogigante.dat']->compress(Phar::GZ);
        }

        $p['imagens/uau.jpg'] = file_get_contents('imagens/uau.jpg');
        // qualquer valor pode ser salvo como metadados específicos do arquivo
        $p['imagens/uau.jpg']->setMetadata(array('mime-type' => 'image/jpeg'));
        $p['index.php'] = file_get_contents('index.php');
        $p->setMetadata(array('bootstrap' => 'index.php'));

        // salva o arquivo phar no disco
        $p->stopBuffering();
    }
} catch (Exception $e) {
    echo 'Não foi possível abrir o Phar: ', $e;
}
?>
```

Além disso, a verificação do conteúdo do arquivo phar pode ser feita usando qualquer um dos
algoritmos de hash simétricos suportados (MD5, SHA1, SHA256 e SHA512 se ext/hash estiver habilitado)
e usando assinatura assimétrica de chave pública/privada usando OpenSSL. Para
aproveitar a assinatura OpenSSL, é necessário gerar um par de chaves pública/privada e
usar a chave privada para definir a assinatura usando
[Phar::setSignatureAlgorithm()](phar.setsignaturealgorithm.md). Adicionalmente, a chave pública
extraída usando este código:

```
<?php
$public = openssl_get_publickey(file_get_contents('private.pem'));
$pkey = '';
openssl_pkey_export($public, $pkey);
?>
```

deve ser salva adjacente ao arquivo phar que ela verifica. Se o arquivo phar
for salvo como `/caminho/para/meu.phar`, a chave pública deve ser salva
como `/caminho/para/meu.phar.pubkey`, ou o phar não conseguirá verificar
a assinatura OpenSSL.

A classe [Phar](class.phar.md) também fornece 3 métodos estáticos, [Phar::webPhar()](phar.webphar.md),
[Phar::mungServer()](phar.mungserver.md) e [Phar::interceptFileFuncs()](phar.interceptfilefuncs.md), que são cruciais
para empacotar aplicações PHP projetadas para uso em sistemas de arquivos comuns e para aplicações web.
[Phar::webPhar()](phar.webphar.md) implementa um controlador de frente que roteia chamadas HTTP para o local correto
dentro do arquivo phar. [Phar::mungServer()](phar.mungserver.md) é usado para modificar os valores
do array [$\_SERVER](reserved.variables.server.md) para enganar aplicações que processam esses valores.
[Phar::interceptFileFuncs()](phar.interceptfilefuncs.md) instrui o Phar a interceptar chamadas para
[fopen()](function.fopen.md), [file\_get\_contents()](function.file-get-contents.md), [opendir()](function.opendir.md) e
todas as funções baseadas em estatísticas ([file\_exists()](function.file-exists.md), [is\_readable()](function.is-readable.md) e assim por diante) e
rotear todos os caminhos relativos para locais dentro do arquivo phar.

Por exemplo, empacotar uma versão do popular aplicativo phpMyAdmin para uso como um arquivo phar requer
apenas este script simples e então `phpMyAdmin.phar.tar.php` pode ser acessado como um arquivo normal
a partir do servidor web após modificar o usuário/senha:

```
<?php
@unlink('phpMyAdmin.phar.tar.php');
copy('phpMyAdmin-2.11.3-english.tar.gz', 'phpMyAdmin.phar.tar.php');
$a = new Phar('phpMyAdmin.phar.tar.php');
$a->startBuffering();
$a["phpMyAdmin-2.11.3-english/config.inc.php"] = '<?php
/* Configuração de servidores */
$i = 0;

/* Servidor localhost (config:root) [1] */
$i++;
$cfg[\'Servers\'][$i][\'host\'] = \'localhost\';
$cfg[\'Servers\'][$i][\'extension\'] = \'mysqli\';
$cfg[\'Servers\'][$i][\'connect_type\'] = \'tcp\';
$cfg[\'Servers\'][$i][\'compress\'] = false;
$cfg[\'Servers\'][$i][\'auth_type\'] = \'config\';
$cfg[\'Servers\'][$i][\'user\'] = \'root\';
$cfg[\'Servers\'][$i][\'password\'] = \'\';

/* Fim da configuração dos servidores */
if (strpos(PHP_OS, \'WIN\') !== false) {
    $cfg[\'UploadDir\'] = getcwd();
} else {
    $cfg[\'UploadDir\'] = \'/tmp/pharphpmyadmin\';
    @mkdir(\'/tmp/pharphpmyadmin\');
    @chmod(\'/tmp/pharphpmyadmin\', 0777);
}';
$a->setStub('<?php
Phar::interceptFileFuncs();
Phar::webPhar("phpMyAdmin.phar", "phpMyAdmin-2.11.3-english/index.php");
echo "O phpMyAdmin foi projetado para ser executado a partir de um navegador da web\n";
exit -1;
__HALT_COMPILER();
');
$a->stopBuffering();
?>
```

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
