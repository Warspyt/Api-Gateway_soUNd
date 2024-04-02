from fastapi import APIRouter
import strawberry
from resolvers.notifications_management.DistNoti import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

DistNoti_Query = Query
DistNoti_Mutation = Mutation
