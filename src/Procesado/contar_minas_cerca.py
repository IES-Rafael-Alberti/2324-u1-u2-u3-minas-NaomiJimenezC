def contar_minas_cercas(fila:int, columna:int, tablero:list)->int:
    """
    Cuenta las cantidad de minas cercanas a una casilla concreta
    Parameters
    ----------
    fila
        Fila donde está la casilla
    columna
        Columna donde está la casilla
    tablero
        Tablero donde se encuentra la casilla

    Returns
    -------
    int
        Devuelve la cantidad de minas cercanas
    """
    minas_cercanas = 0
    for celdas_horizontales in range(-1, 2):
        for celdas_verticales in range(-1, 2):
            if 0 <= celdas_horizontales + fila < len(tablero) and 0 <= celdas_verticales + columna < len(tablero[0]):
                # Comprueba que no se salga del tablero
                if tablero[celdas_horizontales + fila][celdas_verticales + columna] == '💣':
                    minas_cercanas += 1
    return minas_cercanas
