from fastapi import FastAPI
from schemas.index import app_graphql

app = FastAPI()

app.include_router(app_graphql)
