API do PyHash
*************

Veja também o membro "PyTypeObject.tp_hash" e Hashing de tipos
numéricos.

type Py_hash_t

   Tipo de valor do hash: inteiro com sinal.

   Adicionado na versão 3.2.

type Py_uhash_t

   Tipo de valor do hash: inteiro sem sinal.

   Adicionado na versão 3.2.

Py_HASH_ALGORITHM

   Um valor numérico que indica o algoritmo de hash para "str",
   "bytes" e "memoryview".

   O nome do algoritmo é exposto por "sys.hash_info.algorithm".

   Adicionado na versão 3.4.

Py_HASH_FNV
Py_HASH_SIPHASH24
Py_HASH_SIPHASH13
Py_HASH_EXTERNAL

   Valores numéricos a serem comparados com "Py_HASH_ALGORITHM" para
   determinar qual algoritmo é usado para o hashing. O algoritmo de
   hash embutido pode ser configurado através da opção "--with-hash-
   algorithm" do comando configure.

   "Py_HASH_EXTERNAL" tem o valor "0" e indica uma implementação de
   hash fornecida pela aplicação que embutir o Python; veja
   "PyHash_Func".

   Adicionado na versão 3.4: Adiciona "Py_HASH_FNV",
   "Py_HASH_SIPHASH24" e "Py_HASH_EXTERNAL".

   Adicionado na versão 3.11: Adiciona "Py_HASH_SIPHASH13".

Py_HASH_CUTOFF

   Buffers de comprimento no intervalo "[1, Py_HASH_CUTOFF)" são
   hasheados usando DJBX33A em vez do algoritmo descrito por
   "Py_HASH_ALGORITHM".

   * Uma "Py_HASH_CUTOFF" de 0 desabilita a otimização.

   * "Py_HASH_CUTOFF" deve ser não-negativo ou menor ou igual a 7.

   Plataformas de 32 bits devem usar um limite de corte menor do que
   plataformas de 64 bits, pois é mais fácil criar strings que
   colidam. Um limite de corte de 7 em plataformas de 64 bits e 5 em
   plataformas de 32 bits deve fornecer uma margem de segurança
   adequada.

   Isso corresponde à constante "sys.hash_info.cutoff".

   Adicionado na versão 3.4.

PyHASH_MODULUS

   O primo de Mersenne "P = 2**n -1", usado para esquema de hash
   numérico.

   Isso corresponde à constante "sys.hash_info.modulus".

   Adicionado na versão 3.13.

PyHASH_BITS

   O expoente "n" de "P" em "PyHASH_MODULUS".

   Adicionado na versão 3.13.

PyHASH_MULTIPLIER

   Multiplicador de primo usado em strings e vários outros hashes.

   Adicionado na versão 3.13.

PyHASH_INF

   O valor de hash retornado para um infinito positivo.

   Isso corresponde à constante "sys.hash_info.inf".

   Adicionado na versão 3.13.

PyHASH_IMAG

   O multiplicador usado para a parte imaginária de um número
   complexo.

   Isso corresponde à constante "sys.hash_info.imag".

   Adicionado na versão 3.13.

type PyHash_FuncDef

   Definição de função de hash usada por "PyHash_GetFuncDef()".

   Py_hash_t (*const hash)(const void*, Py_ssize_t)

      Função de hash.

   const char *name

      Nome de função hash (string codificada em UTF-8).

      Isso corresponde à constante "sys.hash_info.algorithm".

   const int hash_bits

      Tamanho interno do valor do hash em bits.

      Isso corresponde à constante "sys.hash_info.hash_bits".

   const int seed_bits

      Tamanho da entrada de seed em bits.

      Isso corresponde à constante "sys.hash_info.seed_bits".

   Adicionado na versão 3.4.

PyHash_FuncDef PyHash_Func

   Quando o Python é construído com "Py_HASH_ALGORITHM" definido como
   "Py_HASH_EXTERNAL", a aplicação que embute o Python deve definir
   esta variável para fornecer uma implementação de hash em vez de
   usar um dos algoritmos de hash embutidos do Python.

   Adicionado na versão 3.4.

   Descontinuado desde a versão 3.15, será removido na versão 3.19:
   Use um dos algoritmos de hash embutidos em vez disso.

PyHash_FuncDef *PyHash_GetFuncDef(void)

   Obtém a definição de função de hash.

   Ver também:

     **PEP 456** "Algoritmo de hash seguro e intercambiável".

   Adicionado na versão 3.4.

Py_hash_t Py_HashPointer(const void *ptr)

   Hash de um valor de ponteiro: processa o valor do ponteiro como um
   inteiro (converte-o para "uintptr_t" internamente). O ponteiro não
   é desreferenciado.

   A função não pode falhar: ela não pode retornar "-1".

   Adicionado na versão 3.13.

Py_hash_t Py_HashBuffer(const void *ptr, Py_ssize_t len)

   Calcula e retorna o valor de hash de um buffer de *len* bytes,
   começando no endereço *ptr*. O hash tem garantia de corresponder ao
   de "bytes", "memoryview" e outros objetos embutidos que implementam
   o protocolo de buffer.

   Usa esta função para implementar hash para objetos imutáveis cuja
   função "tp_richcompare" compara ao buffer de outro objeto.

   *len* deve ser maior que ou igual a "0".

   Esta função sempre tem sucesso.

   Adicionado na versão 3.14.

Py_hash_t PyObject_GenericHash(PyObject *obj)

   Função de hash genérica que deve ser colocada no slot "tp_hash" de
   um objeto de tipo. Seu resultado depende apenas da identidade do
   objeto.

   No CPython, é equivalente a "Py_HashPointer()".

   Adicionado na versão 3.13.
