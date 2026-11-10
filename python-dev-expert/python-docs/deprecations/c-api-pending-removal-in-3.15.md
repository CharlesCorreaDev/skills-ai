Remoção pendente no Python 3.15
*******************************

* A "PyImport_ImportModuleNoBlock()": Use "PyImport_ImportModule()"

* "PyWeakref_GetObject()" e "PyWeakref_GET_OBJECT()": Use
  "PyWeakref_GetRef()". O projeto pythoncapi-compat pod ser usado para
  obter "PyWeakref_GetRef()" no Python 3.12 e versões mais antigas.

* "PyUnicode_AsDecodedObject()": use "PyCodec_Decode()".

* "PyUnicode_AsDecodedUnicode()": Use "PyCodec_Decode()"; Note que
  alguns codecs (por exemplo, "base64") podem retornar um tipo
  diferente de "str", tal como "bytes".

* "PyUnicode_AsEncodedObject()": use "PyCodec_Encode()".

* "PyUnicode_AsEncodedUnicode()": Use "PyCodec_Encode()"; Note que
  alguns codecs (por exemplo, "base64") podem retornar um tipo
  diferente de "bytes", tal com "str".

* Funções de inicialização do Python, descontinuadas no Python 3.9:

  * "Py_GetPath()": Use "PyConfig_Get("module_search_paths")"
    ("sys.path").

  * "Py_GetPrefix()": Use "PyConfig_Get("base_prefix")"
    ("sys.base_prefix"). Use "PyConfig_Get("prefix")" ("sys.prefix")
    se ambientes virtuais precisarem ser tratados.

  * "Py_GetExecPrefix()": Use "PyConfig_Get("base_exec_prefix")"
    ("sys.base_exec_prefix"). Use "PyConfig_Get("exec_prefix")"
    ("sys.exec_prefix") se ambientes virtuais precisarem ser tratados.

  * "Py_GetProgramFullPath()": Use "PyConfig_Get("executable")"
    ("sys.executable").

  * "Py_GetProgramName()": Use "PyConfig_Get("executable")"
    ("sys.executable").

  * "Py_GetPythonHome()": Use "PyConfig_Get("home")" ou a variável de
    ambiente "PYTHONHOME".

  O projeto pythoncapi-compat pode ser usado para obter
  "PyConfig_Get()" no Python 3.13 e versões anteriores.

* Funções para configurar a inicialização do Python, descontinuadas no
  Python 3.11:

  * "PySys_SetArgvEx()": defina "PyConfig.argv".

  * "PySys_SetArgv()": defina "PyConfig.argv".

  * "Py_SetProgramName()": defina "PyConfig.program_name".

  * "Py_SetPythonHome()": defina "PyConfig.home".

  * "PySys_ResetWarnOptions()": Limpe "sys.warnoptions" e
    "warnings.filters".

  Em vez disso, a API "Py_InitializeFromConfig()" deve ser usada com
  "PyConfig".

* Variáveis de configuração globais

  * "Py_DebugFlag": Use "PyConfig.parser_debug" ou
    "PyConfig_Get("parser_debug")".

  * "Py_VerboseFlag": Use "PyConfig.verbose" ou
    "PyConfig_Get("verbose")".

  * "Py_QuietFlag": Use "PyConfig.quiet" ou "PyConfig_Get("quiet")".

  * "Py_InteractiveFlag": Use "PyConfig.interactive" ou
    "PyConfig_Get("interactive")".

  * "Py_InspectFlag": Use "PyConfig.inspect" ou
    "PyConfig_Get("inspect")".

  * "Py_OptimizeFlag": Use "PyConfig.optimization_level" ou
    "PyConfig_Get("optimization_level")".

  * "Py_NoSiteFlag": Use "PyConfig.site_import" ou
    "PyConfig_Get("site_import")".

  * "Py_BytesWarningFlag": Use "PyConfig.bytes_warning" ou
    "PyConfig_Get("bytes_warning")".

  * "Py_FrozenFlag": Use "PyConfig.pathconfig_warnings" ou
    "PyConfig_Get("pathconfig_warnings")".

  * "Py_IgnoreEnvironmentFlag": Use "PyConfig.use_environment" ou
    "PyConfig_Get("use_environment")".

  * "Py_DontWriteBytecodeFlag": Use "PyConfig.write_bytecode" ou
    "PyConfig_Get("write_bytecode")".

  * "Py_NoUserSiteDirectory": Use "PyConfig.user_site_directory" ou
    "PyConfig_Get("user_site_directory")".

  * "Py_UnbufferedStdioFlag": Use "PyConfig.buffered_stdio" ou
    "PyConfig_Get("buffered_stdio")".

  * "Py_HashRandomizationFlag": Use "PyConfig.use_hash_seed" e
    "PyConfig.hash_seed" ou "PyConfig_Get("hash_seed")".

  * "Py_IsolatedFlag": Use "PyConfig.isolated" ou
    "PyConfig_Get("isolated")".

  * "Py_LegacyWindowsFSEncodingFlag": Use
    "PyPreConfig.legacy_windows_fs_encoding" ou
    "PyConfig_Get("legacy_windows_fs_encoding")".

  * "Py_LegacyWindowsStdioFlag": Use "PyConfig.legacy_windows_stdio"
    ou "PyConfig_Get("legacy_windows_stdio")".

  * "Py_FileSystemDefaultEncoding", "Py_HasFileSystemDefaultEncoding":
    Use "PyConfig.filesystem_encoding" ou
    "PyConfig_Get("filesystem_encoding")".

  * "Py_FileSystemDefaultEncodeErrors": Use
    "PyConfig.filesystem_errors" ou
    "PyConfig_Get("filesystem_errors")".

  * "Py_UTF8Mode": Use "PyPreConfig.utf8_mode" ou
    "PyConfig_Get("utf8_mode")". (veja "Py_PreInitialize()")

  A API "Py_InitializeFromConfig()" deve ser usada com "PyConfig" para
  definir essas opções. Ou "PyConfig_Get()" pode ser usado para obter
  essas opções em tempo de execução.
