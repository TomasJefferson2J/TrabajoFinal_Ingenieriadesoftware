import tkinter as tk
import subprocess

def abrir_resumen_ventas():
    # Lógica para abrir la ventana de Resumen de Ventas
    pass

def abrir_gestionar_productos():
    # Abrir el archivo productos.py
    subprocess.run(["python", "productos.py"])


def abrir_registro_ventas():
    # Lógica para abrir la ventana de Registro de Ventas
    subprocess.run(["python", "registro_de_ventas.py"])
    pass

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
titulo.pack(pady=20)

# Contenedor para los botones
contenedor_botones = tk.Frame(ventana_dashboard, bg=color_fondo)
contenedor_botones.pack(pady=50)

# Botón Resumen de Ventas
boton_resumen_ventas = tk.Button(contenedor_botones, text="Resumen de Ventas", font=("Arial", 18), bg=color_boton, fg="white", command=abrir_resumen_ventas)
boton_resumen_ventas.pack(pady=10, padx=100, ipadx=50)

# Botón Gestionar productos
boton_gestionar_productos = tk.Button(contenedor_botones, text="Gestionar productos", font=("Arial", 18), bg=color_boton, fg="white", command=abrir_gestionar_productos)
boton_gestionar_productos.pack(pady=10, padx=100, ipadx=50)

# Botón Registro de Ventas
boton_registro_ventas = tk.Button(contenedor_botones, text="Registro de Ventas", font=("Arial", 18), bg=color_boton, fg="white", command=abrir_registro_ventas)
boton_registro_ventas.pack(pady=10, padx=100, ipadx=50)

# Botón Gestionar Clientes
boton_gestionar_clientes = tk.Button(contenedor_botones, text="Gestionar Clientes", font=("Arial", 18), bg=color_boton, fg="white", command=abrir_gestionar_clientes)
boton_gestionar_clientes.pack(pady=10, padx=100, ipadx=50)

# Centrar el contenedor de botones en la ventana
contenedor_botones.pack(expand=True, fill=tk.BOTH)

# Ejecutar el bucle principal de la ventana
ventana_dashboard.mainloop()
