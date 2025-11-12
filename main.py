#GESTION DE VIDEOJUEGOS 
#FICHERO MAIN
from etapas import (
    videojuegos,        # lista de tablas con los datos de los videojuegos añadidos
    mostrar_catalogo,   # función para mostrar el catálogo de videojuegos
    buscar_videojuego,  # función para buscar un título de un videojuego en especifico
    eliminar_generos,  # función para trabajar y eliminar géneros
    gestionar_lista     # función para  la gestion de la lista de favoritos
    ##por añadir -> etapa 5 y 6
)

if __name__ == "__main__":
    
    mostrar_catalogo()

    nombreVideojuego = input(" Escribe el nombre de un videojuego: ")
    buscar_videojuego(nombreVideojuego)

    eliminar_generos()

    gestionar_lista()
