# Funções e sinônimos e obsoletos do OCI8

> **Fonte / Source:** https://www.php.net/manual/pt_BR/oldaliases.oci8.php

---

# Funções e sinônimos e obsoletos do OCI8

## Índice

- [oci\_internal\_debug](function.oci-internal-debug.md) — Habilita ou desabilita a saíde interna de depuração
- [ocibindbyname](function.ocibindbyname.md) — Sinônimo de oci\_bind\_by\_name
- [ocicancel](function.ocicancel.md) — Sinônimo de oci\_cancel
- [ocicloselob](function.ocicloselob.md) — Sinônimo de OCILob::close
- [ocicollappend](function.ocicollappend.md) — Sinônimo de OCICollection::append
- [ocicollassign](function.ocicollassign.md) — Sinônimo de OCICollection::assign
- [ocicollassignelem](function.ocicollassignelem.md) — Sinônimo de OCICollection::assignElem
- [ocicollgetelem](function.ocicollgetelem.md) — Sinônimo de OCICollection::getElem
- [ocicollmax](function.ocicollmax.md) — Sinônimo de OCICollection::max
- [ocicollsize](function.ocicollsize.md) — Sinônimo de OCICollection::size
- [ocicolltrim](function.ocicolltrim.md) — Sinônimo de OCICollection::trim
- [ocicolumnisnull](function.ocicolumnisnull.md) — Sinônimo de oci\_field\_is\_null
- [ocicolumnname](function.ocicolumnname.md) — Sinônimo de oci\_field\_name
- [ocicolumnprecision](function.ocicolumnprecision.md) — Sinônimo de oci\_field\_precision
- [ocicolumnscale](function.ocicolumnscale.md) — Sinônimo de oci\_field\_scale
- [ocicolumnsize](function.ocicolumnsize.md) — Sinônimo de oci\_field\_size
- [ocicolumntype](function.ocicolumntype.md) — Sinônimo de oci\_field\_type
- [ocicolumntyperaw](function.ocicolumntyperaw.md) — Sinônimo de oci\_field\_type\_raw
- [ocicommit](function.ocicommit.md) — Sinônimo de oci\_commit
- [ocidefinebyname](function.ocidefinebyname.md) — Sinônimo de oci\_define\_by\_name
- [ocierror](function.ocierror.md) — Sinônimo de oci\_error
- [ociexecute](function.ociexecute.md) — Sinônimo de oci\_execute
- [ocifetch](function.ocifetch.md) — Sinônimo de oci\_fetch
- [ocifetchinto](function.ocifetchinto.md) — Variante obsoleta de oci\_fetch\_array, oci\_fetch\_object,
  oci\_fetch\_assoc e
  oci\_fetch\_row
- [ocifetchstatement](function.ocifetchstatement.md) — Sinônimo de oci\_fetch\_all
- [ocifreecollection](function.ocifreecollection.md) — Sinônimo de OCICollection::free
- [ocifreecursor](function.ocifreecursor.md) — Sinônimo de oci\_free\_statement
- [ocifreedesc](function.ocifreedesc.md) — Sinônimo de OCILob::free
- [ocifreestatement](function.ocifreestatement.md) — Sinônimo de oci\_free\_statement
- [ociinternaldebug](function.ociinternaldebug.md) — Sinônimo de oci\_internal\_debug
- [ociloadlob](function.ociloadlob.md) — Sinônimo de OCILob::load
- [ocilogoff](function.ocilogoff.md) — Sinônimo de oci\_close
- [ocilogon](function.ocilogon.md) — Sinônimo de oci\_connect
- [ocinewcollection](function.ocinewcollection.md) — Sinônimo de oci\_new\_collection
- [ocinewcursor](function.ocinewcursor.md) — Sinônimo de oci\_new\_cursor
- [ocinewdescriptor](function.ocinewdescriptor.md) — Sinônimo de oci\_new\_descriptor
- [ocinlogon](function.ocinlogon.md) — Sinônimo de oci\_new\_connect
- [ocinumcols](function.ocinumcols.md) — Sinônimo de oci\_num\_fields
- [ociparse](function.ociparse.md) — Sinônimo de oci\_parse
- [ociplogon](function.ociplogon.md) — Sinônimo de oci\_pconnect
- [ociresult](function.ociresult.md) — Sinônimo de oci\_result
- [ocirollback](function.ocirollback.md) — Sinônimo de oci\_rollback
- [ocirowcount](function.ocirowcount.md) — Sinônimo de oci\_num\_rows
- [ocisavelob](function.ocisavelob.md) — Sinônimo de OCILob::save
- [ocisavelobfile](function.ocisavelobfile.md) — Sinônimo de OCILob::import
- [ociserverversion](function.ociserverversion.md) — Sinônimo de oci\_server\_version
- [ocisetprefetch](function.ocisetprefetch.md) — Sinônimo de oci\_set\_prefetch
- [ocistatementtype](function.ocistatementtype.md) — Sinônimo de oci\_statement\_type
- [ociwritelobtofile](function.ociwritelobtofile.md) — Sinônimo de OCILob::export
- [ociwritetemporarylob](function.ociwritetemporarylob.md) — Sinônimo de OCILob::writeTemporary

`↑` and `↓` to navigate •
`Enter` to select •
`Esc` to close • `/` to open

document.addEventListener("DOMContentLoaded", function() {
/\*{{{Search Modal\*/
const language = 'local';
initSearchModal();
initPHPSearch(language).then((searchCallback) => {
initSearchUI({language, searchCallback, limit: 30});
});
/\*}}}\*/
});
