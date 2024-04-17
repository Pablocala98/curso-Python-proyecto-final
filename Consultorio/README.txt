# Aplicación de Gestión de Consultorios y Masajistas

¡Bienvenido a la aplicación de gestión de consultorios y masajistas! Esta aplicación te permite administrar reservas, masajistas y consultorios de manera eficiente. Puedes crear, eliminar, editar y visualizar reservas, masajistas y consultorios.

## Descripción general

Esta aplicación está desarrollada en Django y proporciona un sistema para gestionar consultorios, masajistas y reservas. Puedes agregar, editar, eliminar y visualizar reservas, masajistas y consultorios desde la interfaz de usuario.

## Características

- **Consultorios**: Crear, editar, eliminar y visualizar consultorios con detalles como nombre, capacidad y disponibilidad.
- **Masajistas**: Crear, editar, eliminar y visualizar masajistas con detalles como nombre, apellido, documento y teléfono.
- **Reservas**: Crear, editar, eliminar y visualizar reservas, incluyendo la relación entre consultorios.
- **Interfaz de usuario**: Interfaz intuitiva y fácil de usar para administrar todos los aspectos de la aplicación.

## Requisitos

- Django (versión `5.0.3`)
- Python (versión `3.12.1` o superior)
- Dependencias adicionales que puedes encontrar en el archivo `requirements.txt`

## Instalación

Sigue estos pasos para instalar y configurar la aplicación:

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/Pablocala98/curso-Python-proyecto-final
    cd repo
    ```


2. **Configurar la base de datos**:
    Modifica los parámetros de la base de datos en `settings.py` según tus necesidades.

5. **Realizar migraciones**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Iniciar el servidor de desarrollo**:
    ```bash
    python manage.py runserver
    ```

7. Abre tu navegador y visita [http://localhost:8000/](http://localhost:8000/).

