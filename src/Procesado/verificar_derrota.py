def verificar_derrota(casilla_seleccionada:str)->bool:
    """
    Comprueba si has perdido la partida, esto sucede cuando la casilla seleccionada
    es una mina
    Parameters
    ----------
    casilla_seleccionada
        La casilla seleccionada por el usuario
    Returns
    -------
        Devuelve si has perdido o no la partida
    """
    derrota = False
    if casilla_seleccionada == "💣":
        derrota = True
    return derrota