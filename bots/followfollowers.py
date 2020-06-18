# Este bot obtiene la lista de seguidores cada minuto
# para seguir a cada usuario que aún no está siguiendo
import tweepy
import logging
# se importa el metodo del archivo config
from config import crearAPI
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def seguirSeguidores(api):

    logger.info("Recuperando seguidores...")

    # Se obtienen y recorren los seguiidores de la lista de seguidores
    for seguidor in tweepy.Cursor(api.followers).items():
        # Si no se está siguiendo a un seguidor
        if not seguidor.following:
            hora = time.strftime("%H:%M:%S")
            logger.info(f"Siguiendo a {seguidor.name} a las {hora}")
            # Se sigue al seguidor
            seguidor.follow()


def main():
    # Se obtiene el objeto api creado en config
    api = crearAPI()

    # Se repite infinitamente
    while True:
        seguirSeguidores(api)
        logger.info("Esperando para volver a verificar...")
        # Se llama una vez por minuto
        # ya que hay un limite de peticiones
        time.sleep(60)


# Se ejecuta el main
if __name__ == "__main__":
    main()
