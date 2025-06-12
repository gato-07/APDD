from apdClass import *
import tkinter as tk


def on_construir_apd():

    # Dado que las variables se definieron como Global, se pueden usar directamente
        # Limpiamos las cadenas de entrada
    estados = entry_estados.get().split(',')
    alfabeto_entrada = entry_entrada.get().split(',')
    alfabeto_pila = entry_pila.get().split(',')
    estado_inicial = entry_inicial.get()
    estados_aceptacion = entry_aceptacion.get().split(',')

    acepta_por_stack_vacio = accept_by_empty_stack_var.get()
    palabra = entry_palabra.get()

    transiciones = {}
    transiciones_texto = entry_transiciones.get("1.0", tk.END).strip().split('\n')

    for linea in transiciones_texto:
        if not linea.strip():
            continue
        try:
            izquierda, derecha = linea.split('=', 1)
            estado_actual, simbolo_entrada, tope_pila = izquierda.split(',')
            estado_siguiente, cadena_a_apilar = derecha.split(',')

            # Conversión para 'eps'
            simbolo_entrada = None if simbolo_entrada.strip() == 'eps' else simbolo_entrada.strip()
            tope_pila = None if tope_pila.strip() == 'eps' else tope_pila.strip()
            cadena_a_apilar = '' if cadena_a_apilar.strip() == 'eps' else cadena_a_apilar.strip()
            transiciones[(estado_actual, simbolo_entrada, tope_pila)] = (estado_siguiente, cadena_a_apilar)
        except Exception as e:
            label_resultado.config(text=f"Error en transición: {linea}")
            label_output_status.config(text="Error", bg="orange")
            return

    try:
        apd = APDDeterminista(
            estados,
            alfabeto_entrada,
            alfabeto_pila,
            estado_inicial,
            estados_aceptacion,
            transiciones
        )
        aceptada = apd.apd_logic(acepta_por_stack_vacio, palabra)
        texto_aceptacion = "ACEPTADA" if aceptada else "NO ACEPTADA"
        texto_output = (
            "=== DATOS DE ENTRADA ===\n"
            f"Estados: {', '.join(estados)}\n"
            f"Alfabeto de entrada: {', '.join(alfabeto_entrada)}\n"
            f"Alfabeto de pila: {', '.join(alfabeto_pila)}\n"
            f"Estado inicial: {estado_inicial}\n"
            f"Estados de aceptación: {', '.join(estados_aceptacion)}\n"
            f"Acepta por stack vacío: {'Sí' if acepta_por_stack_vacio else 'No'}\n"
            f"Palabra de entrada: {palabra}\n"
            f"Transiciones:\n"
        )
        for k, v in transiciones.items():
            texto_output += f"  {k} -> {v}\n"
        texto_output += f"\n=== RESULTADO ===\nPalabra {texto_aceptacion}"
        label_resultado.config(text=texto_output, justify="left", anchor="w")
        # Actualizar el frame izquierdo con el resultado
        if aceptada:
            label_output_status.config(text="ACEPTADA", bg="lightgreen")
        else:
            label_output_status.config(text="NO ACEPTADA", bg="tomato") #lol
        label_output_word.config(text=f"Palabra: {palabra}")
    except Exception as e:
        label_resultado.config(text=f"Error: {e}")
        label_output_status.config(text="Error", bg="orange")

def mainFrame(root):
    marco = tk.Frame(root, width=1620, height=900, borderwidth=3, relief="groove")
    marco.pack(padx=20, pady=20)
    marco.pack_propagate(False)

    # Frame izquierdo
    frame_izq = tk.Frame(marco, width=810, height=900, bg="lightgray")
    frame_izq.grid(row=0, column=0, sticky="nsew")
    frame_izq.pack_propagate(False)

    # Frame derecho
    frame_der = tk.Frame(marco, width=810, height=900, bg="white")
    frame_der.grid(row=0, column=1, sticky="nsew")
    frame_der.pack_propagate(False)

    marco.grid_rowconfigure(0, weight=1)
    marco.grid_columnconfigure(0, weight=1)
    marco.grid_columnconfigure(1, weight=1)

    # Contenido en frame derecho
    global entry_estados, entry_entrada, entry_pila, entry_inicial, entry_aceptacion, entry_transiciones, label_resultado, entry_palabra
    global accept_by_empty_stack_var
    global label_output_status, label_output_word

    label_font = ("Arial", 16)
    entry_font = ("Arial", 16)

    tk.Label(frame_der, text="Estados (separados por coma, q0,q1,q2):", font=label_font).pack()
    entry_estados = tk.Entry(frame_der, font=entry_font)
    entry_estados.pack()

    tk.Label(frame_der, text="Alfabeto entrada (separados por coma, a,b,c):", font=label_font).pack()
    entry_entrada = tk.Entry(frame_der, font=entry_font)
    entry_entrada.pack()

    tk.Label(frame_der, text="Alfabeto pila (separados por coma, A,B,R):", font=label_font).pack()
    entry_pila = tk.Entry(frame_der, font=entry_font)
    entry_pila.pack()

    tk.Label(frame_der, text="Estado inicial:", font=label_font).pack()
    entry_inicial = tk.Entry(frame_der, font=entry_font)
    entry_inicial.pack()

    tk.Label(frame_der, text="Estados Finales (separados por coma):", font=label_font).pack()
    entry_aceptacion = tk.Entry(frame_der, font=entry_font)
    entry_aceptacion.pack()

    tk.Label(frame_der, text="Transiciones (formato: q0,a,Z=q1,AR), dejar vacio para quitar del stack, ej: q0,a,R=q1,", font=label_font).pack()
    entry_transiciones = tk.Text(frame_der, height=8, width=50, font=entry_font)
    entry_transiciones.pack()

    # Checkbox para aceptar por stack vacío
    accept_by_empty_stack_var = tk.BooleanVar()
    check_stack_vacio = tk.Checkbutton(frame_der, text="Aceptar por stack vacío", variable=accept_by_empty_stack_var, font=label_font)
    check_stack_vacio.pack()

    # Agregar label y campo para la palabra de entrada
    tk.Label(frame_der, text="Palabra de entrada:", font=label_font).pack()
    entry_palabra = tk.Entry(frame_der, font=entry_font)
    entry_palabra.pack()

    tk.Button(frame_der, text="Construir APDD", command=on_construir_apd, font=label_font).pack(pady=10)
    label_resultado = tk.Label(frame_der, text="", justify="left", anchor="w", bg="#f0f0f0", width=60, height=18, font=("Arial", 14))
    label_resultado.pack(pady=10, fill="both", expand=True)

    # Output en frame izquierdo
    tk.Label(frame_izq, text="Resultado de la palabra:", bg="lightgray", font=("Arial", 20, "bold")).pack(pady=(30,10))
    label_output_status = tk.Label(frame_izq, text="Esperando...", bg="lightgray", font=("Arial", 28, "bold"), width=20)
    label_output_status.pack(pady=10)
    label_output_word = tk.Label(frame_izq, text="Palabra: ", bg="lightgray", font=("Arial", 18), width=40)
    label_output_word.pack(pady=10)

    return marco

def startGui():
    root = tk.Tk()
    root.title("Determinist Pushdown Automata Simulator")
    root.geometry("1620x900")
    root.resizable(True, True)
    mainFrame(root)
    root.mainloop()