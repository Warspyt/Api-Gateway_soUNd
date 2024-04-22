from fastapi import FastAPI
from schemas.index import app_graphql
from streaming.streaming import app_streaming
import threading
#from RabbitMQ.Audio_manegement.server import consume_messages

app = FastAPI()
app.include_router(app_graphql)
app.include_router(app_streaming)

# Iniciar el consumidor de RabbitMQ en un hilo separado
#consumer_thread = threading.Thread(target=consume_messages)
#consumer_thread.start()   
