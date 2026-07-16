from fastapi import FastAPI, Request, HTTPException, status
from routers import notes
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as starlettHTTPException

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(notes.router, prefix="/notes")

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(request, "home.html", {"title": "Home", "active_page": "dashboard"})

@app.exception_handler(RequestValidationError)
def validation_exception_handler(request:Request, exception: RequestValidationError):
    return templates.TemplateResponse(
        request,
        "note_not_found.html",
        {
            "title": 422,
            "status_code": status.HTTP_422_UNPROCESSABLE_CONTENT,
            "message": "Invalid Input. Please Check your input and try again!",
        },
        status_code= status.HTTP_422_UNPROCESSABLE_CONTENT
    )