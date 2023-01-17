from typing import List
from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    article: str


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    owner_id: int


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str
    is_active: bool = True


class UserInDB(UserBase):
    id: int


class User(UserBase):
    id: int
    articles: List[Article] = []


class ArticleUser(ArticleBase):
    id: int
    owner: UserInDB
