import random


def colocacion_mina(tablero:list):
    #TODO comenta esta función
    MINAS = 8
    minas_colocadas = 0

    while minas_colocadas != MINAS:
        fila = random.randint(0,7)
        columna = random.randint(0,7) #TODO cambia lo del 7

        tablero[fila][columna] == "💣"
        minas_colocadas += 1
