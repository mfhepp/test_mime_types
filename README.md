**Author:** Martin Hepp, martin.hepp@unibw.de

Experiments regarding the support of MIME types (aka media types or IANA media types) and HTTP Content Negotiation for RDF/XML, JSON-LD, Turtle, N3, and NTriples syntaxes.

The purpose of this repository is to test and document whether typical MIME types for Linked Open Data and the Semantic Web are properly derived from local filename extensions and lead to correct MIME type information in the HTTP Response Message header data.

**Source code on Github:** <https://github.com/mfhepp/test_mime_types>

**Github Pages version:**  <https://mfhepp.github.io/test_mime_types/>

**Note:** The actual payload of the examples is just quickly compiled from trivial examples in the respective specifications or other resources. They might not validate and have no meaningful content.

## Files List


| File Format | Filename | Expected MIME Type | Github MIME | Comment |
| --- | --- | --- | --- | --- |
| RDF in RDF/XML |  [test.rdf](test.rdf) | application/rdf+xml  | application/rdf+xml | **OK** |
| OWL in RDF/XML |  [test.owl](test.owl) | application/owl+xml  | application/rdf+xml| **OK** |
| Turtle         |  [test.ttl](test.ttl) | text/turtle | text/turtle| **OK** |
| NTriples       |  [test.nt](test.nt) | application/n-triples | application/n-triples| **OK** |
| N3             |  [test.n3](test.n3) | text/n3 | text/n3 | **OK** |
| JSON-LD        |  [test.jsonld](test.jsonld) | application/ld+json | application/ld+json | **OK** |

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

There is also a Python script [`check_mime_types.py`](./check_mime_types.py) for this purpose.

As of 2024-10-31, **all above files return the proper MIME type from their Github pages URIs.**

For files with the extention `.owl`, Github returns `application/rdf+xml` instead of `application/owl+xml `, but that's technically fine.

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

HTTP/2 200 
...
<b>content-type: text/html; charset=utf-8</b>
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
curl -I -H "Accept: application/rdf+xml" https://mfhepp.github.io/test_mime_types/test
curl -I -H "Accept: application/owl+xml" https://mfhepp.github.io/test_mime_types/test
curl -I -H "Accept: text/turtle" https://mfhepp.github.io/test_mime_types/test
curl -I -H "Accept: application/n-triples" https://mfhepp.github.io/test_mime_types/test
curl -I -H "Accept: text/n3" https://mfhepp.github.io/test_mime_types/test
curl -I -H "Accept: application/ld+json" https://mfhepp.github.io/test_mime_types/test
</pre>

There is also a bash script [`check_conneg.sh`](./check_conneg.sh)  for this purpose.

**Status 2024-10-31:** Unfortunately, Github Pages always returns the HTML version and ignores the indicated MIME type preferences:

<pre>

$ curl -I -H <b>"Accept: application/rdf+xml"</b> https://mfhepp.github.io/test_mime_types<b>/test</b>

HTTP/2 200 
server: GitHub.com
<b>content-type: text/html; charset=utf-8</b>
permissions-policy: interest-cohort=()
last-modified: Thu, 31 Oct 2024 11:56:02 GMT
access-control-allow-origin: *
etag: "67237052-2b2"
expires: Thu, 31 Oct 2024 12:28:16 GMT
cache-control: max-age=600
...
accept-ranges: bytes
age: 509
date: Thu, 31 Oct 2024 12:26:45 GMT
via: 1.1 varnish
...
vary: Accept-Encoding
...
content-length: 690
</pre>

#### 303 Redirects 

In an ideal world, Github Pages would return 303 redirects for an HTTP request with MIME type preferences that recommend another local file, e.g. requestion `application/rdf+xml` from the URI of JSON-LD variant, like so 

```
$ curl -I -H "Accept: application/rdf+xml" https://mfhepp.github.io/test_mime_types/test.jsonld
```

Again, **Github Pages simply returns the static file mapped to that URI, in this case `test.jsonld` with its original MIME type,** but neither redirects to a better matching URI nor hints to alternative representations:

<pre>
$ curl -I -H <b>"Accept: application/rdf+xml"</b> https://mfhepp.github.io/test_mime_types<b>/test.jsonld</b>

HTTP/2 200 
server: GitHub.com
<b>content-type: application/ld+json</b>
permissions-policy: interest-cohort=()
last-modified: Thu, 31 Oct 2024 11:56:02 GMT
access-control-allow-origin: *
etag: "67237052-dd"
expires: Thu, 31 Oct 2024 12:13:31 GMT
cache-control: max-age=600
...
accept-ranges: bytes
age: 203
date: Thu, 31 Oct 2024 12:28:25 GMT
via: 1.1 varnish
...
vary: Accept-Encoding
...
</pre>


## References

1. <https://www.w3.org/TR/rdf-syntax-grammar/#section-MIME-Type>
2. <https://www.w3.org/TR/owl2-xml-serialization/>
3. <https://www.w3.org/TR/turtle/>
4. <https://www.w3.org/TR/n-triples/>
5. <https://www.w3.org/TeamSubmission/n3/>
6. <https://www.w3.org/TR/json-ld11/>


## Changelog

- 2020-11-04: Initial version
- 2024-01-10: Updated status, cosmetic fixes, new theme, wording
- 2024-10-31: Updated status, fixed table, added scripts for automating tests
