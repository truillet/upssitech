import requests // lit requête http
import json // encode et décode JSON

x = requests.get('http://jsonplaceholder.typicode.com/users') // FAKE JSON file

print(x.text)