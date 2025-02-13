
# TaskManagerAPI

API simple realizada en python con FastAPI y MongoDB para el manejo de tareas.




## Utilización

Para lanzar el servidor de la api en local, se puede utilizar uvicorn con el siguiente comando:

```bash
  uvicorn main:app --reload
```

Para lanzar el servidor de MongoDB en local con la base de datos de prueba, utilizar el siguiente comando desde la carpeta raíz del proyecto:

```bash
  mongod --dbpath demo_db
```
## Documentación

Una vez lanzado el servidor, se puede acceder a la documentacion mediante las direcciones:
- 127.0.0.1:8000/docs
- 127.0.0.1:8000/redoc

De todas formas, indico aquí las funcionalidades:

### Crear tareas

- POST a 127.0.0.1:8000/tasks indicando:
```json
{
  "name": "Nombre de la tarea",
  "description": "Descripción de la tarea"
}
```

El resto de campos de la tarea se rellenan automáticamente.

### Obtener tareas

#### Obtenerlas todas

- GET a 127.0.0.1:8000/tasks

#### Filtrar por estado de la tarea

- GET a 127.0.0.1:8000/tasks/filter/_**estado**_

#### Obtener tarea mediante id

- GET a 127.0.0.1:8000/tasks/_**id_tarea**_

### Actualizar tareas

- PUT a 127.0.0.1:8000/tasks/_**id_tarea**_ indicando

```json
{
  "name": "Nuevo nombre",
  "description": "Nueva descripción",
  "status": "Nuevo estado"
}
```

Cabe destacar que los campos son opcionales, si no se indica alguno, se mantiene el original.

#### Eliminar

#### Eliminar una tarea

- DELETE a 127.0.0.1:8000/tasks/_**id_tarea**_

#### Eliminar todas las tareas

- DELETE a 127.0.0.1:8000/tasks