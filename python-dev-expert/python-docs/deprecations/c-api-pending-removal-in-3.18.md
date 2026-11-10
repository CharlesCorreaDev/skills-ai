Remoção pendente no Python 3.18
*******************************

* As seguintes funções privadas estão descontinuado e planejadas para
  remoção no Python 3.18:

  * "_PyBytes_Join()": use "PyBytes_Join()".

  * "_PyDict_GetItemStringWithError()": use
    "PyDict_GetItemStringRef()".

  * "_PyDict_Pop()": use "PyDict_Pop()".

  * "_PyLong_Sign()": use "PyLong_GetSign()".

  * "_PyLong_FromDigits()" e "_PyLong_New()": use
    "PyLongWriter_Create()".

  * "_PyThreadState_UncheckedGet()": use
    "PyThreadState_GetUnchecked()".

  * "_PyUnicode_AsString()": use "PyUnicode_AsUTF8()".

  * "_PyUnicodeWriter_Init()": substitua
    "_PyUnicodeWriter_Init(&writer)" por "writer =
    PyUnicodeWriter_Create(0)".

  * "_PyUnicodeWriter_Finish()": substitua
    "_PyUnicodeWriter_Finish(&writer)" por
    "PyUnicodeWriter_Finish(writer)".

  * "_PyUnicodeWriter_Dealloc()": substitua
    "_PyUnicodeWriter_Dealloc(&writer)" por
    "PyUnicodeWriter_Discard(writer)".

  * "_PyUnicodeWriter_WriteChar()": substituta
    "_PyUnicodeWriter_WriteChar(&writer, ch)" com
    "PyUnicodeWriter_WriteChar(writer, ch)".

  * "_PyUnicodeWriter_WriteStr()": substitua
    "_PyUnicodeWriter_WriteStr(&writer, str)" por
    "PyUnicodeWriter_WriteStr(writer, str)".

  * "_PyUnicodeWriter_WriteSubstring()": substitua
    "_PyUnicodeWriter_WriteSubstring(&writer, str, start, end)" por
    "PyUnicodeWriter_WriteSubstring(writer, str, start, end)".

  * "_PyUnicodeWriter_WriteASCIIString()": substitua
    "_PyUnicodeWriter_WriteASCIIString(&writer, str, size)" por
    "PyUnicodeWriter_WriteASCII(writer, str, size)".

  * "_PyUnicodeWriter_WriteLatin1String()": substitua
    "_PyUnicodeWriter_WriteLatin1String(&writer, str, size)"
    decodificando a string com "PyUnicode_DecodeLatin1()", gravando o
    resultado com "PyUnicodeWriter_WriteStr()" e liberando o resultado
    com "Py_DECREF()".

  * "_PyUnicodeWriter_Prepare()": (sem substituto).

  * "_PyUnicodeWriter_PrepareKind()": (sem substituto).

  * "_Py_HashPointer()": use "Py_HashPointer()".

  * "_Py_fopen_obj()": use "Py_fopen()".

  O projeto pythoncapi-compat pode ser usado para obter essas novas
  funções públicas no Python 3.13 e versões anteriores. (Contribuição
  de Victor Stinner em gh-128863.)
