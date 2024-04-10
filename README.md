# Api-Gateway_soUNd
Orquestador para el manejo de peticiones de la aplicación soUNd

# Correr el proyecto : 
- Crear ambiente : py -m venv .venv
- Entrar al ambiente virtual : .venv\Scripts\activate
- Descargar los paquetes de pip : pip install -r .\requirements.txt
- Desplegar el proyecto en carpeta app : uvicorn main:app --reload

# Correr servidor RabbitMQ con docker
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management
