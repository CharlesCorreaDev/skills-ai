"multiprocessing.shared_memory" --- Memória compartilhada para acesso direto entre processos
********************************************************************************************

**Código-fonte:** Lib/multiprocessing/shared_memory.py

Adicionado na versão 3.8.

======================================================================

Este módulo fornece uma classe, "SharedMemory", para a alocação e
gerenciamento da memória compartilhada a ser acessada por um ou mais
processos em uma máquina multicore ou de multiprocessamento simétrico
(SMP). Para ajudar com o gerenciamento do ciclo de vida da memória
compartilhada especialmente entre processos distintos, uma subclasse
de "BaseManager", "SharedMemoryManager", também é fornecida no módulo
"multiprocessing.managers".

Neste módulo, memória compartilhada refere-se a blocos de memória
compartilhada no "estilo POSIX" (embora não seja necessariamente
implementado explicitamente como tal) e não se refere a "memória
compartilhada distribuída". Este estilo de memória compartilhada
permite que processos distintos potencialmente leiam e escrevam em uma
região comum (ou compartilhada) de memória volátil. Os processos são
convencionalmente limitados a ter acesso somente ao próprio espaço de
memória de processo mas a memória compartilhada permite o
compartilhamento de dados entre processos, evitando a necessidade de
enviar mensagens entre processos contendo estes dados. Compartilhar
dados diretamente via memória pode fornecer ganhos de desempenho
significativos comparado ao compartilhamento de dados via disco ou
soquete ou outras comunicações que requerem a
serialização/desserialização e cópia dos dados.

class multiprocessing.shared_memory.SharedMemory(name=None, create=False, size=0, *, track=True)

   Cria uma instância da classe "SharedMemory" para criar um novo
   bloco de memória compartilhada ou anexar a um bloco de memória
   compartilhada existente. A cada bloco de memória compartilhada é
   atribuído um nome único. Desta forma, um processo pode criar um
   bloco de memória compartilhada com um nome particular e um processo
   diferente pode ser anexado a esse mesmo bloco de memória
   compartilhada usando este mesmo nome.

   Como um recurso para compartilhar dados entre processos, os blocos
   de memória compartilhada podem sobreviver ao processo original que
   os criou. Quando um processo não precisa mais acessar um bloco de
   memória compartilhada que ainda pode ser necessário para outros
   processos, o método "close()" deve ser chamado. Quando um bloco de
   memória compartilhada não é mais necessário para nenhum processo, o
   método "unlink()" deve ser chamado para garantir a limpeza
   apropriada.

   Parâmetros:
      * **name** (*str** | **None*) -- O nome único para a memória
        compartilhada requisitada, especificado como uma string. Ao
        criar um novo bloco de memória compartilhada, se "None" (o
        padrão) é fornecido para o nome, um novo nome será gerado.

      * **create** (*bool*) -- Controla quando um novo bloco de
        memória compartilhada é criado ("True") ou um bloco de memória
        compartilhada existente é anexado ("False").

      * **size** (*int*) -- O número de bytes requeridos ao criar um
        novo bloco de memória compartilhada. Como algumas plataformas
        optam por alocar pedaços de memória com base no tamanho da
        página de memória da própria plataforma, o tamanho exato do
        bloco de memória compartilhada pode ser maior ou igual ao
        tamanho requerido. Ao anexar a um bloco de memória
        compartilhada existente, o parâmetro *size* é ignorado.

      * **track** (*bool*) -- Quando "True", registra o bloco de
        memória compartilhada com um processo de rastreador de
        recursos em plataformas onde o sistema operacional não faz
        isso automaticamente. O rastreador de recursos garante a
        limpeza adequada da memória compartilhada, mesmo se todos os
        outros processos com acesso à memória saírem sem fazer isso.
        Os processos Python criados a partir de um ancestral comum
        usando os recursos de "multiprocessing" compartilham um único
        processo de rastreador de recursos, e o tempo de vida dos
        segmentos de memória compartilhada é manipulado
        automaticamente entre esses processos. Os processos Python
        criados de qualquer outra forma receberão seu próprio
        rastreador de recursos ao acessar a memória compartilhada com
        *track* habilitado. Isso fará com que a memória compartilhada
        seja excluída pelo rastreador de recursos do primeiro processo
        que terminar. Para evitar esse problema, os usuários de
        "subprocess" ou processos Python autônomos devem definir
        *track* como "False" quando já houver outro processo em vigor
        que faça a contabilidade. *track* é ignorado no Windows, que
        tem seu próprio rastreamento e exclui automaticamente a
        memória compartilhada quando todos os identificadores para ele
        foram fechados.

   Alterado na versão 3.13: Adicionado o parâmetro *track*.

   close()

      Fecha o identificador/descritor de arquivo para a memória
      compartilhada desta instância. "close()" deve ser chamado quando
      o acesso ao bloco de memória compartilhada desta instância não
      for mais necessário. Dependendo do sistema operacional, a
      memória subjacente pode ou não ser liberada, mesmo que todos os
      identificadores para ela tenham sido fechados. Para garantir uma
      limpeza adequada, use o método "unlink()".

   unlink()

      Exclui o bloco de memória compartilhada subjacente. Isso deve
      ser chamado apenas uma vez por bloco de memória compartilhada,
      independentemente do número de handles para ele, mesmo em outros
      processos. "unlink()" e "close()" podem ser chamados em qualquer
      ordem, mas tentar acessar dados dentro de um bloco de memória
      compartilhada após "unlink()" pode resultar em erros de acesso à
      memória, dependendo da plataforma.

      Este método não tem efeito no Windows, onde a única maneira de
      excluir um bloco de memória compartilhada é fechar todos os
      identificadores.

   buf

      Uma visualização de memória do conteúdo do bloco de memória
      compartilhada.

   name

      Acesso somente leitura ao nome único do bloco de memória
      compartilhada.

   size

      Acesso somente leitura ao tamanho em bytes do bloco de memória
      compartilhada.

