import requests
import MainFungsi
import os
from bs4 import BeautifulSoup

url = 'https://www.liputan6.com/pemilu'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
datax = soup.find_all('img')

images = []

for img in datax:
    img_url = img.get('src')
    if img_url is not None and img_url.endswith(('.jpg', '.png', '.gif', '.webp', '.jpeg')):
        images.append(img_url)

print(images)

direktori = "Pertemuan 9/Hasil Gambar"
MainFungsi.CreateDirectory(direktori)

for gmb in images:
    response = requests.get(gmb)
    fileName = os.path.basename(gmb)
    MainFungsi.WriteToFile2(direktori, fileName, response)
    print(response)
    print(fileName)