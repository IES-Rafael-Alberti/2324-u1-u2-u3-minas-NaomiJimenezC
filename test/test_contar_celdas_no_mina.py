from src.Procesado.generacion_tablero import generar_tablero
from src.Procesado.colocacion_minas import colocacion_mina
from src.Procesado.contar_celdas_no_minas import contar_celdas_vacias

tablero_prueba = generar_tablero()
minas_prueba = 10
colocacion_mina(tablero_prueba,minas_prueba)

def test_minas_vacias_igual_a_54():
    assert contar_celdas_vacias(tablero_prueba,minas_prueba) == 54