from fastapi import APIRouter
import strawberry
from strawberry.asgi import GraphQL
from strawberry.tools import merge_types
from schemas.interactions.interactions import interaction_query, interaction_mutation
from schemas.interactions.reactions import reaction_query, reaction_mutation
from schemas.interactions.reviews import review_query, review_mutation
from schemas.users.user import user_query, user_mutation

app_graphql_interactions = APIRouter()

# All queries
queries = (interaction_query, reaction_query, review_query, user_query)
mutations = (interaction_mutation, reaction_mutation,
             review_mutation, user_mutation)

# Merge schemas
Query = merge_types("Query", queries)
Mutation = merge_types("Mutation", mutations)
