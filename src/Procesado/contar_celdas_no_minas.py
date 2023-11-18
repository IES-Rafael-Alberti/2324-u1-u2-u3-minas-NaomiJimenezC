def contar_celdas_vacias(tablero_juego:list,minas_colocadas:int)->int:
    """
    Cuenta las celdas que no son minas
    Parameters
    ----------
    tablero_juego
        Tablero donde se juega
    minas_colocadas
        La cantidad de minas colocadas en el juego

    Returns
    -------
        Devuelve la cantidad de celdas vacías que hay en el tablero
    """
    celdas_vacias = 0
    for fila in tablero_juego:
        for celda in fila:
            if celda != "💣":
                celdas_vacias +=1

    return celdas_vacias