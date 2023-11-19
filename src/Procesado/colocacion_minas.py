import random


def colocacion_mina(tablero:list,minas_a_colocar:int):
    """
    Coloca las minas en un tablero de manera aleatoria.
    Parameters
    ----------
    tablero
        Tablero donde hay que colocar las minas
    """

    minas_colocadas = 0

    while minas_colocadas != minas_a_colocar:
        fila = random.randint(0,len(tablero)-1)
        columna = random.randint(0,len(tablero)-1) #TODO cambia lo del 7

        if tablero[fila][columna] != "💣":
            tablero[fila][columna] = "💣"
            minas_colocadas += 1

