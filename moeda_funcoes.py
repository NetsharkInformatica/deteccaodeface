import requests


def cotacao_moeda(moeda):
    if moeda == "dolar":
        url = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL")
        cotacao= url.json()
        nome = cotacao["USDBRL"]["name"]
        data= cotacao["USDBRL"]["create_date"]
        valor= cotacao["USDBRL"]["bid"]
        mensagem= f"A cotação do {nome} é de R$ {valor} reais, atualizada em {data}."
        #return mensagem
    elif moeda == "euro":
        url = requests.get("http://economia.awesomeapi.com.br/json/last/EUR-BRL")
        cotacao= url.json()
        nome = cotacao["EURBRL"]["name"]
        data= cotacao["EURBRL"]["create_date"]
        valor= cotacao["EURBRL"]["bid"]
        mensagem= f"A cotação do {nome} é de R$ {valor} reais, atualizada em {data}."
        #return mensagem
    elif moeda == "libra":
        url = requests.get("http://economia.awesomeapi.com.br/json/last/GBP-BRL")
        cotacao= url.json()
        nome = cotacao["GBPBRL"]["name"]
        data= cotacao["GBPBRL"]["create_date"]
        valor= cotacao["GBPBRL"]["bid"]
        mensagem= f"A cotação do {nome} é de R$ {valor} reais, atualizada em {data}."
        #return mensagem
    elif moeda == "bitcoin":
        url = requests.get("http://economia.awesomeapi.com.br/json/last/BTC-BRL")
        cotacao= url.json()
        nome = cotacao["BTCBRL"]["name"]
        data= cotacao["BTCBRL"]["create_date"]
        valor= cotacao["BTCBRL"]["bid"]
        mensagem= f"A cotação do {nome} é de R$ {valor} reais, atualizada em {data}."
    return mensagem
