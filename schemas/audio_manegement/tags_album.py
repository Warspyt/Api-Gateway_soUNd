from fastapi import APIRouter
import strawberry
from resolvers.audio_manegement.tags_album import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

tags_album_query = Query
tags_album_mutation = Mutation