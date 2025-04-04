import PyPDF2
import csv
import os
import zipfile

# Caminho para o PDF do Anexo I
pdf_path = "anexos/Anexo_I.pdf"
if not os.path.exists(pdf_path):
    print("Arquivo não encontrado:", pdf_path)
    exit()

# Abre o PDF e extrai o texto de todas as páginas
with open(pdf_path, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    full_text = ""
    for page in pdf_reader.pages:
        full_text += page.extract_text() + "\n"

# Divide o texto em linhas
lines = full_text.splitlines()

# Cria um mapeamento de todas as abreviações para seus nomes completos (exemplo genérico):
coluna_legenda = {
    "OD": "Procedimento Odontológico",
    "AMB": "Procedimento Ambulatorial",
    # Adicione outras colunas e legendas aqui conforme o rodapé do PDF
}

# Identifica as linhas que pertencem à tabela (pressupondo que ela contenha as abreviações)
table_lines = []
for line in lines:
    if any(abreviacao in line for abreviacao in coluna_legenda.keys()):
        table_lines.append(line)

if not table_lines:
    print("Tabela não foi encontrada no PDF.")
    exit()

# Processa a primeira linha como cabeçalho e substitui todas as abreviações pela legenda completa
header = table_lines[0].split()
header = [coluna_legenda.get(col, col) for col in header]  # Substitui pelo nome completo ou mantém o original

# Processa as demais linhas (assumindo que as colunas estejam separadas por espaço)
data = [header]
for line in table_lines[1:]:
    row = line.split()
    data.append(row)

# Salva os dados em um CSV
csv_filename = "rol_de_procedimentos.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)

print("Dados salvos em", csv_filename)

# Compacta o CSV em um arquivo ZIP nomeado "Teste_Erick.zip"
zip_filename = "Teste_Erick.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    zipf.write(csv_filename)
print("CSV compactado em", zip_filename)