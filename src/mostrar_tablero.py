from src.generacion_tablero import generar_tablero

def mostrar_tablero(tablero_a_mostrar:list)->str:

    """
    Función que se encarga de imprimir en condiciones el contenido del tablero
    Parameters
    ----------
    tablero_a_mostrar
        El tablero que se va a mostrar

    Returns
    -------
        Devuelve la string adecuada para mostrarlo bien a la hora de imprimir

    """
    mensaje_tablero = ""
    for fila in tablero_a_mostrar:
        for celda in fila:
            mensaje_tablero += celda + " "
        mensaje_tablero += "\n"

        # te quiero post https://www.lawebdelprogramador.com/foros/Python/1418909-Imprimir-matriz-sin-corchetes.html
    return mensaje_tablero


