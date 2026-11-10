"mmap" --- Suporte a arquivos mapeados na memória
*************************************************

======================================================================

Disponibilidade: not WASI.

Este módulo não funciona ou não está disponível em WebAssembly. Veja
Plataformas WebAssembly para mais informações.

Memory-mapped file objects behave like both "bytearray" and like *file
objects*.  You can use mmap objects in most places where "bytearray"
are expected; for example, you can use the "re" module to search
through a memory-mapped file.  You can also change a single byte by
doing "obj[index] = 97", or change a subsequence by assigning to a
slice: "obj[i1:i2] = b'...'".  You can also read and write data
starting at the current file position, and "seek()" through the file
to different positions.

Um arquivo mapeado na memória é criado pelo construtor "mmap", que é
diferente no Unix e no Windows. Nos dois casos, você deve fornecer um
descritor de arquivo para um arquivo aberto para atualização. Se você
deseja mapear um objeto arquivo Python existente, use o método
"fileno()" para obter o valor correto para o parâmetro *fileno*. Caso
contrário, você pode abrir o arquivo usando a função "os.open()", que
retorna um descritor de arquivo diretamente (o arquivo ainda precisa
ser fechado quando terminar).

Nota:

  Se você deseja criar um mapeamento de memória para um arquivo
  gravável e armazenado em buffer, deve usar "flush()" no arquivo
  primeiro. Isso é necessário para garantir que as modificações locais
  nos buffers estejam realmente disponíveis para o mapeamento.

Para as versões Unix e Windows do construtor, *access* pode ser
especificado como um parâmetro opcional de palavra-chave. *access*
aceita um dos quatro valores: "ACCESS_READ", "ACCESS_WRITE" ou
"ACCESS_COPY" para especificar memória somente leitura, gravação ou
cópia na gravação, respectivamente "ACCESS_DEFAULT" para adiar para
*prot*. *access* pode ser usado no Unix e no Windows. Se *access* não
for especificado, o mmap do Windows retornará um mapeamento de
gravação. Os valores iniciais da memória para todos os três tipos de
acesso são obtidos do arquivo especificado. A atribuição a um mapa de
memória "ACCESS_READ" gera uma exceção "TypeError". A atribuição a um
mapa de memória "ACCESS_WRITE" afeta a memória e o arquivo subjacente.
A atribuição a um mapa de memória "ACCESS_COPY" afeta a memória, mas
não atualiza o arquivo subjacente.

Alterado na versão 3.7: Adicionada a constante "ACCESS_DEFAULT".

Para mapear a memória anônima, -1 deve ser passado como o fileno junto
com o comprimento.

class mmap.mmap(fileno, length, tagname=None, access=ACCESS_DEFAULT, offset=0, *, trackfd=True)

   **(Windows version)** Maps *length* bytes from the file specified
   by the file descriptor *fileno*, and creates a mmap object.  If
   *length* is larger than the current size of the file, the file is
   extended to contain *length* bytes.  If *length* is "0", the
   maximum length of the map is the current size of the file, except
   that if the file is empty Windows raises an exception (you cannot
   create an empty mapping on Windows).

   *tagname*, se especificado e não "None", é uma string que fornece
   um nome de tag para o mapeamento. O Windows permite que você tenha
   muitos mapeamentos diferentes no mesmo arquivo. Se você especificar
   o nome de uma marca existente, essa marca será aberta; caso
   contrário, uma nova marca com esse nome será criada. Se este
   parâmetro for omitido ou "None", o mapeamento será criado sem um
   nome. Evitar o uso do parâmetro *tagname* ajudará a manter seu
   código portátil entre o Unix e o Windows.

   *offset* pode ser especificado como um deslocamento inteiro não
   negativo. As referências mmap serão relativas ao deslocamento do
   início do arquivo. *offset* tem como padrão 0. *offset* deve ser um
   múltiplo de "ALLOCATIONGRANULARITY".

   If *trackfd* is "False", the file handle corresponding to *fileno*
   will not be duplicated, and the resulting "mmap" object will not be
   associated with the map's underlying file. This means that the
   "size()" and "resize()" methods will fail. This mode is useful to
   limit the number of open file handles. The original file can be
   renamed (but not deleted) after closing *fileno*.

   Alterado na versão 3.15: The *trackfd* parameter was added.

   Levanta um evento de auditoria "mmap.__new__" com os argumentos
   "fileno", "length", "access", "offset".