O exemplo a seguir demonstra um uso baixo nível de instâncias de
"SharedMemory":

   >>> from multiprocessing import shared_memory
   >>> shm_a = shared_memory.SharedMemory(create=True, size=10)
   >>> type(shm_a.buf)
   <class 'memoryview'>
   >>> buffer = shm_a.buf
   >>> len(buffer)
   10
   >>> buffer[:4] = bytearray([22, 33, 44, 55])  # Modifica vários de uma só vez
   >>> buffer[4] = 100                           # Modifica um único byte de cada vez
   >>> # Anexa a um bloco de memória compartilhada existente
   >>> shm_b = shared_memory.SharedMemory(shm_a.name)
   >>> import array
   >>> array.array('b', shm_b.buf[:5])  # Copia os dados para um novo array.array
   array('b', [22, 33, 44, 55, 100])
   >>> shm_b.buf[:5] = b'howdy'  # Modifica via shm_b usando bytes
   >>> bytes(shm_a.buf[:5])      # Acessa via shm_a
   b'howdy'
   >>> shm_b.close()   # Fecha cada instância de SharedMemory
   >>> shm_a.close()
   >>> shm_a.unlink()  # Chama unlink uma vez para liberar a memória Compartilhada

O exemplo a seguir demonstra um uso prático da classe "SharedMemory"
com arrays do NumPy, acessando o mesmo "numpy.ndarray" de dois
consoles Python distintos.

   >>> # No primeiro console interativo do Python
   >>> import numpy as np
   >>> a = np.array([1, 1, 2, 3, 5, 8])  # Inicia com um array de NumPy existente
   >>> from multiprocessing import shared_memory
   >>> shm = shared_memory.SharedMemory(create=True, size=a.nbytes)
   >>> # Agora cria um array de NumPy suportado por memória compartilhada
   >>> b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
   >>> b[:] = a[:]  # Copia os dados originais para memória compartilhada
   >>> b
   array([1, 1, 2, 3, 5, 8])
   >>> type(b)
   <class 'numpy.ndarray'>
   >>> type(a)
   <class 'numpy.ndarray'>
   >>> shm.name  # Não especificamos um nome, então um foi escolhido por nós
   'psm_21467_46075'

   >>> # No mesmo shell ou em um novo console do Python na mesma máquina
   >>> import numpy as np
   >>> from multiprocessing import shared_memory
   >>> # Anexa ao bloco de memória compartilhada existente
   >>> existing_shm = shared_memory.SharedMemory(name='psm_21467_46075')
   >>> # Observe que a.shape é (6,) e a.dtype é np.int64 neste exemplo
   >>> c = np.ndarray((6,), dtype=np.int64, buffer=existing_shm.buf)
   >>> c
   array([1, 1, 2, 3, 5, 8])
   >>> c[-1] = 888
   >>> c
   array([  1,   1,   2,   3,   5, 888])

   >>> # De volta ao primeiro console interativo do Python, b reflete essa mudança
   >>> b
   array([  1,   1,   2,   3,   5, 888])

   >>> # Limpeza de dentro do segundo console Python
   >>> del c  # Desnecessário; apenas enfatizar a array não é mais usado
   >>> existing_shm.close()

   >>> # Limpeza de dentro do primeiro console Python
   >>> del b  # Desnecessário; apenas enfatizar a array não é mais usado
   >>> shm.close()
   >>> shm.unlink()  # Libera o bloco de memória compartilhada no final

