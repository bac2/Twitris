import httplib

conn = httplib.HTTPConnection("www.google.com")
conn.request("GET", "/index.html")
r1 = conn.getresponse()
print r1.read()
