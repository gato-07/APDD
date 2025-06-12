# Clase APDD
class APDDeterminista:
    def __init__(self, estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estados_finales, transiciones):
        self.estados = set(estados)
        self.alfabeto_entrada = set(alfabeto_entrada)
        self.alfabeto_pila = set(alfabeto_pila)
        self.estado_inicial = estado_inicial
        self.estados_finales = set(estados_finales)
        self.transiciones = dict(transiciones)
        self.pila = []

    def reiniciar(self):
        self.pila = []

    def __str__(self):
        return (f"Estados: {self.estados}\n"
                f"Alfabeto entrada: {self.alfabeto_entrada}\n"
                f"Alfabeto pila: {self.alfabeto_pila}\n"
                f"Estado inicial: {self.estado_inicial}\n"
                f"Estados de aceptación: {self.estados_finales}\n"
                f"Transiciones: {self.transiciones}\n"
                f"Pila: {self.pila}")

    def construir_apd(estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estados_aceptacion, transiciones):

        apd = APDDeterminista(
            estados,
            alfabeto_entrada,
            alfabeto_pila,
            estado_inicial,
            estados_aceptacion,
            transiciones
        )
        return apd

    def apd_logic(self, acepta_por_stack_vacio, palabra):
        """
        Procesa la palabra y retorna True si es aceptada por pila vacía o por estado final.
        Soporta transiciones epsilon (None) que permiten desapilar sin consumir entrada.
        """
        self.reiniciar()

        estado_actual = self.estado_inicial

        pila = ['R']  # Inicializamos la pila con un símbolo de inicio

        i = 0  # Índice de la palabra

        while True:
            simbolo_entrada = palabra[i] if i < len(palabra) else None
            tope_pila = pila[-1] if pila else None
            clave = (estado_actual, simbolo_entrada, tope_pila)

            if simbolo_entrada is not None and clave in self.transiciones:
                estado_siguiente, cadena_a_apilar = self.transiciones[clave]
                estado_actual = estado_siguiente
                if pila:
                    pila.pop()
                if cadena_a_apilar:
                    for simbolo in reversed(cadena_a_apilar):
                        pila.append(simbolo)
                i += 1  # Avanza porque se consumió un símbolo real
                continue

            # Transición épsilon
            clave_epsilon = (estado_actual, None, tope_pila)
            if clave_epsilon in self.transiciones:
                estado_siguiente, cadena_a_apilar = self.transiciones[clave_epsilon]
                estado_actual = estado_siguiente
                if pila:
                    pila.pop()
                if cadena_a_apilar:
                    for simbolo in reversed(cadena_a_apilar):
                        pila.append(simbolo)
                continue  # Repite en caso de otra épsilon posible

            break  # Ninguna transición válida encontrada

        return len(pila) == 0 if acepta_por_stack_vacio else estado_actual in self.estados_finales
