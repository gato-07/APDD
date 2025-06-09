
# Clase APDD
class APDDeterminista:
    def __init__(self, estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estados_aceptacion, transiciones):
        self.estados = set(estados)
        self.alfabeto_entrada = set(alfabeto_entrada)
        self.alfabeto_pila = set(alfabeto_pila)
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = set(estados_aceptacion)
        self.transiciones = dict(transiciones)
        self.pila = []

    def reiniciar(self):
        self.pila = []

    def __str__(self):
        return (f"Estados: {self.estados}\n"
                f"Alfabeto entrada: {self.alfabeto_entrada}\n"
                f"Alfabeto pila: {self.alfabeto_pila}\n"
                f"Estado inicial: {self.estado_inicial}\n"
                f"Estados de aceptación: {self.estados_aceptacion}\n"
                f"Transiciones: {self.transiciones}\n"
                f"Pila: {self.pila}")
