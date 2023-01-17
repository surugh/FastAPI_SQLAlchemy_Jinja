import schemas
from db import db_func

from typing import List
from fastapi import APIRouter, HTTPException

api_router = APIRouter(prefix='/api', tags=['api'])


@api_router.get("/users", response_model=List[schemas.User])
async def get_users_list(skip: int = 0, limit: int = 100):
    return await db_func.get_users(skip=skip, limit=limit)


@api_router.get("/user/{user_id}", response_model=schemas.User)
async def get_user_by_id(user_id: int):
    db_user = await db_func.get_user(user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@api_router.post("/user", response_model=schemas.User)
async def create_new_user(user: schemas.UserCreate):
    # проверяем нет ли уже пользователя с таким именем
    db_user = await db_func.get_user_by_username(username=user.username)
    if db_user:
        raise HTTPException(
            status_code=400, detail="Username already registered"
        )
    return await db_func.create_user(user=user)


@api_router.post("/user/{user_id}/article", response_model=schemas.Article)
async def create_new_article(user_id: int, article: schemas.ArticleCreate):
    return await db_func.create_user_article(
        article=article, user_id=user_id
    )


@api_router.get("/article/{article_id}", response_model=schemas.ArticleUser)
async def get_article_by_id(article_id: int):
    return await db_func.get_user_article(article_id)


@api_router.get("/articles", response_model=List[schemas.Article])
async def get_articles_list(skip: int = 0, limit: int = 100):
    return await db_func.get_articles(skip=skip, limit=limit)
