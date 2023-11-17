from src.generacion_tablero import generar_tablero
from src.colocacion_minas import colocacion_mina

def test_colocacion_mina_en_tablero():
    tablero_generado = generar_tablero()
    colocacion_mina(tablero_generado)

    minas_colocadas = 0

    for fila in tablero_generado:
        for casilla in fila:
            if casilla == "💣":
                minas_colocadas += 1

    assert minas_colocadas == 8