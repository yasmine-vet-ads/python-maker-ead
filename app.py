from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles # 1. Importe o módulo

app = FastAPI()

# 2. Diga ao FastAPI para servir os arquivos da pasta "static" na rota "/static"
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
