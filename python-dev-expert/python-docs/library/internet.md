Protocolos de Internet e Suporte
********************************

Os módulos descritos neste capítulo implementam protocolos de internet
e suporte para tecnologia relacionada. Todos eles são implementados em
Python. A maioria desses módulos requer a presença do módulo
dependente do sistema "socket", que atualmente é suportado na maioria
das plataformas populares. Segue uma visão geral:

* "webbrowser" --- Controlador de navegador web conveniente

  * Interface de linha de comando

  * Objetos controladores de navegador

* "wsgiref" --- Implementação de referência e utilitários WSGI

  * "wsgiref.util" -- WSGI environment utilities

  * "wsgiref.headers" -- WSGI response header tools

  * "wsgiref.simple_server" -- a simple WSGI HTTP server

  * "wsgiref.validate" --- WSGI conformance checker

  * "wsgiref.handlers" -- server/gateway base classes

  * "wsgiref.types" -- WSGI types for static type checking

  * Exemplos

* "urllib" --- Módulos de manipulação de URL

* "urllib.request" --- Biblioteca extensível para abrir URLs

  * Objeto Request

  * OpenerDirector Objects

  * BaseHandler Objects

  * HTTPRedirectHandler Objects

  * HTTPCookieProcessor Objects

  * ProxyHandler Objects

  * HTTPPasswordMgr Objects

  * HTTPPasswordMgrWithPriorAuth Objects

  * AbstractBasicAuthHandler Objects

  * HTTPBasicAuthHandler Objects

  * ProxyBasicAuthHandler Objects

  * AbstractDigestAuthHandler Objects

  * HTTPDigestAuthHandler Objects

  * ProxyDigestAuthHandler Objects

  * HTTPHandler Objects

  * Objetos HTTPSHandler

  * FileHandler Objects

  * DataHandler Objects

  * FTPHandler Objects

  * CacheFTPHandler Objects

  * Objetos UnknownHandler

  * HTTPErrorProcessor Objects

  * Exemplos

  * Legacy interface

  * "urllib.request" Restrictions

* "urllib.response" --- Response classes used by urllib

* "urllib.parse" --- Analisa URLs para componentes

  * Análise de URL

  * Segurança ao analisar URLs

  * Analisando bytes codificados em ASCII

  * Structured Parse Results

  * URL Quoting

* "urllib.error" --- Classes de exceção levantadas por urllib.request

* "urllib.robotparser" ---  Analisador sintático de robots.txt

* "http" --- Módulos HTTP

  * Códigos de estado HTTP

  * Categoria de estado HTTP

  * Métodos HTTP

* "http.client" --- HTTP protocol client

  * Objetos de HTTPConnection

  * Objetos HTTPResponse

  * Exemplos

  * HTTPMessage Objects

* "ftplib" --- FTP protocol client

  * Referência

    * FTP objects

    * FTP_TLS objects

    * Module variables

* "poplib" --- Cliente de protocolo POP3

  * Objetos POP3

  * Exemplo POP3

* "imaplib" --- IMAP4 protocol client

  * Objetos IMAP4

  * Exemplo IMAP4

* "smtplib" --- Cliente de protocolo SMTP

  * Objetos SMTP

  * Exemplo SMTP

* "uuid" --- Objetos UUID conforme **RFC 9562**

  * Uso na linha de comando

  * Exemplo

  * Exemplo de linha de comando

* "socketserver" --- Um framework para servidores de rede

  * Notas sobre criação do servidor

  * Objetos Server

  * Objetos manipulador de requisições

  * Exemplos

    * Exemplo de "socketserver.TCPServer"

    * Exemplo "socketserver.UDPServer"

    * Mixins assíncronos

* "http.server" --- HTTP servers

  * Interface de linha de comando

  * Considerações de segurança

* "http.cookies" --- HTTP state management

  * Objetos Cookie

  * Objetos Morsel

  * Exemplo

* "http.cookiejar" --- Cookie handling for HTTP clients

  * CookieJar and FileCookieJar objects

  * FileCookieJar subclasses and co-operation with web browsers

  * CookiePolicy objects

  * DefaultCookiePolicy objects

  * Cookie objects

  * Exemplos

* "xmlrpc" --- Módulos de servidor e cliente XMLRPC

* "xmlrpc.client" --- Cliente XML-RPC

  * Objetos ServerProxy

  * Objetos DateTime

  * Objetos Binários

  * Objetos Fault

  * Objetos ProtocolError

  * Objetos MultiCall

  * Convenience Functions

  * Exemplo de uso do cliente

  * Example of Client and Server Usage

* "xmlrpc.server" --- Servidores XML-RPC básicos

  * SimpleXMLRPCServer objects

    * SimpleXMLRPCServer example

  * CGIXMLRPCRequestHandler

  * Documentando servidor XMLRPC

  * DocXMLRPCServer objects

  * DocCGIXMLRPCRequestHandler

* "ipaddress" --- Biblioteca de manipulação de IPv4/IPv6

  * Funções de fábrica de conveniência

  * Endereços IP

    * Objetos de endereço

    * Conversão para strings e inteiros

    * Operadores

      * Operadores de comparação

      * Operadores aritméticos

  * Definições de rede IP

    * Prefixo, máscara de rede e máscara de host

    * Objetos de rede

    * Operadores

      * Operadores lógicos

      * Iteração

      * Redes como contêineres de endereços

  * Objetos de interface

    * Operadores

      * Operadores lógicos

  * Outras funções de nível de módulo

  * Exceções personalizadas
