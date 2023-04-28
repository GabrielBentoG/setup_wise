from download import download
from install import install

# Lista das URLs dos aplicativos para download
app_urls = [ 'https://download.scdn.co/SpotifySetup.exe',
            'https://www.ccleaner.com/pt-br/ccleaner/download/standard']
            

# Faz o download de cada aplicativo e salva dentro da pasta "setup_wise"
download(app_urls)

install()



