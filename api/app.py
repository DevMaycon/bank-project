#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS
import routes


def main() -> None:
    """Executa a api."""
    
    # Start flask app
    flask_app = Flask(__name__)
    
    # Configura as rotas
    routes.configure_routes(flask_app)
    
    # Configuração do Cors
    CORS(app=flask_app, origins=["https://devmaycon.github.io"])
    
    # Por fim, deploy da aplicação
    flask_app.run(host='localhost', port=5500)


if __name__ == '__main__':
    main()
