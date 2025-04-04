import requests
from bs4 import BeautifulSoup
import os
import zipfile

# Define a URL alvo
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Acessa o site
response = requests.get(url)
if response.status_code != 200:
    print("Erro ao acessar o site:", response.status_code)
    exit()

html = response.text
soup = BeautifulSoup(html, 'html.parser')

# Procura por links que terminem com .pdf e que contenham “Anexo I” ou “Anexo II”
links_pdf = {}
for a in soup.find_all("a", href=True):
    text = a.get_text()
    href = a["href"]
    if href.lower().endswith(".pdf"):
        # Se for relativo, transforma em URL absoluta
        if not href.startswith("http"):
            href = requests.compat.urljoin(url, href)
        if ("Anexo_I" in text or "Anexo_I" in href) and "Anexo_I" not in links_pdf:
            links_pdf["Anexo_I"] = href
        elif ("Anexo_II" in text or "Anexo_II" in href) and "Anexo_II" not in links_pdf:
            links_pdf["Anexo_II"] = href

if not links_pdf:
    print("Nenhum link para os anexos foi encontrado.")
    exit()

# Cria uma pasta para salvar os PDFs
os.makedirs("anexos", exist_ok=True)

# Baixa e salva cada PDF
for key, pdf_url in links_pdf.items():
    print("Baixando", key, "de", pdf_url)
    pdf_resp = requests.get(pdf_url)
    if pdf_resp.status_code == 200:
        filename = f"anexos/{key.replace(' ', '_')}.pdf"
        with open(filename, "wb") as f:
            f.write(pdf_resp.content)
        print(f"{key} salvo em {filename}")
    else:
        print("Erro ao baixar", key)

# Compacta os arquivos PDF baixados em um único arquivo ZIP
zip_filename = "anexos.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in os.listdir("anexos"):
        zipf.write(os.path.join("anexos", file), file)
print("Arquivos compactados em", zip_filename)