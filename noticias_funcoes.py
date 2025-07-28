import requests
from bs4 import BeautifulSoup as bs


def ultimas_noticias():
    url="https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419"
    site=requests.get(url)
    noticias= bs(site.text, "html.parser")
    noticiastexto = []
    for item in noticias.findAll('item')[:4]:
        titulo=item.title.text
        noticiastexto.append(titulo)
        return " ".join(noticiastexto)






