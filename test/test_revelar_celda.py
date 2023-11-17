from src.revelar_celda import revelar_celda
import pytest

tablero_prueba = [
                ['_', '_', '_', '_', '_', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '💣', '💣', '_'],
                ['_', '_', '_', '_', '_', '_', '_', '_'],
                ['_', '_', '💣', '💣', '_', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', '_', '💣'],
                ['_', '_', '_', '_', '_', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', '_', '💣'],
                ['_', '_', '💣', '_', '_', '_', '_', '💣']
                ]


def test_revelar_casilla_bomba():
    assert revelar_celda(tablero_prueba,1,5) == '💣'

def test_revelar_casilla_vacia():
    assert revelar_celda(tablero_prueba,0,0) == '_'

def test_revelar_casilla_fuera_rango():

    with pytest.raises(IndexError):
        revelar_celda(tablero_prueba,8,8)

