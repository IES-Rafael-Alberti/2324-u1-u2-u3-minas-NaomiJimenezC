from src.Procesado.contar_minas_cerca import contar_minas_cercas

def test_contar_una_mina():
    tablero = [
        [' ', ' ', ' '],
        [' ', '💣', ' '],
        [' ', ' ', ' ']
    ]
    resultado = contar_minas_cercas(0, 0, tablero)
    assert resultado == 1

def test_contar_varias_minas():
    tablero = [
        ['💣', ' ', ' ', '💣'],
        [' ', ' ', ' ', ' '],
        [' ', ' ', '💣', ' '],
        ['💣', ' ', ' ', '💣']
    ]
    resultado = contar_minas_cercas(2, 3, tablero)
    assert resultado == 2
