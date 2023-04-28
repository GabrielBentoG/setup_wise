import os
import pathlib
import requests
from urllib.parse import urlparse

def download(apps_urls):  
  desktop_path = pathlib.Path.home() / "Desktop"
  setup_wise_path = desktop_path / "setup_wise"
  setup_wise_path.mkdir(parents=True, exist_ok=True)

  if os.path.exists(str(setup_wise_path)):
      print(f"A pasta 'setup_wise' foi criada com sucesso em {setup_wise_path}!")
  else:
      print("Não foi possível criar a pasta 'setup_wise'.")

  for url in apps_urls:
    url_parts = urlparse(url)
    file_name = os.path.basename(url_parts.path)
    file_path = os.path.join(str(setup_wise_path), file_name)
    if any(file_name in f and f.endswith('.exe') for f in os.listdir(setup_wise_path)):
        print(f"{file_name} já existe com extensão .exe.")
        continue
    elif os.path.isfile(file_path + '.exe'):
        print(f"{file_name} já existe com extensão .exe.")
        continue
    elif os.path.exists(file_path):
        print(f"{file_name} já existe. Pulando download...")
        continue
    else: 
        print(f"Baixando {file_name}...")
        try:
            response = requests.get(url)
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"{file_name} baixado com sucesso.")
        except:
            print(f"O download do arquivo {file_name} falhou.")
            continue
    # Verifica se o arquivo não tem a extensão .exe e renomeia o arquivo com a extensão .exe
    if not file_name.endswith('.exe'):
        new_file_path = os.path.join(str(setup_wise_path), f"{file_name}.exe")
        os.rename(file_path, new_file_path)
        file_path = new_file_path
        #print(f"Arquivo renomeado para {new_file_path}.")
