FROM nginx

# Instala herramientas adicionales si es necesario
RUN apt-get update -qq && apt-get -y install apache2-utils
ENV NODE_ROOT /var/www/api-gateway
WORKDIR $NODE_ROOT
RUN mkdir log
COPY app.conf /tmp/app.nginx
RUN envsubst '$NODE_ROOT' < /tmp/app.nginx > /etc/nginx/conf.d/default.conf

# Configura el directorio de trabajo
WORKDIR /etc/nginx
# Copia el archivo de configuración de Nginx
COPY app.conf /etc/nginx/conf.d/default.conf
# Copia los archivos SSL/TLS al contenedor
COPY cert.pem /etc/ssl/cert.pem
COPY key.pem /etc/ssl/key.pem
# Exponer los puertos HTTP y HTTPS
EXPOSE 80
EXPOSE 443

# Inicia Nginx en modo daemon
CMD ["nginx", "-g", "daemon off;"]
