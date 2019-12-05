import pymongo
from datetime import datetime

# client = pymongo.MongoClient(
#     'mongodb://blog_dev:password@localhost:27017/blog_dev')
client = pymongo.MongoClient(
    'mongodb://rbac:password@localhost:20017/rbac')

user = client['rbac']['user']


if __name__ == "__main__":
    user.update_many({},
    {
        '$inc': {
            'role': +64
        }
    })
    print(user.find_one({'username':'嬴政'}))