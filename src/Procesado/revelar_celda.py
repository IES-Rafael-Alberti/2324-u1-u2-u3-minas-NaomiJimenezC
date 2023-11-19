def revelar_celda(tablero:list,fila:int,columna:int)->str:
    """
    Mediante las coordenadas se obtiene el valor de una casilla del tablero
    Parameters
    ----------
    tablero
        De donde se saca la casilla
    fila
        La fila del tablero donde se vaya a acceder
    columna
        La columna del tablero donde se quiera acceder

    Returns
    -------
    str
        Devuelve el contenido de la casilla obtenida
    """
    return tablero[fila][columna]