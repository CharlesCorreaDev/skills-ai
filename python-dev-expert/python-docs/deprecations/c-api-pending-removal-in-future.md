Remoção pendente em versões futuras
***********************************

As APIs a seguir foram descontinuadas e serão removidas, embora
atualmente não haja uma data agendada para sua remoção.

* "Py_TPFLAGS_HAVE_FINALIZE": Desnecessária desde o Python 3.8.

* "PyErr_Fetch()": Use "PyErr_GetRaisedException()".

* "PyErr_NormalizeException()": Use "PyErr_GetRaisedException()".

* "PyErr_Restore()": Use "PyErr_SetRaisedException()".

* "PyModule_GetFilename()": Use "PyModule_GetFilenameObject()".

* "PyOS_AfterFork()": Use "PyOS_AfterFork_Child()".

* "PySlice_GetIndicesEx()": Use "PySlice_Unpack()" e
  "PySlice_AdjustIndices()".

* "PyUnicode_READY()": Desnecessário desde o Python 3.12

* "PyErr_Display()": Use "PyErr_DisplayException()".

* "_PyErr_ChainExceptions()": Use "_PyErr_ChainExceptions1()".

* O membro "PyBytesObject.ob_shash": chame "PyObject_Hash()".

* API do Thread Local Storage (TLS):

  * "PyThread_create_key()": Use "PyThread_tss_alloc()".

  * "PyThread_delete_key()": Use "PyThread_tss_free()".

  * "PyThread_set_key_value()": Use "PyThread_tss_set()".

  * "PyThread_get_key_value()": Use "PyThread_tss_get()".

  * "PyThread_delete_key_value()": Use "PyThread_tss_delete()".

  * "PyThread_ReInitTLS()": Desnecessário desde o Python 3.7.
