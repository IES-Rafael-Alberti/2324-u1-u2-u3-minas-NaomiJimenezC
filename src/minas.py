"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""

from src.Procesado.generacion_tablero import generar_tablero
from src.Procesado.colocacion_minas import colocacion_mina

MINAS = 10
def jugar():
    """
    Esta función ejecuta el juego.

    """


if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
    tablero_prueba = generar_tablero()
    colocacion_mina(tablero_prueba,MINAS)

    for fila in tablero_prueba:
        print(fila)
