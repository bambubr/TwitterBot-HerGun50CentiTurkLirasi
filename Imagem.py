import os
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class Imagem:
    def __init__ (self, cotacaoDolar):
       self.cotacaoDolar = cotacaoDolar

    def selecionarImagem(self):
        path = ("BancoDeImagens")
        imagens = os.listdir(path)
        imgEscolhida  = random.choice(imagens)
        return imgEscolhida

    def CriarImagemAlterada(self):
        img = Image.open("BancoDeImagens/" + self.selecionarImagem())
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fontes/arial.ttf", round(img.height/5))
        draw.text((round((img.width - font.getsize(self.cotacaoDolar)[0])/2), img.height-round(img.height/4)), self.cotacaoDolar, font=font, stroke_width=10, stroke_fill='black')
        img.save("ImagensCriadas/MeioDolar.jpg")