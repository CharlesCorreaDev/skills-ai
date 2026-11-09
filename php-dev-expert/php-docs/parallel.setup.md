# Instalação

> **Fonte / Source:** https://www.php.net/manual/pt_BR/parallel.setup.php

---

# Instalação

### Dependências

parallel requer uma compilação de PHP com ZTS (Zend Thread Safety) habilitado
(**--enable-zts**, ou em sistemas não-Windows anteriores ao PHP 8.0.0,
**--enable-maintainer-zts**)

**Cuidado**

Zend Thread Safety não pode ser habilitado após a construção; é uma opção de configuração de tempo de construção.

parallel deve ser construído em qualquer lugar onde haja um cabeçalho Posix Threads funcional (pthread.h) e uma compilação ZTS de PHP, incluindo Windows (usando o projeto pthread-w32 do redhat).

### Instalação

Versões do parallel são hospedadas pelo PECL e o código-fonte pelo
[» github](https://github.com/krakjoe/parallel),
o caminho mais fácil para instalação é a rota normal do PECL:
[» https://pecl.php.net/package/parallel](https://pecl.php.net/package/parallel).

Usuários do Windows podem baixar binários de versão pré-construídos no site [» PECL](https://pecl.php.net/package/parallel).

**Cuidado**

Usuários do Windows precisam realizar a etapa adicional de incluir os arquivos pthreadVC?.dll (distribuído com as versões do Windows) ao seu PATH.

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
