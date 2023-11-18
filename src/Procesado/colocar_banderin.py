def colocar_banderin(tablero:list,fila:int,columna:int):
    """
    Función básica para colocar banderín en el tablero
    Parameters
    ----------
    tablero
        Recibe el tablero donde se quiera colocar el banderín
    fila
        Fila donde se encuentra la celda donde se quiera colocar el banderín
    columna
        Columna donde se encuentra la celda donde se quiera colocar el banderín

    """
    if tablero[fila][columna] != "🚩":
        tablero[fila][columna] = "🚩"