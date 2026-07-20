from pydantic import BaseModel, Field, ConfigDict

class NoteBase(BaseModel):
    
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)
    category: str = Field(min_length=1, max_length=100)
    
    
class NoteResponse(NoteBase):
    
    model_config = ConfigDict(from_attributes= True)
    
    id: int
    date_created: str
    

class CreateNote(NoteBase):
    pass