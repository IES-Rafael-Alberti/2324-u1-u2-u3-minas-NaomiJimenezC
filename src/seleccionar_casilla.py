import re
def seleccionar_casilla()->tuple:
    """
    Se encarga de recoger las coordenadas por consola.
    Se usan expresiones regulares para asegurar el formato

    Returns
    -------
    tuple
        Se devuelve una tupla con las coordenaadas introducidas por el usuario.
    """
    formato_casilla_incorrecto = False
    while formato_casilla_incorrecto != True:
        casilla_seleccionada = input("Ingrese las coordenadas de la siguiente manera (fila,columna): ")
        formato_coodenadas = "\d{1},\d{1}"
        try:
            if re.match(formato_coodenadas,casilla_seleccionada):
                return tuple(map(int,casilla_seleccionada.split(",")))
        except:
            pass