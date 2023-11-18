def verificar_victoria(casillas_restantes:int)->bool:
    """
    Comprueba si has ganado la partida mediante contar que no queden más celdas vacias
    Parameters
    ----------
    casillas_restantes
        Casillas que no sean minas restantes para ganar la partida
    Returns
    -------
        Devuelve si has ganado o no la partida
    """
    victoria = False
    if casillas_restantes == 0:
        victoria = True
    return victoria