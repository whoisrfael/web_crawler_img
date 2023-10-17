import os
import requests
from bs4 import BeautifulSoup

# Solicita a URL ao usuário
URL = input("Por favor, insira a URL da página: ")
DIR_NAME = 'remax_images'

if not os.path.exists(DIR_NAME):
    os.makedirs(DIR_NAME)

response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

# Seletor ajustado para buscar imagens dentro do elemento com id "gallery-map-images"
img_tags = soup.select('#gallery-map-images img')

for img_tag in img_tags:
    img_url = img_tag['src']

    if not img_url.startswith('http'):
        img_url = 'https://www.remax.com.br' + img_url

    img_name = os.path.basename(img_url)
    img_path = os.path.join(DIR_NAME, img_name)

    img_data = requests.get(img_url).content
    with open(img_path, 'wb') as img_file:
        img_file.write(img_data)

print("Imagens baixadas com sucesso.")
