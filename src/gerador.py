def generate_html(body: str) -> str:
    return __generate_header(f"<body> {body} </body>")    
    
def generate(filme) -> str:
    return f"""
        <div class=\"card text-white bg-dark mb-3\" style=\"max-width: 18rem;\">
	        <h4 class=\"card-header\">{filme.titulo}</h4>
	        <div class=\"card-body\">
		        <img class=\"card-img\" src=\"{filme.imagem_url}\" alt=\"{filme.titulo}\">
		        <p class=\"card-text mt-2\">Nota: {filme.nota} - Ano: {filme.ano}</p>
	        </div>
        </div>   
        """

def __generate_header(body: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="pt">
    <head>
        <meta charset=\"utf-8\">
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">
        <link rel=\"stylesheet\" href=\"https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css\" 
            "integrity=\"sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm\" crossorigin=\"anonymous\">					
    </head>
        {body}
    </html>
    """