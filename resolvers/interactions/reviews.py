import strawberry
import typing
from typing import Optional
import requests
from server import url, interactions_port

api_url = f'http://{url}:{interactions_port}/v1/interactions'


@strawberry.type
class Comment:
    userID: int
    comment: str

# QUERIES


@strawberry.type
class Query:
    # Get all comments of specific audio
    @strawberry.field
    def get_comments(self, audio_id: int) -> typing.List[Comment]:
        response = requests.get(f'{api_url}/audios/{audio_id}/comments')

        if response.status_code == 200:
            data = response.json()
            print("200")
            print(type(data['comments']))

            return [
                Comment(
                    userID=com.get('userID'),
                    comment=com.get('comment')
                )
                for com in data['comments']
            ]


# MUTATIONS
@strawberry.type
class Mutation:
    # New comment
    @strawberry.mutation
    def post_comment(self, user_id: int, audio_id: int, comment: str) -> str:

        data = {
            'user_id': user_id,
            'comment': comment
        }

        # Hacer request
        response = requests.post(
            f'{api_url}/audios/{audio_id}/comments', json=data)

        if response.status_code == 201:
            return response.json()["State"]
