from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
INDEX_FILE = BASE_DIR / "index.html"
STATIC_DIR = BASE_DIR / "static"

app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def render_index() -> HTMLResponse:
    return HTMLResponse(content=INDEX_FILE.read_text(encoding="utf-8"))


@app.get("/")
async def get_home():
    return render_index()


@app.get("/python-show")
async def get_python_show():
    return render_index()
