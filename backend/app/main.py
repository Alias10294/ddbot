from fastapi                 import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.chat     import router   as chat_router
from app.api.health   import router   as health_router
from app.config       import settings
from app.rag          import configRag
from app.rag.creerRag import creer_rag


if not configRag.DATA_FILE.exists():
    print("rag en creation")
    creer_rag()
else:
    print("rag deja cree")

app = FastAPI(title = settings.app_name)

app.add_middleware(
    CORSMiddleware,
    allow_origins     = [settings.frontend_origin],
    allow_credentials = True,
    allow_methods     = ["*"],
    allow_headers     = ["*"])

app.include_router(health_router)
app.include_router(chat_router)
