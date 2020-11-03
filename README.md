# Test for MIME Support in Github Pages

The purpose of this repository is to test whether typical MIME types for Linked Open Data and the Semantic Web are properly derived from local filename extensions and lead to correct MIME type information in the HTTP Response Message header data.

The source code is [on Github](https://github.com/mfhepp/test_mime_types).

The actual Github Pages version is at https://mfhepp.github.io/test_mime_types/.

## Files List

|File Format|Filename|Expected MIME Type|Comment|
|---|---|---|---|
|RDF in RDF/XML | [test.rdf](test.rdf) | application/rdf+xml  |   |
|OWL in RDF/XML | test.owl | application/owl+xml  |   |
|Turtle         | test.ttl | text/turtle |   |
|N3             | test.n3 | text/n3 |   |
|JSON-LD        | test.jsonld | application/ld+json  |   |


## References
1. https://www.w3.org/TR/rdf-syntax-grammar/#section-MIME-Type
2. https://www.w3.org/TR/owl2-xml-serialization/
3. https://www.w3.org/TR/turtle/
4. https://www.w3.org/TeamSubmission/n3/
5. https://www.w3.org/TR/json-ld11/
