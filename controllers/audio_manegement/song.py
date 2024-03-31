from fastapi import APIRouter
import strawberry
from type.audio_manegement.song import Query, Mutation
from strawberry.asgi import GraphQL

song = APIRouter()
schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)

song.add_route('/graphql', graphql_app)
