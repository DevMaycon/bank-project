from services.auth_logic import require_auth
from handlers import message_handler
from database import connection

def register_user(username, password, email):
    """Cria um usuário."""    
    pass

@require_auth
def add_user_transaction(user_id, amount, description):
    """Cria uma transação."""
    pass

@require_auth
def add_user_balance(user_id, amount, description):
    """Adiciona saldo a uma carteira."""
    pass

@require_auth
def get_user_balance(user_id):
    """Consulta o saldo da carteira do usuário."""
    with connection.database.cursor() as query:
        user_id = int(user_id[0])
        query.execute(
            "SELECT * FROM balances WHERE user_id = %s",
            (user_id,)
        )
        balance = query.fetchall()
    return balance

@require_auth
def get_user_transactions(user_id):
    """Lista transações do usuário."""
    with connection.database.cursor() as query:
        user_id = int(user_id[0])
        query.execute(
            "SELECT * FROM transactions WHERE user_origin_id = %s OR user_destination_id = %s",
            (user_id, user_id)
        )
        transactions = query.fetchall()
    return transactions
