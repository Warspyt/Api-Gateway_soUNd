from fastapi import FastAPI
from controllers.audio_manegement.song import song

app = FastAPI()

app.include_router(song)
