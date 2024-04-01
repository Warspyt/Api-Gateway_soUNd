import pika
from server import url
import json

# Conexión RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(url))
channel = connection.channel()
channel.queue_declare(queue='song_queue')

# Enviar peticiones a la cola RabbitMQ
def send_to_queue(data):
    channel.basic_publish(exchange='', routing_key='song_queue', body=json.dumps(data))
    print ("Song request sent")
    

