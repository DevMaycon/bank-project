from services.auth_logic import require_auth
from handlers import message_handler
from database import connection


@require_auth
def add_user_transaction(user_id, destination_user_id, amount):
    """Cria uma transação."""
    with connection.database.cursor() as query:
        query.execute(
            "INSERT INTO transactions (user_origin_id, user_destination_id, value) VALUES (%s, %s, %s)",
            (user_id, destination_user_id, amount)
        )
        query.execute(
            "UPDATE balances SET value = value - %s WHERE user_id = %s",
            (amount, user_id)
        )
        query.execute(
            "UPDATE balances SET value = value + %s WHERE user_id = %s",
            (amount, destination_user_id)
        )
    connection.database.commit()
    return message_handler.success_message("transaction_created")

@require_auth
def add_user_balance(user_id, amount):
    """Adiciona saldo a uma carteira."""
    with connection.database.cursor() as query:
        user_id = int(user_id)
        amount = float(amount)
        query.execute(
            "UPDATE balances SET value = value + %s WHERE user_id = %s",
            (amount, user_id)
        )
    connection.database.commit()
    return message_handler.success_message("balance_added")

@require_auth
def get_user_balance(user_id):
    """Consulta o saldo da carteira do usuário."""
    with connection.database.cursor() as query:
        user_id = int(user_id)
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
        user_id = int(user_id)
        query.execute(
            "SELECT * FROM transactions WHERE user_origin_id = %s OR user_destination_id = %s",
            (user_id, user_id)
        )
        transactions = query.fetchall()
    return transactions
