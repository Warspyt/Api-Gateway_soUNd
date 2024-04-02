import strawberry
import typing
from typing import Optional
import requests
from server import url, interactions_port, audioManegement_port

audio_api_url = f'http://{url}:{audioManegement_port}/songs'
api_url = f'http://{url}:{interactions_port}/v1/interactions'


@strawberry.type
class Reactions:
    _id: hex
    userID: int
    audioID: int
    reaction: str


@strawberry.type
class ReactionsCount:
    count: int


@strawberry.type
class Songs:
    id: int
    name: str

# QUERIES


@strawberry.type
class Query:
    # Get number of likes by audio
    @strawberry.field
    def likes(self, audio_id: int) -> ReactionsCount:
        response = requests.get(f'{api_url}/audios/{audio_id}/likes')

        if response.status_code == 200:
            data = response.json()

            return ReactionsCount(
                count=data.get('count')
            )
    # Get number of dislikes by audio

    @strawberry.field
    def dislikes(self, audio_id: int) -> int:
        response = requests.get(f'{api_url}/audios/{audio_id}/dislikes')

        if response.status_code == 200:
            data = response.json()

            return data.get('count')
    # Find if an user liked the audio

    @strawberry.field
    def user_liked(self, audio_id: int, user_id: int) -> bool:
        response = requests.get(
            f'{api_url}/audios/{audio_id}/likes?user={user_id}')

        if response.status_code == 200:
            data = response.json()

            return data.get('reaction')
    # Find if an user disliked the audio

    @strawberry.field
    def user_disliked(self, audio_id: int, user_id: int) -> bool:
        response = requests.get(
            f'{api_url}/audios/{audio_id}/dislikes?user={user_id}')

        if response.status_code == 200:
            data = response.json()

            return data.get('reaction')
    # Get user liked songs

    @strawberry.field
    def liked_audios(self, user_id: int) -> typing.List[Songs]:
        response = requests.get(f'{api_url}/likes?user={user_id}')
        # TO DO: Convertir IDs a nombres de canciones
        print(response)
        if response.status_code == 200:
            data = response.json()
            return [Songs(
                    id=song,
                    name=requests.get(
                        f'{audio_api_url}/{id}').json().get('title')
                    )
                    for song in data['songs']
                    ]


# MUTATIONS
@strawberry.type
class Mutation:
    # Like an audio
    @strawberry.mutation
    def like(self, user_id: int, audio_id: int) -> str:

        data = {
            'user_id': user_id,
        }

        # Hacer request
        response = requests.post(
            f'{api_url}/audios/{audio_id}/likes', json=data)

        if response.status_code == 201:
            return response.json()["Type"]
    # Dislike an audio

    @strawberry.mutation
    def dislike(self, user_id: int, audio_id: int) -> str:

        data = {
            'user_id': user_id,
        }

        # Hacer request
        response = requests.post(
            f'{api_url}/audios/{audio_id}/dislikes', json=data)

        if response.status_code == 201:
            return response.json()["Type"]
    # Delete like

    @strawberry.mutation
    def delete_like(self, user_id: int, audio_id: int) -> bool:

        data = {
            'user_id': user_id,
        }

        # Hacer request
        response = requests.delete(
            f'{api_url}/audios/{audio_id}/likes', json=data)

        if response.status_code == 200:
            return response.json()["State"]
    # Delete dislike

    @strawberry.mutation
    def delete_dislike(self, user_id: int, audio_id: int) -> bool:

        data = {
            'user_id': user_id,
        }

        # Hacer request
        response = requests.delete(
            f'{api_url}/audios/{audio_id}/dislikes', json=data)

        if response.status_code == 200:
            return response.json()["State"]
