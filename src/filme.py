import json

class Filme:
    def __init__(self, titulo: str, imagem_url: str, ano: int, nota: float) -> None:
        self.__titulo = titulo
        self.__imagem_url = imagem_url
        self.__ano = ano
        self.__nota = nota

    @property
    def titulo(self) -> str:
        return self.__titulo

    @property
    def imagem_url(self) -> str:
        return self.__imagem_url

    @property
    def ano(self) -> int:
        return self.__ano

    @property
    def nota(self) -> float:
        return self.__nota