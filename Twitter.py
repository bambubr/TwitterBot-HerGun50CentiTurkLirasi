import tweepy

class Bot:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret

    def authenticate(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth)

    def publicar(self, api, dolar, dataHora):
        #media = api.media_upload(filename="ImagensCriadas/MeioDolar.jpg")
        api.update_with_media(filename="ImagensCriadas/MeioDolar.jpg", status="Valor do dólar: R$ " + dolar + "\nAtualizado: " + dataHora), 