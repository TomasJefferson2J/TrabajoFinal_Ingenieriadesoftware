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

# Contenedor principal
contenedor_principal = tk.Frame(ventana_dashboard, bg=color_fondo)
contenedor_principal.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Parte izquierda - Contenedor para los botones
contenedor_botones = tk.Frame(contenedor_principal, bg=color_fondo)
contenedor_botones.pack(side=tk.LEFT, padx=20)

# Título del panel de control
titulo = tk.Label(contenedor_botones, text="Panel de Control", font=("Arial", 11, "bold"), fg="#1DA1F2", bg=color_fondo)
titulo.pack(pady=(20, 0), anchor="w")  # Alinear a la izquierda (west)
titulo.config(width=15)  # Reducir el ancho del título

# Botón Resumen de Ventas
boton_resumen_ventas = ttk.Button(contenedor_botones, text="Resumen de Ventas", style="Boton.TButton", command=abrir_resumen_ventas)
boton_resumen_ventas.pack(pady=20, ipadx=20, anchor="w")  # Anclar a la izquierda (west)

# Botón Gestionar productos
boton_gestionar_productos = ttk.Button(contenedor_botones, text="Gestionar productos", style="Boton.TButton", command=abrir_gestionar_productos)
boton_gestionar_productos.pack(pady=20, ipadx=20, anchor="w")  # Anclar a la izquierda (west)

# Botón Registro de Ventas
boton_registro_ventas = ttk.Button(contenedor_botones, text="Registro de Ventas", style="Boton.TButton", command=abrir_registro_ventas)
boton_registro_ventas.pack(pady=20, ipadx=20, anchor="w")  # Anclar a la izquierda (west)

# Gestionar Clientes
boton_gestionar_clientes = ttk.Button(contenedor_botones, text="Gestionar Clientes", style="Boton.TButton", command=abrir_gestionar_clientes)
boton_gestionar_clientes.pack(pady=20, ipadx=20, anchor="w")  # Anclar a la izquierda (west)

# Parte central y derecha (se deja para futuras modificaciones)
contenedor_central = tk.Frame(contenedor_principal, bg=color_fondo)
contenedor_central.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Parte superior - Nombre "Loren"
nombre_loren = tk.Label(contenedor_central, text="Loren", font=("Arial", 36, "bold"), fg="#FFFFFF", bg=color_fondo)
nombre_loren.pack(pady=(40, 20))

# Parte inferior - Gráficos
graficos = tk.Frame(contenedor_central, bg="#FFFFFF")
graficos.pack(pady=(0, 20), padx=40, fill=tk.BOTH, expand=True)



# Ejecutar el bucle principal de la ventana
ventana_dashboard.mainloop()






