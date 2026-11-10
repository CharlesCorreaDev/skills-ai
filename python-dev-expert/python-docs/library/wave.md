"wave" --- Read and write WAV files
***********************************

**Código-fonte:** Lib/wave.py

======================================================================

The "wave" module provides a convenient interface to the Waveform
Audio "WAVE" (or "WAV") file format.

The module supports uncompressed PCM and IEEE floating-point WAV
formats.

Alterado na versão 3.12: Support for "WAVE_FORMAT_EXTENSIBLE" headers
was added, provided that the extended format is
"KSDATAFORMAT_SUBTYPE_PCM".

Alterado na versão 3.15: Support for reading and writing
"WAVE_FORMAT_IEEE_FLOAT" files was added.

The "wave" module defines the following function and exception:

wave.open(file, mode=None)

   If *file* is a string, a *path-like object* or a *bytes-like
   object* open the file by that name, otherwise treat it as a file-
   like object.  *mode* can be:

   "'rb'"
      Modo somente para leitura.

   "'wb'"
      Modo somente para escrita.

   Note that it does not allow read/write WAV files.

   A *mode* of "'rb'" returns a "Wave_read" object, while a *mode* of
   "'wb'" returns a "Wave_write" object.  If *mode* is omitted and a
   file-like object is passed as *file*, "file.mode" is used as the
   default value for *mode*.

   If you pass in a file-like object, the wave object will not close
   it when its "close()" method is called; it is the caller's
   responsibility to close the file object.

   The "open()" function may be used in a "with" statement.  When the
   "with" block completes, the "Wave_read.close()" or
   "Wave_write.close()" method is called.

   Alterado na versão 3.4: Added support for unseekable files.

   Alterado na versão 3.15: Added support for *path-like objects* and
   *bytes-like objects*.

exception wave.Error

   An error raised when something is impossible because it violates
   the WAV specification or hits an implementation deficiency.

wave.WAVE_FORMAT_PCM

   Format code for uncompressed PCM audio.

wave.WAVE_FORMAT_IEEE_FLOAT

   Format code for IEEE floating-point audio.

   Adicionado na versão 3.15.

wave.WAVE_FORMAT_EXTENSIBLE

   Format code for WAVE extensible headers.

   Adicionado na versão 3.12.


Objetos Wave_read
=================

class wave.Wave_read

   Read a WAV file.

   Wave_read objects, as returned by "open()", have the following
   methods:

   close()

      Close the stream if it was opened by "wave", and make the
      instance unusable.  This is called automatically on object
      collection.

   getnchannels()

      Returns number of audio channels ("1" for mono, "2" for stereo).

   getsampwidth()

      Retorna a largura da amostra em bytes.

   getframerate()

      Retorna a frequência de amostragem.

   getnframes()

      Retorna o número de quadros de áudio.

   getformat()

      Returns the frame format code.

      This is one of "WAVE_FORMAT_PCM", "WAVE_FORMAT_IEEE_FLOAT", or
      "WAVE_FORMAT_EXTENSIBLE".

      Adicionado na versão 3.15.

   getcomptype()

      Returns compression type ("'NONE'" is the only supported type).

   getcompname()

      Human-readable version of "getcomptype()". Usually "'not
      compressed'" parallels "'NONE'".

   getparams()

      Returns a "namedtuple()" "(nchannels, sampwidth, framerate,
      nframes, comptype, compname)", equivalent to output of the
      "get*()" methods.

   readframes(n)

      Reads and returns at most *n* frames of audio, as a "bytes"
      object.

   rewind()

      Volta o ponteiro do arquivo para o início do fluxo de áudio.

   Os dois métodos a seguir definem um termo "posição" que é
   compatível entre eles e é dependente da implementação.

   setpos(pos)

      Define o ponteiro de arquivo para a posição especificada.

   tell()

      Retorna a posição atual do ponteiro de arquivo.


Objetos Wave_write
==================

