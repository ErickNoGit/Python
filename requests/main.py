import os
from Banco import Banco
from Raspagem import Raspagem
from Solicitacoes import Solicitacoes

path_dados_sql = 'C:/Users/erick/Documents/Python/requests/DATA'
if not os.path.exists(path_dados_sql):
    os.mkdir(path_dados_sql)

path_dados_csv = 'C:/Users/erick/Documents/Python/requests/CSV'
if not os.path.exists(path_dados_csv):
    os.mkdir(path_dados_csv)

solicita = Solicitacoes()
arquivo_html = solicita.baixa_dados()

raspar = Raspagem(arquivo=arquivo_html)
dados = raspar.coleta_dados()

banco = Banco(data_frame=dados)
banco.baixa_csv(nome_arq=arquivo_html)

# Caminho do arquivo atual (html) e o destino para movê-lo
caminho_destino = arquivo_html.replace('HTML', 'TEMP')
if os.path.exists(arquivo_html):
    os.rename(arquivo_html, caminho_destino)
    print("Arquivo movido com sucesso!")
else:
    print("O arquivo de origem não foi encontrado.")
