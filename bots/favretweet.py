import tweepy
import logging
from config import crearAPI
import json

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

# Clase que hereda de StreamListener
# StreamListener es un oyente de flujo que imprime el texto de estado

class FavRetweetListener(tweepy.StreamListener):

    def __init__(self, api):
        self.api = api
        # api.me() devuelve la informacion del usuario autenticado (yo)
        self.me = api.me()

    # Recibe un tweet y lo marca como me gusta y retweet
    def on_status(self, tweet):

        logger.info(
            f"Procesando tweet con id {tweet.id} de {tweet.user.screen_name}")

        # Si el tweet es una respuesta a otro tweet o si yo soy el autor del tweet (user.id)
        if tweet.in_reply_to_status_id is not None or tweet.user.id == self.me.id:
            return

        # si el tweet no se le ha dado me gusta
        if not tweet.favorited:

            try:

                logger.info("Dando me gusta al tweet...")
                tweet.favorite()

            except Exception as e:
                logger.error("Error en el me gusta.", exc_info=True)

        # Si el tweet no ha sido retweteado
        if not tweet.retweeted:
            try:

                logger.info("Retweeteando...")
                tweet.retweet()

            except Exception as e:
                logger.error("Error en el retweet.", exc_info=True)

    # Si ocurre algun error
    def on_error(self, status):
        logger.error(status)


# Recibe las palabras claves para filtrar tweets

def main(palabrasClaves):
    # Se crea el objeto API y un objeto de tipo FavRetweetListener
    api = crearAPI()
    tweetsListener = FavRetweetListener(api)

    # Se crea un objeto de transmision de tipo Stream de la API de transmision de Twitter
    # tweepy.Stream establece una sesion de transmision
    # y enruta los mensajes (tweets) a la instancia de StreamListener
    stream = tweepy.Stream(auth=api.auth, listener=tweetsListener)

    logger.info("Escuchando tweets...")

    # Se usa filter para transmitir todos los tweets que contengan dichas palabras
    stream.filter(track=palabrasClaves)


if __name__ == "__main__":
    main(["getClima"])
