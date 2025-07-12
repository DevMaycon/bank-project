from os import environ
from time import sleep
import psycopg
import dotenv


dotenv.load_dotenv('../.env')

def connect():
    try:
        connection = psycopg.connect(
            f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
        )
        print("API Conectada com o banco de dados com sucesso.")
        return connection
    except:
        print("API Não conectada com o banco de dados.")
        sleep(2)
        return connect()


DATABASE_NAME=environ.get('DATABASE_NAME'.lower())
DATABASE_HOST=environ.get('DATABASE_HOST'.lower())
DATABASE_PORT=environ.get('DATABASE_PORT'.lower())
DATABASE_PASSWORD=environ.get('DATABASE_PASSWORD'.lower())
DATABASE_USERNAME=environ.get('DATABASE_USERNAME'.lower())

database = connect()
