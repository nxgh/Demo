from . import api

@api.route('/api')
def apis():
    return 'api'