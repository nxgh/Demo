from functools import wraps

from flask import request, g, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired

from app.model.user import user

def generate_token(user_id: str, ) -> str:
    data = {
        'user_id': user_id,
    }
    s = Serializer('SECRET_KEY', expires_in = 3600)

    token = s.dumps(data).decode("ascii")
    return token

def validate_token(token: str):
    
    s: Serializer = Serializer('SECRET_KEY')
    try:
        data = s.loads(token)
        # {'user_id': 'xxx'}
    except SignatureExpired:
        return {
            'status': False,
            'msg': 'SignatureExpired'
        }
    except BadSignature:
        return {
            'status': False,
            'msg': 'BadSignature'
        }
    return {
        'status': True,
        'msg':  data.get('user_id', '')
    }


def get_token():
    """获取 token 令牌
    Return：
        token_type: 令牌类型，需要为 Bearer
        token: 令牌内容
    """

    if "Authorization" in request.headers:
        try:
            token_type, token = request.headers["Authorization"].split(None, 1)
        except ValueError:
            token_type = token = None
    else:
        token_type = token = None

    return token_type, token

def api_abort(code, message=None, **kwargs):
    if message is None:
        message = HTTP_STATUS_CODES.get(code, '')

    response = jsonify(code=code, message=message, **kwargs)
    response.status_code = code
    return response  # You can also just return (response, code) tuple


def permission_required(perm):
    def decorated(f):
        """ 管理员验证装饰器"""
        @wraps(f)
        def wrapper(*args, **kwargs):

            token_type, token = get_token()

            if request.method != "OPTIONS":
                if token_type is None or token_type.lower() != "bearer":
                    return api_abort(400, "The token type must be bearer.")
                if token is None:
                    return api_abort(400, 'token missing')
                
                result = validate_token(token)

                if not result["status"]:
                    return api_abort(401, "admin 错误")
                g.uid = result.get('msg') 
                if not user.has_permission(perm):
                    return api_abort(401, '莫得权限')

            return f(*args, **kwargs)
        return wrapper
    return decorated