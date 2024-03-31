from fastapi import APIRouter
import strawberry
from resolvers.audio_manegement.playlist import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

playlist_query = Query
playlist_mutation = Mutation