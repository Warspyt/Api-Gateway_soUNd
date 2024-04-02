from fastapi import APIRouter
import strawberry
from strawberry.asgi import GraphQL
from strawberry.tools import merge_types
from schemas.users.user import user_query, user_mutation


app_graphql_User = APIRouter()

# All queries
queries = (user_query)
mutations = (user_mutation)

# Merge schemas
Query = merge_types("Query", queries)
# Query = queries
Mutation = merge_types("Mutation", mutations)
# Mutation = mutations
