import tkinter as tk


def construir_apd(estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estados_aceptacion, transiciones):
    from apdClass import APDDeterminista
    apd = APDDeterminista(
        estados,
        alfabeto_entrada,
        alfabeto_pila,
        estado_inicial,
        estados_aceptacion,
        transiciones
    )
    return apd

# funcion que literalmente recibe un apd xddddd
    # queda logica por implementar
def apd_logic(apd):

    return