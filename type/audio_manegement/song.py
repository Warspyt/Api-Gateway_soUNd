import strawberry
import requests
from server import url, audioManegement_port

api_url = f'http://{url}:{audioManegement_port}/songs'

@strawberry.type
class Song:
    title: str
    publicationDate: str
    lyrics: str
    version: int
    userid: int
    albumid: int
    
# Queries
@strawberry.type
class Query:
    @strawberry.field    
    def song(self, id: int) -> Song:
        
        # Hacer request en soUNd_AudioManegement_MS
        response = requests.get(f'{api_url}/{id}')
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            return Song(
                        title=data.get('title'),
                        publicationDate=data.get('publicationDate'),
                        lyrics=data.get('lyrics'),
                        version=data.get('version'),
                        userid=data.get('userid'),
                        albumid=data.get('albumid')
                    )
        else:
            raise Exception(f'Error al obtener la canción con ID {id} desde el microservicio Audio Manegement')
    
# Mutations
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_song() -> Song:
        
        return
