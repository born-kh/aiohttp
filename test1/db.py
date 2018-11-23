import datetime
from sqlalchemy import (
	Table, Text, Integer, VARCHAR, MetaData, Column, DateTime
	)


meta = MetaData()


post = Table(
	'post', meta,
	Column('id', Integer, primary_key=True),
	Column('title', VARCHAR, nullable=True),
	Column('body', Text,)
	)


users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('username', VARCHAR(200), nullable=False),
    Column('email', VARCHAR(200), nullable=False),
    Column('password', VARCHAR(200), nullable=False)
)

article = Table(
    'article', meta,
    Column('article_id', Integer, primary_key=True),
    Column('article_title', VARCHAR(200), nullable=False),
    Column('article_text', Text, nullable=False),
    Column('article_date', DateTime, default=datetime.datetime.utcnow)
)


comments =  Table(
    'comments', meta,
    Column('comments_id', Integer, primary_key=True),
    Column('comments_text', Text, nullable=True),
    Column('article_id', Integer,)
    )



async def check_user(conn, username, password):
    result= await conn.fetchrow(users.select().where((users.c.username == username)&(users.c.password==password)))
    if result:
        records=dict(result)
        return records
    else:
        return None

async def registration(conn, username, email,password):
    stmt= users.insert().values(username=username, email=email, password=password)
    await conn.execute(stmt)

async def check_identity(conn, email):
    result= await conn.fetchrow(users.select().where(users.c.email==email))
    if result:
        return True
    return False

async def chek_article(conn, article_id):
    result= await conn.fetchrow(article.select().where(article.c.article_id==article_id))
    if result:
        return True
    return False


