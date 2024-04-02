import strawberry
import typing
from typing import Optional
import requests
from server import url, notification_port

api_url = f'http://{url}:{notification_port}/GetInfoNotification'

@strawberry.type
class Notification:
    id: str
    title: str
    text: str

@strawberry.type
class Query:
    # Get noti by id
    @strawberry.field    
    def notification(self) -> typing.List[Notification]:

        response = requests.get(f'{api_url}')
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            return [Notification(
                        id = Notida.get('id'),
                        title = Notida.get('title'),
                        text = Notida.get('text'),
                    )for Notida in data ]
        else:
            raise Exception(f'Error al obtener la notificación con id {id} desde el microservicio Notifications\nError: {response.status_code}, {response.text}')


@strawberry.type
class Mutation:
    # post Notification
    @strawberry.mutation
    def create_notification(self, id: str, title: str, text: str) -> str:
        
        data = {
            'id': id,
            'title': title,
            'text': text
        }
        
        # Hacer request en NotificationMs
        response = requests.post((api_url+"/PostNotification"), json=data)
        
        if response.status_code == 200:
            return "SI SE CREO, CONFIA EN MI"
        
        else:
            raise Exception(f'Error al crear la notificación\nError: {response.status_code}, {response.text}')
    
    # put Notification
    @strawberry.mutation
    def update_notification(self, id:str, title: Optional[str] = None, text: Optional[str] = None) -> str:
        
        info = {
            'id': id,
            'title': title,
            'text': text,
        }
        
        info = {key: value for key, value in info.items() if value is not None}
        
        # Hacer request en NotificationMs
        response = requests.put(f'{api_url}/UpdateNotification/', json=info)
        
        if response.status_code == 200:
            return "Se actualizo correctamente"
        else:
            raise Exception(f'Error al actualizar la Notificación con ID {id} desde el microservicio Notification\nError: {response.status_code}, {response.text}')




    # delete Notification
    @strawberry.mutation
    def delete_notification(self, id: str) -> str:
        # Hacer request en NotificationMs
        response = requests.delete(f'{api_url}/DeleteNotification?id='+id)
        
        if response.status_code == 200:
            return f'Notificación con id {id} eliminado exitosamente'
        
        else:
            raise Exception(f'Error al eliminar la notificaión con ID {id} desde el microservicio Notification\nError: {response.status_code}, {response.text}')



