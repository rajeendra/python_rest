import requests
# pip install requests

import json

# 1.
response = requests.get("http://127.0.0.1:8000/drinks/")

my_json = response.content.decode('utf8').replace("'", '"')
data = json.loads(my_json)

print(data['drinks'], type(data))

# 2.
print('')
response = requests.get("http://127.0.0.1:8000/drinks/2")

my_json = response.content.decode('utf8').replace("'", '"')
data = json.loads(my_json)

print(data, type(data))