from api import api
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

TITLE = "FastAPI & SQLAlchemy & Jinja"

root_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@root_router.get("/", response_class=HTMLResponse)
async def home(request: Request, title: str = TITLE):
    content = "PG Tech DeV"
    context = dict(request=request, title=title, content=content)
    return templates.TemplateResponse("bak_base.html", context)


@root_router.get("/articles", response_class=HTMLResponse)
async def articles(request: Request, title: str = TITLE):
    articles_list: list = await api.get_articles_list()
    context = dict(request=request, title=title, articles=articles_list)
    return templates.TemplateResponse("bak_articles.html", context)


@root_router.get("/article/{article_id}", response_class=HTMLResponse)
async def article(request: Request, article_id: int, title: str = TITLE):
    article_dict: int = await api.get_article_by_id(article_id)
    context = dict(request=request, title=title, article=article_dict)
    return templates.TemplateResponse("bak_article.html", context)
