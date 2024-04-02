from fastapi import APIRouter
import strawberry
from strawberry.asgi import GraphQL
from strawberry.tools import merge_types
from schemas.notification_management.DistNoti import DistNoti_Query, DistNoti_Mutation
from schemas.notification_management.InfoNoti import InfoNoti_Query, InfoNoti_Mutation


app_graphql = APIRouter()

# All queries
queries = (DistNoti_Query, InfoNoti_Query)
mutations = (DistNoti_Mutation,InfoNoti_Mutation)
print("fium fium fium fium")
print(mutations)

# Merge schemas
Query = merge_types("Query", queries)
Mutation = merge_types("Mutation", mutations)

