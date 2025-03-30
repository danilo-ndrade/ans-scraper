import requests
import os
import logging

def baixar_anexos_ans(links_pdf, pasta_download):
    if not os.path.exists(pasta_download):
        os.makedirs(pasta_download)
        logging.info(f"Pasta para armazenamento criada: {pasta_download}")

    for link_pdf in links_pdf:
        nome_arquivo = link_pdf.split("/")[-1]
        caminho_arquivo = os.path.join(pasta_download, nome_arquivo)
        try:
            logging.info(f"Fazendo download do arquivo: {nome_arquivo}")
            response_pdf = requests.get(link_pdf)
            response_pdf.raise_for_status()
            with open(caminho_arquivo, "wb") as f:
                f.write(response_pdf.content)
            logging.info(f"Download do arquivo: {nome_arquivo} concluído.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao baixar o arquivo {nome_arquivo}: {e}")

    return pasta_download