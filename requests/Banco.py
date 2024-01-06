import sqlite3 as sql
import pandas as pd

class Banco:
    def __init__(self, data_frame) -> None:
        self.data_frame = pd.DataFrame(data_frame).astype(str)
        self.path_db = 'C:/Users/erick/Documents/Python/requests/DATA/'
        self.path_csv = 'C:/Users/erick/Documents/Python/requests/CSV/'
        self.nome_banco = 'dados_aliexpress.db'

        conn = sql.connect(self.path_db + self.nome_banco)
        self.data_frame.to_sql(
            name='aliexpress_2024', 
            con=conn, if_exists='append',
            index=False
            )


    def baixa_csv(self, nome_arq):
        numeros = ''.join(num for num in nome_arq if num.isdigit())
        self.data_frame.to_csv(self.path_csv + f'dados_aliexpress{numeros}.csv', index=False)