import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox
from controladores.usuarios import *

def centrar_ventana(ventana, ancho, alto):
  screen_width = ventana.winfo_screenwidth()
  screen_height = ventana.winfo_screenheight()
  x = (screen_width - ancho) // 2
  y = (screen_height - alto) // 2
  ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

inicializar_db()
root = tk.Tk()
root.title("Gestión de Usuarios")
root.resizable(False, False)
centrar_ventana(root, 500, 400)

# Inputs
frame_form = tk.Frame(root)
frame_form.pack(pady=10)

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_form)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Edad:").grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(frame_form)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

# Botones
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_agregar = tk.Button(
  frame_buttons, 
  text="Agregar", 
  command=lambda: agregar_usuario(entry_nombre.get(), entry_edad.get(), entry_nombre, entry_edad, lambda: cargar_usuarios(tree))
)
btn_agregar.grid(row=0, column=0, padx=5)

btn_eliminar = tk.Button(
  frame_buttons, 
  text="Eliminar", 
  command=lambda: eliminar_usuario(tree, lambda: cargar_usuarios(tree))
)
btn_eliminar.grid(row=0, column=2, padx=5)

# Tabla de usuarios
frame_table = tk.Frame(root)
frame_table.pack(pady=10)

columns = ("ID", "Nombre", "Edad")
tree = ttk.Treeview(frame_table, columns=columns, show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre") 
tree.heading("Edad", text="Edad")

tree.column("ID", width=50)
tree.column("Nombre", width=150)
tree.column("Edad", width=50)

tree.pack()

cargar_usuarios(tree)

root.mainloop()