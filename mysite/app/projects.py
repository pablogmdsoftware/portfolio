from pydantic import BaseModel

class Project(BaseModel):
    name: str
    summary: str
    tech_stack: list[str]
    keywords: list[str]