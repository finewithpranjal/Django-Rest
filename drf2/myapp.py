import requests
import json
URL = "http://127.0.0.1:8000/stucr/"

data = {
    'name' : 'John Doe',
    'roll' : 101,
    'city' : 'New York'
}

json_data = json.dumps(data) # CONVERTING PYTHON DICTIONARY TO JSON DATA
r = requests.post(url=URL, data= json_data)

data = r.json()
print(data)