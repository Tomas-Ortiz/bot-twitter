import tweepy
import logging
from config import crearAPI
import time
import API.weatherAPI as weatherAPI

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()

# since_id especifica resultados con una ID mayor que la id especificada (más reciente)

def verificarMenciones(api, palabrasClaves, idDesde):

    logger.info("Recuperando menciones...")

    idDesdeNuevo = idDesde

    # Cursor maneja la paginacion de resultados
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=idDesde).items():

        idDesdeNuevo = max(tweet.id, idDesdeNuevo)

        me = api.me()

        if any(palabraClave in tweet.text.lower() for palabraClave in palabrasClaves) and tweet.user.id != me.id:

            logger.info(f"Respondiendo al usuario {tweet.user.screen_name}")

            if not tweet.user.following:

                logger.info(f"Siguiendo al usuario {tweet.user.screen_name}")

                tweet.user.follow()

            if not tweet.favorited:

                logger.info("Dando me gusta al tweet...")

                tweet.favorite()

            usuario = tweet.user.screen_name

            ciudad = 'Mendoza, AR'

            clima = weatherAPI.getClima(ciudad)

            hora = time.strftime("%H:%M:%S")

            clima += f"\nHora: {hora}"

            # Se responde al tweet que nos mencionaron
            try:
                api.update_status(f"@{usuario} {clima}",
                                  in_reply_to_status_id=tweet.id)
            except Exception as e:
                logger.info(
                    "No se pudo responder, el tweet está duplicado.", exc_info=True)

    return idDesdeNuevo


def main():
    api = crearAPI()
    idDesde = 1

    while True:

        idDesde = verificarMenciones(
            api, ["getclima"], idDesde)

        logger.info("Esperando para volver a verificar en 1 minuto...")

        time.sleep(60)


if __name__ == "__main__":
    main()
