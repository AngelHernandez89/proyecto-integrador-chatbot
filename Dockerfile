# 1. Imagen base adecuada
FROM python:3.11-slim

# 2. Instalar dependencias necesarias
# 'json' ya viene con Python. Como nuestra app es de terminal, 
# no instalamos tkinter para evitar errores de pantalla en Docker.
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# 3. Directorio de trabajo e instalar requisitos si existieran
WORKDIR /app

# 4. Copiar los archivos de la aplicación
COPY . .

# 5. Exponer puertos (aunque sea una app de consola, se indica por buena práctica)
EXPOSE 8080

# 6. Ejecutar la aplicación al iniciar
CMD ["python", "chatbot.py"]
