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

    def apd_logic(apd, acepta_por_stack_vacio, palabra):
        """
        Procesa la palabra y retorna True si es aceptada por stack vacío (si acepta_por_stack_vacio=True)
        o por estado final (si acepta_por_stack_vacio=False).
        """
        apd.reiniciar()
        estado_actual = apd.estado_inicial
        pila = ['Z']  # Cambia 'Z' por el símbolo inicial de tu pila si es necesario
        i = 0
        while i <= len(palabra):
            simbolo_entrada = palabra[i] if i < len(palabra) else None
            tope_pila = pila[-1] if pila else None
            clave = (estado_actual, simbolo_entrada, tope_pila)
            if clave not in apd.transiciones:
                break
            estado_siguiente, cadena_a_apilar = apd.transiciones[clave]
            estado_actual = estado_siguiente
            if pila:
                pila.pop()
            if cadena_a_apilar and cadena_a_apilar != 'None':
                for simbolo in reversed(cadena_a_apilar):
                    pila.append(simbolo)
            i += 1 if simbolo_entrada is not None else 0

        if acepta_por_stack_vacio:
            return len(pila) == 0
        else:
            return estado_actual in apd.estados_finales