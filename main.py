from fastapi import FastAPI
from schemas.audio_manegement.index import app_graphql

app = FastAPI()

app.include_router(app_graphql)