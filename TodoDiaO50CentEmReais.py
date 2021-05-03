from Imagem import Imagem
from Twitter import Bot
from CotacaoDolar import Cotacao
from os import environ

# chaves de acesso da API / usuário do bot
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

# acessar o json com a cotação do dólar e salvar o valor da cotação + momento da atualização
cotDolar = Cotacao("https://economia.awesomeapi.com.br/last/USD-BRL")
dolar = cotDolar.retornarValorDolar()
dataCotacao = cotDolar.retornarData()

# criar/sobrescrever a imagem MeioDolar.jpg
img = Imagem()
img.CriarImagemAlterada(dolar)

# acessar a api do twitter e publicar a imagem
bot = Bot(consumer_key, consumer_secret, access_token, access_token_secret)
api = bot.authenticate()
bot.publicar(api, dolar, dataCotacao)