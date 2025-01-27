from flask import jsonify

ERROR_MESSAGES = {
    'not_found': 'Recurso não encontrado',
    'unauthorized': 'Você não tem permissão para acessar este recurso',
    'validation_error': 'Os dados fornecidos são inválidos',
}


def success_message(message, data=None):
    response = {
        'status': 'success',
        'message': message,
        'data': data
    }
    return jsonify(response), 200


def error_message(error_type, custom_message=None, error_code=400):
    message = ERROR_MESSAGES.get(error_type, 'Erro desconhecido')
    if custom_message:
        message = custom_message
    
    response = {
        'status': 'error',
        'message': message
    }
    return jsonify(response), error_code