class multiprocessing.managers.SharedMemoryManager([address[, authkey]])

   Uma subclasse de "multiprocessing.managers.BaseManager" que pode
   ser usada para o gerenciamento dos blocos de memória compartilhada
   entre processos.

   A call to "start()" on a "SharedMemoryManager" instance causes a
   new process to be started. This new process's sole purpose is to
   manage the life cycle of all shared memory blocks created through
   it.  To trigger the release of all shared memory blocks managed by
   that process, call "shutdown()" on the instance. This triggers a
   "unlink()" call on all of the "SharedMemory" objects managed by
   that process and then stops the process itself. By creating
   "SharedMemory" instances through a "SharedMemoryManager", we avoid
   the need to manually track and trigger the freeing of shared memory
   resources.

   This class provides methods for creating and returning
   "SharedMemory" instances and for creating a list-like object
   ("ShareableList") backed by shared memory.

   Consulte "BaseManager" para obter uma descrição dos argumentos de
   entrada opcionais herdados *address* e *authkey* e como eles podem
   ser usados para conectar-se a um serviço "SharedMemoryManager"
   existente de outros processos.

   SharedMemory(size)

      Create and return a new "SharedMemory" object with the specified
      *size* in bytes.

   ShareableList(sequence)

      Create and return a new "ShareableList" object, initialized by
      the values from the input *sequence*.

O exemplo a seguir demonstra os mecanismos básicos de um
"SharedMemoryManager":

   >>> from multiprocessing.managers import SharedMemoryManager
   >>> smm = SharedMemoryManager()
   >>> smm.start()  # Inicia o procsso que gerencia os blocos de memória compartilhada
   >>> sl = smm.ShareableList(range(4))
   >>> sl
   ShareableList([0, 1, 2, 3], name='psm_6572_7512')
   >>> raw_shm = smm.SharedMemory(size=128)
   >>> another_sl = smm.ShareableList('alpha')
   >>> another_sl
   ShareableList(['a', 'l', 'p', 'h', 'a'], name='psm_6572_12221')
   >>> smm.shutdown()  # Chama unlink() em sl, raw_shm, e another_sl

O exemplo a seguir retrata um padrão potencialmente mais conveniente
para usar objetos "SharedMemoryManager" através da instrução "with"
para garantir que todos os blocos de memória compartilhada são
liberados depois que não são mais necessários.

   >>> with SharedMemoryManager() as smm:
   ...     sl = smm.ShareableList(range(2000))
   ...     # Divide o trabalho entre dois processos, armazenando resultados parciais em sl
   ...     p1 = Process(target=do_work, args=(sl, 0, 1000))
   ...     p2 = Process(target=do_work, args=(sl, 1000, 2000))
   ...     p1.start()
   ...     p2.start()  # Um multiprocessing.Pool pode ser mais eficiente
   ...     p1.join()
   ...     p2.join()   # Espera todo trabalho ser concluído nos dois procssos
   ...     total_result = sum(sl)  # Consolida os resutlados parciais agora em sl

Ao usar um "SharedMemoryManager" em uma instrução "with", os blocos de
memória compartilhada criados utilizando este gerenciador são todos
liberados quando o bloco de código com a instrução "with" termina sua
execução.

