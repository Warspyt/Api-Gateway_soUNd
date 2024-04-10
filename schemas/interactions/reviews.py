from fastapi import APIRouter
import strawberry
from resolvers.interactions.reviews import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

review_query = Query
review_mutation = Mutation
