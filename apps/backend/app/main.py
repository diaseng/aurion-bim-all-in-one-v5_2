
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from .routes.health import router as health_router
from .routes.minerva import router as minerva_router
from .routes.vulcano import router as vulcano_router
from .routes.netuno import router as netuno_router
from .routes.jupiter import router as jupiter_router
from .routes.saturno import router as saturno_router
from .routes.flora import router as flora_router
from .routes.apolo import router as apolo_router
from .routes.topos import router as topos_router
from .routes.hermes import router as hermes_router
from .routes.diana import router as diana_router
from .routes.cef import router as cef_router
from .routes.stadium import router as stadium_router

from .settings import settings

VERSION = "5.2"
app = FastAPI(title="Aurion BIM API", version=VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if settings.METRICS_ENABLED:
    Instrumentator().instrument(app).expose(app, include_in_schema=False, should_gzip=True)

app.include_router(health_router, prefix="/health", tags=["health"])
app.include_router(minerva_router, prefix="/minerva", tags=["minerva"])
app.include_router(vulcano_router, prefix="/vulcano", tags=["vulcano"])
app.include_router(netuno_router, prefix="/netuno", tags=["netuno"])
app.include_router(jupiter_router, prefix="/jupiter", tags=["jupiter"])
app.include_router(saturno_router, prefix="/saturno", tags=["saturno"])
app.include_router(flora_router,   prefix="/flora",   tags=["flora"])
app.include_router(apolo_router,   prefix="/apolo",   tags=["apolo"])
app.include_router(topos_router,   prefix="/topos",   tags=["topos"])
app.include_router(hermes_router,  prefix="/hermes",  tags=["hermes"])
app.include_router(diana_router,   prefix="/diana",   tags=["diana"])
app.include_router(cef_router,     prefix="/cef",     tags=["cef"])
app.include_router(stadium_router, prefix="/stadium", tags=["stadium"])
