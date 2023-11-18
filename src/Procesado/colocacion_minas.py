import random


def colocacion_mina(tablero:list):
    """
    Coloca las minas en un tablero de manera aleatoria.
    Parameters
    ----------
    tablero
        Tablero donde hay que colocar las minas
    """
    MINAS = 8
    minas_colocadas = 0

    while minas_colocadas != MINAS:
        fila = random.randint(0,len(tablero)-1)
        columna = random.randint(0,len(tablero)-1) #TODO cambia lo del 7

        if tablero[fila][columna] != "💣":
            tablero[fila][columna] = "💣"
            minas_colocadas += 1

