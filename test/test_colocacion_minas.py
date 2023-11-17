from src.generacion_tablero import generar_tablero


def test_colocacion_tablero():
    tablero_generado = generar_tablero()
    colocar_minas(tablero_generado)

    minas_colocadas = 0

    for fila in tablero_generado:
        for casilla in fila:
            if casilla == "💣":
                minas_colocadas += 1

    assert minas_colocadas == 8