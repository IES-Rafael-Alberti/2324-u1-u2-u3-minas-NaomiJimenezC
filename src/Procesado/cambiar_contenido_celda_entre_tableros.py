def cambiar_contenido_entre_tableros(tablero_real:list,tablero_falso:list,casilla_seleccionada:tuple):
    """
    Funcion que sirve para cambiar el contenido del tablero que muestra en pantalla
    con el valor correspondiente en tablero de verdad
    Parameters
    ----------
    tablero_real
        Es el tablero con el que se trabaja verdaderamente
    tablero_falso
        Es el tablero que se le muestra al jugador
    casilla_seleccionada
        La casilla que ha seleccionado el juegador

    Returns
    -------

    """
    fila = casilla_seleccionada[0]
    columa = casilla_seleccionada[1]
    tablero_falso[fila][columa] = tablero_real[fila][columa]