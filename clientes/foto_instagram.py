import requests
from bs4 import BeautifulSoup
import os
from PIL import Image
import io

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
        # Carrega a imagem usando Pillow (PIL)
        img = Image.open(io.BytesIO(response.content))

        # Ajusta a qualidade da imagem (0 a 100, sendo 100 a melhor qualidade)
        img.save('temp.jpg', format='JPEG', quality=100)
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



