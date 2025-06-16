from flask import jsonify

ERROR_MESSAGES = {
    'not_found': 'Recurso não encontrado',
    'unauthorized': 'Você não tem permissão para acessar este recurso',
    'validation_error': 'Os dados fornecidos são inválidos',
    'token_invalid': 'Token de autenticação inválido',
    'token_expired': 'Token de autenticação expirado',
    'insufficient_balance': 'Saldo insuficiente para realizar a transação',
    'transaction_failed': 'Falha ao processar a transação',
    'user_not_found': 'Usuário não encontrado',
}

SUCCESS_MESSAGES = {
    'login_success': 'Login realizado com sucesso',
    'token_valid': 'Token de autenticação válido',
    'logout_success': 'Logout realizado com sucesso',
    'access_granted': 'Acesso autorizado',
    'user_found': 'Usuário encontrado com sucesso',
    'user_created': 'Usuário criado com sucesso',
    'balance_added': 'Saldo adicionado com sucesso',
    'balance_updated': 'Saldo atualizado com sucesso',
    'transaction_success': 'Transação realizada com sucesso',
    'transaction_created': 'Transação criada com sucesso',
    'transaction_cancelled': 'Transação cancelada com sucesso',
    'transfer_completed': 'Transferência concluída com sucesso',
}


def success_message(success_type: str, data=None, success_code=200):
    message = SUCCESS_MESSAGES.get(success_type, success_type)
    response = {
        'status': 'success',
        'message': message,
        'data': data
    }
    
    if not data: del response['data']
    
    return jsonify(response), success_code


def error_message(error_type, custom_message=None, error_code=400):
    message = ERROR_MESSAGES.get(error_type, 'Erro desconhecido')
    if custom_message:
        message = custom_message
    
    response = {
        'status': 'error',
        'message': message
    }
    return jsonify(response), error_code