# ANS Scraper
Script para fazer download e compactar os anexos AnexoI.pdf(A lista de consultas, exames e tratamentos de cobertura obrigatória) e AnexoII.pdf(Diretrizes de utilização) do O Rol de Procedimentos e Eventos em Saúde(https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos).

---

## Funcionalidades

- Acessa a página da ANS para buscar os links dos PDFs.
- Faz o download dos arquivos PDF encontrados.
- Compacta os arquivos baixados em um arquivo ZIP.
- Logs do processo utilizando o módulo logging

---

## Requisitos

- **Python 3.12 ou superior**
- Dependências listadas no arquivo `requirements.txt`.

---

## Execução do script

1. **Crie o ambiente virtual python**
  python3 -m venv venv
  source venv/bin/activate  # Linux/Mac
  # ou
  venv\Scripts\activate     # Windows

2. **Instale as dependências**
   pip install -r requirements.txt

3. **Execute o script**
   python src/main.py



