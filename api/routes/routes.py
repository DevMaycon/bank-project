from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from json import loads

from services import auth_logic, user_logic

# Blueprints das rotas
auth_blueprint = Blueprint('auth', __name__)
user_blueprint = Blueprint('user', __name__)

# Função que configura todas as rotas
def configure_routes(app):
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(user_blueprint, url_prefix='/account')


# Autenticação
@auth_blueprint.route('/login', methods=["POST"])
@cross_origin(supports_credentials=True)
def auth():
    login_data = request.json
    response = auth_logic.auth(login_data)
    
    response_text = loads(response[0].response[0])
    
    if  response_text['status'] == "success":
        return response
    else:
        return response

# Rotas do usuario
@user_blueprint.route('/register', methods=["POST"])
def register_user():
    """Cria um usuário."""
    pass

@user_blueprint.route('/addtransaction', methods=["POST"])
def add_user_transaction():
    """Cria uma transação."""
    pass

@user_blueprint.route('/addbalance', methods=["POST"])
def add_user_balance():
    """Adiciona saldo a uma carteira."""
    pass

@user_blueprint.route('/balance', methods=["GET"])
def get_user_balance():
    """Consulta o saldo da carteira do usuário."""
    pass

@user_blueprint.route('/transactions/<int:user_id>', methods=["GET"])
def get_user_transactions(user_id):
    """Lista transações do usuário."""
    return user_logic.get_user_transactions(user_id)
