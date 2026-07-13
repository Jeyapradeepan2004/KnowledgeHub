from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

notes: list[dict] = [
    {
        "note_id": 1,
        "note_title": "What is Flask",
        "note_content": "Flask is a python framework used to \
create web application and it a lightwight \
useful for micro web application we use flask bacically \
when want the full control of the web application",
        "note_category": "Python Framework",
        "note_tag": "Flask",
    },
    {
        "note_id": 2,
        "note_title": "What is FastAPI",
        "note_content": "FastAPI is a modren python framework used to build web application \
it is fastest and has good in-build things like pydantic, swegger and much more",
        "note_category": "Python Framework",
        "note_tag": "FastAPI",
    },
]


@router.get("/")
def view_notes(request: Request):
    return templates.TemplateResponse(request, "notes.html", {"notes": notes, "title": "Notes", "active_page": "notes"})


@router.post("/")
def add_notes():
    # write code to add notes
    return "Note Successfully Added"


@router.put("/{note_id}")
def update_notes(note_id: int):
    # Write code to update notes
    return "Note updation is Successfull"


@router.delete("/{note_id}")
def delete_notes(note_id: int):
    # Write code to delete notes
    return "Note Deleted Successfully"
