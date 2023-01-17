from db.database import database
from declare_models import users, articles
import schemas


# получаем список статей
async def get_articles(skip: int = 0, limit: int = 100):
    query = articles.select().offset(skip).limit(limit)
    results = await database.fetch_all(query)
    return [dict(result) for result in results]


# ищем статью
async def get_user_article(article_id: int):
    article = dict(await database.fetch_one(
        articles.select().where(articles.c.id == article_id))
                )
    user = dict(await database.fetch_one(
        users.select().where(users.c.id == article["owner_id"]))
                )
    article.update({"owner": user})
    return article


# добавляем статью пользователю
async def create_user_article(article: schemas.ArticleCreate, user_id: int):
    query = articles.insert().values(**article.dict(), owner_id=user_id)
    item_id = await database.execute(query)
    return schemas.Article(**article.dict(), id=item_id, owner_id=user_id)


# получаем список всех пользователей
async def get_users(skip: int = 0, limit: int = 100):
    results = await database.fetch_all(
        users.select().offset(skip).limit(limit)
    )
    return [dict(result) for result in results]


# ищем пользователя и его контент по id
async def get_user(user_id: int):
    user = dict(await database.fetch_one(
        users.select().where(users.c.id == user_id))
                )
    list_articles = await database.fetch_all(
        articles.select().where(articles.c.owner_id == user["id"])
    )
    user.update({"articles": [dict(result) for result in list_articles]})
    return user


# ищем пользователя по имени в базе
async def get_user_by_username(username: str):
    return await database.fetch_one(
        users.select().where(users.c.username == username)
    )


# добавляем нового пользователя в БД
async def create_user(user: schemas.UserCreate):
    password = user.password
    db_user = users.insert().values(
        username=user.username, password=password
    )
    user_id = await database.execute(db_user)
    return schemas.User(**user.dict(), id=user_id)
