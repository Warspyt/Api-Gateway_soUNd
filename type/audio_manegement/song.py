import strawberry
import typing
import requests
from server import url, audioManegement_port

api_url = f'http://{url}:{audioManegement_port}/songs'

@strawberry.type
class Song:
    id: int
    title: str
    publicationDate: str
    lyrics: str
    version: int
    userid: int
    albumid: int
    
# Queries
@strawberry.type
class Query:
    # Get song by id
    @strawberry.field    
    def song(self, id: int) -> Song:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(f'{api_url}/{id}')
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return Song(
                        id = data.get('id'),
                        title = data.get('title'),
                        publicationDate = data.get('publicationDate'),
                        lyrics = data.get('lyrics'),
                        version = data.get('version'),
                        userid = data.get('userid'),
                        albumid = data.get('albumid')
                    )
        else:
            raise Exception(f'Error al obtener la canción con ID {id} desde el microservicio Audio Manegement')
        
    # Get all songs
    @strawberry.field    
    def songs(self) -> typing.List[Song]:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(api_url)
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return [
                Song(
                    id = song_data.get('id'),
                    title = song_data.get('title'),
                    publicationDate = song_data.get('publicationDate'),
                    lyrics = song_data.get('lyrics'),
                    version = song_data.get('version'),
                    userid = song_data.get('userid'),
                    albumid = song_data.get('albumid')
                )
                for song_data in data
            ]
        else:
            raise Exception(f'Error al obtener las canciones desde el microservicio Audio Manegement')
    
# Mutations
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_song() -> Song:
        
        return
