import click
from flask import Flask

from app.extension import mongo
from app.model.user import user, Permission

def register_cli(app: Flask):
    @app.cli.command('hello', help="print help")
    @click.argument('name')
    def hello(name):
        print("hello", name)

    @app.cli.command()
    def init():
        click.echo('Initializing the database...')

        fake_data =['孟德','玄德','翼德','孔明','公瑾','云长','子龙']
        for i in fake_data:
            click.echo('Generating name:{0}'.format(i))
            mongo.db.test.insert_one({'name': i})

        click.echo('Done.')

    @app.cli.command()
    def admin():

        click.echo('Generating admin ...')

        uid = mongo.db.user.insert_one({
             'username': '嬴政',
            'password': 'password',
            'email': 'yingzheng@foxmail.com',
            'role': Permission.ADMIN,
        }).inserted_id

        click.echo('Generated Admin: {0}'.format(uid))