import pycurl
import re
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

headers = {}


def header_function(header_line):
    # On Python 3, decoding step is required.
    header_line = header_line.decode('iso-8859-1')

    # Header lines include the first status line (HTTP/1.x ...).
    # We are going to ignore all lines that don't have a colon in them.
    # This will botch headers that are split on multiple lines...
    if ':' not in header_line:
        return

    name, value = header_line.split(':', 1)
    name = name.strip().lower()
    value = value.strip()

    # Now we can actually record the header name and value.
    # Note: this only works when headers are not duplicated, see below.
    headers[name] = value


buffer = BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, 'http://pycurl.io')
c.setopt(c.WRITEFUNCTION, buffer.write)
# Set our header function.
c.setopt(c.HEADERFUNCTION, header_function)
c.perform()
c.close()

# Figure out what encoding was sent with the response, if any.
# Check against lowercased header name.
encoding = None
if 'content-type' in headers:
    content_type = headers['content-type'].lower()
    match = re.search(r'charset=(\S+)', content_type)
    if match:
        encoding = match.group(1)
        print('Decoding using %s' % encoding)
if encoding is None:
    # Default encoding for HTML is iso-8859-1.
    # Other content types may have different default encoding,
    # or in case of binary data, may have no encoding at all.
    encoding = 'iso-8859-1'
    print('Assuming encoding is %s' % encoding)

body = buffer.getvalue()
# Decode using the encoding we figured out.
print(body.decode(encoding))


if name in headers:
    if isinstance(headers[name], list):
        headers[name].append(value)
    else:
        headers[name] = [headers[name], value]
else:
    headers[name] = value
