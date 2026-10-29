# Constantes predefinidas

> **Fonte / Source:** https://www.php.net/manual/pt_BR/password.constants.php

---

# Constantes predefinidas

As constantes abaixo estão sempre disponíveis como parte do núcleo do PHP.

**`PASSWORD_BCRYPT`** ([string](language.types.string.md))
:   **`PASSWORD_BCRYPT`** é usada para criar novas hashes
    de senha usando o algoritmo **`CRYPT_BLOWFISH`**.

    Sempre terminará com um hash usando o formato de criptografia "$2y$",
    com 60 caracteres.

    Opções suportadas:

    - `salt` ([string](language.types.string.md)) - para fornecer manualmente um salt que será usado ao fazer o hash da senha.
      Observe que isso irá substituir e evitar que um salt seja gerado automaticamente.

      Se omitido, um salt aleatório será gerado pela função [password\_hash()](function.password-hash.md) para
      cada senha sofrendo hash. Esse é o modo de operação desejado
      e a partir do PHP 7.0.0 a opção salt foi descontinuada.
    - `cost` ([int](language.types.integer.md)) - indica o custo de algoritmo que deve ser usado.
      Exemplos desses valores podem ser encontrados na página da função [crypt()](function.crypt.md).

      Se omitido, um valor padrão de `12` será usado. Esta é uma boa
      base de custo, mas pode-se considerar aumentar esse valor dependendo do equipamento.

**`PASSWORD_BCRYPT_DEFAULT_COST`** ([int](language.types.integer.md))
:   Custo algorítmico padrão usado por [password\_hash()](function.password-hash.md) ao
    fazer hash de senhas com **`PASSWORD_BCRYPT`**.

    Disponível a partir do PHP 7.0.0.

**`PASSWORD_ARGON2I`** ([string](language.types.string.md))
:   **`PASSWORD_ARGON2I`** é utilizado para criar novos hashes
    utilizando o algoritmo Argon2i.

    Opções:

    - `memory_cost` ([int](language.types.integer.md)) - Memória máxima (em bytes) que poderá
      ser utilizada para calcular o hash Argon2. Padrão: **`PASSWORD_ARGON2_DEFAULT_MEMORY_COST`**.
    - `time_cost` ([int](language.types.integer.md)) - Número de iterações (passagens) usadas
      para calcular o hash Argon2. Padrão: **`PASSWORD_ARGON2_DEFAULT_TIME_COST`**.
    - `threads` ([int](language.types.integer.md)) - Número de threads utilizada para calcular
      o hash Argon2. Padrão: **`PASSWORD_ARGON2_DEFAULT_THREADS`**.
      Somente disponível com libargon2, mas não na implementação libsodium.

    Disponível a partir do PHP 7.2.0.

**`PASSWORD_ARGON2ID`** ([string](language.types.string.md))
:   **`PASSWORD_ARGON2ID`** é utilizado para criar novos hashes de
    senha com o algoritmo Argon2id. Ele suporta as mesmas opções de
    [**`PASSWORD_ARGON2I`**](password.constants.md#constant.password-argon2i).

    Disponível a partir do PHP 7.3.0.

**`PASSWORD_ARGON2_DEFAULT_MEMORY_COST`** ([int](language.types.integer.md))
:   Quantidade de memória padrão, em quilobytes (KiB) que será utilizada
    para calcular um hash.

    Disponível a partir do PHP 7.2.0.

**`PASSWORD_ARGON2_DEFAULT_TIME_COST`** ([int](language.types.integer.md))
:   Número padrão de iterações (passagens) usadas para calcular um hash.

    Disponível a partir do PHP 7.2.0.

**`PASSWORD_ARGON2_DEFAULT_THREADS`** ([int](language.types.integer.md))
:   Número de threads padrão qual a Argon2lib irá utilizar.
    Não disponível na implementação libsodium.

    Disponível a partir do PHP 7.2.0.

**`PASSWORD_ARGON2_PROVIDER`** ([string](language.types.string.md))
:   Disponível a partir do PHP 7.4.0.

**`PASSWORD_DEFAULT`** ([string](language.types.string.md))
:   O algoritmo padrão a ser usado para fazer o hash se nenhum algoritmo for fornecido.
    Ele pode mudar com as novas versões do PHP quando algoritmos de hash novos e mais
    fortes forem suportados.

    É importante notar que ao longo do tempo essa constante pode mudar.
    Assim sendo, deve-se estar ciente que o comprimento do hash resultante
    pode mudar.
    Portanto, ao usar **`PASSWORD_DEFAULT`**, o hash
    resultante deve ser armazanado de uma forma que possa armazenar hashes arbitrários,
    o comprimento recomendado é de `255` bytes.

    Atualmente é um sinônimo de **`PASSWORD_BCRYPT`**.

##### Registro de Alterações

| Versão | Descrição |
| --- | --- |
| 7.4.0 | Os valores informados como IDs de algoritimo (**`PASSWORD_BCRYPT`**, **`PASSWORD_ARGON2I`**, **`PASSWORD_ARGON2ID`** e **`PASSWORD_DEFAULT`**) agora são do tipo [string](language.types.string.md). Anteriormente eles eram do tipo [int](language.types.integer.md). |

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
