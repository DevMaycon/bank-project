from handlers import message_handler
from database import connection
import datetime
import jwt

logged_users: dict[str, str] = {}


def auth(form_data: dict):
    # Logica de login.
    username, password = form_data.get("username", None), form_data.get('password', None)
    sql_response = connection.execute_login(username)
    sql_response = {
        "STATUS": sql_response[0],
        "ID": sql_response[1][0],
        "PASSWORD": sql_response[1][1]
    }
    
    if sql_response["STATUS"] and (password == sql_response['PASSWORD']):
        if (username in logged_users and isinstance(decode_token(logged_users[username]), str)):
            jwt_token = logged_users[username]
        else:
            token_payload = { "user_id": sql_response["ID"] }
            
            jwt_token = encode_token(payload=token_payload)
            logged_users[username] = jwt_token  
            
            del token_payload
            
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
    # Cria um jwt-token com 15 minutos de vida.
    payload['exp'] = datetime.datetime.now() + datetime.timedelta(minutes=15)
    
    jwt_token = jwt.encode(payload, "secret-key", algorithm="HS256")
    
    return jwt_token


def decode_token(token_jwt: str):
    # Decodifica um token jwt-token e verifica sua assinatura.
    
    try:
        jwt_token = jwt.decode(token_jwt, "secret-key", algorithms="HS256")
        response = jwt_token
    except jwt.InvalidSignatureError:
        response = message_handler.error_message(
            error_type="token_invalid",
            error_code=401
        )
        return response
    except jwt.ExpiredSignatureError:
        response = message_handler.error_message(
            error_type="token_expired",
            error_code=401
        )
        return response
    
    # Retorna Token Caso Nenhum Erro.
    return response