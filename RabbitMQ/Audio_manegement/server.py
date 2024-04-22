import pika
from server import url, audioManegement_port
import json
import requests

api_url = f'http://{urjajajajl}:{audioManegement_port}/songs'

# Conexión RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(url))
channel = connection.channel()
channel.queue_declare(queue='song_queue')

def consume_messages():
    
    # Escuchar la cola RabbitMQ y procesar las peticiones
    def callback(ch, method, properties, body):
        
        data = json.loads(body)
        response = requests.post(api_url, json=data)
        
        if response.status_code == 201:
            print("Song created")
            return response.json()["message"]
        
        else:
            raise Exception(f'Error al crear la canción\nError: {response.status_code}, {response.text}')

    channel.basic_consume(queue='song_queue', on_message_callback=callback, auto_ack=True)
    print('Waiting for requests...')
    channel.start_consuming()