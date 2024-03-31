import strawberry
import typing
from typing import Optional
import requests
from server import url, audioManegement_port

api_url = f'http://{url}:{audioManegement_port}/playlists'

@strawberry.type
class Playlist:
    id: int
    name: str
    userid: int
    
# Queries
@strawberry.type
class Query:
    # Get playlist by id
    @strawberry.field    
    def playlist(self, id: int) -> Playlist:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(f'{api_url}/{id}')
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Playlist(
                        id = data.get('id'),
                        name = data.get('name'),
                        userid = data.get('userid')
                    )
        else:
            raise Exception(f'Error al obtener la playlist con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
        
    # Get all playlists
    @strawberry.field    
    def playlists(self) -> typing.List[Playlist]:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return [
                Playlist(
                    id = playlist_data.get('id'),
                    name = playlist_data.get('name'),
                    userid = playlist_data.get('userid')
                )
                for playlist_data in data
            ]
        else:
            raise Exception(f'Error al obtener las playlists desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
    
# Mutations
@strawberry.type
class Mutation:
    # post playlist
    @strawberry.mutation
    def create_playlist(self, name: str, userid: int) -> str:
        
        data = {
            'name': name,
            'userid': userid
        }
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.post(api_url, json=data)
        
        if response.status_code == 201:
            return response.json()["message"]
        
        else:
            raise Exception(f'Error al crear la playlist\nError: {response.status_code}, {response.text}')
    
    # put playlist
    @strawberry.mutation
    def update_playlist(self, id:int, name: Optional[str] = None, userid: Optional[int] = None) -> Playlist:
        
        info = {
            'name': name,
            'userid': userid,
        }
        
        info = {key: value for key, value in info.items() if value is not None}
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.put(f'{api_url}/{id}', json=info)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Playlist(
                        id = data.get('id'),
                        name = data.get('name'),
                        userid = data.get('userid')
                    )
        else:
            raise Exception(f'Error al actualizar la playlist con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
            
    # delete playlist
    @strawberry.mutation
    def delete_playlist(self, id: int) -> str:
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.delete(f'{api_url}/{id}')
        
        if response.status_code == 204:
            return f'Playlist con id {id} eliminado exitosamente'
        
        else:
            raise Exception(f'Error al eliminar la playlist con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
