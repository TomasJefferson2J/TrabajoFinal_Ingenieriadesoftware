import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from datetime import date

# Variable para almacenar los datos de las ventas
datos_ventas = []

def guardar_venta():
    cliente = entry_cliente.get()
    producto = entry_producto.get()
    cantidad = entry_cantidad.get()

    if cliente == "" or producto == "" or cantidad == "":
        messagebox.showerror("Error", "Por favor, completa todos los campos.")
    else:
        # Aquí puedes agregar la lógica para guardar la venta en la base de datos
        messagebox.showinfo("Registro de Ventas", "Venta registrada correctamente.")
        entry_cliente.delete(0, tk.END)
        entry_producto.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)

        # Añadir los datos de la venta a la lista
        datos_venta = (producto, cantidad, "...", "...", "...")
        datos_ventas.append(datos_venta)

        # Actualizar el cuadro grande con los nuevos datos
        actualizar_cuadro_grande()

def actualizar_cuadro_grande():
    # Eliminar todas las etiquetas del cuadro grande
    for widget in cuadro_grande.winfo_children():
        widget.destroy()

    # Encabezados de la tabla
    encabezados = ["Producto", "Cantidad", "Precio", "Descuento", "Precio Total"]
    for col, encabezado in enumerate(encabezados):
        label_encabezado = tk.Label(cuadro_grande, text=encabezado, font=fuente_entry, anchor="w", width=15, bg="white", padx=5)
        label_encabezado.grid(row=0, column=col)
        if col > 0:
            separator = ttk.Separator(cuadro_grande, orient="vertical")
            separator.grid(row=0, column=col, sticky="ns")

    # Datos de las ventas
    for i, datos_venta in enumerate(datos_ventas):
        producto_valor = tk.Label(cuadro_grande, text=datos_venta[0], font=fuente_entry, anchor="w", width=20)
        producto_valor.grid(row=i+1, column=0)
        cantidad_valor = tk.Label(cuadro_grande, text=datos_venta[1], font=fuente_entry, anchor="w", width=10)
        cantidad_valor.grid(row=i+1, column=1)
        precio_valor = tk.Label(cuadro_grande, text=datos_venta[2], font=fuente_entry, anchor="w", width=10)
        precio_valor.grid(row=i+1, column=2)
        descuento_valor = tk.Label(cuadro_grande, text=datos_venta[3], font=fuente_entry, anchor="w", width=10)
        descuento_valor.grid(row=i+1, column=3)
        precio_total_valor = tk.Label(cuadro_grande, text=datos_venta[4], font=fuente_entry, anchor="w", width=10)
        precio_total_valor.grid(row=i+1, column=4)

# Crear la ventana de registro de ventas
ventana_registro_ventas = tk.Tk()
ventana_registro_ventas.title("Registro de Ventas")
ventana_registro_ventas.geometry("600x400")

# Configurar estilos
fuente_titulo = ("Arial", 24, "bold")
fuente_label = ("Arial", 14)
fuente_entry = ("Arial", 14)
fuente_boton = ("Arial", 14)

# Título del registro de ventas
titulo = tk.Label(ventana_registro_ventas, text="Registro de Ventas", font=fuente_titulo)
titulo.pack(pady=20)

# Contenedor para el formulario
contenedor_formulario = tk.Frame(ventana_registro_ventas)

# Label y Entry para el campo Cliente
label_cliente = tk.Label(contenedor_formulario, text="Cliente:", font=fuente_label)
label_cliente.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_cliente = tk.Entry(contenedor_formulario, font=fuente_entry)
entry_cliente.grid(row=0, column=1, padx=10, pady=10)

# Label y Entry para el campo Producto
label_producto = tk.Label(contenedor_formulario, text="Producto:", font=fuente_label)
label_producto.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_producto = tk.Entry(contenedor_formulario, font=fuente_entry)
entry_producto.grid(row=1, column=1, padx=10, pady=10)

# Label y Entry para el campo Cantidad
label_cantidad = tk.Label(contenedor_formulario, text="Cantidad:", font=fuente_label)
label_cantidad.grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_cantidad = tk.Entry(contenedor_formulario, font=fuente_entry)
entry_cantidad.grid(row=2, column=1, padx=10, pady=10)

# Label para la fecha
fecha_actual = date.today().strftime("%d/%m/%Y")
label_fecha = tk.Label(contenedor_formulario, text="Fecha:", font=fuente_label)
label_fecha.grid(row=3, column=0, padx=10, pady=10, sticky="e")
label_fecha_valor = tk.Label(contenedor_formulario, text=fecha_actual, font=fuente_entry)
label_fecha_valor.grid(row=3, column=1, padx=10, pady=10, sticky="w")

# Botón para guardar la venta
boton_registrar = tk.Button(contenedor_formulario, text="Registrar", font=fuente_boton, bg="#4CAF50", fg="white", command=guardar_venta)
boton_registrar.grid(row=4, column=0, padx=10, pady=10, sticky="w")

# Botón para cancelar
boton_cancelar = tk.Button(contenedor_formulario, text="Cancelar", font=fuente_boton, bg="#FF0000", fg="white", command=ventana_registro_ventas.quit)
boton_cancelar.grid(row=4, column=1, padx=10, pady=10, sticky="e")

# Agregar el contenedor del formulario a la ventana principal
contenedor_formulario.pack()

# Cuadro grande
cuadro_grande = tk.Frame(ventana_registro_ventas, bg="white", relief="solid", borderwidth=1)
cuadro_grande.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Encabezados de la tabla
encabezados = ["Producto", "Cantidad", "Precio", "Descuento", "Precio Total"]
for col, encabezado in enumerate(encabezados):
    label_encabezado = tk.Label(cuadro_grande, text=encabezado, font=fuente_entry, anchor="w", width=15, bg="white", padx=5)
    label_encabezado.grid(row=0, column=col)
    if col > 0:
        separator = ttk.Separator(cuadro_grande, orient="vertical")
        separator.grid(row=0, column=col, sticky="ns")

# Ejecutar la aplicación
ventana_registro_ventas.mainloop()