class multiprocessing.shared_memory.ShareableList(sequence=None, *, name=None)

   Fornece um objeto mutável do tipo lista onde todos os valores
   armazenados dentro são armazenados em um bloco de memória
   compartilhada. Isso restringe valores armazenáveis aos seguintes
   tipos de dados embutidos:

   * "int" (com sinal, 64-bit)

   * "float"

   * "bool"

   * "str" (menos de 10M bytes cada quando codificado como UTF-8)

   * "bytes" (menos de 10M bytes cada)

   * "None"

   Ele também difere notavelmente do tipo embutido "list", pois essas
   listas não podem alterar seu comprimento geral (ou seja, sem
   "append()", "insert()", etc.) e não oferecem suporte à criação
   dinâmica de novas instâncias "ShareableList" por meio de
   fatiamento.

   *sequence* é usado para preencher um "ShareableList" com valores.
   Defina como "None" para anexar a uma "ShareableList" já existente
   pelo seu nome único de memória compartilhada.

   *name* é um nome único para a memória compartilhada requerida, como
   descrito na definição de "SharedMemory". Ao anexar a uma
   "ShareableList" já existente, deve-se especificar o nome único do
   bloco de memória compartilhada e definir *sequence* como "None".

   Nota:

     Existe um problema conhecido para os valores "bytes" e "str". Se
     eles terminarem com bytes ou caracteres nulos "\x00", eles podem
     ser *silenciosamente removidos* ao buscá-los pelo índice da
     "ShareableList". Esse comportamento ".rstrip(b'\x00')" é
     considerado um bug e pode desaparecer no futuro. Veja gh-106939.

   Para aplicações onde a remoção de nulos finais é um problema,
   contorne-o sempre anexando incondicionalmente um byte extra
   diferente de 0 ao final de tais valores ao armazená-los e
   removendo-os incondicionalmente ao buscá-los:

      >>> from multiprocessing import shared_memory
      >>> nul_bug_demo = shared_memory.ShareableList(['?\x00', b'\x03\x02\x01\x00\x00\x00'])
      >>> nul_bug_demo[0]
      '?'
      >>> nul_bug_demo[1]
      b'\x03\x02\x01'
      >>> nul_bug_demo.shm.unlink()
      >>> padded = shared_memory.ShareableList(['?\x00\x07', b'\x03\x02\x01\x00\x00\x00\x07'])
      >>> padded[0][:-1]
      '?\x00'
      >>> padded[1][:-1]
      b'\x03\x02\x01\x00\x00\x00'
      >>> padded.shm.unlink()

   count(value)

      Retorna o número de ocorrências de *value*.

   index(value)

      Retorna a primeira posição do índice de *value*. Levanta
      "ValueError" se *value* não estiver presente.

   format

      Atributo somente leitura contendo o formato de empacotamento
      "struct" usado por todos os valores armazenados atualmente.

   shm

      A instância de "SharedMemory" onde os valores são armazenados.

O exemplo a seguir demonstra o uso básico de uma instância de
"ShareableList":

>>> from multiprocessing import shared_memory
>>> a = shared_memory.ShareableList(['howdy', b'HoWdY', -273.154, 100, None, True, 42])
>>> [ type(entry) for entry in a ]
[<class 'str'>, <class 'bytes'>, <class 'float'>, <class 'int'>, <class 'NoneType'>, <class 'bool'>, <class 'int'>]
>>> a[2]
-273.154
>>> a[2] = -78.5
>>> a[2]
-78.5
>>> a[2] = 'dry ice'  # Changing data types is supported as well
>>> a[2]
'dry ice'
>>> a[2] = 'larger than previously allocated storage space'
Traceback (most recent call last):
  ...
ValueError: exceeds available storage for existing str
>>> a[2]
'dry ice'
>>> len(a)
7
>>> a.index(42)
6
>>> a.count(b'howdy')
0
>>> a.count(b'HoWdY')
1
>>> a.shm.close()
>>> a.shm.unlink()
>>> del a  # Use of a ShareableList after call to unlink() is unsupported

O exemplo a seguir retrata como um, dois ou mais processos podem
acessar a mesma "ShareableList" fornecendo o nome do bloco de memória
compartilhada por trás dela:

>>> b = shared_memory.ShareableList(range(5))         # In a first process
>>> c = shared_memory.ShareableList(name=b.shm.name)  # In a second process
>>> c
ShareableList([0, 1, 2, 3, 4], name='...')
>>> c[-1] = -999
>>> b[-1]
-999
>>> b.shm.close()
>>> c.shm.close()
>>> c.shm.unlink()

Os exemplos a seguir demonstram que os objetos  "ShareableList" (e o
subjacente "SharedMemory") podem ser serializados e desserializados
com pickle, se preciso. Note, ainda será o mesmo objeto compartilhado.
Isto acontece pois o objeto desserializado tem o mesmo nome único e é
somente anexado ao objeto existente com o mesmo nome (se o objeto
ainda existe):

>>> import pickle
>>> from multiprocessing import shared_memory
>>> sl = shared_memory.ShareableList(range(10))
>>> list(sl)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> deserialized_sl = pickle.loads(pickle.dumps(sl))
>>> list(deserialized_sl)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

>>> sl[0] = -1
>>> deserialized_sl[1] = -2
>>> list(sl)
[-1, -2, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(deserialized_sl)
[-1, -2, 2, 3, 4, 5, 6, 7, 8, 9]

>>> sl.shm.close()
>>> sl.shm.unlink()
