import tweepy
import time
import logging
from config import crearAPI
import API.weatherAPI as weatherAPI

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()


def publicarTweet(api, clima):

    try:
        logger.info("Creando tweet...")
        api.update_status(clima)

    except Exception as e:
        logger.error("Error al crear el tweet.", exc_info=True)


def main():

    api = crearAPI()

    while True:

        ciudad = 'Mendoza, AR'
        clima = weatherAPI.getClima(ciudad)
        hora = time.strftime("%H:%M:%S")

        clima += f"\nHora: {hora}"

        publicarTweet(api, clima)

        logger.info("Esperando para volver a publicar...")
        time.sleep(60)


if __name__ == "__main__":
    main()
