import requests
import pprint

r = requests.get('http://127.0.0.1:5000/')
print("status ", r.status_code)
print()
print("headers \n", pprint.pformat(r.headers, indent=4))
print()
print("content:\n", r.text)
print()

try:
    print("content as JSON:\n", r.json())
except ValueError:
    print("Response content is not in JSON format.")
