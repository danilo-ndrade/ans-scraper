import os
import zipfile
import logging

def zip_file(pasta_arquivos, nome_arquivo_zip):
    try:
        with zipfile.ZipFile(nome_arquivo_zip, "w") as arquivo_zip:
            for nome_arquivo in os.listdir(pasta_arquivos):
                caminho_arquivo = os.path.join(pasta_arquivos, nome_arquivo)
                if os.path.isfile(caminho_arquivo):
                    arquivo_zip.write(caminho_arquivo, nome_arquivo)
        logging.info(f"Arquivos compactados em: {nome_arquivo_zip}")
        return True
    except Exception as e:
        logging.error(f"Erro ao compactar arquivos: {e}")
        return False