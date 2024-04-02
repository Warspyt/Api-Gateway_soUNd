import datetime
import strawberry
import typing
from typing import Optional
import requests
from resolvers.interactions.reactions import Songs
from server import url, interactions_port, audioManegement_port

audio_api_url = f'http://{url}:{audioManegement_port}/songs'
api_url = f'http://{url}:{interactions_port}/v1/interactions'


@strawberry.type
class Reproduction:
    userID: int
    audioID: int
    date: datetime


# QUERIES


@strawberry.type
class Query:
    # Get number of reproductions by audio
    @strawberry.field
    def get_reproductions(self, audio_id: int) -> int:
        response = requests.get(f'{api_url}/audios/{audio_id}/reproductions')

        if response.status_code == 200:
            data = response.json()

            return data.get('count')

    # Recently played songs

    @strawberry.field
    def recently_played(self, user_id: int) -> typing.List[Songs]:
        response = requests.get(f'{api_url}/user/{user_id}/audios/recent')

        if response.status_code == 200:
            data = response.json()

            return [Songs(
                    id=song,
                    name=requests.get(
                        f'{audio_api_url}/{song}').json().get('title')
                    )
                    for song in data['songs']
                    ]


# MUTATIONS
@strawberry.type
class Mutation:
    # New reproduction
    @strawberry.mutation
    def new_reproduction(self, user_id: int, audio_id: int) -> str:

        data = {
            'user_id': user_id
        }

        # Hacer request
        response = requests.post(
            f'{api_url}/audios/{audio_id}/reproductions', json=data)

        if response.status_code == 201:
            return response.json()["State"]
