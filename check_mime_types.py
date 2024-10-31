#!/usr/bin/env python3

import http.client
import urllib.parse

# List of URLs to check
urls = [
    "https://mfhepp.github.io/test_mime_types/test.rdf",
    "https://mfhepp.github.io/test_mime_types/test.owl",
    "https://mfhepp.github.io/test_mime_types/test.ttl",
    "https://mfhepp.github.io/test_mime_types/test.nt",
    "https://mfhepp.github.io/test_mime_types/test.n3",
    "https://mfhepp.github.io/test_mime_types/test.jsonld"
]

# Define expected MIME types by file extension
mime_types = {
    "rdf": "application/rdf+xml",
    "owl": "application/owl+xml",
    "ttl": "text/turtle",
    "nt": "application/n-triples",
    "n3": "text/n3",
    "jsonld": "application/ld+json"
}

# Default MIME type if no extension matches
default_mime = "text/html"

# Function to get the expected MIME type based on file extension
def get_expected_mime(url):
    ext = url.split('.')[-1]  # Extract file extension from URL
    return mime_types.get(ext, default_mime)

# Function to fetch the Content-Type of a URL
def get_actual_mime(url):
    parsed_url = urllib.parse.urlparse(url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)
    conn.request("HEAD", parsed_url.path)
    response = conn.getresponse()
    content_type = response.getheader("Content-Type")
    conn.close()
    if content_type:
        # Split the MIME type and charset (e.g., "text/turtle; charset=UTF-8")
        return content_type.split(";")[0].strip()
    return None

# Loop through each URL and check the MIME type
for url in urls:
    expected_mime = get_expected_mime(url)
    actual_mime = get_actual_mime(url)

    if actual_mime == expected_mime:
        print(f"OK: {url} - MIME Type: {actual_mime}")
    else:
        print(f"ERROR: {url} - Expected MIME: {expected_mime}, Got: {actual_mime}")
