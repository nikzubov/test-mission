import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from database.engine import database
from database.models import Base
from handlers.router import router

logging.basicConfig(
    level=logging.INFO,
    filename='bot_log.log',
    format="%(asctime)s %(levelname)s %(message)s"
)


@asynccontextmanager
async def lifespan(app: FastAPI):
   await database.create_db(base=Base)
   yield
   await database.dispose()


app = FastAPI(
   lifespan=lifespan,
   default_response_class=ORJSONResponse
)

app.include_router(
   router=router,
   prefix='/api'
)
