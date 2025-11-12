from src.gestor.catalogo import catalogo, crear_juego, leer_juego, actualizar_juego, eliminar_juego
from src.gestor.busquedas import buscar_por_titulo, buscar_parcial, buscar_por_genero, buscar_por_rango
from src.gestor.estadisticas import total_juegos, conteo_por_genero

def mostrar_catalogo():
    print("\nCatálogo de videojuegos:")
    for juego in catalogo.values():
        generos = ", ".join(juego["genero"])
        print(f"- {juego['titulo']} ({juego['anio']}) | Género(s): {generos}")
    print()

def mostrar_estadisticas():
    print("\nEstadísticas del catálogo:")
    print(f"Total de videojuegos: {total_juegos(catalogo)}")
    print("Conteo por género:")
    for genero, cantidad in conteo_por_genero(catalogo).items():
        print(f"  - {genero}: {cantidad}")
    print()

def menu():
    while True:
        print("\nMenú del Gestor de Videojuegos")
        print("1. Listar videojuegos")
        print("2. Buscar por título exacto")
        print("3. Buscar por fragmento de título")
        print("4. Buscar por género")
        print("5. Buscar por rango de años")
        print("6. Añadir videojuego")
        print("7. Actualizar videojuego")
        print("8. Eliminar videojuego")
        print("9. Mostrar estadísticas")
        print("0. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_catalogo()

        elif opcion == "2":
            titulo = input("Título exacto: ")
            juego = buscar_por_titulo(catalogo, titulo)
            print(juego if juego else "No encontrado.")

        elif opcion == "3":
            fragmento = input("Fragmento del título: ")
            resultados = buscar_parcial(catalogo, fragmento)
            for juego in resultados:
                print(juego)

        elif opcion == "4":
            genero = input("Género: ")
            resultados = buscar_por_genero(catalogo, genero)
            for juego in resultados:
                print(juego)

        elif opcion == "5":
            try:
                min_año = int(input("Año mínimo: "))
                max_año = int(input("Año máximo: "))
                resultados = buscar_por_rango(catalogo, min_año, max_año)
                for juego in resultados:
                    print(juego)
            except ValueError:
                print("Introduce años válidos.")

        elif opcion == "6":
            titulo = input("Título: ")
            try:
                anio = int(input("Año: "))
                genero = input("Género: ")
                crear_juego(catalogo, titulo, anio, genero)
            except ValueError:
                print("Año inválido.")

        elif opcion == "7":
            clave = input("Clave del juego (título en minúsculas con guiones bajos): ")
            nuevo_year = input("Nuevo año (dejar vacío para no cambiar): ")
            nuevo_genero = input("Nuevo género (dejar vacío para no cambiar): ")
            actualizar_juego(
                catalogo,
                clave,
                nuevo_year=int(nuevo_year) if nuevo_year else None,
                nuevo_genero=nuevo_genero if nuevo_genero else None
            )

        elif opcion == "8":
            clave = input("Clave del juego a eliminar: ")
            eliminar_juego(catalogo, clave)

        elif opcion == "9":
            mostrar_estadisticas()

        elif opcion == "0":
            print("Fin del programa")
            break

        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()
