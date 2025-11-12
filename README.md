**Gestion-de-videojuegos**

Práctica realizada por el grupo 3 conformado por Alejandro Rodrigo, David Gallegos, Francisco Javier López y Mateus Leandro.
#

**Roles**
  - Integrador: Alejandro Rodrigo
  - Encargado de hacer las etapas 1 y 2: Francisco Javier López
  - Encargado de hacer las etapas 3 y 4: Mateus Leandro
  - Encargado de hacer las etapas 5 y 6: David Gallegos

#

**Ejecución del programa**

Para ejecutar el programa, descargue la carpeta e inicie el main.py de la carpeta en un editor de código (VS Code o PyCharm).

#
**Etapa 1: Listas**

Es la encargada de mostrar una lista de títulos con los videojuegos que se han añadido mediante el uso de un array. Esta  lista es utilizada para realizar operaciones como añadir, insertar, eliminar y ordenar videojuegos.

#

**Etapa 2: Tuplas**

Encargado de imprimir el catálogo de videojuegos almacenado agarrando informacion de la  como una lista de tuplas sa. Cada tupla contiene un:

   - Título  
   - Año de lanzamiento  
   - Género
#

**Etapa 3: Cadenas**

Nos permite introducir un nombre de un videojuego y busca coincidencias en el catálogo, en caso de que encuentre un nombre que coincida con el que hay almacenado en las tuplas, mostrará el nombre del videojuego, el género al que pertece el videojuego y el año de lanzamiento de este mismo. 

Además, el buscador del titulo del videojuego tiene una comparación insensible a mayúsculas y espacios.

#

**Etapa 4: Conjuntos**

Trabaja con los géneros extraídos del catálogo usando conjuntos como el `pop`. También incluye operaciones para:
   - Añadir nuevos géneros
   - Eliminar elementos
   - Comprobar si un género favorito está en la colección
   - Operaciones de teoría de conjuntos con otra colección (unión, intersección, diferencia)

#

**Etapa 5:  Diccionarios**

Implementa un sistema completo de gestión de videojuegos utilizando diccionarios como estructura de datos principal. Las funcionalidades incluyen:

CRUD completo (Crear, Leer, Actualizar, Eliminar) de videojuegos en el catálogo usando la clave de referencia 

#

**Etapa 6:  Proyecto final (menú interactivo)**

El sistema ya integrado se encarga de combinar todas las etapas anteriores en un menú interactivo completo con las siguientes opciones:

  - Listar videojuegos -> Muestra todo el catálogo organizado
  - Buscar por título exacto -> Hace una búsqueda del titulo de un videojuego para saber si existe 
  - Buscar por fragmento de título -> Realiza una búsqueda de un videojuego solo agregando parte del nombre (Ej: The Legend)
  - Buscar por género -> Filtra por categoría los videojuegos
  - Buscar por rango de años -> Búsqueda de los titulos de los videojuego por su año de lanzamiento
  - Añadir videojuego -> Encargado de agregar nuevos juegos al catálogo
  - Actualizar videojuego -> Modificar información existente que pide el usuario e ingresa este mismo
  - Eliminar videojuego -> Elimina juegos del catálogo que introduce el usuario
  - Mostrar estadísticas -> Muestra las métricas y conteos del catálogo
  - Salir -> Finalizar el programa