class wave.Wave_write

   Escreve um arquivo WAV.

   Objetos Wave_write, como retornados por "open()".

   For seekable output streams, the "wave" header will automatically
   be updated to reflect the number of frames actually written.  For
   unseekable streams, the *nframes* value must be accurate when the
   first frame data is written.  An accurate *nframes* value can be
   achieved either by calling "setnframes()" or "setparams()" with the
   number of frames that will be written before "close()" is called
   and then using "writeframesraw()" to write the frame data, or by
   calling "writeframes()" with all of the frame data to be written.
   In the latter case "writeframes()" will calculate the number of
   frames in the data and set *nframes* accordingly before writing the
   frame data.

   Alterado na versão 3.4: Added support for unseekable files.

   Wave_write objects have the following methods:

   close()

      Make sure *nframes* is correct, and close the file if it was
      opened by "wave".  This method is called upon object collection.
      It will raise an exception if the output stream is not seekable
      and *nframes* does not match the number of frames actually
      written.

   setnchannels(n)

      Define o número de canais.

   getnchannels()

      Return the number of channels.

   setsampwidth(n)

      Set the sample width to *n* bytes.

      For "WAVE_FORMAT_IEEE_FLOAT", only 4-byte (32-bit) and 8-byte
      (64-bit) sample widths are supported.

   getsampwidth()

      Return the sample width in bytes.

   setframerate(n)

      Set the frame rate to *n*.

      Alterado na versão 3.2: A non-integral input to this method is
      rounded to the nearest integer.

   getframerate()

      Return the frame rate.

   setnframes(n)

      Set the number of frames to *n*.  This will be changed later if
      the number of frames actually written is different (this update
      attempt will raise an error if the output stream is not
      seekable).

   getnframes()

      Return the number of audio frames written so far.

   setcomptype(type, name)

      Set the compression type and description. At the moment, only
      compression type "NONE" is supported, meaning no compression.

   getcomptype()

      Return the compression type ("'NONE'").

   getcompname()

      Return the human-readable compression type name.

   setformat(format)

      Set the frame format code.

      Supported values are "WAVE_FORMAT_PCM" and
      "WAVE_FORMAT_IEEE_FLOAT".

      When setting "WAVE_FORMAT_IEEE_FLOAT", the sample width must be
      4 or 8 bytes.

      Adicionado na versão 3.15.

   getformat()

      Return the current frame format code.

      Adicionado na versão 3.15.

   setparams(tuple)

      The *tuple* should be "(nchannels, sampwidth, framerate,
      nframes, comptype, compname, format)", with values valid for the
      "set*()" methods. Sets all parameters.

      For backwards compatibility, a 6-item tuple without *format* is
      also accepted and defaults to "WAVE_FORMAT_PCM".

      For "format=WAVE_FORMAT_IEEE_FLOAT", *sampwidth* must be 4 or 8.

      Alterado na versão 3.15: Added optional item *format* to the
      *tuple*.

   getparams()

      Return a "namedtuple()" "(nchannels, sampwidth, framerate,
      nframes, comptype, compname)" containing the current output
      parameters.

   tell()

      Return current position in the file, with the same disclaimer
      for the "Wave_read.tell()" and "Wave_read.setpos()" methods.

   writeframesraw(data)

      Escreve quadros de áudio, sem corrigir *nframes*.

      Alterado na versão 3.4: Todo *objeto bytes ou similar* agora é
      aceito.

   writeframes(data)

      Write audio frames and make sure *nframes* is correct.  It will
      raise an error if the output stream is not seekable and the
      total number of frames that have been written after *data* has
      been written does not match the previously set value for
      *nframes*.

      Alterado na versão 3.4: Todo *objeto bytes ou similar* agora é
      aceito.

      Note that it is invalid to set any parameters after calling
      "writeframes()" or "writeframesraw()", and any attempt to do so
      will raise "wave.Error".

      For "WAVE_FORMAT_IEEE_FLOAT" output, a "fact" chunk is written
      as required by the WAVE specification for non-PCM formats.
