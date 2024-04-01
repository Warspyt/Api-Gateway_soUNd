from fastapi import FastAPI
from schemas.audio_manegement.index import app_graphql
import threading
from RabbitMQ.Audio_manegement.server import consume_messages

app = FastAPI()

app.include_router(app_graphql)


# Iniciar el consumidor de RabbitMQ en un hilo separado
consumer_thread = threading.Thread(target=consume_messages)
consumer_thread.start()   