import logging
from bs4 import BeautifulSoup
import requests

def acessar_pagina_ans(url):
    try:
        logging.info(f"Acessando página da ANS: {url}")
        response = requests.get(url)
        response.raise_for_status()
        logging.info("Página acessada com sucesso.")
        return BeautifulSoup(response.content, "html.parser")
    except requests.exceptions.RequestException as e:
        logging.error(f"Erro ao acessar a URL: {e}")
        return None
    
def encontrar_links_pdf(soup):
    links_pdf = []
    if soup:
        logging.info("Buscando links para os Anexos I e II em PDF...")
        for link in soup.find_all("a", href=True):
            href = link["href"]
            if ("Anexo I." in link.text or "Anexo II." in link.text) and href.endswith(".pdf"):
                links_pdf.append(href)
        # if links_pdf:
        #     logging.info(f"Encontrados {len(links_pdf)} links para download.")
        # else:
        #     logging.warning("Nenhum link encontrado.")
    return links_pdf