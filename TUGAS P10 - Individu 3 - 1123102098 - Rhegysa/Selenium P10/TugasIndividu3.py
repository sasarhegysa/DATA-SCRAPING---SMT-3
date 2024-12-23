from selenium import webdriver
from bs4 import BeautifulSoup

URL = 'https://www.bukalapak.com/products?'
params = {
    'from' : 'omnisearch',
    'search[keywords]' : 'banyuwangi'
};

headers = {'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36'}
driver = webdriver.Chrome()
fullURL = f"{URL}&from={params['from']}&search[keywords]={params['search[keywords]']}"
driver.get(fullURL);
html = driver.page_source

soup = BeautifulSoup(html, 'html.parser')
data = soup.find_all('div', {'class': 'bl-product-card-new__description'})

for i in range(len(data)):
    nama_produk = data[i].find('p', {'class': 'bl-text bl-text--body-14 bl-text--secondary bl-text--ellipsis__2'})
    harga = data[i].find('p', {'class': 'bl-text bl-text--semi-bold bl-text--ellipsis__1 bl-product-card-new__price'})
    penjual = data[i].find('p', {'class': 'bl-text bl-text--caption-12 bl-text--secondary bl-text--ellipsis__1 bl-product-card-new__store-name'})
    if nama_produk and harga and penjual:
        print("Nama Produk:", nama_produk.text.strip())
        print("Harga:", harga.text.strip())
        print("Penjual:", penjual.text.strip())
        
print(data)
driver.quit()

