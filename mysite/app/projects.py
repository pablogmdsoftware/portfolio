from pydantic import BaseModel

class Project(BaseModel):
    name: str
    summary: str
    tech_stack: list[str]
    keywords: list[str]
    view_name: str
    link_github: str

WEB_DEVELOPMENT = [
    Project(
        name = "Bus System",
        summary = """
        Ticket purchase system for an imaginary bus business in Spain.
        You can create a profile and order tickets for some travels along the country.
        """,
        tech_stack = ["Python","Django","PostgreSQL","HTML","CSS","JavaScript","Nginx"],
        keywords = [
            "Full Stack",
            "Web Design",
            "SQL",
            "CRUD Application",
        ],
    ),
]