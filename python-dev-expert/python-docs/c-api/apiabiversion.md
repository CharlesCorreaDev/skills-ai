API e Versionamento de ABI
**************************


Constantes de versão de tempo de construção
===========================================

O CPython expõe seu número de versão nas seguintes macros. Note que
estes correspondem ao código da versão com a qual está **construída**.
Veja "Py_Version" para a versão usada em **tempo de execução**.

Veja C API and ABI Stability para uma discussão da estabilidade da API
e ABI através das versões.

PY_MAJOR_VERSION

   O "3" em "3.4.1a2".

PY_MINOR_VERSION

   O "4" em "3.4.1a2".

PY_MICRO_VERSION

   O "1" em "3.4.1a2".

PY_RELEASE_LEVEL

   O "a" em "3.4.1a2". Isto pode ser "0xA" para alfa, "0xB" para beta,
   "0xC" para o candidato a lançamento ou "0xF" para final.

   Para uma maior clareza, os valores estão disponíveis como macros:
   "PY_RELEASE_LEVEL_ALPHA" ("0xA"), "PY_RELEASE_LEVEL_BETA" ("0xB"),
   "PY_RELEASE_LEVEL_GAMMA" ("0xC") e "PY_RELEASE_LEVEL_FINAL"
   ("0xF").

PY_RELEASE_SERIAL

   O "2" em "3.4.1a2". Zero para os lançamentos finais.

PY_VERSION_HEX

   O número da versão do Python codificado em um único inteiro.
   Consulte "Py_PACK_FULL_VERSION()" para obter detalhes sobre a
   codificação.

   Use isso para comparações numéricas como, por exemplo, "#if
   PY_VERSION_HEX >= ...".

PY_VERSION

   A versão do Python como uma string, por exemplo, ""3.4.1a2"".

Essas macros estão definidas em Include/patchlevel.h.


Versão de tempo de execução
===========================

const unsigned long Py_Version
    * Parte da ABI Estável desde a versão 3.11.*

   O número da versão do tempo de execução do Python codificado em um
   único inteiro constante. Consulte "Py_PACK_FULL_VERSION()" para
   obter detalhes sobre a codificação. Contém a versão do Python usada
   em tempo de execução.

   Use isso para comparações numéricas como, por exemplo, "if
   (Py_Version >= ...)".

   Adicionado na versão 3.11.


Macros de empacotamento de bits
===============================

uint32_t Py_PACK_FULL_VERSION(int major, int minor, int micro, int release_level, int release_serial)
    * Parte da ABI Estável desde a versão 3.14.*

   Retorna a versão fornecida, codificada como um único inteiro de 32
   bits com a seguinte estrutura:

   +--------------------+---------+------------------+-------------+---------------+--------------+
   | Argumento          | Nº de   | Máscara de bits  | Deslocamen  | Exemplo de valores           |
   |                    | bits    |                  | to de bits  |                              |
   |                    |         |                  |             +---------------+--------------+
   |                    |         |                  |             | "3.4.1a2"     | "3.10.0"     |
   |                    |         |                  |             |               |              |
   |====================|=========|==================|=============|===============|==============|
   | *major*            | 8       | "0xFF000000"     | 24          | "0x03"        | "0x03"       |
   +--------------------+---------+------------------+-------------+---------------+--------------+
   | *minor*            | 8       | "0x00FF0000"     | 16          | "0x04"        | "0x0A"       |
   +--------------------+---------+------------------+-------------+---------------+--------------+
   | *micro*            | 8       | "0x0000FF00"     | 8           | "0x01"        | "0x00"       |
   +--------------------+---------+------------------+-------------+---------------+--------------+
   | *release_level*    | 4       | "0x000000F0"     | 4           | "0xA"         | "0xF"        |
   +--------------------+---------+------------------+-------------+---------------+--------------+
   | *release_serial*   | 4       | "0x0000000F"     | 0           | "0x2"         | "0x0"        |
   +--------------------+---------+------------------+-------------+---------------+--------------+

   Por exemplo:

   +---------------+--------------------------------------+-------------------+
   | Versão        | Argumentos de "Py_PACK_FULL_VERSION" | Versão codificada |
   |===============|======================================|===================|
   | "3.4.1a2"     | "(3, 4, 1, 0xA, 2)"                  | "0x030401a2"      |
   +---------------+--------------------------------------+-------------------+
   | "3.10.0"      | "(3, 10, 0, 0xF, 0)"                 | "0x030a00f0"      |
   +---------------+--------------------------------------+-------------------+

   Bits fora do intervalo nos argumentos são ignorados. Ou seja, a
   macro pode ser definida como:

      #ifndef Py_PACK_FULL_VERSION
      #define Py_PACK_FULL_VERSION(X, Y, Z, LEVEL, SERIAL) ( \
         (((X) & 0xff) << 24) |                              \
         (((Y) & 0xff) << 16) |                              \
         (((Z) & 0xff) << 8) |                               \
         (((LEVEL) & 0xf) << 4) |                            \
         (((SERIAL) & 0xf) << 0))
      #endif

   "Py_PACK_FULL_VERSION" é principalmente uma macro, destinada ao uso
   em diretivas "#if", mas também está disponível como uma função
   exportada.

   Adicionado na versão 3.14.

uint32_t Py_PACK_VERSION(int major, int minor)
    * Parte da ABI Estável desde a versão 3.14.*

   Equivalente a "Py_PACK_FULL_VERSION(major, minor, 0, 0, 0)". O
   resultado não corresponde a nenhuma versão do Python, mas é útil em
   comparações numéricas.

   Adicionado na versão 3.14.
