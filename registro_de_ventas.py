import tkinter as tk
from tkinter import messagebox
import sqlite3

# Crear la ventana de registro de ventas
ventana_registro_ventas = tk.Tk()
ventana_registro_ventas.title("Registro de Ventas")
ventana_registro_ventas.geometry("800x600")

# Configurar el fondo y estilos
color_fondo = "#1DA1F2"
color_blanco = "white"
fuente_titulo = ("Arial", 24, "bold")
fuente_label = ("Arial", 14)
fuente_entry = ("Arial", 14)
fuente_boton = ("Arial", 14, "bold")

ventana_registro_ventas.configure(bg=color_fondo)


# Función para guardar la venta en la base de datos
def guardar_venta():
    # Obtener los valores ingresados
    cliente = entry_cliente.get()
    producto = entry_producto.get()
    cantidad = entry_cantidad.get()

    # Validar que se ingresen todos los campos
    if cliente == "" or producto == "" or cantidad == "":
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return

    # Validar que la cantidad sea un número entero positivo
    try:
        cantidad = int(cantidad)
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese una cantidad válida.")
        return

    # Conectar a la base de datos
    conexion = sqlite3.connect("ventas.db")
    cursor = conexion.cursor()

    # Insertar la venta en la base de datos
    cursor.execute("INSERT INTO ventas (cliente, producto, cantidad) VALUES (?, ?, ?)", (cliente, producto, cantidad))
    conexion.commit()
    conexion.close()

    # Mostrar mensaje de confirmación
    messagebox.showinfo("Registro de Ventas", "La venta se ha registrado correctamente.")

    # Limpiar los campos de entrada
    entry_cliente.delete(0, tk.END)
    entry_producto.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)


# Título del formulario
titulo = tk.Label(ventana_registro_ventas, text="Registro de Ventas", font=fuente_titulo, fg=color_blanco,
                  bg=color_fondo)
titulo.pack(pady=20)

# Contenedor para el formulario
contenedor_formulario = tk.Frame(ventana_registro_ventas, bg=color_fondo)
contenedor_formulario.pack(pady=50)

# Etiquetas y campos de entrada
label_cliente = tk.Label(contenedor_formulario, text="Cliente:", font=fuente_label, fg=color_blanco, bg=color_fondo)
label_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_cliente = tk.Entry(contenedor_formulario, font=fuente_entry)
entry_cliente.grid(row=0, column=1, padx=10, pady=10)

label_producto = tk.Label(contenedor_formulario, text="Producto:", font=fuente_label, fg=color_blanco, bg=color_fondo)
label_producto.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_producto = tk.Entry(contenedor_formulario, font=fuente_entry)
entry_producto.grid(row=1, column=1, padx=10, pady=10)

label_cantidad = tk.Label(contenedor_formulario, text="Cantidad:", font=fuente_label, fg=color_blanco, bg=color_fondo)
label_cantidad.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_cantidad = tk.Entry(contenedor_formulario, font=fuente_entry)
entry_cantidad.grid(row=2, column=1, padx=10, pady=10)

# Botón para guardar la venta
boton_guardar = tk.Button(contenedor_formulario, text="Guardar", font=fuente_boton, bg=color_blanco, fg=color_fondo, command=guardar_venta)
boton_guardar.grid(row=3, column=1, padx=10, pady=10)

# Centrar el contenedor de formulario en la ventana
contenedor_formulario.pack(expand=True, fill=tk.BOTH)

# Ejecutar el bucle principal de la ventana
ventana_registro_ventas.mainloop()

