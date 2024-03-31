from fastapi import APIRouter
import strawberry
from resolvers.audio_manegement.album import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

album_query = Query
album_mutation = Mutation