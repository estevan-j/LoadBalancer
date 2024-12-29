# Usa una imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt en el directorio de trabajo
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el contenido de la aplicación en el directorio de trabajo
COPY . .

# Establece la variable de entorno para Flask
ENV FLASK_APP=app.py

# Expone el puerto en el que correrá la aplicación
EXPOSE 5000

# Elimina las migraciones existentes, crea nuevas migraciones y luego inicia la aplicación
CMD ["sh", "-c", "flask db init && flask db migrate -m 'Create Producto entity' && flask db upgrade && flask run --host=0.0.0.0"]