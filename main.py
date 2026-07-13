from fastapi import FastAPI, Request
from routers import notes
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(notes.router, prefix="/notes")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"title": "Home", "active_page": "dashboard"})
