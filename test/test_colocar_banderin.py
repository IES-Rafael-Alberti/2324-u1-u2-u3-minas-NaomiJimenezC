from src.generacion_tablero import generar_tablero
from src.colocar_banderin import  colocar_banderin

def test_colocacion_bandera_correcta():
    tablero_prueba = generar_tablero()
    colocar_banderin(tablero_prueba,5,5)

    assert tablero_prueba[5][5] == "🚩"