# Comparação direta de Phar, Tar e Zip

> **Fonte / Source:** https://www.php.net/manual/pt_BR/phar.fileformat.comparison.php

---

## Comparação direta de Phar, Tar e Zip

Quais são os pontos positivos e negativos dos três formatos de arquivo suportados
na extensão phar? Esta tabela tenta responder a essa pergunta.

**Matriz de Características: Phar vs. Tar vs. Zip**

| Característica | Phar | Tar | Zip |
| --- | --- | --- | --- |
| Formato de arquivo padrão | Não | Sim | Sim |
| Pode ser executado sem a extensão Phar [[1]](phar.fileformat.comparison.md#phar.fileformat.phartip) | Sim | Não | Não |
| Compactação por arquivo | Sim | Não | Sim |
| Compactação de arquivo inteiro | Sim | Sim | Não |
| Validação de assinatura de arquivo inteiro | Sim | Sim | Sim |
| Suporte a aplicativos específicos da Web | Sim | Sim | Sim |
| Metadados por arquivo | Sim | Sim | Sim |
| Metadados de arquivo inteiro | Sim | Sim | Sim |
| Criação/modificação de arquivo [[2]](phar.fileformat.comparison.md#phar.fileformat.phartip2) | Sim | Sim | Sim |
| Suporte total para todas as funções do empacotador de fluxo | Sim | Sim | Sim |
| Pode ser criado/modificado mesmo que phar.readonly=1 [[3]](phar.fileformat.comparison.md#phar.fileformat.phartip3) | Não | Sim | Sim |

**Dica**

[1] O PHP só pode acessar diretamente o conteúdo de um arquivo Phar
sem a extensão Phar se estiver usando um `stub`
que extrai o conteúdo do arquivo Phar. O stub
criado por [Phar::createDefaultStub()](phar.createdefaultstub.md) extrai
o arquivo Phar e executa seu conteúdo a partir de um diretório temporário
se nenhuma extensão Phar for encontrada.

**Dica**

[2] Todo acesso de gravação requer que `phar.readonly`
seja desabilitado no php.ini ou diretamente na linha de comando.

**Dica**

[3] Somente arquivos tar e zip sem `.phar` em seu
nome de arquivo e sem um stub executável `.phar/stub.php`
podem ser criados se phar.readonly=1.

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
