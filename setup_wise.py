from download import download
from install import install

# Lista das URLs dos aplicativos para download
app_urls = ['https://discordapp.com/api/download?platform=win', 
            'https://download.scdn.co/SpotifySetup.exe']
            

# Faz o download de cada aplicativo e salva dentro da pasta "setup_wise"
download(app_urls)

install()



