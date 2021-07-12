from logging import log
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
emojisFelizes = ["😊", "😁", "😄", "🥳", "😍", "🥰", "😻", "😆", "😋", "🤑"]
emojisTristes = ["😭", "😢", "😞", "🙁", "🥺", "😿", "💩", "😾", "😡", "😰"]

# acessar o json com a cotacao do dolar e salvar o valor da cotacao com o momento da atualizacao
cotDolar = Cotacao("https://economia.awesomeapi.com.br/last/USD-TRY")
dolar = cotDolar.retornarValorDolar()
dataCotacao = cotDolar.retornarData()

# verificar se o dolar subiu e guardar novo valor
arquivo = open("ImagensCriadas/info.txt", "r")
dolarAntes = float(arquivo.readline())
dolarMudou = False
dolarAumentou = False
if (round(dolar, 2) != round(dolarAntes, 2)):
    dolarMudou = True
    if (dolar > dolarAntes):
        dolarAumentou = True
    elif (dolar < dolarAntes):
        dolarAumentou = False
else:
    dolarMudou = False
arquivo = open("ImagensCriadas/info.txt", "w")
arquivo.write(str(dolar))

# criar/sobrescrever a imagem MeioDolar.jpg
img = Imagem()
img.CriarImagemAlterada(dolar)

# se o dolar tiver mudado, acessar a api do twitter, preparar a legenda e publicar a imagem
if (dolarMudou):
    bot = Bot(consumer_key, consumer_secret, access_token, access_token_secret)
    api = bot.authenticate()
    if (dolarAumentou):
        legenda = "Dolar yükseldi " + random.choice(emojisTristes) + "\n\nDolar değeri: " + "{:.2f}".format(round(dolar, 2)) + "₺" + "\nGüncellendi: " + dataCotacao
    else:
        legenda = "Dolar düştü " + random.choice(emojisFelizes) + "\n\nDolar değeri: " + "{:.2f}".format(round(dolar, 2)) + "₺" + "\nGüncellendi: " + dataCotacao
    bot.publicar(api, "ImagensCriadas/MeioDolar.jpg", legenda)
    print("Postou!")
else:
    print("Dolar değişmedi!")
