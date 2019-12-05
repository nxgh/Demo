from flask import g
from bson import ObjectId

from app.extension import mongo


class Permission:

    FOLLOW = 1
    COLLECT = 2
    COMMENT = 4
    PUBLISH = 8
    MODERATE = 16
    ADMIN = 32


roles = {
    'Visitor': [
        Permission.FOLLOW,
        Permission.COLLECT, 
        Permission.COMMENT, 
    ],
    'User': [
        Permission.FOLLOW,
        Permission.COLLECT, 
        Permission.COMMENT, 
        Permission.PUBLISH, 
    ],
    'Moderator': [
        Permission.FOLLOW,
        Permission.COLLECT, 
        Permission.COMMENT, 
        Permission.PUBLISH, 
        Permission.MODERATE
    ],
    'Administrator': [
        Permission.FOLLOW, 
        Permission.COLLECT, 
        Permission.COMMENT, 
        Permission.MODERATE, 
        Permission.PUBLISH, 
        Permission.ADMIN, 
    ]
}
class User():

    def insert(self, user_info):
        uid = mongo.db.user.insert_one({
            'username': user_info['username'],
            'password': user_info['password'],
            'email': user_info['email'],
            'role': sum(roles['Visitor']),
        }).inserted_id
        g.uid = uid
        return uid

    def find(self, query):
        if type(query) != str: 
            u =  mongo.db.user.find_one(query)
            # u['_id'] = str(u['_id'])
            return u
        else: 
            u = mongo.db.user.find_one({'_id': ObjectId(query)})
            # print(u)
            u['_id'] = str(u['_id'])
            return u


    def has_permission(self, perm: int) -> bool:
        print('has_permission g.uid',g.uid)
        role = int(self.find(g.uid)['role'])
        return role & perm == perm # 使用位与运算符 & 检查权限是否包含指定的单独权限



    def add_permission(self, perm: int) -> None:
        print('update_permission g.uid', g.uid)
        if not self.has_permission(perm):
            mongo.db.user.update(
                {'_id': ObjectId(g.uid)},
                {
                    "$inc": {
                        "role": +perm 
                    }
                }
            )        

    def remove_permission(self, perm: int) -> None:
        print('update_permission g.uid', g.uid)
        print('perm', perm)
        if self.has_permission(perm):
            print('yes!')
            mongo.db.user.update(
                {'_id': ObjectId(g.uid)},
                {
                    "$inc": {
                        "role": -perm 
                    }
                }
            )        
      

user = User()