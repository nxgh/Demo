from flask import request, g, jsonify

from app.model.user import user, Permission
from app.auth import generate_token, validate_token, permission_required

from . import hello_bp

@hello_bp.route('/hello')
def hello():
    return 'Hello Flask!'


@hello_bp.route('/register', methods=['POST'])
def register():
    """
    向注册邮箱发送一个 url/token 形式的链接
    此处仅发送token，需要自己手动拼接
    """
    user_info = request.get_json()
    if user_info.get('username', None):
        uid = user.insert(user_info)
        token = generate_token(str(uid))
        return jsonify({'token': token})



@hello_bp.route('/auth_email/<string:token>')
def auth_email(token):
    """
    访问 register 生成的 token
    """
    res = validate_token(token)
    if res['status']:
        uid = res['msg']
        g.uid = uid
        user.add_permission(Permission.PUBLISH)
        return '添加 PUBLISH 成功'

@hello_bp.route('/remove_permission/<string:token>')
def remove_permission(token):
    """
    访问 register 生成的 token
    """
    res = validate_token(token)
    if res['status']:
        uid = res['msg']
        g.uid = uid
        user.remove_permission(Permission.PUBLISH)
        return '删除 PUBLISH 成功'


@hello_bp.route('/login', methods=['POST'])
def login():
    user_info = request.get_json()
    print(user_info)
    if user_info.get('username', None):
        uid = user.find({'username': user_info['username']})['_id']
        print(uid)
        token = generate_token(str(uid))
        return jsonify({'token': token})

@hello_bp.route('/test_user')
@permission_required(Permission.PUBLISH)
def test_user():
    return jsonify({'msg': 'successs'})