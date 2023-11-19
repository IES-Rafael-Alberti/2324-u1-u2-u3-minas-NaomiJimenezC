def escoger_opcion()->str:
    """
    Te permite escoger una opción entre 3 opciones disponibles
    Si se mete alguna otra cosa te pedirá que lo añadas de nuevo
    Returns
    -------
    str
        Devuelve la opción escogida
    """
    opciones_disponibles = ("1","2","3")
    opcion_escogida = input("Escoge alguna de las 3 opciones (1,2 o 3): ")
    while opcion_escogida not in opciones_disponibles:
        opcion_escogida = input("Escoge alguna de las 3 opciones (1,2 o 3): ")
    return opcion_escogida