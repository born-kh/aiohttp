from .views import frontend
from pathlib import Path

def setup_routes(app):
	app.router.add_route('*','/', frontend.login, name='login')
	app.router.add_route('GET', '/post', frontend.post, name='post')
	app.router.add_route('GET', r'/articles', frontend.articles, name='articles')
	app.router.add_route('GET', r'/articles/get/{article_id}', frontend.article, )
	app.router.add_get(r'/registration', frontend.register, name='registration')
	app.router.add_post(r'/registration', frontend.register)


	app.router.add_static('/static', Path(__file__).parent/'static', name='static')






	
                          