import requests
import sys
import json
import gerador


from filme import Filme

def exibir_valores(lista: list) -> None:
    for i in lista:
        print(i)


token = sys.argv[1]

response = requests.get(f'https://imdb-api.com/en/API/Top250Movies/{token}')

json = json.loads(response.text)["items"]

filmes = []

for item in json:
    filme = Filme(
        item["title"],
        item["image"],
        item["year"],
        item["imDbRating"]
    )
    filmes.append(filme)

body = ""

with open('main.html', 'w+') as html:
    for filme in filmes:
        body += gerador.generate(filme)

    html_finalizado = gerador.generate_html(body)
    
    html.write(html_finalizado)
