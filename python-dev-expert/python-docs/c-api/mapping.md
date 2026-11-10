Protocolo de mapeamento
***********************

Veja também "PyObject_GetItem()", "PyObject_SetItem()" e
"PyObject_DelItem()".

int PyMapping_Check(PyObject *o)
    * Parte da ABI Estável.*

   Retorna "1" se o objeto fornece protocolo de mapeamento ou suporta
   fatiamento e "0" caso contrário. Note que ele retorna "1" para
   classes Python com um método "__getitem__()" visto que geralmente é
   impossível determinar a que tipo de chaves a classe tem suporte.
   Esta função sempre tem sucesso.

Py_ssize_t PyMapping_Size(PyObject *o)
Py_ssize_t PyMapping_Length(PyObject *o)
    * Parte da ABI Estável.*

   Retorna o número de chaves no objeto *o* em caso de sucesso e "-1"
   em caso de falha. Isso é equivalente à expressão Python "len(o)".

PyObject *PyMapping_GetItemString(PyObject *o, const char *key)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   É o mesmo que "PyObject_GetItem()", mas *key* é especificada como
   uma string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

int PyMapping_GetOptionalItem(PyObject *obj, PyObject *key, PyObject **result)
    * Parte da ABI Estável desde a versão 3.13.*

   Variante de "PyObject_GetItem()" que não levanta "KeyError" se a
   chave não for encontrada.

   Se a chave for encontrada, retorna "1" e define **result* como uma
   nova *referência forte* para o valor correspondente. Se a chave não
   for encontrada, retorna "0" e define **result* como "NULL"; o
   "KeyError" é silenciado. Se um erro diferente de "KeyError" for
   levanta, retorna "-1" e define **result* como "NULL".

   Adicionado na versão 3.13.

int PyMapping_GetOptionalItemString(PyObject *obj, const char *key, PyObject **result)
    * Parte da ABI Estável desde a versão 3.13.*

   É o mesmo que "PyMapping_GetOptionalItem()", mas *key* é
   especificado como uma string de bytes codificada em UTF-8 const
   char*, em vez de um PyObject*.

   Adicionado na versão 3.13.

int PyMapping_SetItemString(PyObject *o, const char *key, PyObject *v)
    * Parte da ABI Estável.*

   É o mesmo que "PyObject_SetItem()", mas *key* é especificada como
   uma string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

int PyMapping_DelItem(PyObject *o, PyObject *key)

   Este é um apelido de "PyObject_DelItem()".

int PyMapping_DelItemString(PyObject *o, const char *key)

   É o mesmo que "PyObject_DelItem()", mas *key* é especificada como
   uma string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

int PyMapping_HasKeyWithError(PyObject *o, PyObject *key)
    * Parte da ABI Estável desde a versão 3.13.*

   Retorna "1" se o objeto de mapeamento tiver a chave *key* e "0"
   caso contrário. Isso é equivalente à expressão Python "key in o".
   Em caso de falha, retorna "-1".

   Adicionado na versão 3.13.

int PyMapping_HasKeyStringWithError(PyObject *o, const char *key)
    * Parte da ABI Estável desde a versão 3.13.*

   É o mesmo que "PyMapping_HasKeyWithError()", mas *key* é
   especificada como uma string de bytes const char* codificada em
   UTF-8, em vez de um PyObject*.

   Adicionado na versão 3.13.

int PyMapping_HasKey(PyObject *o, PyObject *key)
    * Parte da ABI Estável.*

   Retorna "1" se o objeto de mapeamento tiver a chave *key* e "0"
   caso contrário. Isso é equivalente à expressão Python "key in o".
   Esta função sempre tem sucesso.

   Nota:

     As exceções que ocorrem quando este construtor chama o método
     "__getitem__()" são silenciosamente ignoradas. Para o tratamento
     adequado de erros, use "PyMapping_HasKeyWithError()",
     "PyMapping_GetOptionalItem()" ou "PyObject_GetItem()" em vez
     disso.

int PyMapping_HasKeyString(PyObject *o, const char *key)
    * Parte da ABI Estável.*

   É o mesmo que "PyMapping_HasKey()", mas *key* é especificada como
   uma string de bytes const char* codificada em UTF-8, em vez de um
   PyObject*.

   Nota:

     As exceções que ocorrem quando este construtor chama o método
     "__getitem__()" ou ao criar o objeto temporário "str" são
     silenciosamente ignoradas. Para o tratamento adequado de erros,
     use "PyMapping_HasKeyStringWithError()",
     "PyMapping_GetOptionalItemString()" ou
     "PyMapping_GetItemString()" em vez disso.

PyObject *PyMapping_Keys(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Em caso de sucesso, retorna uma lista das chaves no objeto *o*. Em
   caso de falha, retorna "NULL".

   Alterado na versão 3.7: Anteriormente, a função retornava uma lista
   ou tupla.

PyObject *PyMapping_Values(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Em caso de sucesso, retorna uma lista dos valores no objeto *o*. Em
   caso de falha, retorna "NULL".

   Alterado na versão 3.7: Anteriormente, a função retornava uma lista
   ou tupla.

PyObject *PyMapping_Items(PyObject *o)
    *Retorna valor: Nova referência.** Parte da ABI Estável.*

   Em caso de sucesso, retorna uma lista dos itens no objeto *o*, onde
   cada item é uma tupla contendo um par de valores-chave. Em caso de
   falha, retorna "NULL".

   Alterado na versão 3.7: Anteriormente, a função retornava uma lista
   ou tupla.
