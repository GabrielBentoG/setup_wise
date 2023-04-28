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

    user_home = os.path.expanduser('~')
    setup_wise_path = os.path.join(user_home, 'Desktop', 'setup_wise')
    filepath = os.path.join(setup_wise_path, 'download.exe')
    process = subprocess.Popen(filepath)
    process.communicate()
