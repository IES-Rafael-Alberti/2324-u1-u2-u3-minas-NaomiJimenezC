from src.generacion_tablero import generar_tablero


def test_asegurar_longitud_tablero():

    assert len(generar_tablero()) == 8