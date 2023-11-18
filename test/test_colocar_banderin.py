from src.Procesado.generacion_tablero import generar_tablero
from src.Procesado.colocar_banderin import  colocar_banderin

def test_colocacion_bandera_correcta():
    tablero_prueba = generar_tablero()
    colocar_banderin(tablero_prueba,5,5)

    assert tablero_prueba[5][5] == "🚩"