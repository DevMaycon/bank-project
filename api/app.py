from flask import Flask
from flask_cors import CORS
from routes import routes
from dotenv import load_dotenv
from os import environ

config = load_dotenv('./configs/.env')

API_HOST, API_PORT = environ.get("api-host"), environ.get('api-port')
API_ORIGIN=environ.get('api-origin', '')

def main() -> None:
    """Executa a api."""
    
    # Start flask app
    flask_app = Flask(__name__)
    
    # Configura as rotas
    routes.configure_routes(flask_app)
    
    # Configuração do Cors
    CORS(app=flask_app, origins=[API_ORIGIN])
    
    # Por fim, deploy da aplicação
    flask_app.run(host=str(API_HOST), port=int(API_PORT))


if __name__ == '__main__':
    main()
