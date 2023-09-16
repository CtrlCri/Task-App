# Utiliza la imagen base de Python 3.11 en Alpine Linux
FROM python:3.11.0-alpine3.17

# Establece la variable de entorno PYTHONUNBUFFERED en 1
ENV PYTHONUNBUFFERED 1

# Instala dockerize en el contenedor
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.6.1.tar.gz \
    && rm dockerize-linux-amd64-v0.6.1.tar.gz

# Crea un directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requerimientos al directorio de trabajo
COPY ./requirements.txt ./

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Copia todo el contenido del proyecto al directorio de trabajo en el contenedor
COPY ./ ./

# Comando para esperar a que la base de datos esté disponible y luego iniciar la aplicación
CMD ["sh", "-c", "dockerize -wait tcp://db:5432 -timeout 60s python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
