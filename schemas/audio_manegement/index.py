from fastapi import APIRouter
import strawberry
from strawberry.asgi import GraphQL
from strawberry.tools import merge_types
from schemas.audio_manegement.song import song_query, song_mutation
from schemas.audio_manegement.album import album_query, album_mutation

app_graphql = APIRouter()

# All queries
queries = (song_query, album_query)
mutations = (song_mutation, album_mutation)

# Merge schemas
Query = merge_types("Query", queries)
Mutation = merge_types("Mutation", mutations)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app_graphql.add_route('/graphql', graphql_app)