import tweepy
# Logging se utiliza para informar errores y mensajes que nos ayudan en caso de un problema
import logging
# os interactua con el sistema operativo, en este caso las variables de entorno
import os

# Archivo de configuracion
# Autenticarse en la API de Twitter
# Crear y devolver el objeto api de tipo API

# Al leer las credenciales de las variables de entorno se evita
# codificarlas/mostrarlas en el codigo fuente, lo que lo hace más seguro

logger = logging.getLogger()

# Se leen las credenciales de autenticacion de las variables de entorno
# y crea el objeto API Tweepy

def crearAPI():

    consumerKey = os.getenv('CONSUMER_KEY')
    consumerSecret = os.getenv('CONSUMER_SECRET')
    accessToken = os.getenv('ACCESS_TOKEN')
    accessTokenSecret = os.getenv('ACCESS_TOKEN_SECRET')

    aut=tweepy.OAuthHandler(consumerKey, consumerSecret)
    aut.set_access_token(accessToken, accessTokenSecret)

# Se crea el objeto api de tipo API
# Tweepy espera e imprime un mensaje cuando se excede el límite de velocidad
    api=tweepy.API(aut, wait_on_rate_limit = True,
                     wait_on_rate_limit_notify = True)

# Se verifica si las credenciales son válidas
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error al verificar las credenciales.", exc_info = True)
        raise e

    logger.info("API creada correctamente.")

    return api
