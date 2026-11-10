Remoção pendente no Python 3.20
*******************************

* "_PyObject_CallMethodId()", "_PyObject_GetAttrId()" e
  "_PyUnicode_FromId()" foram descontinuadas desde o 3.15 e serão
  removidas na versão 3.20. Em vez delas, use
  "PyUnicode_InternFromString()" and armazene em cache o resultado no
  estado do módulo e chame "PyObject_CallMethod()" ou
  "PyObject_GetAttr()". (Contribuição de Victor Stinner em gh-141049.)

* O campo "cval" em "PyComplexObject" (gh-128813). Use
  "PyComplex_AsCComplex()" e "PyComplex_FromCComplex()" para converter
  um número complexo Python de/para a representação C de "Py_complex".

* Macros "Py_MATH_PIl" e "Py_MATH_El".
