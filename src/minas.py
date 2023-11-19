"""
En esta solución, se ha estructurado el código para que sea claro y fácil de seguir. Cada función tiene una responsabilidad específica, lo que hace que el código sea más legible y mantenible. Además, se han utilizado constantes para mejorar la comprensión del código y evitar el uso de "números mágicos" o cadenas de texto repetidas.

Notas Adicionales
La función revelar_celdas_vacias y verificar_victoria necesitan ser implementadas según las reglas del Buscaminas.
Este ejercicio es una excelente manera de evaluar y mejorar las habilidades de programación de tus alumnos, enfocándose en las estructuras de datos y el manejo de lógica básica en Python.

"""
from src.entrada.escoger_opcion import escoger_opcion
from src.entrada.seleccionar_casilla import seleccionar_casilla
from src.Procesado.generacion_tablero import generar_tablero
from src.Procesado.colocacion_minas import colocacion_mina
from src.Procesado.contar_celdas_no_minas import contar_celdas_vacias
from src.Procesado.revelar_celda import revelar_celda
from src.Procesado.comprobar_victoria import verificar_victoria
from src.Procesado.colocar_banderin import colocar_banderin
from src.Procesado.cambiar_contenido_celda_entre_tableros import cambiar_contenido_entre_tableros
from src.Salida.mostrar_tablero import mostrar_tablero
from src.Salida.menu import mostrar_menu


MINAS = 10
def jugar():

    """
    Esta función se encarga de ejecutar el juego
    """

    tablero_falso = generar_tablero()
    tablero_real = generar_tablero()
    colocacion_mina(tablero_real,MINAS)
    celdas_restantes = contar_celdas_vacias(tablero_real,MINAS)

    ha_ganado = False
    ha_perdido = False
    no_quiero_seguir_jugando = False

    while ha_perdido != True and ha_ganado != True and no_quiero_seguir_jugando != True:
        tablero_grafico = mostrar_tablero(tablero_falso) #cambialo luego por el tablero falso
        menu = mostrar_menu()
        print(tablero_grafico, menu)
        opcion_escogida = escoger_opcion()

        match opcion_escogida:
            case "1":
                casilla_seleccionada = seleccionar_casilla(tablero_real)
                contenido_celda = revelar_celda(tablero_real,casilla_seleccionada[0],casilla_seleccionada[1])
                cambiar_contenido_entre_tableros(tablero_falso,tablero_real,casilla_seleccionada)
                if contenido_celda != "💣":
                    celdas_restantes =- 1
                    ha_ganado = verificar_victoria(celdas_restantes)
                else:
                    ha_perdido = True

            case "2":
                casilla_seleccionada = seleccionar_casilla(tablero_real)
                colocar_banderin(tablero_falso,casilla_seleccionada[0],casilla_seleccionada[1])
            case "3":
                no_quiero_seguir_jugando = True



if __name__ == "__main__":
    """
    Esta sección del código se ejecuta solo si ejecutamos este archivo directamente.
    """
    jugar()
