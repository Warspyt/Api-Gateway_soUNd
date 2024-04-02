import strawberry
import typing
from typing import Optional
import requests
from server import url, audioManegement_port

api_url = f'http://{url}:{audioManegement_port}/tag_albums'
tag_api_url = f'http://{url}:{audioManegement_port}/tags'
album_api_url = f'http://{url}:{audioManegement_port}/albums'

@strawberry.type
class Tag_album:
    id: int
    tagid: int
    tag_name: str
    albumid: int
    album_name: str
    album_description: str
    album_userid: int
    
# Queries
@strawberry.type
class Query:
    # Get albums by tag
    @strawberry.field    
    def albums_by_tag(self, id: int) -> typing.List[Tag_album]:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(f'{api_url}/{id}')
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return [
                Tag_album(
                    id = tag_data.get('id'),
                    tagid = tag_data.get('tagid'),
                    tag_name = requests.get(f'{tag_api_url}/{tag_data.get("tagid")}').json().get('name'),
                    albumid = tag_data.get('albumid'),
                    album_name = requests.get(f'{album_api_url}/{tag_data.get("albumid")}').json().get('name'),
                    album_description = requests.get(f'{album_api_url}/{tag_data.get("albumid")}').json().get('description'),
                    album_userid = requests.get(f'{album_api_url}/{tag_data.get("albumid")}').json().get('userid')
                )
                for tag_data in data
            ]
        else:
            raise Exception(f'Error al obtener los albumes de tag con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
        
    # Get all tags_albums
    @strawberry.field    
    def tags_albums(self) -> typing.List[Tag_album]:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
                    
            return  [
                        Tag_album(
                            id = tag_data.get('id'),
                            tagid = tag_data.get('tagid'),
                            tag_name = requests.get(f'{tag_api_url}/{tag_data.get("tagid")}').json().get('name'),
                            albumid = tag_data.get('albumid'),
                            album_name = requests.get(f'{album_api_url}/{tag_data.get("albumid")}').json().get('name'),
                            album_description = requests.get(f'{album_api_url}/{tag_data.get("albumid")}').json().get('description'),
                            album_userid = requests.get(f'{album_api_url}/{tag_data.get("albumid")}').json().get('userid')
                        )
                        for key, value_list in data.items()
                        for tag_data in value_list
                ]  
        else:
            raise Exception(f'Error al obtener las tags_album desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
    
# Mutations
@strawberry.type
class Mutation:
    # post tag_album
    @strawberry.mutation
    def create_tag_album(self, tagid: int, albumid:int) -> str:
        
        data = {
            'tagid': tagid,
            'albumid': albumid
        }
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.post(api_url, json=data)
        
        if response.status_code == 201:
            return response.json()["message"]
        
        else:
            raise Exception(f'Error al crear la tag_album\nError: {response.status_code}, {response.text}')
    
    # put tag_album
    @strawberry.mutation
    def update_tag_album(self, id:int, tagid: Optional[int] = None, albumid: Optional[int] = None) -> Tag_album:
        
        info = {
            'tagid': tagid,
            'albumid': albumid
        }
        
        info = {key: value for key, value in info.items() if value is not None}
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.put(f'{api_url}/{id}', json=info)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Tag_album(
                        id = data.get('id'),
                        tagid = data.get('tagid'),
                        tag_name = requests.get(f'{tag_api_url}/{data.get("tagid")}').json().get('name'),
                        albumid = data.get('albumid'),
                        album_name = requests.get(f'{album_api_url}/{data.get("albumid")}').json().get('name'),
                        album_description = requests.get(f'{album_api_url}/{data.get("albumid")}').json().get('description'),
                        album_userid = requests.get(f'{album_api_url}/{data.get("albumid")}').json().get('userid')
                    )
        else:
            raise Exception(f'Error al actualizar la tag_song con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
            
    # delete tag_album
    @strawberry.mutation
    def delete_tag_album(self, id: int) -> str:
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.delete(f'{api_url}/{id}')
        
        if response.status_code == 204:
            return f'Tag_album con id {id} eliminado exitosamente'
        
        else:
            raise Exception(f'Error al eliminar la tag_album con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
