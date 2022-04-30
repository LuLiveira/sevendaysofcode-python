import requests
import sys

token = sys.argv[1]

response = requests.get(f'https://imdb-api.com/en/API/Top250Movies/{token}')

print(response.text)