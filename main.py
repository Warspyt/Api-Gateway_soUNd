from fastapi import FastAPI
from schemas.Index import app_graphql


app = FastAPI()
app.include_router(app_graphql)
app.include_router(app_streaming)

# # Iniciar el consumidor de RabbitMQ en un hilo separado
# consumer_thread = threading.Thread(target=consume_messages)
# consumer_thread.start()   
