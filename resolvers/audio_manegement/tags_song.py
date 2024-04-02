import strawberry
import typing
from typing import Optional
import requests
from server import url, audioManegement_port

api_url = f'http://{url}:{audioManegement_port}/tag_songs'
tag_api_url = f'http://{url}:{audioManegement_port}/tags'
song_api_url = f'http://{url}:{audioManegement_port}/songs'

@strawberry.type
class Tag_song:
    id: int
    tagid: int
    tag_name: str
    songid: int
    song_title: str
    song_publicationDate: str
    song_lyrics: str
    song_version: int
    song_userid: int
    song_audioid: int
    song_albumid: int
    song_image_url: str
    
# Queries
@strawberry.type
class Query:
    # Get songs by tag
    @strawberry.field    
    def songs_by_tag(self, id: int) -> typing.List[Tag_song]:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(f'{api_url}/{id}')
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return [
                Tag_song(
                    id = tag_data.get('id'),
                    tagid = tag_data.get('tagid'),
                    tag_name = requests.get(f'{tag_api_url}/{tag_data.get("tagid")}').json().get('name'),
                    songid = tag_data.get('songid'),
                    song_title = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('title'),
                    song_publicationDate = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('publicationDate'),
                    song_lyrics = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('lyrics'),
                    song_version = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('version'),
                    song_userid = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('userid'),
                    song_audioid = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('audioid'),
                    song_albumid = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('albumid'),
                    song_image_url = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('image_url')
                )
                for tag_data in data
            ]
        else:
            raise Exception(f'Error al obtener la las canciones de tag con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
        
    # Get all tags_songs
    @strawberry.field    
    def tags_song(self) -> typing.List[Tag_song]:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
                    
            return  [
                        Tag_song(
                            id = tag_data.get('id'),
                            tagid = tag_data.get('tagid'),
                            tag_name = requests.get(f'{tag_api_url}/{tag_data.get("tagid")}').json().get('name'),
                            songid = tag_data.get('songid'),
                            song_title = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('title'),
                            song_publicationDate = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('publicationDate'),
                            song_lyrics = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('lyrics'),
                            song_version = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('version'),
                            song_userid = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('userid'),
                            song_audioid = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('audioid'),
                            song_albumid = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('albumid'),
                            song_image_url = requests.get(f'{song_api_url}/{tag_data.get("songid")}').json().get('image_url')
                        )
                        for key, value_list in data.items()
                        for tag_data in value_list
                ]  
        else:
            raise Exception(f'Error al obtener las tags_song desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
    
# Mutations
@strawberry.type
class Mutation:
    # post tag_song
    @strawberry.mutation
    def create_tag_Song(self, tagid: int, songid:int) -> str:
        
        data = {
            'tagid': tagid,
            'songid': songid
        }
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.post(api_url, json=data)
        
        if response.status_code == 201:
            return response.json()["message"]
        
        else:
            raise Exception(f'Error al crear la tag_song\nError: {response.status_code}, {response.text}')
    
    # put tag_song
    @strawberry.mutation
    def update_tag_song(self, id:int, tagid: Optional[int] = None, songid: Optional[int] = None) -> Tag_song:
        
        info = {
            'tagid': tagid,
            'songid': songid
        }
        
        info = {key: value for key, value in info.items() if value is not None}
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.put(f'{api_url}/{id}', json=info)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Tag_song(
                        id = data.get('id'),
                        tagid = data.get('tagid'),
                        tag_name = requests.get(f'{tag_api_url}/{data.get("tagid")}').json().get('name'),
                        songid = data.get('songid'),
                        song_title = requests.get(f'{song_api_url}/{data.get("songid")}').json().get('title'),
                        song_publicationDate = requests.get(f'{song_api_url}/{data.get("songid")}').json().get('publicationDate'),
                        song_lyrics = requests.get(f'{song_api_url}/{data.get("songid")}').json().get('lyrics'),
                        song_version = requests.get(f'{song_api_url}/{data.get("songid")}').json().get('version'),
                        song_userid = requests.get(f'{song_api_url}/{data.get("songid")}').json().get('userid'),
                        song_audioid = requests.get(f'{song_api_url}/{data.get("songid")}').json().get('audioid'),
                        song_albumid = requests.get(f'{song_api_url}/{data.get("songid")}').json().get('albumid'),
                        song_image_url = requests.get(f'{song_api_url}/{data.get("songid")}').json().get('image_url')
                    )
        else:
            raise Exception(f'Error al actualizar la tag_song con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
            
    # delete tag_song
    @strawberry.mutation
    def delete_tag_song(self, id: int) -> str:
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.delete(f'{api_url}/{id}')
        
        if response.status_code == 204:
            return f'Tag_song con id {id} eliminado exitosamente'
        
        else:
            raise Exception(f'Error al eliminar la tag_song con ID {id} desde el microservicio Audio Manegement\nError: {response.status_code}, {response.text}')
