import strawberry
import typing
from typing import Optional
import requests
from server import url, audioManegement_port

api_url = f'http://{url}:{audioManegement_port}/albums'

@strawberry.type
class Album:
    id: int
    name: str
    description: str
    userid: int
    
# Queries
@strawberry.type
class Query:
    # Get album by id
    @strawberry.field    
    def album(self, id: int) -> Album:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(f'{api_url}/{id}')
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Album(
                        id = data.get('id'),
                        name = data.get('name'),
                        description = data.get('description'),
                        userid = data.get('userid')
                    )
        else:
            raise Exception(f'Error al obtener el album con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
        
    # Get all albums
    @strawberry.field    
    def albums(self) -> typing.List[Album]:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return [
                Album(
                    id = album_data.get('id'),
                    name = album_data.get('name'),
                    description = album_data.get('description'),
                    userid = album_data.get('userid')
                )
                for album_data in data
            ]
        else:
            raise Exception(f'Error al obtener los albumes desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
    
# Mutations
@strawberry.type
class Mutation:
    # post album
    @strawberry.mutation
    def create_album(self, name: str, description: str, userid: int) -> str:
        
        data = {
            'name': name,
            'description': description,
            'userid': userid
        }
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.post(api_url, json=data)
        
        if response.status_code == 201:
            return response.json()["message"]
        
        else:
            raise Exception(f'Error al crear el album\nError: {response.status_code}, {response.text}')
    
    # put album
    @strawberry.mutation
    def update_album(self, id:int, name: Optional[str] = None, description: Optional[str] = None, userid: Optional[int] = None) -> Album:
        
        info = {
            'name': name,
            'description': description,
            'userid': userid,
        }
        
        info = {key: value for key, value in info.items() if value is not None}
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.put(f'{api_url}/{id}', json=info)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Album(
                        id = data.get('id'),
                        name = data.get('name'),
                        description = data.get('description'),
                        userid = data.get('userid')
                    )
        else:
            raise Exception(f'Error al actualizar el album con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
            
    # delete album
    @strawberry.mutation
    def delete_album(self, id: int) -> str:
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.delete(f'{api_url}/{id}')
        
        if response.status_code == 204:
            return f'Album con id {id} eliminado exitosamente'
        
        else:
            raise Exception(f'Error al eliminar el album con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
