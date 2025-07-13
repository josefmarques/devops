import os
import shutil # Importa o módulo shutil para mover arquivos

# Define o diretório de destino principal
destination_folder = "downloads"

# Define os tipos de arquivo e seus respectivos diretórios
file_types = {
    "images": [".jpeg", ".png", ".gif"],
    "docs": [".txt", ".csv", ".doc", ".pdf", ".yaml", ".yml", ".xls"],
    "videos": [".mp4", ".mov"], 
    "software": [".zip", ".exe", ".dmg", ".pkg", ".msi", ".war"],
    "others": [] # 'others' continua sendo o fallback
}

def get_destination_folder(file_name):
    """
    Determina o nome do subdiretório de destino com base na extensão do arquivo.
    """
    # Obtém a extensão do arquivo em letras minúsculas para comparação consistente
    ext = os.path.splitext(file_name)[1].lower()
    
    for folder_name, extensions in file_types.items():
        if ext in extensions:
            return folder_name
    return "others" # Se a extensão não for encontrada em nenhuma categoria, vai para 'others'

# --- Criação dos subdiretórios ---
# Garante que o diretório principal 'downloads' exista
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Cria todos os subdiretórios dentro de 'downloads' se eles ainda não existirem
for folder_name in file_types:
    subfolder_path = os.path.join(destination_folder, folder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

# --- Movimentação dos arquivos ---
# Lista os arquivos no diretório atual (onde o script está sendo executado)
# e que não são o diretório 'downloads' em si.
current_directory_files = [arquivo for arquivo in os.listdir('.') if os.path.isfile(arquivo) and arquivo != os.path.basename(__file__)] # Ignora o próprio script
current_directory_files = [arquivo for arquivo in current_directory_files if arquivo != destination_folder] # Ignora a pasta downloads

for file_name in current_directory_files:
    origin_path = file_name # O arquivo já está na raiz do diretório atual
    
    # Obtém o nome da pasta de destino para o arquivo
    destiny_subfolder = get_destination_folder(file_name)
    
    # Constrói o caminho completo para o destino
    destiny_path = os.path.join(destination_folder, destiny_subfolder, file_name)
    
    try:
        # Move o arquivo
        shutil.move(origin_path, destiny_path)
        print(f"Arquivo '{file_name}' movido para '{os.path.join(destination_folder, destiny_subfolder)}'")
    except FileNotFoundError:
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
    except Exception as e:
        print(f"Erro ao mover o arquivo '{file_name}': {e}")