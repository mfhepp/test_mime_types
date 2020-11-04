# Test for MIME Support in Github Pages

The purpose of this repository is to test whether typical MIME types for Linked Open Data and the Semantic Web are properly derived from local filename extensions and lead to correct MIME type information in the HTTP Response Message header data.

The source code is [on Github](https://github.com/mfhepp/test_mime_types).

The actual Github Pages version is at <https://mfhepp.github.io/test_mime_types/>.

**Note:** The actual payload of the examples is just quickly compiled from trivial examples in the respective specifications or other resources. They might not validate and have no meaningful content.

## Files List

|File Format|Filename|Expected MIME Type|Github MIME |Comment|
|---|---|---|---|
|RDF in RDF/XML | [test.rdf](test.rdf) | application/rdf+xml  | application/rdf+xml | **OK** |
|OWL in RDF/XML | [test.owl](test.owl) | application/owl+xml  | application/rdf+xml| **OK**|
|Turtle         | [test.ttl](test.ttl) | text/turtle |text/turtle| **OK** |
|NTriples       | [test.nt](test.nt) | application/n-triples | application/n-triples| **OK** |
|N3             | [test.n3](test.n3) | text/n3 | text/n3 | **OK** |
|JSON-LD        | [test.jsonld](test.jsonld) | application/ld+json | application/ld+json | **OK** |

## Status of Github Pages Support

### Correct MIME Type 

You can always check the current status of support by using `curl`.

```
$ curl -I https://mfhepp.github.io/test_mime_types/test.rdf
$ curl -I https://mfhepp.github.io/test_mime_types/test.owl
$ curl -I https://mfhepp.github.io/test_mime_types/test.ttl
$ curl -I https://mfhepp.github.io/test_mime_types/test.nt
$ curl -I https://mfhepp.github.io/test_mime_types/test.n3
$ curl -I https://mfhepp.github.io/test_mime_types/test.jsonld
```

As of 2020-11-03, **all above files return the proper MIME type from their Github pages URIs.**

So Github Pages is able to recognize the proper MIME type from the file extension and signal it back to the client in the HTTP response header.

### Content Negotiation

Some of the current recommendations for the deployment of Linked Data and Web ontologies on the Web require server-side [HTTP Content Negotiation](https://tools.ietf.org/html/rfc7231#section-3.4) (called "pro-active content negotiation" in the new [IETF RFC 7231](https://tools.ietf.org/html/rfc7231).

- https://www.w3.org/TR/swbp-vocab-pub/
- http://wifo5-03.informatik.uni-mannheim.de/bizer/pub/LinkedDataTutorial/
- https://www.w3.org/TR/ld-bp/

This can also be checked with `curl`, see e.g. [Richard Cyganiak's nice tutorial on this](http://richard.cyganiak.de/blog/2007/02/debugging-semantic-web-sites-with-curl/).

The very simple case of returning HTML as a default for an HTTP HEAD request without any file extension returns the HTML version, is properly supported:

<pre>
$ curl -I https://mfhepp.github.io/test_mime_types/test

HTTP/1.1 200 OK
...
<b>Content-Type: text/html;</b> charset=utf-8
Server: GitHub.com
...
</pre>

Ideally, two other scenarios would be supported:

#### Server-side Content Negotiation for URI without File Extension Suffix

Cool URIs for Linked Data would ideally be supported, i.e. the best-matching representation would be returned baded on the `Accept` request header parameter, like so

```
$ curl -I -H "Accept: application/rdf+xml" 
```

for `text/html` and all available RDF syntaxes:

- application/rdf+xml
- application/owl+xml
- text/turtle
- application/n-triples
- text/n3
- application/ld+json

<pre>
$ curl -I -H "Accept: application/rdf+xml" https://mfhepp.github.io/test_mime_types/test
$ curl -I -H "Accept: application/owl+xml" https://mfhepp.github.io/test_mime_types/test
$ curl -I -H "Accept: text/turtle" https://mfhepp.github.io/test_mime_types/test
$ curl -I -H "Accept: application/n-triples" https://mfhepp.github.io/test_mime_types/test
$ curl -I -H "Accept: text/n3" https://mfhepp.github.io/test_mime_types/test
$ curl -I -H "Accept: application/ld+json" https://mfhepp.github.io/test_mime_types/test
</pre>

**Status 2020-11-04:** Unfortunately, Github Pages always returns the HTML version and ignores the indicated MIME type preferences:

<pre>

$ curl -I -H <b>"Accept: application/rdf+xml"</b> https://mfhepp.github.io/test_mime_types<b>/test</b>

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 690
<b>Content-Type: text/html; charset=utf-8</b>
Server: GitHub.com
Last-Modified: Tue, 03 Nov 2020 16:30:18 GMT
ETag: "5fa1859a-2b2"
Access-Control-Allow-Origin: *
Expires: Wed, 04 Nov 2020 15:43:50 GMT
Cache-Control: max-age=600
Accept-Ranges: bytes
Date: Wed, 04 Nov 2020 15:48:18 GMT
Via: 1.1 varnish
Vary: Accept-Encoding
</pre>

#### 303 Redirects 

In an ideal world, Github Pages would return 303 redirects for an HTTP request with MIME type preferences that recommend another local file, e.g. requestion `application/rdf+xml` from the URI of JSON-LD variant, like so 

```
$ curl -I -H "Accept: application/rdf+xml" https://mfhepp.github.io/test_mime_types/test.jsonld
```

Again, **Github Pages simply returns the static file mapped to that URI, in this case `test.jsonld` with its original MIME type,** but neither redirects to a better matching URI nor hints to alternative representations:

<pre>
$ curl -I -H <b>"Accept: application/rdf+xml"</b> https://mfhepp.github.io/test_mime_types<b>/test.jsonld</b>

HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 221
<b>Content-Type: application/ld+json</b>
Server: GitHub.com
Last-Modified: Tue, 03 Nov 2020 16:30:18 GMT
ETag: "5fa1859a-dd"
Access-Control-Allow-Origin: *
Expires: Wed, 04 Nov 2020 16:02:11 GMT
Cache-Control: max-age=600
Accept-Ranges: bytes
Date: Wed, 04 Nov 2020 15:52:11 GMT
Via: 1.1 varnish
Age: 0
Vary: Accept-Encoding
</pre>

## References
1. <https://www.w3.org/TR/rdf-syntax-grammar/#section-MIME-Type>
2. <https://www.w3.org/TR/owl2-xml-serialization/>
3. <https://www.w3.org/TR/turtle/>
4. <https://www.w3.org/TR/n-triples/>
5. <https://www.w3.org/TeamSubmission/n3/>
6. <https://www.w3.org/TR/json-ld11/>
