from src.Procesado.comprobar_victoria import verificar_victoria


def test_verificar_victoria_ganada():
    casillas_restantes = 0
    assert verificar_victoria(casillas_restantes) == True

def test_verificar_victoria_no_ganada_aun():
    casillas_restantes = 54
    assert verificar_victoria(casillas_restantes) == False