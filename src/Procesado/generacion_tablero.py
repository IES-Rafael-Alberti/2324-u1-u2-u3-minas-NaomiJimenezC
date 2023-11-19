def generar_tablero() -> list:
    """Busca generar un tablero en el que se pueda añadir y seleccionar minas

    Returns
    -------
    list
        Devuelve una matriz que será la simulación del tablero
    """

    tablero: list = [
        ["•", "•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•", "•"],
        ["•", "•", "•", "•", "•", "•", "•", "•"]
    ]

    return tablero
