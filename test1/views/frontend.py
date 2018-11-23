from sqlalchemy import select
from sqlalchemy.sql import text
from aiohttp import web
import aiohttp
from aiohttp_jinja2 import template
from .. import db

@template('index.html')
async def index(request):
	site_name = request.app['config'].get('site_name')
	return {'site_name': site_name}



def redirect(router, router_name):
    location = router[router_name].url_for()
    return web.HTTPFound(location)

@template('post.html')
async def post(request):
	async with request.app['db'].acquire() as conn:
		query = select([db.post.c.id, db.post.c.title])
		print(query)
		result = await conn.fetch(query)
	return  {'posts': result}



@template('articles.html')
async def articles(request):
    async with request.app['db'].acquire() as conn:
        query = select([db.article]) 
        result = await conn.fetch(query)
    return  {'articles': result}


@template('article.html')
async def article(request):
    article_id= int(request.match_info.get('article_id'))
    async with request.app['db'].acquire() as conn:
        query = select([db.article]).where(db.article.c.article_id==article_id)
        print(query)
        article = await conn.fetch(query)
        query = select([db.comments]).where(db.comments.c.article_id==article_id)
        comments = await conn.fetch(query)
    return  {'articles': article, 'comments': comments}


@template('login.html')
async def login(request):
    if request.method == 'POST':
        form_data=await request.post()
        username=form_data['username']
        password=form_data['password']
        async with request.app['db'].acquire() as conn:
            check= await db.check_user(conn, username,password)
            if check:
                response=redirect(request.app.router, 'articles')
                raise response
            else:
                error='Пользователь не найден'
                return {'error':error}
    return {}


@template('register.html')
async def register(request):
    if request.method == 'POST':
        form_data= await request.post()
        password=form_data['password']
        async with request.app['db'].acquire() as conn:
            result= await db.check_identity(conn, form_data['email'])
            if result:
                error='Этот пользователь уже существует'
                return {'error':error}
            if not result:
                await db.registration(conn, form_data['username'], form_data['email'], password)
                raise redirect(request.app.router, 'login')


    return {}
