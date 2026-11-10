descontinuações suave
*********************

Não há planos para remover APIs *suavemente descontinuadas*

* "re.match()" e "re.Pattern.match()" estão agora *suavemente
  descontinuado*s em favor das novas APIs "re.prefixmatch()" e
  "re.Pattern.prefixmatch()", adicionadas como nomes alternativos e
  mais explícitos. Elas visam reduzir a confusão sobre o significado
  de *match*, seguindo o princípio do Zen do Python: *"Explícito é
  melhor que implícito"*. A maioria das bibliotecas de expressões
  regulares de outras linguagens utiliza uma API chamada *match* para
  a funcionalidade que o Python sempre chamou de *search*.

  **Não** planejamos remover o nome mais antigo "match()", pois ele
  tem sido utilizado no código há mais de 30 anos. Códigos que
  oferecem suporte a versões mais antigas do Python devem continuar
  utilizando "match()", enquanto novos códigos devem dar preferência a
  "prefixmatch()". Veja prefixmatch() vs. match().

  (Contribuição de Gregory P. Smith em gh-86519 e Hugo van Kemenade em
  gh-148100.)

* O uso dos códigos de tipo de formato "'F'" e "'D'" do módulo
  "struct" está agora *suavemente descontinuado* em favor das formas
  de duas letras "'Zf'" e "'Zd'". (Contribuição de Sergey B Kirpichev
  em gh-121249.)
