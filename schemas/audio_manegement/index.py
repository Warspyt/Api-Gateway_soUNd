from fastapi import APIRouter
import strawberry
from strawberry.asgi import GraphQL
from strawberry.tools import merge_types
from schemas.audio_manegement.song import song_query, song_mutation
from schemas.audio_manegement.album import album_query, album_mutation
from schemas.audio_manegement.playlist import playlist_query, playlist_mutation
from schemas.audio_manegement.tags import tag_query, tag_mutation
from schemas.audio_manegement.tags_song import tags_song_query, tags_song_mutation
from schemas.audio_manegement.tags_album import tags_album_query, tags_album_mutation

app_graphql = APIRouter()

# All queries
queries = (song_query, album_query, playlist_query, tag_query, tags_song_query, tags_album_query)
mutations = (song_mutation, album_mutation, playlist_mutation, tag_mutation, tags_song_mutation, tags_album_mutation)

# Merge schemas 

Query = merge_types("Query", queries)
Mutation = merge_types("Mutation", mutations)