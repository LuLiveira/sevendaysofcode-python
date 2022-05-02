import requests
import sys
import json
import gerador

from filme import Filme

token = sys.argv[1]

response = requests.get(f'https://imdb-api.com/en/API/Top250Movies/{token}')

json = json.loads(response.text)["items"]

filmes = []

for item in json:
    filmes.append(Filme(
        item["title"],
        item["image"],
        item["year"],
        item["imDbRating"]
    ))

body = ""

with open('index.html', 'w+') as html:
    for filme in filmes:
        body += gerador.generate_body(filme)

    html_finalizado = gerador.generate_html(body)
    
    html.write(html_finalizado)
