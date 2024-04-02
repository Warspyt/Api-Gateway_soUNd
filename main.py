from fastapi import FastAPI
from schemas.Index import app_graphql


app = FastAPI()

app.include_router(app_graphql)