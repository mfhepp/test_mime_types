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

On top of that, an HTTP HEAD request without any file extension returns the HTML version, which is good:

```
$ curl -I https://mfhepp.github.io/test_mime_types/test

HTTP/1.1 200 OK
...
**Content-Type: text/html;** charset=utf-8
Server: GitHub.com
...
```

## References
1. <https://www.w3.org/TR/rdf-syntax-grammar/#section-MIME-Type>
2. <https://www.w3.org/TR/owl2-xml-serialization/>
3. <https://www.w3.org/TR/turtle/>
4. <https://www.w3.org/TR/n-triples/>
5. <https://www.w3.org/TeamSubmission/n3/>
6. <https://www.w3.org/TR/json-ld11/>
