from fastapi import APIRouter
import strawberry
from resolvers.notifications_management.InfoNoti import Query, Mutation
from strawberry.asgi import GraphQL

schema = strawberry.Schema(Query, Mutation)

InfoNoti_Query = Query
InfoNoti_Mutation = Mutation
