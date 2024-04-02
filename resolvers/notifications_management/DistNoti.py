import strawberry
import typing
from typing import Optional
import requests
from server import url, notification_port

api_url = f'http://{url}:{notification_port}/GetDistributionNot'

@strawberry.type
class NotificationDist:
    id: str
    IsView: str
    usuarioID: str

@strawberry.type
class Query:
    # Get notis
    @strawberry.field    
    def notificationDist(self) -> typing.List[NotificationDist]:

        response = requests.get(f'{api_url}')
        
        if response.status_code == 200:
            # Devolver los datos obtenidos en formato JSON
            data = response.json()
            
            return [NotificationDist (
                        id = Notida.get('id'),
                        IsView = Notida.get('isView'),
                        usuarioID = Notida.get('usuarioID'),
                    )for Notida in data ] 
        else:
            raise Exception(f'Error al obtener la notificación con id {id} desde el microservicio Notifications\nError: {response.status_code}, {response.text}')


@strawberry.type
class Mutation:
    # post Notification
    @strawberry.mutation
    def create_DistNotification(self, id: str, IsView: str, usuarioID: str) -> str:
        
        data = {
            'id': id,
            'isView': IsView,
            'usuarioID': usuarioID
        }
        
        # Hacer request en NotificationMs
        response = requests.post(api_url+"/PostDistribution", json=data)
        print("nuy")
        if response.status_code == 200:
            return "SI SE CREO"
        
        else:
            raise Exception(f'Error al crear la notificación\nError: {response.status_code}, {response.text}')
    
    # put Notification
    @strawberry.mutation
    def update_DistNotification(self, id:str, IsView: Optional[str] = None, usuarioID: Optional[str] = None) -> str:
        
        info = {
            'id': id,
            'IsView': IsView,
            'usuarioID': usuarioID,
        }
        
        info = {key: value for key, value in info.items() if value is not None}
        
        # Hacer request en NotificationMs
        response = requests.put(f'{api_url}/UpdateDistribution', json=info)
        print("sdadasdcccc")
        if response.status_code == 200:
            return "Se actualizo"
        else:
            raise Exception(f'Error al actualizar la Notificación con ID {id} desde el microservicio Notification\nError: {response.status_code}, {response.text}')
            
    # delete Notification
    @strawberry.mutation
    def delete_DistNotification(self, id: str) -> str:
        # Hacer request en NotificationMs
        response = requests.delete(f'{api_url}/DeleteDistribution?id='+id)
        
        if response.status_code == 200:
            return f'Notificación con id {id} eliminado exitosamente'
        
        else:
            raise Exception(f'Error al eliminar la notificaión con ID {id} desde el microservicio Notification\nError: {response.status_code}, {response.text}')
