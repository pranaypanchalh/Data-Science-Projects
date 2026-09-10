from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def welcomePage(
    request: Request,
    name: str | None = None,
    surname: str | None = None,
    language: str | None = None
):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "name": name,
            "surname": surname,
            "language": language
        }
    )