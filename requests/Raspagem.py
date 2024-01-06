import numpy as np
from bs4 import BeautifulSoup


class Raspagem:
    def __init__(self, arquivo) -> None:
        # Le o arquivo html baixado
        self.html = arquivo
        with open(self.html, 'r', encoding='utf-8') as arq:
            self.html = arq.read()

    def coleta_dados(self):
        # API responsável por retornar um dicionario de dados
        nome_produto = []
        link_produto = []
        link_imagem = []
        vendidos = []
        frete = []
        preco_atual = []
        preco_certo = []
        oferta = []
        nome_loja = []


        soup = BeautifulSoup(self.html, 'html.parser')
        css_classe = 'list--list--3wn4cH5 search-item-card-wrapper-list'
        div_padrao = soup.find_all('div', class_=css_classe) # retorna bloco com elementos


        for div in div_padrao:
            classe_do_link = "multi--container--1UZxxHY"
            nome_tag_link = div.find('a', class_=classe_do_link)
            link_a = nome_tag_link.get('href') if nome_tag_link else 'NaN'
            if link_a:
                link_produto.append(link_a) # armazena o link para produto


            classe_da_imagem = "images--item--3XZa6xf"
            nome_tag_img = div.find('img', class_=classe_da_imagem)
            link_img = nome_tag_img.get('src') if nome_tag_img else 'NaN'
            if link_img:
                link_imagem.append(link_img)


            classe_do_titulo = "multi--titleText--nXeOvyr"
            nome_tag_titulo = div.find('h1', class_=classe_do_titulo)
            texto = nome_tag_titulo.get_text(strip=True) if nome_tag_titulo else 'NaN'
            if texto:
                nome_produto.append(texto)


            classe_do_titulo = "multi--trade--Ktbl2jB"
            nome_tag_titulo = div.find('span', class_=classe_do_titulo)
            qtd_vendidos = nome_tag_titulo.get_text(strip=True) if nome_tag_titulo else 'NaN'
            if qtd_vendidos:
                vendidos.append(''.join(filter(str.isdigit, qtd_vendidos)))


            classe_do_titulo = "tag--text--1BSEXVh tag--textStyle--3dc7wLU multi--serviceStyle--1Z6RxQ4"
            nome_tag_titulo = div.find('span', class_=classe_do_titulo)
            texto = nome_tag_titulo.get_text(strip=True) if nome_tag_titulo else 'NaN'
            if texto:
                frete.append(texto)


            classe_do_titulo = "multi--price-sale--U-S0jtj"
            nome_tag_titulo = div.find('div', class_=classe_do_titulo)
            price_organized = nome_tag_titulo.get_text(strip=True) if nome_tag_titulo else 'NaN'
            if price_organized:
                preco_atual.append(price_organized)


            classe_do_titulo = "multi--price-original--1zEQqOK"
            nome_tag_titulo = div.find('div', class_=classe_do_titulo)
            preco_original = nome_tag_titulo.get_text(strip=True) if nome_tag_titulo else 'NaN'
            if preco_original:
                preco_certo.append(preco_original)


            classe_do_titulo = "multi--discount--3hksz5G"
            nome_tag_titulo = div.find('span', class_=classe_do_titulo)
            moeda_oferta = nome_tag_titulo.get_text(strip=True) if nome_tag_titulo else 'NaN'
            if moeda_oferta:
                oferta.append(moeda_oferta)


            classe_do_titulo = "cards--store--3GyJcot"
            nome_tag_titulo = div.find('span', class_=classe_do_titulo)
            nome_loja_text = nome_tag_titulo.find_next('a').text.strip() if nome_tag_titulo else np.nan
            if nome_loja_text:
                nome_loja.append(nome_loja_text)


        # Garante que todas as listas tenham o mesmo comprimento
        max_len = max(
            len(nome_produto), len(link_produto),
            len(link_imagem), len(vendidos),
            len(frete), len(preco_atual),
            len(preco_certo), len(oferta),
            len(nome_loja)
        )


        nome_produto += [np.nan] * (max_len - len(nome_produto))
        link_produto += [np.nan] * (max_len - len(link_produto))
        link_imagem += [np.nan] * (max_len - len(link_imagem))
        vendidos += [np.nan] * (max_len - len(vendidos))
        frete += [np.nan] * (max_len - len(frete))
        preco_atual += [np.nan] * (max_len - len(preco_atual))
        preco_certo += [np.nan] * (max_len - len(preco_certo))
        oferta += [np.nan] * (max_len - len(oferta))
        nome_loja += [np.nan] * (max_len - len(nome_loja))


        return {
            'nome_produto': nome_produto,
            'link_produto': link_produto,
            'link_imagem': link_imagem,
            'quant_vendida': vendidos,
            'dados_frete': frete,
            'preco_atual': preco_atual,
            'preco_certo': preco_certo,
            'oferta': oferta,
            'nome_loja': nome_loja
        }