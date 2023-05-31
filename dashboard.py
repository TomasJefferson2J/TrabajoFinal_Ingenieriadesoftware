import tkinter as tk

def abrir_resumen_ventas():
    # Lógica para abrir la ventana de Resumen de Ventas
    pass

def abrir_gestionar_productos():
    # Lógica para abrir la ventana de Gestionar productos
    pass

def abrir_registro_ventas():
    # Lógica para abrir la ventana de Registro de Ventas
    pass

def abrir_gestionar_clientes():
    # Lógica para abrir la ventana de Gestionar Clientes
    pass

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
contenedor_botones.pack(side=tk.LEFT, fill=tk.Y, padx=20)

# Botón Resumen de Ventas
boton_resumen_ventas = tk.Button(contenedor_botones, text="Resumen de Ventas", font=("Arial", 18), bg=color_boton, fg="white", command=abrir_resumen_ventas)
boton_resumen_ventas.pack(pady=10, padx=20, ipadx=10, ipady=5)

# Botón Gestionar productos
boton_gestionar_productos = tk.Button(contenedor_botones, text="Gestionar productos", font=("Arial", 18), bg=color_boton, fg="white", command=abrir_gestionar_productos)
boton_gestionar_productos.pack(pady=10, padx=20, ipadx=10, ipady=5)

# Botón Registro de Ventas
boton_registro_ventas = tk.Button(contenedor_botones, text="Registro de Ventas", font=("Arial", 18), bg=color_boton, fg="white", command=abrir_registro_ventas)
boton_registro_ventas.pack(pady=10, padx=20, ipadx=10, ipady=5)

# Botón Gestionar Clientes
boton_gestionar_clientes = tk.Button(contenedor_botones, text="Gestionar Clientes", font=("Arial", 18), bg=color_boton, fg="white", command=abrir_gestionar_clientes)
boton_gestionar_clientes.pack(pady=10, padx=20, ipadx=10, ipady=5)

# Separador vertical
separator = tk.Frame(ventana_dashboard, width=2, bg="black")
separator.pack(side=tk.LEFT, fill=tk.Y)

# Contenedor para el contenido principal
contenedor_contenido = tk.Frame(ventana_dashboard, bg=color_fondo)
contenedor_contenido.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=20, pady=20)


# Ejemplo de un Label en el contenido principal
label_contenido = tk.Label(contenedor_contenido, text="Contenido principal", font=("Arial", 18), fg="black", bg=color_fondo)
label_contenido.pack(pady=10)


# Centrar el contenedor de botones en la ventana
contenedor_botones.pack(side=tk.LEFT, fill=tk.Y)

# Ejecutar el bucle principal de la ventana
ventana_dashboard.mainloop()
