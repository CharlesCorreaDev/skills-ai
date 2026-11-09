# Dependências

> **Fonte / Source:** https://www.php.net/manual/pt_BR/oci8.requirements.php

---

## Dependências

OCI8 3.0 é incluído com o PHP 8. Também está disponível em [» PECL](https://pecl.php.net/). Para
o PHP 7, use OCI8 2.2 de [» PECL](https://pecl.php.net/). OCI8 requer Oracle
10*g* ou bibliotecas de cliente Oracle mais recentes.

Se o banco de dados Oracle estiver na mesma máquina que o PHP, o software do banco de dados
já conterá os arquivos de biblioteca e de cabeçalho necessários. Quando o PHP estiver um uma
máquina diferente, use as bibliotecas
[» Oracle Instant Client](https://www.oracle.com/database/technologies/instant-client.html) gratuitas.

Para usar o Oracle Instant Client, instale o arquivo ZIP, pacote RPM
ou pacote DMG do Oracle Instant Client `Basic`
ou `Basic Light`. Ao compilar o OCI8 a partir do código-fonte, instale também
o `SDK` do Instant Client.

Deve-se executar o PHP com mesma versão ou uma mais recente das bibliotecas
Oracle com as quais o OCI8 foi compilado.

> **Nota**:
>
> A interoperabilidade de rede cliente-servidor padrão da Oracle permite conexões
> entre diferentes versões do Oracle Client e do Oracle Database. Para
> configurações certificadas, consulte o Doc ID 207303.1 do suporte da Oracle. Em
> resumo, as versões Oracle Client 19, 18 e 12.2 podem se conectar ao Oracle Database 11.2
> ou superior. O Oracle Client 12.1 pode se conectar ao Oracle Database 10.2 ou
> superior. O Oracle Client 11.2 pode se conectar ao Oracle Database 9.2 ou superior.

> **Nota**:
>
> O suporte completo ao recurso OCI8 está disponível apenas ao usar as versões
> mais recentes das bibliotecas cliente e do banco de dados Oracle.

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
