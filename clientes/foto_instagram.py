import requests
from bs4 import BeautifulSoup
import os

def obter_url_foto_perfil(usuario_instagram):
    url = f"https://www.instagram.com/{usuario_instagram}/"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        profile_picture_url = soup.find('meta', {'property': 'og:image'})['content']
        return profile_picture_url
    else:
        print('Erro ao acessar o perfil do Instagram')
        return None

def baixar_foto_perfil(url, usuario_instagram):
    response = requests.get(url)
    if response.status_code == 200:
        # Certifique-se de que a pasta "imagens" exista
        if not os.path.exists('imagens'):
            os.makedirs('imagens')

        file_path = os.path.join('imagens', f'{usuario_instagram}.jpg')
        with open(file_path, 'wb') as file:
            file.write(response.content)
        return file_path
    else:
        print('Erro ao baixar a foto de perfil')
        return None

# Exemplo de utilização

