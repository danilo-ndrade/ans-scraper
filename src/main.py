import logging
from scraping.scraper import acessar_pagina_ans, encontrar_links_pdf
from utils.download import baixar_anexos_ans
from utils.zip_file import zip_file
from pathlib import Path

#Config para logs
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

RAIZ = Path(__file__).resolve().parent.parent

URL_ANS = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
PASTA_DOWNLOAD = RAIZ / "data" / "anexos_ans"
NOME_ARQUIVO_ZIP = RAIZ / "data" / "anexos_ans.zip"

def main():
    soup = acessar_pagina_ans(URL_ANS)
    links_pdf = encontrar_links_pdf(soup)
    if links_pdf:
        logging.info(f"Encontrados {len(links_pdf)} links para download.")
        download = baixar_anexos_ans(links_pdf, PASTA_DOWNLOAD)
        if download:
            logging.info("Arquivos baixados com sucesso.")
            zip_file(download, NOME_ARQUIVO_ZIP)
            logging.info(f"Arquivos zipados em {NOME_ARQUIVO_ZIP}.")
    else:
        logging.warning("Nenhum link encontrado.")

if __name__ == "__main__":
    main()