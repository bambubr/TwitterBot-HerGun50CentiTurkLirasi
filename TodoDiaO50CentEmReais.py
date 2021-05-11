from Imagem import Imagem
from Twitter import Bot
from CotacaoDolar import Cotacao
from os import environ
import random

# chaves de acesso da API / usuário do bot
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

# emojis felizes/tristes
emojisFelizes = [":)"]
emojisTristes = [":("]

# acessar o json com a cotação do dólar e salvar o valor da cotação + momento da atualização
cotDolar = Cotacao("https://economia.awesomeapi.com.br/last/USD-BRL")
dolar = cotDolar.retornarValorDolar()
dataCotacao = cotDolar.retornarData()

# verificar se o dolar subiu e guardar novo valor
arquivo = open("ImagensCriadas/info.txt", "r")
dolarAntes = float(arquivo.readline())
dolarMudou = False
dolarAumentou = False
if (round(dolar, 2) != round(dolarAntes, 2)):
    dolarMudou = True
else:
    dolarMudou = False
    if (dolar > dolarAntes):
        dolarAumentou = True
    elif (dolar < dolarAntes):
        dolarAumentou = False
arquivo = open("ImagensCriadas/info.txt", "w")
arquivo.write(str(dolar) + "\n" + dataCotacao)

# criar/sobrescrever a imagem MeioDolar.jpg
img = Imagem()
img.CriarImagemAlterada(dolar)

# se o dolar tiver mudado, acessar a api do twitter, preparar a legenda e publicar a imagem
if (dolarMudou):
    bot = Bot(consumer_key, consumer_secret, access_token, access_token_secret)
    api = bot.authenticate()
    if (dolarAumentou):
        legenda = "O dólar subiu " + random.choice(emojisTristes) + "\n\nValor do dólar: R$ " + "{:.2f}".format(round(dolar, 2)) + "\nAtualizado: " + dataCotacao
    else:
        legenda = "O dólar caiu " + random.choice(emojisFelizes) + "\n\nValor do dólar: R$ " + "{:.2f}".format(round(dolar, 2)) + "\nAtualizado: " + dataCotacao
    bot.publicar(api, "ImagensCriadas/MeioDolar.jpg", legenda)