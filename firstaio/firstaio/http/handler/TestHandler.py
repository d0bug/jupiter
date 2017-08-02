from firstaio.http.HttpDecorator import get, post


@get('/')
async def index(*args, **kwargs):
    return '<h1>hello world</h1>'


@get('/redirect')
async def redirect(*args, **kwargs):
    return 'redirect:http://www.baidu.com'


@post('/users')
async def getUsers(*args, **kwargs):
    pass
