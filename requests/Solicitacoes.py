import os
import time
import requests
from numpy import random


class Solicitacoes:
    def __init__(self) -> None:
        # Cria o diretorio se nao existe
        path_dados_html = 'C:/Users/erick/Documents/Python/requests/HTML'
        if not os.path.exists(path_dados_html):
            os.mkdir(path_dados_html)


    def baixa_dados(self):
        # Baixa os 60 HTMLs, e coloca em um arquivo index aleatorio
        num = random.randint(9, size=6)
        num = [str(n) for n in num]
        num = ''.join(num)
        path = f'C:/Users/erick/Documents/Python/requests/HTML/index{num}.html'


        with open(path, 'a', encoding='utf-8') as file:
            # Lista de URLs para as 60 requisições
            urls = [
                f'https://pt.aliexpress.com/w/wholesale-placa-de-video.html?page={page}&g=n&SearchText=placa+de+video'
                for page in range(1, 61)
            ]

            # Fazendo as 60 requisições GET para as URLs
            for i, url in enumerate(urls):
                response = requests.get(url)
                if response.status_code == 200:
                    print(response, f"Solicitação: {i}")
                    file.write(response.text)
                    file.write('/n/n')
                else:
                    print(f"A requisição para {url} falhou com o código de status: {response.status_code}")

                # Intervalo de 30s entre as requisições
                time.sleep(30)

        return path