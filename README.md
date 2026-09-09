# Endpoints de la API

URL base: `http://127.0.0.1:8000/api/`

### Computadoras
* GET `/computadoras/` -> trae todas las PCs (con los juegos anidados)
* POST `/computadoras/` -> crea una PC
* GET `/computadoras/<id>/` -> ver una sola PC
* PUT / PATCH `/computadoras/<id>/` -> editar PC
* DELETE `/computadoras/<id>/` -> borrar PC

### Juegos
* GET `/juegos/` -> lista de juegos
* POST `/juegos/` -> agrega un juego nuevo y a qué PCs va
* GET `/juegos/<id>/` -> detalle de un juego
* PUT / PATCH `/juegos/<id>/` -> editar juego
* DELETE `/juegos/<id>/` -> borrar juego

### Sesiones
* GET `/sesiones/` -> lista de sesiones
* POST `/sesiones/` -> abre sesión (pone la PC en ocupada)
* GET `/sesiones/<id>/` -> ver una sesión
* PUT / PATCH `/sesiones/<id>/` -> actualiza (si terminó o pagó, libera la PC)
* DELETE `/sesiones/<id>/` -> borra sesión (y libera la PC)

### Tarifas
* GET `/tarifas/` -> lista las tarifas
* POST `/tarifas/` -> crea tarifa por hora
* GET `/tarifas/<id>/` -> ver una tarifa
* PUT / PATCH `/tarifas/<id>/` -> cambiar precio o nombre
* DELETE `/tarifas/<id>/` -> borrar tarifa

### Usuarios
* GET `/usuarios/` -> lista los usuarios
* POST `/usuarios/` -> crea un usuario
* GET `/usuarios/<id>/` -> ver un usuario
* PUT / PATCH `/usuarios/<id>/` -> editar usuario
* DELETE `/usuarios/<id>/` -> borrar usuario