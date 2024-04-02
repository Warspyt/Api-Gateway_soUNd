import strawberry
import typing
from typing import Optional
import requests
from server import url, audioManegement_port

api_url = f'http://{url}:{audioManegement_port}/tags'

@strawberry.type
class Tag:
    id: int
    name: str
    
# Queries
@strawberry.type
class Query:
    # Get tag by id
    @strawberry.field    
    def tag(self, id: int) -> Tag:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(f'{api_url}/{id}')
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Tag(
                        id = data.get('id'),
                        name = data.get('name')
                    )
        else:
            raise Exception(f'Error al obtener la tag con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
        
    # Get all tags
    @strawberry.field    
    def tags(self) -> typing.List[Tag]:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return [
                Tag(
                    id = tag_data.get('id'),
                    name = tag_data.get('name')
                )
                for tag_data in data
            ]
        else:
            raise Exception(f'Error al obtener las tags desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
    
# Mutations
@strawberry.type
class Mutation:
    # post tag
    @strawberry.mutation
    def create_tag(self, name: str) -> str:
        
        data = {
            'name': name
        }
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.post(api_url, json=data)
        
        if response.status_code == 201:
            return response.json()["message"]
        
        else:
            raise Exception(f'Error al crear la tag\nError: {response.status_code}, {response.text}')
    
    # put tag
    @strawberry.mutation
    def update_tag(self, id:int, name: Optional[str] = None) -> Tag:
        
        info = {
            'name': name
        }
        
        info = {key: value for key, value in info.items() if value is not None}
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.put(f'{api_url}/{id}', json=info)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Tag(
                        id = data.get('id'),
                        name = data.get('name')
                    )
        else:
            raise Exception(f'Error al actualizar la tag con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
            
    # delete tag
    @strawberry.mutation
    def delete_tag(self, id: int) -> str:
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.delete(f'{api_url}/{id}')
        
        if response.status_code == 204:
            return f'Tag con id {id} eliminado exitosamente'
        
        else:
            raise Exception(f'Error al eliminar la tag con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
