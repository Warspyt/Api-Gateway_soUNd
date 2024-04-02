from fastapi import FastAPI
from schemas.audio_manegement.index import app_graphql
from streaming.streaming import app_streaming
from schemas.index import app_graphql

app = FastAPI()
app.include_router(app_graphql)
app.include_router(app_streaming)
