from fastapi import APIRouter, Request, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as starlettHTTPException
from schemas import NoteResponse, CreateNote

router = APIRouter()

templates = Jinja2Templates(directory="templates")

notes: list[dict] = [
    {
        "id": 1,
        "title": "What is Flask",
        "content": "Flask is a python framework used to \
create web application and it a lightwight \
useful for micro web application we use flask bacically \
when want the full control of the web application",
        "category": "Python Framework",
        "date_created": "01-01-2026",
    },
    {
        "id": 2,
        "title": "What is FastAPI",
        "content": "FastAPI is a modren python framework used to build web application \
it is fastest and has good in-build things like pydantic, swegger and much more",
        "category": "Python Framework",
        "date_created": "02-01-2026",
    },
]


@router.get("/")
def view_notes(request: Request):
    return templates.TemplateResponse(
        request,
        "notes.html",
        {"notes": notes, "title": "Notes", "active_page": "notes"},
    )


@router.get("/{note_id}")
def get_note(request: Request, note_id: int):

    for note in notes:
        if note.get("id") == note_id:
            return templates.TemplateResponse(
                request,
                "note.html",
                {"note": note, "title": "Note", "active_page": "notes"},
            )
    return templates.TemplateResponse(
        request, 
        "note_not_found.html", 
        {
            "title": "404",
            "status_code": status.HTTP_404_NOT_FOUND,
            "message": "Note Not Found"
        }, 
        status_code= status.HTTP_404_NOT_FOUND
    )
    


@router.post("/", response_model= NoteResponse, status_code= status.HTTP_201_CREATED)
def create_notes(note: CreateNote):
    
    new_id = max(n["id"] for n in notes) + 1 if notes else 1
    new_note = {
        "id": new_id,
        "title": note.title,
        "content": note.content,
        "category": note.category,
        "date_created": "03-01-2026"
    }
    
    notes.append(new_note)
    return new_note
    


@router.put("/{note_id}")
def update_notes(note_id: int):
    # Write code to update notes
    return "Note updation is Successfull"


@router.delete("/{note_id}")
def delete_notes(note_id: int):
    # Write code to delete notes
    return "Note Deleted Successfully"
