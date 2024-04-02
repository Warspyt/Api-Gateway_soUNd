from fastapi import APIRouter
import strawberry
from resolvers.audio_manegement.tags import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

tag_query = Query
tag_mutation = Mutation