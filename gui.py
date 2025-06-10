from functions import *
import tkinter as tk


# Creo que la logica aca esta rebundante pero la dejare asi mientras
def on_construir_apd():
    estados = entry_estados.get().split(',')
    alfabeto_entrada = entry_entrada.get().split(',')
    alfabeto_pila = entry_pila.get().split(',')
    estado_inicial = entry_inicial.get()
    estados_aceptacion = entry_aceptacion.get().split(',')

    # Procesar transiciones
    transiciones = {}
    # Limpiar espacios y saltos de línea
    transiciones_texto = entry_transiciones.get("1.0", tk.END).strip().split('\n')

    for linea in transiciones_texto:

        # Limpiar espacios al inicio y al final de la línea
        if not linea.strip():
            continue
        
        try:
            izquierda, derecha = linea.split('=')
            estado_actual, simbolo_entrada, tope_pila = izquierda.split(',')
            estado_siguiente, cadena_a_apilar = derecha.split(',')
            # Convertir 'None' a None real, por si no hay entrada.
            simbolo_entrada = None if simbolo_entrada == 'None' else simbolo_entrada
            tope_pila = None if tope_pila == 'None' else tope_pila
            transiciones[(estado_actual, simbolo_entrada, tope_pila)] = (estado_siguiente, cadena_a_apilar)
        except Exception as e:
            label_resultado.config(text=f"Error en transición: {linea}")
            return

    try:
        apd = construir_apd(estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estados_aceptacion, transiciones)
        label_resultado.config(text="APDD creado correctamente.")
        apd_logic(apd) # Implementar la lógica del APD aquí, osea en el modulo functions.py
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")

def mainFrame(root):
    marco = tk.Frame(root, width=1200, height=700, borderwidth=3, relief="groove")
    marco.pack(padx=20, pady=20)
    marco.pack_propagate(False)

    # Frame izquierdo
    frame_izq = tk.Frame(marco, width=600, height=700, bg="lightgray")
    frame_izq.grid(row=0, column=0, sticky="nsew")
    frame_izq.pack_propagate(False)

    # Frame derecho
    frame_der = tk.Frame(marco, width=600, height=700, bg="white")
    frame_der.grid(row=0, column=1, sticky="nsew")
    frame_der.pack_propagate(False)

    marco.grid_rowconfigure(0, weight=1)
    marco.grid_columnconfigure(0, weight=1)
    marco.grid_columnconfigure(1, weight=1)

    # Contenido en frame derecho
    global entry_estados, entry_entrada, entry_pila, entry_inicial, entry_aceptacion, entry_transiciones, label_resultado

    tk.Label(frame_der, text="Estados (separados por coma, q0,q1,q2):").pack()
    entry_estados = tk.Entry(frame_der)
    entry_estados.pack()

    tk.Label(frame_der, text="Alfabeto entrada (separados por coma, a,b,c):").pack()
    entry_entrada = tk.Entry(frame_der)
    entry_entrada.pack()

    tk.Label(frame_der, text="Alfabeto pila (separados por coma, A,B,Z):").pack()
    entry_pila = tk.Entry(frame_der)
    entry_pila.pack()

    tk.Label(frame_der, text="Estado inicial:").pack()
    entry_inicial = tk.Entry(frame_der)
    entry_inicial.pack()

    tk.Label(frame_der, text="Estados Finales (separados por coma):").pack()
    entry_aceptacion = tk.Entry(frame_der)
    entry_aceptacion.pack()

    tk.Label(frame_der, text="Transiciones (formato: q0,a,Z=q1,AZ):").pack()
    entry_transiciones = tk.Text(frame_der, height=8, width=40)
    entry_transiciones.pack()

    # Agregar label y campo para la palabra de entrada
    tk.Label(frame_der, text="Palabra de entrada:").pack()
    entry_palabra = tk.Entry(frame_der)
    entry_palabra.pack()

    tk.Button(frame_der, text="Construir APDD", command=on_construir_apd).pack(pady=10)
    label_resultado = tk.Label(frame_der, text="")
    label_resultado.pack()

    # Ejemplo en frame izquierdo
    label_izq = tk.Label(frame_izq, text="Contenido Izquierdo")
    label_izq.pack(pady=10)

    return marco

def startGui():
    root = tk.Tk()
    root.title("Determinist Pushdown Automata")
    root.geometry("1280x720")
    mainFrame(root)
    root.mainloop()