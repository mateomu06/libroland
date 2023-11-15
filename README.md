# Proyecto Final - LibroLand
Este proyecto implementa una aplicación web utilizando Flask y Docker, que actúa como una API para buscar libros en Open Library y una interfaz web para visualizar los resultados.

## Cómo Funciona?
Estructura del Proyecto:
El proyecto consta de dos servicios principales: api y web.
api utiliza Flask para crear una API que busca libros en Open Library y expone los resultados a través del puerto 5000.
web proporciona una interfaz web en el puerto 80 para realizar consultas y visualizar los resultados de la búsqueda de libros.


### API de Libros (apilibros.py):
Puerto: 5000.
Funcionamiento: Busca libros en Open Library y expone los resultados en JSON.
### Interfaz Web (weblibros.py):
Puerto: 80.
Funcionamiento: Permite realizar consultas a la API de Libros y visualizar los resultados en una interfaz web.


## Uso de docker-compose.yml

Se utiliza `docker-compose.yml` para configurar servicios. Los servicios comparten la red `mynetwork`, permitiendo la comunicación mediante alias (api y web).

### Despliegue

#### Requisitos Previos
- Docker: [Instrucciones de instalación](https://docs.docker.com/get-docker/)
- Docker Compose: [Instrucciones de instalación](https://docs.docker.com/compose/install/)

#### Pasos de Instalación
1. Clona el repositorio:
   ```bash
   git clone https://tu-repositorio.com/api-libros.git
   cd api-libros
    ```
2. Levanta los servicios con Docker Compose (requiere permisos de administrador):
    ```bash
    docker-compose up -d --build
    ```
3. Accede a la interfaz web en http://localhost:80 