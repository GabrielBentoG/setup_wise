import os
import pathlib
import subprocess

def install():
    desktop_path = pathlib.Path.home() / "Desktop"
    setup_wise_path = desktop_path / "setup_wise"
    if os.path.exists(str(setup_wise_path)):
        print(f"A pasta 'setup_wise' existe em {setup_wise_path}!")
    else:
        print("Não foi possível encontrar a pasta 'setup_wise'.")
        return

    user_home = os.path.expanduser('~')
    setup_wise_path = os.path.join(user_home, 'Desktop', 'setup_wise')

    exe_files = [f for f in os.listdir(setup_wise_path) if f.endswith('.exe')]
    if not exe_files:
        print("Não foram encontrados arquivos executáveis na pasta 'setup_wise'.")
        return

    for filename in exe_files:
        print(f"Instalando {filename}")
        try:
            filepath = os.path.join(setup_wise_path, filename)
            process = subprocess.Popen(filepath)
            return_code = process.wait()
            if return_code == 0:
                print(f"A instalação de {filename} foi concluída com sucesso.")
            else:
                print(f"Ocorreu um erro durante a instalação de {filename}.")
        except Exception as e:
            print(f"Ocorreu um erro durante a instalação de {filename}: {str(e)}")
