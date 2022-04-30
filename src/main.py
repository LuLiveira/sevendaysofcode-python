import requests
import sys
import json


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
        body += f"""
        <div class=\"card text-white bg-dark mb-3\" style=\"max-width: 18rem;\">
	        <h4 class=\"card-header\">{filme.titulo}</h4>
	        <div class=\"card-body\">
		        <img class=\"card-img\" src=\"{filme.imagem_url}\" alt=\"%s\">
		        <p class=\"card-text mt-2\">Nota: {filme.nota} - Ano: {filme.ano}</p>
	        </div>
        </div>   
        """

    html_principal = f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset=\"utf-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">
        <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css\" 
            + "integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">					
    </head>
    <body>
        {body}
    </body>
    </html>
    """

    html.write(html_principal)
