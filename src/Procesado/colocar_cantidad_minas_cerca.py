from src.Procesado.contar_minas_cerca import contar_minas_cercas

def colocar_cantidad_minas_cercanas(tablero:list):
    """
    Coloca la cantidad de minas cercas
    Parameters
    ----------
    tablero
        Donde se coloca la cantidad de minas cercanas

    """
    for fila_index, fila in enumerate(tablero):
        for columna_index, columna in enumerate(fila):
            if columna != "💣":
                minas_cerca = contar_minas_cercas(fila_index,columna_index,tablero)
                tablero[fila_index][columna_index] = minas_cerca

