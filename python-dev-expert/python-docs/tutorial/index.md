O tutorial do Python
********************

Dica:

  Este tutorial foi desenvolvido para pessoas *que já programam*, mas
  são recém-chegadas na linguagem Python, **não** pessoas *iniciantes*
  em programação.

Python é uma linguagem fácil de aprender e poderosa. Ela tem
estruturas de dados de alto nível eficientes e uma abordagem simples
mas efetiva de programação orientada a objetos. A sintaxe elegante e a
tipagem dinâmica do Python, aliadas com sua natureza interpretativa, o
tornam uma linguagem ideal para fazer scripts e desenvolvimento de
aplicações rápidas em diversas áreas e na maioria das plataformas.

O interpretador Python e a extensiva biblioteca padrão estão
disponíveis gratuitamente em código ou na forma binária para toda as
maiores plataformas no endereço eletrônico do Python,
https://www.python.org/, e pode ser livremente distribuído. O mesmo
endereço contém distribuições de diversos módulos, programas e
ferramentas gratuitos produzidos por terceiros e documentação
adicional.

O interpretador do Python pode ser facilmente estendido com novas
funções e tipos de dados implementados em C ou C++ (ou outras
linguagens chamáveis a partir de C). Python também é adequado como uma
linguagem de extensão para aplicações personalizáveis.

Este tutorial introduz informalmente o leitor aos conceitos básicos e
aos recursos da linguagem e do sistema Python. Esteja ciente de que
ele espera que você tenha um conhecimento básico de programação em
geral. É mais fácil se você possuir um interpretador Python para uma
experiência prática, mas os exemplos são autossuficientes e, portanto,
o tutorial pode apenas ser lido off-line também.

Para uma descrição detalhada dos módulos e objetos padrões, veja
Referência da bibliotecas embutidas do Python e A biblioteca padrão do
Python. Em A Referência da Linguagem Python você encontra uma
definição mais formal da linguagem. Para escrever extensões em C ou
C++, leia Estendendo e incorporando o interpretador Python e Manual de
referência da API C/Python. Existe também uma série de livros que
cobrem Python em profundidade.

Este tutorial não espera ser abrangente e cobrir todos os recursos ou
mesmo os recursos mais usados. Ele busca introduzir diversos dos
recursos mais notáveis do Python e lhe dará uma boa ideia do sabor e
estilo da linguagem. Depois de lê-lo, você terá condições de ler e
escrever programas e módulos Python e estará pronto para aprender mais
sobre os diversos módulos descritos em A biblioteca padrão do Python.

O Glossário também vale a pena ser estudado.

* 1. Abrindo seu apetite

* 2. Utilizando o interpretador Python

  * 2.1. Chamando o interpretador

    * 2.1.1. Passagem de argumentos

    * 2.1.2. Modo interativo

  * 2.2. O interpretador e seu ambiente

    * 2.2.1. Edição de código-fonte

* 3. Uma introdução informal ao Python

  * 3.1. Usando Python como uma calculadora

    * 3.1.1. Números

    * 3.1.2. Texto

    * 3.1.3. Listas

  * 3.2. Primeiros passos para a programação

* 4. Mais ferramentas de controle de fluxo

  * 4.1. Instruções "if"

  * 4.2. Instruções "for"

  * 4.3. A função "range()"

  * 4.4. Instruções "break" e "continue"

  * 4.5. Cláusulas "else" em laços

  * 4.6. Instruções "pass"

  * 4.7. Instruções "match"

  * 4.8. Definindo funções

  * 4.9. Mais sobre definição de funções

    * 4.9.1. Argumentos com valor padrão

    * 4.9.2. Argumentos nomeados

    * 4.9.3. Parâmetros especiais

      * 4.9.3.1. Argumentos posicional-ou-nomeados

      * 4.9.3.2. Parâmetros somente-posicionais

      * 4.9.3.3. Argumentos somente-nomeados

      * 4.9.3.4. Exemplos de funções

      * 4.9.3.5. Recapitulando

    * 4.9.4. Listas de argumentos arbitrárias

    * 4.9.5. Desempacotando listas de argumentos

    * 4.9.6. Expressões lambda

    * 4.9.7. Strings de documentação

    * 4.9.8. Anotações de função

  * 4.10. Intermezzo: estilo de codificação

