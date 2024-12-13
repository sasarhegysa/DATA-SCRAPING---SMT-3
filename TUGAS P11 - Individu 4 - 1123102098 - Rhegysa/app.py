
from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/kompas-pertanian")
def KompasPertanian():
    htmlDoc = requests.get("https://www.kompas.com/tag/pertanian")
    soup = BeautifulSoup(htmlDoc.text, "html.parser")
    popularArea = soup.find(attrs={'class':'latest ga--latest mt2 clearfix -newlayout'})

    images = popularArea.find_all('div', class_='article__list clearfix')
    return render_template("popular.html", gambar = images)

if __name__=="__main__":
    app.run(debug=True)