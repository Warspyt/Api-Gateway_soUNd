from fastapi import APIRouter
import strawberry
from resolvers.audio_manegement.tags_song import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

tags_song_query = Query
tags_song_mutation = Mutation