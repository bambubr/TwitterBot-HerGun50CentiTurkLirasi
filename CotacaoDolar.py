import os
import json
import requests
from datetime import datetime

class Cotacao:
    def __init__ (self, url):
        self.url = url

    def retornarData(self):
        requisicao = requests.get(self.url)
        cotacao = json.loads(requisicao.text)
        data = cotacao['USDTRY']['create_date']
        data = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
        data = data.strftime("%d/%m/%Y - %H:%M")
        return data

    def retornarValorDolar(self):
        requisicao = requests.get(self.url)
        cotacao = json.loads(requisicao.text)
        return float(cotacao['USDTRY']['ask'])
