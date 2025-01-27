from flask import Blueprint, jsonify
from utils import messages

# Blueprints das rotas
auth_blueprint = Blueprint('auth', __name__)
user_blueprint = Blueprint('user', __name__)

# Função que configura todas as rotas
def configure_routes(app):
    app.register_blueprint(auth_blueprint, url_prefix='/auth')
    app.register_blueprint(user_blueprint, url_prefix='/account')


# Autenticação
@auth_blueprint.route('/login', methods=["POST"])
def auth():
    pass

# Rotas do usuario
@user_blueprint.route('/register', methods=["POST"])
def register():
    """Cria um usuário."""
    pass

@user_blueprint.route('/addtransaction', methods=["POST"])
def add_transaction():
    """Cria uma transação."""
    pass

@user_blueprint.route('/addbalance', methods=["POST"])
def add_balance():
    """Adiciona saldo a uma carteira."""
    pass

@user_blueprint.route('/balance', methods=["GET"])
def balance():
    """Consulta o saldo da carteira do usuário."""
    pass

@user_blueprint.route('/transactions', methods=["GET"])
def get_transactions():
    """Lista transações do usuário."""
    pass
