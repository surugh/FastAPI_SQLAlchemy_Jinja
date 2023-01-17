from api import api
from config import API_METADATA
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


root_router = APIRouter(tags=['www'])

templates = Jinja2Templates(directory="templates")


@root_router.get("/", response_class=HTMLResponse)
async def home(request: Request, api_metadata: dict = API_METADATA):
    articles_list: list = await api.get_articles_list()
    users_list: list = await api.get_users_list()
    context = dict(request=request, api_metadata=api_metadata,
                   articles=articles_list, users=users_list)
    return templates.TemplateResponse("home.html", context)


@root_router.get("/articles", response_class=HTMLResponse)
async def articles(request: Request, api_metadata: dict = API_METADATA):
    articles_list: list = await api.get_articles_list()
    users_list: list = await api.get_users_list()
    context = dict(request=request, api_metadata=api_metadata,
                   articles=articles_list, users=users_list)
    return templates.TemplateResponse("home.html", context)


@root_router.get("/article/{article_id}", response_class=HTMLResponse)
async def article(request: Request, article_id: int,
                  api_metadata: dict = API_METADATA):
    article_dict: int = await api.get_article_by_id(article_id)
    users_list: list = await api.get_users_list()
    context = dict(request=request, api_metadata=api_metadata,
                   article=article_dict, users=users_list)
    return templates.TemplateResponse("article.html", context)
