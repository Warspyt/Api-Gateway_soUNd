from fastapi import APIRouter
import strawberry
from type.audio_manegement.song import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

song_query = Query
song_mutation = Mutation
