from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent

LANDING_INDEX = BASE_DIR / "landing.html"
INDEX_ORIGINAL = BASE_DIR / "index.html"
PYTHON_START_HEALTH_INDEX = BASE_DIR / "python-start-health" / "index.html"
PYTHON_SHOW_HEALTH_INDEX = BASE_DIR / "python-start-health-show.html"

STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="Python Maker EAD",
    description="Plataforma EAD com curso Maker e versão Python Start Health.",
    version="1.3.0",
)

if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


def render_html(file_path: Path) -> HTMLResponse:
    return HTMLResponse(content=file_path.read_text(encoding="utf-8"))


@app.get("/")
async def get_home():
    """
    Página principal com escolha entre os cursos.
    """
    return render_html(LANDING_INDEX)


@app.get("/python-maker")
async def get_python_maker():
    """
    Curso original Maker.
    """
    return render_html(INDEX_ORIGINAL)


@app.get("/python-show")
async def get_python_show():
    """
    Mantém a rota antiga funcionando para o Python Show Maker.
    """
    return render_html(INDEX_ORIGINAL)


@app.get("/python-start-health")
async def get_python_start_health():
    """
    Curso Python Start Health.
    """
    return render_html(PYTHON_START_HEALTH_INDEX)


@app.get("/python-show-health")
async def get_python_show_health():
    """
    Python Show Health em página própria, com música, quiz e certificado.
    """
    return render_html(PYTHON_SHOW_HEALTH_INDEX)