from handlers import message_handler
from database import connection
import datetime
import jwt

logged_users: dict[str, str] = {}


def require_auth(func):
    """Decorator for routes what is required login."""
    from flask import request
    def wrapper(*args):
        try:
            # Verifica se o jwt é valido.
            auth_token = decode_token(request.headers["X-Auth-Key"])
            if isinstance(auth_token, dict):
                # Executa a função caso seja valido.
                response = func(args)
            else:
                # Senão retorna status não autorizado para a requisição.
                response = message_handler.error_message(
                    error_type="unauthorized",
                    error_code=401
                )
            return response
        except KeyError as key:
            response = message_handler.error_message(
                error_type="unauthorized",
                error_code=401,
                custom_message=f"{str(key).replace('HTTP_', '')} Header Not Found."
            )
            return response
    return wrapper

def execute_login(username):
    with connection.database.cursor() as cursor:
        cursor.execute(
            "SELECT id, password FROM users where (username = %s or email = %s)",
            (username,username)
        )
        response = cursor.fetchone()
    if response:
        return True, response
    else:
        return False, "Error"

def auth(form_data: dict):
    # Logica de login.
    username, password = form_data.get("username", None), form_data.get('password', None)
    sql_response = execute_login(username)
    sql_response = {
        "STATUS": sql_response[0],
        "ID": sql_response[1][0],
        "PASSWORD": sql_response[1][1]
    }
    
    if sql_response["STATUS"] and (password == sql_response['PASSWORD']):
        token_payload = { "user_id": sql_response["ID"] }
        
        if logged_users.get(username):
            jwt_token = logged_users[username]

        elif logged_users.get(username) and not isinstance(decode_token(jwt_token), str):
            jwt_token = encode_token(payload=token_payload)
            logged_users[username] = jwt_token
            
        else:
            jwt_token = encode_token(payload=token_payload)
            logged_users[username] = jwt_token
            
        response = message_handler.success_message(
            success_type="login_success",
            data=jwt_token,
        )
    else:
        response = message_handler.error_message(
            error_type="validation_error",
            error_code=200
        )
        
    return response


def encode_token(payload: dict):
    payload['exp'] = datetime.datetime.now() + datetime.timedelta(minutes=15)
    jwt_token = jwt.encode(payload, "secret-key", algorithm="HS256")
    
    return jwt_token


def decode_token(token_jwt: str):
    # Decodifica um token jwt-token e verifica sua assinatura.
    # Se for valido retorna o token, caso contrario retorna um erro.
    try:
        jwt_token = jwt.decode(token_jwt, "secret-key", algorithms="HS256")
        response = jwt_token
    except jwt.InvalidSignatureError:
        response = message_handler.error_message(
            error_type="token_invalid",
            error_code=401
        )
    except jwt.exceptions.DecodeError:
        response = message_handler.error_message(
            error_type="token_invalid",
            error_code=401
        )
    except jwt.ExpiredSignatureError:
        response = message_handler.error_message(
            error_type="token_expired",
            error_code=401
        )
    
    return response
