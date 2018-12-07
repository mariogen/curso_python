import requests
import json

requests.get('http://localhost:5000/hello').text

requests.get('http://localhost:5000/sum/2/3').text

requests.post(
    'http://localhost:5000/operations',
    json={"a":2,s
          "b":3}).json()