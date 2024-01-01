import os
import time
import requests
from numpy import random

class Solicitacoes:
    def __init__(self) -> None:
        path_dados_csv = 'C:/Users/erick/Documents/Python/requests/HTML'
        if not os.path.exists(path_dados_csv):
            os.mkdir(path_dados_csv)

    def baixa_dados():
        num = random.randint(9, size=6)
        num = [str(n) for n in num]
        num = ''.join(num)

        path = f'C:/Users/erick/Documents/Python/requests/HTML/index{num}.html'

        # Abre o arquivo index.html para adicionar conteúdo no final
        with open(path, 'a', encoding='utf-8') as file:
            # Lista de URLs para as 60 requisições
            urls = [
                f'https://pt.aliexpress.com/w/wholesale-placa-de-video.html?page={page}&g=n&SearchText=placa+de+video'
                for page in range(1, 61)
            ]

            # Fazendo as 60 requisições GET para as URLs com um intervalo de 2 segundos entre elas
            for i, url in enumerate(urls):
                response = requests.get(url)
                print(response, f"Solicitação: {i}")
                if response.status_code == 200:
                    file.write(response.text)
                    file.write('/n/n')  # Adiciona linhas em branco entre os conteúdos das requisições
                else:
                    print(f"A requisição para {url} falhou com o código de status: {response.status_code}")

                # Adiciona um intervalo de 2 segundos entre as requisições
                time.sleep(60)

        return path