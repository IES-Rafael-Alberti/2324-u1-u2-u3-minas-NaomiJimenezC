from src.Procesado.verificar_derrota import verificar_derrota

def test_derrota_asegurada():
    celda_seleccionada = "💣"
    assert verificar_derrota(celda_seleccionada) == True

def test_todavia_no_perdio():
    celda_seleccionada = "_"
    assert verificar_derrota(celda_seleccionada) == False