import tkinter as tk
from tkinter import ttk
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

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("División en tres secciones")
ventana.geometry("800x600")

# Colores de fondo para cada sección
color_negro = "#0D1117"
color_blanco = "#FFFFFF"
color_gris_oscuro = "#24292E"

# Barra de navegación vertical (sección izquierda)
barra_navegacion = tk.Frame(ventana, bg=color_negro, width=200)
barra_navegacion.pack(side=tk.LEFT, fill=tk.Y)

# Calcular el espacio entre los botones
espacio_botones = 30

# Espacio en blanco para separar los botones
espacio_blanco = tk.Frame(barra_navegacion, bg=color_negro, height=20)
espacio_blanco.pack()

# Contenedor de los botones
contenedor_botones = tk.Frame(barra_navegacion, bg=color_negro)
contenedor_botones.pack(pady=espacio_botones)

# Botón Resumen de Ventas
boton_resumen_ventas = ttk.Button(contenedor_botones, text="Resumen de Ventas", style="Boton.TButton", command=abrir_resumen_ventas)
boton_resumen_ventas.pack(pady=espacio_botones)

# Botón Gestionar productos
boton_gestionar_productos = ttk.Button(contenedor_botones, text="Gestionar productos", style="Boton.TButton", command=abrir_gestionar_productos)
boton_gestionar_productos.pack(pady=espacio_botones)

# Botón Registro de Ventas
boton_registro_ventas = ttk.Button(contenedor_botones, text="Registro de Ventas", style="Boton.TButton", command=abrir_registro_ventas)
boton_registro_ventas.pack(pady=espacio_botones)

# Botón Gestionar Clientes
boton_gestionar_clientes = ttk.Button(contenedor_botones, text="Gestionar Clientes", style="Boton.TButton", command=abrir_gestionar_clientes)
boton_gestionar_clientes.pack(pady=espacio_botones)

# Área de contenido principal (sección central)
contenido_principal = tk.Frame(ventana, bg=color_blanco)
contenido_principal.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Barra de navegación horizontal (sección superior dentro del contenido principal)
barra_navegacion_horizontal = tk.Frame(contenido_principal, bg=color_gris_oscuro, height=80)
barra_navegacion_horizontal.pack(fill=tk.X)

# Resto del contenido principal (sección inferior dentro del contenido principal)
contenido_principal_resto = tk.Frame(contenido_principal, bg=color_blanco)
contenido_principal_resto.pack(fill=tk.BOTH, expand=True)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()




