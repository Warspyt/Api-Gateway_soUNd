from fastapi import APIRouter
import strawberry
from resolvers.interactions.interactions import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

interaction_query = Query
interaction_mutation = Mutation
