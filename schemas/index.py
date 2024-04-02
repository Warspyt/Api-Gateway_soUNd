from fastapi import APIRouter
import strawberry
from strawberry.asgi import GraphQL
from strawberry.tools import merge_types
from schemas.audio_manegement.index import queries as audio_manegement_queries, mutations as audio_manegement_mutations

app_graphql = APIRouter()

# All queries
queries = audio_manegement_queries
mutations = audio_manegement_mutations

# Merge schemas 

Query = merge_types("Query", queries)
Mutation = merge_types("Mutation", mutations)

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQL(schema)

app_graphql.add_route('/graphql', graphql_app)