import tkinter as tk

def on_button_click():
    print("Button clicked!")

def mainFrame(root):
    print("Main frame initialized.")
    marco = tk.Frame(root, width=1280, height=720, borderwidth=2, relief="groove")
    marco.pack(padx=100, pady=100)

    label = tk.Label(marco, text="Hello World!")
    label.pack(pady=10)

    button = tk.Button(marco, text="Click Me", command=on_button_click)
    button.pack(pady=5)

    return marco

def startGui():
    root = tk.Tk()
    root.title("Determinist Pushdown Automata")
    root.geometry("1280x720")
    mainFrame(root)

    root.mainloop()