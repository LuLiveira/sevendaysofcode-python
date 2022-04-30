import requests
import sys
import json


def exibir_valores(lista: list) -> None:
    for i in lista:
        print(i)


token = sys.argv[1]

response = requests.get(f'https://imdb-api.com/en/API/Top250Movies/{token}')

json = json.loads(response.text)["items"]

titulos = []
imagens_url = []
anos = []
notas = []

for filme in json:
    titulos.append(filme["title"])
    imagens_url.append(filme["image"])
    anos.append(filme["year"])
    notas.append(filme["imDbRating"])

exibir_valores(titulos)
exibir_valores(imagens_url)
exibir_valores(anos)
exibir_valores(notas)
