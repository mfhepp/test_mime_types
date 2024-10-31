#!/bin/bash

# Target URL
url="https://mfhepp.github.io/test_mime_types/test"

# Define MIME types for content negotiation
accept_types=(
    "application/rdf+xml"
    "application/owl+xml"
    "text/turtle"
    "application/n-triples"
    "text/n3"
    "application/ld+json"
)

# Loop through each MIME type and make the request
echo "Trying content negotiation on $url"
echo ===========================================================================
for accept in "${accept_types[@]}"; do
    echo -n "Testing $accept == returns => "
    # Use curl with grep to filter only the Content-Type line
    curl -I -H "Accept: $accept" "$url" 2>/dev/null | grep -i '^content-type:'
done
