from fastapi import APIRouter
import strawberry
from resolvers.interactions.reactions import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

reaction_query = Query
reaction_mutation = Mutation
