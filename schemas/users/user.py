from fastapi import APIRouter
import strawberry
from resolvers.users.user import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

user_query = Query
user_mutation = Mutation
