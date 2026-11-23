import os
import pathlib

from fastapi import FastAPI, Form, Request
from fastapi.responses import PlainTextResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.store import make_store

BASE = pathlib.Path(__file__).parent
app = FastAPI(title="Factory app")
app.mount("/static", StaticFiles(directory=BASE / "static"), name="static")
templates = Jinja2Templates(directory=BASE / "templates")
templates.env.globals["sf"] = {"expires": os.environ.get("SF_EXPIRES", ""), "env": os.environ.get("SF_ENV", "local")}
store = make_store()

MAX_LEN = 500


@app.get("/healthz", response_class=PlainTextResponse)
def healthz():
    return "ok"


@app.get("/")
def index(request: Request):
    items = store.list("items", order_by="-created_at")
    return templates.TemplateResponse(request, "index.html", {"items": items})


@app.post("/items")
def create_item(name: str = Form(..., max_length=MAX_LEN), note: str = Form("", max_length=MAX_LEN)):
    store.create("items", {"name": name.strip(), "note": note.strip()})
    return RedirectResponse("/", status_code=303)


@app.post("/items/{item_id}/delete")
def delete_item(item_id: str):
    store.delete("items", item_id)
    return RedirectResponse("/", status_code=303)
