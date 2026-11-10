API C do Expat
**************

O módulo "xml.parsers.expat" expõe funções selecionadas do Expat por
meio de sua cápsula "expat_CAPI". Isso permite que os módulos de
extensão utilizem a mesma biblioteca Expat que o Python. A interface é
declarada em "pyexpat.h", que deve ser incluída após o cabeçalho
"expat.h" do Expat.

PyExpat_CAPSULE_NAME

   O nome da cápsula que contém a API C Expat: ""pyexpat.expat_CAPI"".
   Passe isso para "PyCapsule_Import()" para obter um ponteiro para um
   "PyExpat_CAPI".

PyExpat_CAPI_MAGIC

   A string que identifica o layout de "PyExpat_CAPI". Antes de
   utilizar os ponteiros de função presentes na estrutura, verifique
   se o seu membro "magic" é igual a esta string (usando "strcmp()") e
   se o seu membro "size" é, no mínimo, sizeof(struct PyExpat_CAPI).

struct PyExpat_CAPI

   Tabela de ponteiros de função exportada por "xml.parsers.expat". A
   cápsula detém esta estrutura: trate-a como somente leitura e não a
   libere. Mantenha uma referência forte à cápsula enquanto estiver
   utilizando a tabela.

   Verifique os campos de compatibilidade, conforme descrito em
   "PyExpat_CAPI_MAGIC", antes de utilizar os ponteiros de função.

   char *magic

      Identificador da interface, define para "PyExpat_CAPI_MAGIC".

   int size

      Tamanho da estrutura em bytes, definido como "sizeof(struct
      PyExpat_CAPI)" pelo módulo "xml.parsers.expat" que criou a
      cápsula.

   int MAJOR_VERSION
   int MINOR_VERSION
   int MICRO_VERSION

      Números de versão major, minor e micro da biblioteca Expat
      utilizados por "xml.parsers.expat".

   void (*SetUnknownEncodingHandler)(XML_Parser parser, XML_UnknownEncodingHandler handler, void *encodingHandlerData)

      Ponteiro para XML_SetUnknownEncodingHandler. O manipulador pode
      definir uma exceção Python em caso de falha. O chamador deve
      verificar se ocorreu uma exceção Python após a análise.

   int (*DefaultUnknownEncodingHandler)(void *encodingHandlerData, const XML_Char *name, XML_Encoding *info)

      Manipulador de codificação desconhecida do Python para o Expat,
      utilizado com "XML_SetUnknownEncodingHandler". Ele emprega o
      registro de codecs do Python para preencher *info*. O argumento
      *encodingHandlerData* não é utilizado. A chamada deste
      manipulador requer um *estado de thread anexado*.

   Abaixo, estão listados os ponteiros para as funções correspondentes
   da Expat ou "NULL", caso não estejam disponíveis na versão da Expat
   utilizada pelo "xml.parsers.expat".

   Os nomes dos membros não incluem o prefixo "XML_"; por exemplo,
   "SetHashSalt" corresponde à função "XML_SetHashSalt" do Expat.
   Consulte a referência da API do Expat para obter detalhes sobre o
   comportamento desses membros e a versão mínima do Expat em que eles
   estão presentes.

   const XML_LChar *(*ErrorString)(enum XML_Error code)
   enum XML_Error (*GetErrorCode)(XML_Parser parser)
   XML_Size (*GetErrorColumnNumber)(XML_Parser parser)
   XML_Size (*GetErrorLineNumber)(XML_Parser parser)
   enum XML_Status (*Parse)(XML_Parser parser, const char *s, int len, int isFinal)
   XML_Parser (*ParserCreate_MM)(const XML_Char *encoding, const XML_Memory_Handling_Suite *memsuite, const XML_Char *namespaceSeparator)
   void (*ParserFree)(XML_Parser parser)
   void (*SetCharacterDataHandler)(XML_Parser parser, XML_CharacterDataHandler handler)
   void (*SetCommentHandler)(XML_Parser parser, XML_CommentHandler handler)
   void (*SetDefaultHandlerExpand)(XML_Parser parser, XML_DefaultHandler handler)
   void (*SetElementHandler)(XML_Parser parser, XML_StartElementHandler start, XML_EndElementHandler end)
   void (*SetNamespaceDeclHandler)(XML_Parser parser, XML_StartNamespaceDeclHandler start, XML_EndNamespaceDeclHandler end)
   void (*SetProcessingInstructionHandler)(XML_Parser parser, XML_ProcessingInstructionHandler handler)
   void (*SetUserData)(XML_Parser parser, void *userData)
   void (*SetStartDoctypeDeclHandler)(XML_Parser parser, XML_StartDoctypeDeclHandler start)
   enum XML_Status (*SetEncoding)(XML_Parser parser, const XML_Char *encoding)
   int (*SetHashSalt)(XML_Parser parser, unsigned long hash_salt)
   XML_Bool (*SetReparseDeferralEnabled)(XML_Parser parser, XML_Bool enabled)
   XML_Bool (*SetAllocTrackerActivationThreshold)(XML_Parser parser, unsigned long long activationThresholdBytes)
   XML_Bool (*SetAllocTrackerMaximumAmplification)(XML_Parser parser, float maxAmplificationFactor)
   XML_Bool (*SetBillionLaughsAttackProtectionActivationThreshold)(XML_Parser parser, unsigned long long activationThresholdBytes)
   XML_Bool (*SetBillionLaughsAttackProtectionMaximumAmplification)(XML_Parser parser, float maxAmplificationFactor)
   XML_Bool (*SetHashSalt16Bytes)(XML_Parser parser, const uint8_t entropy[16])

      Consulte a referência da API do Expat .
