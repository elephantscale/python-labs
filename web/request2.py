import httplib2
from pprint import pprint

h = httplib2.Http('.cache')
response, content = h.request('http://127.0.0.1:5000/')
#response, content = h.request('http://www.google.com/')
print("-----headers----")
pprint(response)
print('-----content----')
pprint(content)
