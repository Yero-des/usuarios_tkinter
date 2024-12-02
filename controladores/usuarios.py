import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

def inicializar_db():
  conn = sqlite3.connect('usuarios.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      nombre TEXT NOT NULL,
      edad INTEGER NOT NULL
    )
  ''')
  conn.commit()
  conn.close()

def cargar_usuarios(tree):

  for fila in tree.get_children():
    tree.delete(fila)

  conn = sqlite3.connect('usuarios.db')
  cursor = conn.cursor()
  cursor.execute('SELECT * FROM usuarios')
  for usuario in cursor.fetchall():
    tree.insert('', tk.END, values=usuario)
  conn.close()

def agregar_usuario(nombre, edad, entry_nombre, entry_edad, cargar_usuarios):

  nombre = entry_nombre.get()
  edad = entry_edad.get()

  if not nombre or not edad.isdigit():
    messagebox.showerror("Error", "Por favor, ingrese datos validos")

  conn = sqlite3.connect('usuarios.db')
  cursor = conn.cursor()
  cursor.execute('INSERT INTO usuarios (nombre, edad) VALUES (?, ?)', (nombre, int(edad)))
  conn.commit()
  conn.close()

  entry_nombre.delete(0, tk.END)
  entry_edad.delete(0, tk.END)

  cargar_usuarios()
  messagebox.showinfo("Éxito", "Usuario agregado exitosamente")

def eliminar_usuario(tree, cargar_usuarios):
  seleccion = tree.selection()

  if not seleccion:
    messagebox.showerror("Error", "Seleccione un usuario para eliminar")
    return
  
  usuario_id = tree.item(seleccion[0])['values'][0]

  conn = sqlite3.connect('usuarios.db')
  cursor = conn.cursor()
  cursor.execute('DELETE FROM usuarios WHERE id = ?', (usuario_id,))
  conn.commit()
  conn.close()

  cargar_usuarios()
  messagebox.showinfo("Éxito", "Usuario eliminado exitosamente")

def actualizar_usuario(tree, nombre, edad, entry_nombre, entry_edad, cargar_usuarios):
  seleccion = tree.selection()
  
  if not seleccion:
    messagebox.showerror("Error", "Selecciones un usuario para actualizar")
    return
  
  usuario_id = tree.item(seleccion[0])['values'][0]

  if not nombre or not edad.isdigit():
    messagebox.showerror("Error", "Por favor, ingrese datos válidos")
    return

  conn = sqlite3.connect('usuarios.db')
  cursor = conn.cursor()
  cursor.execute('UPDATE usuarios SET nombre = ?, edad = ? WHERE id = ?', (
    nombre,
    int(edad),
    usuario_id
  ))
  conn.commit()
  conn.close()

  entry_nombre.delete(0, "end")
  entry_edad.delete(0, "end")
  cargar_usuarios()
  messagebox.showinfo("Éxito", "Usuario actualizado exitosamente")