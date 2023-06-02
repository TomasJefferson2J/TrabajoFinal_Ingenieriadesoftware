import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import subprocess

def abrir_resumen_ventas():
    # Lógica para abrir la ventana de Resumen de Ventas
    subprocess.run(["python", "abrir_resumen_de_ventas.py"])

def abrir_gestionar_productos():
    # Abrir el archivo productos.py
    subprocess.run(["python", "productos.py"])

def abrir_registro_ventas():
    # Lógica para abrir la ventana de Registro de Ventas
    subprocess.run(["python", "registro_de_ventas.py"])

def abrir_gestionar_clientes():
    # Abrir el archivo clientes.py
    subprocess.run(["python", "clientes.py"])

# Crear la ventana principal del dashboard
ventana_dashboard = tk.Tk()
ventana_dashboard.title("Panel de Control - Sistema de Ventas")
ventana_dashboard.geometry("800x600")

# Configurar el fondo y estilos
color_fondo = "#F5F5F5"
color_boton = "#1DA1F2"
fuente_titulo = ("Arial", 24, "bold")

ventana_dashboard.configure(bg=color_fondo)




# Título del panel de control
titulo = tk.Label(ventana_dashboard, text="Panel de Control", font=fuente_titulo, fg="#1DA1F2", bg=color_fondo)
titulo.pack(pady=(20, 0), padx=20, anchor="w")  # Alinear a la izquierda (west)

# Contenedor para los botones
contenedor_botones = tk.Frame(ventana_dashboard, bg=color_fondo)
contenedor_botones.pack(pady=(10, 50), padx=20, anchor="w")  # Alinear a la izquierda (west)

# Botón Resumen de Ventas
boton_resumen_ventas = ttk.Button(contenedor_botones, text="Resumen de Ventas", style="Boton.TButton", command=abrir_resumen_ventas)
boton_resumen_ventas.pack(pady=10, ipadx=20, anchor="w")  # Anclar a la izquierda (west)

# Botón Gestionar productos
boton_gestionar_productos = ttk.Button(contenedor_botones, text="Gestionar productos", style="Boton.TButton", command=abrir_gestionar_productos)
boton_gestionar_productos.pack(pady=10, ipadx=20, anchor="w")  # Anclar a la izquierda (west)

# Botón Registro de Ventas
boton_registro_ventas = ttk.Button(contenedor_botones, text="Registro de Ventas", style="Boton.TButton", command=abrir_registro_ventas)
boton_registro_ventas.pack(pady=10, ipadx=20, anchor="w")  # Anclar a la izquierda (west)

# Gestionar Clientes
boton_gestionar_clientes = ttk.Button(contenedor_botones, text="Gestionar Clientes", style="Boton.TButton", command=abrir_gestionar_clientes)
boton_gestionar_clientes.pack(pady=10, ipadx=20, anchor="w")  # Anclar a la izquierda (west)


# Ejecutar el bucle principal de la ventana
ventana_dashboard.mainloop()