* 5. Estruturas de dados

  * 5.1. Mais sobre listas

    * 5.1.1. Usando listas como pilhas

    * 5.1.2. Usando listas como filas

    * 5.1.3. Compreensões de lista

    * 5.1.4. Compreensões de lista aninhadas

    * 5.1.5. Desempacotamento em Listas e Compreensões de Lista

  * 5.2. A instrução "del"

  * 5.3. Tuplas e Sequências

  * 5.4. Conjuntos

  * 5.5. Dicionários

  * 5.6. Técnicas de iteração

  * 5.7. Mais sobre condições

  * 5.8. Comparando sequências e outros tipos

* 6. Módulos

  * 6.1. Mais sobre módulos

    * 6.1.1. Executando módulos como scripts

    * 6.1.2. O caminho de busca dos módulos

    * 6.1.3. Arquivos Python "compilados"

  * 6.2. Módulos padrões

  * 6.3. A função "dir()"

  * 6.4. Pacotes

    * 6.4.1. Importando * de um pacote

    * 6.4.2. Referências em um mesmo pacote

* 7. Entrada e saída

  * 7.1. Formatação de saída mais elaborada

    * 7.1.1. Literais de string formatados

    * 7.1.2. O método format() de strings

    * 7.1.3. Formatação manual de strings

    * 7.1.4. Formatação de strings à moda antiga

  * 7.2. Lendo e escrevendo arquivos

    * 7.2.1. Métodos de objetos arquivo

    * 7.2.2. Gravando dados estruturados com "json"

* 8. Erros e exceções

  * 8.1. Erros de sintaxe

  * 8.2. Exceções

  * 8.3. Tratamento de exceções

  * 8.4. Levantando exceções

  * 8.5. Encadeamento de exceções

  * 8.6. Exceções definidas pelo usuário

  * 8.7. Definindo ações de limpeza

  * 8.8. Ações de limpeza predefinidas

  * 8.9. Criando e tratando várias exceções não relacionadas

  * 8.10. Enriquecendo exceções com notas

* 9. Classes

  * 9.1. Uma palavra sobre nomes e objetos

  * 9.2. Escopos e espaços de nomes do Python

    * 9.2.1. Exemplo de escopos e espaço de nomes

  * 9.3. Uma primeira olhada nas classes

    * 9.3.1. Sintaxe da definição de classe

    * 9.3.2. Objetos classe

    * 9.3.3. Objetos instância

    * 9.3.4. Objetos método

    * 9.3.5. Variáveis de classe e instância

  * 9.4. Observações aleatórias

  * 9.5. Herança

    * 9.5.1. Herança múltipla

  * 9.6. Variáveis privadas

  * 9.7. Curiosidades e conclusões

  * 9.8. Iteradores

  * 9.9. Geradores

  * 9.10. Expressões geradoras

* 10. Um breve passeio pela biblioteca padrão

  * 10.1. Interface com o sistema operacional

  * 10.2. Caracteres curinga

  * 10.3. Argumentos de linha de comando

  * 10.4. Redirecionamento de erros e encerramento do programa

  * 10.5. Reconhecimento de padrões em strings

  * 10.6. Matemática

  * 10.7. Acesso à internet

  * 10.8. Data e hora

  * 10.9. Compressão de dados

  * 10.10. Medição de desempenho

  * 10.11. Controle de qualidade

  * 10.12. Baterias incluídas

* 11. Um breve passeio pela biblioteca padrão --- parte II

  * 11.1. Formatando a saída

  * 11.2. Usando templates

  * 11.3. Trabalhando com formatos binários de dados

  * 11.4. Multi-threading

  * 11.5. Gerando logs

  * 11.6. Referências fracas

  * 11.7. Ferramentas para trabalhar com listas

  * 11.8. Aritmética decimal com ponto flutuante

* 12. Ambientes virtuais e pacotes

  * 12.1. Introdução

  * 12.2. Criando ambientes virtuais

  * 12.3. Gerenciando pacotes com o pip

* 13. E agora?

* 14. Edição de entrada interativa e substituição de histórico

  * 14.1. Tab completion e histórico de edição

  * 14.2. Alternativas ao interpretador interativo

* 15. Aritmética de ponto flutuante: problemas e limitações

  * 15.1. Erro de representação

* 16. Anexo

  * 16.1. Modo interativo

    * 16.1.1. Tratamento de erros

    * 16.1.2. Scripts Python executáveis

    * 16.1.3. Arquivo de inicialização do modo interativo

    * 16.1.4. Módulos de customização