class mmap.mmap(fileno, length, flags=MAP_SHARED, prot=PROT_WRITE | PROT_READ, access=ACCESS_DEFAULT, offset=0, *, trackfd=True)

   **(Versão Unix)** Mapeia *length* bytes do arquivo especificado
   pelo descritor de arquivo *fileno* e retorna um objeto mmap. Se
   *length* for "0", o comprimento máximo do mapa será o tamanho atual
   do arquivo quando "mmap" for chamado.

   *flags* especifica a natureza do mapeamento. "MAP_PRIVATE" cria um
   mapeamento privado de cópia na gravação, de modo que alterações no
   conteúdo do objeto mmap serão privadas para este processo, e
   "MAP_SHARED" cria um mapeamento compartilhado com todos os outros
   processos que mapeiam as mesmas áreas do arquivo. O valor padrão é
   "MAP_SHARED". Alguns sistemas têm sinalizadores adicionais
   possíveis, com a lista completa especificada em constantes MAP_*.

   *prot*, if specified, gives the desired memory protection; the two
   most useful values are "PROT_READ" and "PROT_WRITE", to specify
   that the pages may be read or written.  *prot* defaults to
   "PROT_READ" | "PROT_WRITE".

   *access* pode ser especificado em vez de *flags* e *prot* como um
   parâmetro nomeado opcional. É um erro especificar *flags*, *prot* e
   *access*. Consulte a descrição de *access* acima para obter
   informações sobre como usar este parâmetro.

   *offset* pode ser especificado como um deslocamento inteiro não
   negativo. As referências mmap serão relativas ao deslocamento do
   início do arquivo. *offset* tem como padrão 0. *offset* deve ser um
   múltiplo de "ALLOCATIONGRANULARITY", que é igual a "PAGESIZE" em
   sistemas Unix.

   Se *trackfd* for "False", o descritor de arquivo especificado por
   *fileno* não será duplicado e o objeto "mmap" resultante não será
   associado ao arquivo subjacente do mapa. Isso significa que os
   métodos "size()" e "resize()" falharão. Este modo é útil para
   limitar o número de descritores de arquivo abertos.

   Para garantir a validade do mapeamento de memória criado, o arquivo
   especificado pelo descritor *fileno* é sincronizado internamente de
   forma automática com o armazenamento de suporte físico no macOS.

   Alterado na versão 3.13: The *trackfd* parameter was added.

   This example shows a simple way of using "mmap":

      import mmap

      # write a simple example file
      with open("hello.txt", "wb") as f:
          f.write(b"Hello Python!\n")

      with open("hello.txt", "r+b") as f:
          # memory-map the file, size 0 means whole file
          mm = mmap.mmap(f.fileno(), 0)
          # read content via standard file methods
          print(mm.readline())  # prints b"Hello Python!\n"
          # read content via slice notation
          print(mm[:5])  # prints b"Hello"
          # update content using slice notation;
          # note that new content must have same size
          mm[6:] = b" world!\n"
          # ... and read again using standard file methods
          mm.seek(0)
          print(mm.readline())  # prints b"Hello  world!\n"
          # close the map
          mm.close()

   "mmap" can also be used as a context manager in a "with" statement:

      import mmap

      with mmap.mmap(-1, 13) as mm:
          mm.write(b"Hello world!")

   Adicionado na versão 3.2: Suporte a gerenciador de contexto.

   The next example demonstrates how to create an anonymous map and
   exchange data between the parent and child processes:

      import mmap
      import os

      mm = mmap.mmap(-1, 13)
      mm.write(b"Hello world!")

      pid = os.fork()

      if pid == 0:  # In a child process
          mm.seek(0)
          print(mm.readline())

          mm.close()

   Levanta um evento de auditoria "mmap.__new__" com os argumentos
   "fileno", "length", "access", "offset".

   Memory-mapped file objects support the following methods:

   close()

      Closes the mmap. Subsequent calls to other methods of the object
      will result in a ValueError exception being raised. This will
      not close the open file.

   closed

      "True" if the file is closed.

      Adicionado na versão 3.2.

   find(sub[, start[, end]])

      Returns the lowest index in the object where the subsequence
      *sub* is found, such that *sub* is contained in the range
      [*start*, *end*]. Optional arguments *start* and *end* are
      interpreted as in slice notation. Returns "-1" on failure.

      Alterado na versão 3.5: Writable *bytes-like object* is now
      accepted.

   flush([offset, [size, ]]*, flags=MS_SYNC)

      Flushes changes made to the in-memory copy of a file back to
      disk. Without use of this call there is no guarantee that
      changes are written back before the object is destroyed.  If
      *offset* and *size* are specified, only changes to the given
      range of bytes will be flushed to disk; otherwise, the whole
      extent of the mapping is flushed.  *offset* must be a multiple
      of the "PAGESIZE" or "ALLOCATIONGRANULARITY".

      The *flags* parameter specifies the synchronization behavior.
      *flags* must be one of the MS_* constants available on the
      system.

      On Windows, the *flags* parameter is ignored.

      "None" is returned to indicate success.  An exception is raised
      when the call failed.

      Alterado na versão 3.8: Previously, a nonzero value was returned
      on success; zero was returned on error under Windows.  A zero
      value was returned on success; an exception was raised on error
      under Unix.

      Alterado na versão 3.15: Allow specifying *offset* without
      *size*. Previously, both *offset* and *size* parameters were
      required together. Now *offset* can be specified alone, and the
      flush operation will extend from *offset* to the end of the
      mmap.

      Alterado na versão 3.15: Added *flags* parameter to control
      synchronization behavior.

   madvise(option[, start[, length]])

      Send advice *option* to the kernel about the memory region
      beginning at *start* and extending *length* bytes.  *option*
      must be one of the MADV_* constants available on the system.  If
      *start* and *length* are omitted, the entire mapping is spanned.
      On some systems (including Linux), *start* must be a multiple of
      the "PAGESIZE".

      Availability: Systems with the "madvise()" system call.

      Adicionado na versão 3.8.

   move(dest, src, count)

      Copy the *count* bytes starting at offset *src* to the
      destination index *dest*.  If the mmap was created with
      "ACCESS_READ", then calls to move will raise a "TypeError"
      exception.

   read([n])

      Return a "bytes" containing up to *n* bytes starting from the
      current file position. If the argument is omitted, "None" or
      negative, return all bytes from the current file position to the
      end of the mapping. The file position is updated to point after
      the bytes that were returned.

      Alterado na versão 3.3: Argument can be omitted or "None".

   read_byte()

      Returns a byte at the current file position as an integer, and
      advances the file position by 1.

   readline()

      Returns a single line, starting at the current file position and
      up to the next newline. The file position is updated to point
      after the bytes that were returned.

   resize(newsize)

      Resizes the map and the underlying file, if any.

      Resizing a map created with *access* of "ACCESS_READ" or
      "ACCESS_COPY", will raise a "TypeError" exception. Resizing a
      map created with *trackfd* set to "False", will raise a
      "ValueError" exception.

      **On Windows**: Resizing the map will raise an "OSError" if
      there are other maps against the same named file. Resizing an
      anonymous map (ie against the pagefile) will silently create a
      new map with the original data copied over up to the length of
      the new size.

      Availability: Windows and systems with the "mremap()" system
      call.

      Alterado na versão 3.11: Correctly fails if attempting to resize
      when another map is held Allows resize against an anonymous map
      on Windows

   rfind(sub[, start[, end]])

      Returns the highest index in the object where the subsequence
      *sub* is found, such that *sub* is contained in the range
      [*start*, *end*]. Optional arguments *start* and *end* are
      interpreted as in slice notation. Returns "-1" on failure.

      Alterado na versão 3.5: Writable *bytes-like object* is now
      accepted.

   seek(pos[, whence])

      Set the file's current position.  *whence* argument is optional
      and defaults to "os.SEEK_SET" or "0" (absolute file
      positioning); other values are "os.SEEK_CUR" or "1" (seek
      relative to the current position) and "os.SEEK_END" or "2" (seek
      relative to the file's end).

      Alterado na versão 3.13: Return the new absolute position
      instead of "None".

   seekable()

      Return whether the file supports seeking, and the return value
      is always "True".

      Adicionado na versão 3.13.

   set_name(name, /)

      Annotate the memory mapping with the given *name* for easier
      identification in "/proc/<pid>/maps" if the kernel supports the
      feature and "-X dev" is passed to Python or if Python is built
      in debug mode. The length of *name* must not exceed 67 bytes
      including the "'\0'" terminator.

      Disponibilidade: Linux >= 5.17 (kernel built with
      "CONFIG_ANON_VMA_NAME" option)

      Adicionado na versão 3.15.

   size()

      Return the length of the file, which can be larger than the size
      of the memory-mapped area. For an anonymous mapping, return its
      size.

      Alterado na versão 3.15: Anonymous mappings are now supported on
      Unix.

   tell()

      Returns the current position of the file pointer.

   write(bytes)

      Write the bytes in *bytes* into memory at the current position
      of the file pointer and return the number of bytes written
      (never less than "len(bytes)", since if the write fails, a
      "ValueError" will be raised).  The file position is updated to
      point after the bytes that were written.  If the mmap was
      created with "ACCESS_READ", then writing to it will raise a
      "TypeError" exception.

      Alterado na versão 3.5: Writable *bytes-like object* is now
      accepted.

      Alterado na versão 3.6: The number of bytes written is now
      returned.

   write_byte(byte)

      Write the integer *byte* into memory at the current position of
      the file pointer; the file position is advanced by "1". If the
      mmap was created with "ACCESS_READ", then writing to it will
      raise a "TypeError" exception.


ACCESS_* constants
==================

mmap.ACCESS_DEFAULT
mmap.ACCESS_READ
mmap.ACCESS_WRITE
mmap.ACCESS_COPY

   These constants specify the access mode for a memory mapping.
   "ACCESS_READ" provides read-only access, "ACCESS_WRITE" provides
   write-through access, and "ACCESS_COPY" provides copy-on-write
   access. "ACCESS_DEFAULT" defers to the *prot* argument of "mmap".


Page size constants
===================

mmap.PAGESIZE
mmap.ALLOCATIONGRANULARITY

   "PAGESIZE" is the system memory page size in bytes.
   "ALLOCATIONGRANULARITY" is the minimum alignment in bytes required
   for the *offset* argument of "mmap". On Unix,
   "ALLOCATIONGRANULARITY" is equal to "PAGESIZE".


PROT_* constants
================

mmap.PROT_READ
mmap.PROT_WRITE
mmap.PROT_EXEC

   Memory protection flags accepted by the *prot* argument of "mmap".
   "PROT_READ" allows pages to be read, "PROT_WRITE" allows pages to
   be written, and "PROT_EXEC" allows pages to be executed. Values can
   be combined using the bitwise OR operator. Not every option is
   present on every system.

   Disponibilidade: Unix.


MADV_* constants
================

mmap.MADV_NORMAL
mmap.MADV_RANDOM
mmap.MADV_SEQUENTIAL
mmap.MADV_WILLNEED
mmap.MADV_DONTNEED
mmap.MADV_REMOVE
mmap.MADV_DONTFORK
mmap.MADV_DOFORK
mmap.MADV_HWPOISON
mmap.MADV_MERGEABLE
mmap.MADV_UNMERGEABLE
mmap.MADV_SOFT_OFFLINE
mmap.MADV_HUGEPAGE
mmap.MADV_NOHUGEPAGE
mmap.MADV_DONTDUMP
mmap.MADV_DODUMP
mmap.MADV_FREE
mmap.MADV_NOSYNC
mmap.MADV_AUTOSYNC
mmap.MADV_NOCORE
mmap.MADV_CORE
mmap.MADV_PROTECT
mmap.MADV_FREE_REUSABLE
mmap.MADV_FREE_REUSE

   These options can be passed to "mmap.madvise()".  Not every option
   will be present on every system.

   Availability: Systems with the madvise() system call.

   Adicionado na versão 3.8.


MAP_* constants
===============

mmap.MAP_SHARED
mmap.MAP_PRIVATE
mmap.MAP_32BIT
mmap.MAP_ALIGNED_SUPER
mmap.MAP_ANON
mmap.MAP_ANONYMOUS
mmap.MAP_CONCEAL
mmap.MAP_DENYWRITE
mmap.MAP_EXECUTABLE
mmap.MAP_HASSEMAPHORE
mmap.MAP_JIT
mmap.MAP_NOCACHE
mmap.MAP_NOEXTEND
mmap.MAP_NORESERVE
mmap.MAP_POPULATE
mmap.MAP_RESILIENT_CODESIGN
mmap.MAP_RESILIENT_MEDIA
mmap.MAP_STACK
mmap.MAP_TPRO
mmap.MAP_TRANSLATED_ALLOW_EXECUTE
mmap.MAP_UNIX03

   These are the various flags that can be passed to "mmap.mmap()".
   "MAP_ALIGNED_SUPER" is only available at FreeBSD and "MAP_CONCEAL"
   is only available at OpenBSD.  Note that some options might not be
   present on some systems.

   Alterado na versão 3.10: Added "MAP_POPULATE" constant.

   Adicionado na versão 3.11: Added "MAP_STACK" constant.

   Adicionado na versão 3.12: Added "MAP_ALIGNED_SUPER" and
   "MAP_CONCEAL" constants.

   Adicionado na versão 3.13: Added "MAP_32BIT", "MAP_HASSEMAPHORE",
   "MAP_JIT", "MAP_NOCACHE", "MAP_NOEXTEND", "MAP_NORESERVE",
   "MAP_RESILIENT_CODESIGN", "MAP_RESILIENT_MEDIA", "MAP_TPRO",
   "MAP_TRANSLATED_ALLOW_EXECUTE", and "MAP_UNIX03" constants.


MS_* constants
==============

mmap.MS_SYNC
mmap.MS_ASYNC
mmap.MS_INVALIDATE

   These flags control the synchronization behavior for
   "mmap.flush()":

   * "MS_SYNC" - Synchronous flush: writes are scheduled and the call
     blocks until they are physically written to storage.

   * "MS_ASYNC" - Asynchronous flush: writes are scheduled but the
     call returns immediately without waiting for completion.

   * "MS_INVALIDATE" - Invalidate cached data: invalidates other
     mappings of the same file so they can see the changes.

   Adicionado na versão 3.15.
