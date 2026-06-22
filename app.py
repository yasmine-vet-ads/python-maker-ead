from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent

INDEX_ORIGINAL = BASE_DIR / "index.html"
PYTHON_START_HEALTH_INDEX = BASE_DIR / "python-start-health" / "index.html"

STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="Python Maker EAD",
    description="Plataforma EAD com curso original de Python e versão Python Start Health.",
    version="1.1.0",
)

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def render_html(file_path: Path) -> HTMLResponse:
    return HTMLResponse(content=file_path.read_text(encoding="utf-8"))


@app.get("/")
async def get_home():
    """
    Curso original já publicado.
    """
    return render_html(INDEX_ORIGINAL)


@app.get("/python-show")
async def get_python_show():
    """
    Mantém a rota antiga funcionando para o curso original.
    """
    return render_html(INDEX_ORIGINAL)


@app.get("/python-start-health")
async def get_python_start_health():
    """
    Nova versão do curso voltada à saúde, dados e automação.
    """
    return render_html(PYTHON_START_HEALTH_INDEX)