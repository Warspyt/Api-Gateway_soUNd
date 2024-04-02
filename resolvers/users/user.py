import datetime
import strawberry
import typing
from typing import Optional
import requests
from server import url, users_port

api_url = f'http://{url}:{users_port}/api/users'


@strawberry.type
class User:
    name: int
    title: str
    publicationDate: str
    lyrics: str
    version: int
    userid: int
    audioid: int
    albumid: int
    image_url: str

# Queries


@strawberry.type
class Query:
    # Get song by id
    @strawberry.field
    def getInfo(self, id: int) -> User:

        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(f'{api_url}/{id}')

        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()

            return User(
                id=data.get('id'),
                title=data.get('title'),
                publicationDate=data.get('publicationDate'),
                lyrics=data.get('lyrics'),
                version=data.get('version'),
                userid=data.get('userid'),
                audioid=data.get('audioid'),
                albumid=data.get('albumid'),
                image_url=data.get('image_url')
            )
        else:
            raise Exception(
                f'Error al obtener el usuario con ID {id} desde el microservicio User\nError: {response.status_code}, {response.text}')

    @strawberry.field
    def login(self, username: str, password: str) -> User:
        info = {
            'username': username,
            'password': password
        }
        response = requests.put(f'{api_url}/login', json=info)
        if response.status_code == 200:
            return f'Inicio de sesión exitoso'

        else:
            raise Exception(
                f'Error al iniciar sesión \nError: {response.status_code}, {response.text}')


# Mutations
@strawberry.type
class Mutation:
    # delete user
    @strawberry.mutation
    def delete_user(self, id: int) -> str:

        response = requests.delete(f'{api_url}/{id}')
        if response.status_code == 200:
            return f'Usuario con {id} eliminado exitosamente'

        else:
            raise Exception(
                f'Error al eliminar al usuario con ID {id} desde el microservicio Users \nError: {response.status_code}, {response.text}')

    # put song
    @strawberry.mutation
    def update_song(self, name: Optional[str] = None, lastname: Optional[str] = None, username: Optional[str] = None, password: Optional[str] = None, email: Optional[str] = None, phone: Optional[str] = None) -> str:

        info = {
            'name': name,
            'lastname': lastname,
            'username': username,
            'password': password,
            'email': email,
            'phone': phone,
        }

        info = {key: value for key, value in info.items() if value is not None}

        # Hacer request en soUNd_AudioManegement_MS
        response = requests.put(f'{api_url}/{id}', json=info)

        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            return f'La información del Usuario con {id} fue actualizado exitosamente'
        else:
            raise Exception(
                f'Error al actualizar la canción con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')

    @strawberry.mutation
    def sign_user(self, name: str, lastname: str, username: str, password: str, email: str, phone: str, role: str, birthday: str) -> str:
        info = {
            'name': name,
            'lastname': lastname,
            'role': role,
            'birthday': birthday,
            'username': username,
            'password': password,
            'email': email,
            'phone': phone,
        }

        response = requests.post(f'{api_url}/signup', json=info)

        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            return f'Se ha creado un usuario de forma exitosa!!!'
        else:
            raise Exception(
                f'Error al crear el usuario desde el microservicio Users\nError: {response.status_code}, {response.text}')
