import os
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class Imagem:
    def __init__ (self):
        pass

    def selecionarImagem(self):
        path = ("BancoDeImagens")
        imagens = os.listdir(path)
        imgEscolhida  = random.choice(imagens)
        return imgEscolhida

    def CriarImagemAlterada(self, cotacaoDolar):
        cotacaoDolar = "R$ " + "{:.2f}".format(round(cotacaoDolar/2, 2))
        img = Image.open("BancoDeImagens/" + self.selecionarImagem())
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("Fontes/arial.ttf", round(img.height/5))
        draw.text((round((img.width - font.getsize(cotacaoDolar)[0])/2), img.height-round(img.height/4)), cotacaoDolar, font=font, stroke_width=10, stroke_fill='black')
        img.save("ImagensCriadas/MeioDolar.jpg")