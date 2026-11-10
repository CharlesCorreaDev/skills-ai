Remoção pendente no Python 3.19
*******************************

* "ctypes":

  * Troca implícita para o layout de estrutura compatível com MSVC
    definindo "_pack_", mas não "_layout_" em plataformas não Windows.

* "hashlib":

  * Em construtores de funções de hash, como "new()", ou nos
    construtores nomeados diretamente pelo algoritmo de hash, como
    "md5()" e "sha256()", o parâmetro opcional de dados iniciais
    também podia ser passado como um argumento nomeado "data=" ou
    "string=" em várias implementações do "hashlib".

    O suporte ao nome do argumento nomeado "string" está agora
    descontinuado e previsto para ser removido no Python 3.19.

    Antes do Python 3.13, o parâmetro nomeado "string" não era
    suportado corretamente, dependendo da implementação de funções de
    hash do backend. Dê preferência a passar os dados iniciais como um
    argumento posicional para garantir a máxima retrocompatibilidade.

* "http.cookies":

  * "http.cookies.Morsel.js_output()" está descontinuado e será
    removido no Python 3.19.

  * "http.cookies.BaseCookie.js_output()" está descontinuado e será
    removido no Python 3.19.

* "imaplib":

  * A alteração de "IMAP4.file" agora está descontinuado e programado
    para remoção no Python 3.19. Esta propriedade agora não é
    utilizada e alterar seu valor não fecha automaticamente o arquivo
    atual.

    Antes do Python 3.14, essa propriedade era usada para implementar
    os métodos "read()" e "readline()" correspondentes para "IMAP4",
    mas isso não ocorre mais desde então.
