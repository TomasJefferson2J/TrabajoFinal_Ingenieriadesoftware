import tkinter as tk
from tkinter import messagebox
from datetime import date


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
cuadro_grande = tk.Text(ventana_registro_ventas, font=fuente_entry)
cuadro_grande.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Ejecutar la aplicaciónn
ventana_registro_ventas.mainloop()



