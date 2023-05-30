import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# Función para abrir la ventana de agregar producto
def abrir_ventana_agregar_producto():
    def guardar_producto():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        categoria = seleccion_categoria.get()

        if nombre and precio and cantidad and categoria:
            # Realizar la lógica para guardar el producto en la base de datos
            # ...

            messagebox.showinfo("Éxito", "El producto se ha agregado correctamente.")
            ventana_agregar_producto.destroy()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    ventana_agregar_producto = tk.Toplevel(ventana_productos)
    ventana_agregar_producto.title("Agregar Producto")
    ventana_agregar_producto.geometry("400x300")

    contenedor_principal = tk.Frame(ventana_agregar_producto)
    contenedor_principal.pack(padx=20, pady=20)

    label_nombre = tk.Label(contenedor_principal, text="Nombre del producto:")
    label_nombre.grid(row=0, column=0, sticky="w")

    entry_nombre = tk.Entry(contenedor_principal)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    label_precio = tk.Label(contenedor_principal, text="Precio:")
    label_precio.grid(row=1, column=0, sticky="w")

    entry_precio = tk.Entry(contenedor_principal)
    entry_precio.grid(row=1, column=1, padx=10, pady=5)

    label_cantidad = tk.Label(contenedor_principal, text="Cantidad:")
    label_cantidad.grid(row=2, column=0, sticky="w")

    entry_cantidad = tk.Entry(contenedor_principal)
    entry_cantidad.grid(row=2, column=1, padx=10, pady=5)

    label_categoria = tk.Label(contenedor_principal, text="Categoría:")
    label_categoria.grid(row=3, column=0, sticky="w")

    opciones_categoria = ["Categoría 1", "Categoría 2", "Categoría 3"]
    seleccion_categoria = tk.StringVar()
    dropdown_categoria = tk.OptionMenu(contenedor_principal, seleccion_categoria, *opciones_categoria)
    dropdown_categoria.grid(row=3, column=1, padx=10, pady=5)

    boton_buscar_imagen = tk.Button(contenedor_principal, text="Buscar imagen")
    boton_buscar_imagen.grid(row=4, column=0, columnspan=2, pady=10)

    contenedor_botones = tk.Frame(ventana_agregar_producto)
    contenedor_botones.pack()

    boton_guardar = tk.Button(contenedor_botones, text="Guardar", width=10, command=guardar_producto)
    boton_guardar.pack(side="left", padx=5, pady=10)

    boton_cancelar = tk.Button(contenedor_botones, text="Cancelar", width=10, command=ventana_agregar_producto.destroy)
    boton_cancelar.pack(side="left", padx=5, pady=10)

    ventana_agregar_producto.mainloop()
    pass

# Función para abrir la ventana de actualizar producto
def abrir_ventana_actualizar_producto():
    def actualizar_producto():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        categoria = seleccion_categoria.get()

        if nombre and precio and cantidad and categoria:
            # Realizar la lógica para actualizar el producto en la base de datos
            # ...

            messagebox.showinfo("Éxito", "El producto se ha actualizado correctamente.")
            ventana_agregar_producto.destroy()
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def eliminar_producto():
        # Realizar la lógica para eliminar el producto de la base de datos
        # ...

        messagebox.showinfo("Éxito", "El producto se ha eliminado correctamente.")
        ventana_agregar_producto.destroy()

    # Crear la ventana de agregar/actualizar producto
    ventana_agregar_producto = tk.Toplevel(ventana_productos)
    ventana_agregar_producto.title("Actualizar Producto")
    ventana_agregar_producto.geometry("400x300")

    contenedor_principal = tk.Frame(ventana_agregar_producto)
    contenedor_principal.pack(padx=20, pady=20)

    label_nombre = tk.Label(contenedor_principal, text="Nombre del producto:")
    label_nombre.grid(row=0, column=0, sticky="w")

    entry_nombre = tk.Entry(contenedor_principal)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    label_precio = tk.Label(contenedor_principal, text="Precio:")
    label_precio.grid(row=1, column=0, sticky="w")

    entry_precio = tk.Entry(contenedor_principal)
    entry_precio.grid(row=1, column=1, padx=10, pady=5)

    label_cantidad = tk.Label(contenedor_principal, text="Cantidad:")
    label_cantidad.grid(row=2, column=0, sticky="w")

    entry_cantidad = tk.Entry(contenedor_principal)
    entry_cantidad.grid(row=2, column=1, padx=10, pady=5)

    label_categoria = tk.Label(contenedor_principal, text="Categoría:")
    label_categoria.grid(row=3, column=0, sticky="w")

    opciones_categoria = ["Categoría 1", "Categoría 2", "Categoría 3"]
    seleccion_categoria = tk.StringVar()
    dropdown_categoria = tk.OptionMenu(contenedor_principal, seleccion_categoria, *opciones_categoria)
    dropdown_categoria.grid(row=3, column=1, padx=10, pady=5)

    boton_buscar_imagen = tk.Button(contenedor_principal, text="Buscar imagen")
    boton_buscar_imagen.grid(row=4, column=0, columnspan=2, pady=10)

    contenedor_botones = tk.Frame(ventana_agregar_producto)
    contenedor_botones.pack()

    boton_guardar = tk.Button(contenedor_botones, text="Actualizar", width=10, command=actualizar_producto)
    boton_guardar.pack(side="left", padx=5, pady=10)

    boton_eliminar = tk.Button(contenedor_botones, text="Eliminar", width=10, command=eliminar_producto)
    boton_eliminar.pack(side="left", padx=5, pady=10)

    ventana_agregar_producto.mainloop()
    pass

# Función para abrir la ventana de eliminar producto
def abrir_ventana_eliminar_producto():
    def eliminar_producto():
        # Obtener los valores del producto a eliminar
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        categoria = seleccion_categoria.get()

        # Validar los campos de entrada
        if nombre and precio and cantidad and categoria:
            # Realizar la lógica para eliminar el producto de la base de datos
            # ...

            # Mostrar mensaje de éxito
            tk.messagebox.showinfo("Éxito", "El producto se ha eliminado correctamente.")

            # Cerrar la ventana de eliminar producto
            ventana_eliminar_producto.destroy()
        else:
            # Mostrar mensaje de error
            tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")

        # Crear la ventana de eliminar producto

    ventana_eliminar_producto = tk.Toplevel(ventana_productos)
    ventana_eliminar_producto.title("Eliminar Producto")
    ventana_eliminar_producto.geometry("400x300")

    # Contenedor principal
    contenedor_principal = tk.Frame(ventana_eliminar_producto)
    contenedor_principal.pack(padx=20, pady=20)

    # Etiqueta "Nombre del producto"
    label_nombre = tk.Label(contenedor_principal, text="Nombre del producto:")
    label_nombre.grid(row=0, column=0, sticky="w")

    # Cuadro de entrada para el nombre del producto
    entry_nombre = tk.Entry(contenedor_principal)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    # Etiqueta "Precio"
    label_precio = tk.Label(contenedor_principal, text="Precio:")
    label_precio.grid(row=1, column=0, sticky="w")

    # Cuadro de entrada para el precio
    entry_precio = tk.Entry(contenedor_principal)
    entry_precio.grid(row=1, column=1, padx=10, pady=5)

    # Etiqueta "Cantidad"
    label_cantidad = tk.Label(contenedor_principal, text="Cantidad:")
    label_cantidad.grid(row=2, column=0, sticky="w")

    # Cuadro de entrada para la cantidad
    entry_cantidad = tk.Entry(contenedor_principal)
    entry_cantidad.grid(row=2, column=1, padx=10, pady=5)

    # Etiqueta "Categoría"
    label_categoria = tk.Label(contenedor_principal, text="Categoría:")
    label_categoria.grid(row=3, column=0, sticky="w")

    # Menú desplegable para seleccionar la categoría
    opciones_categoria = ["Categoría 1", "Categoría 2", "Categoría 3"]  # Ejemplo de opciones de categoría
    seleccion_categoria = tk.StringVar()
    dropdown_categoria = tk.OptionMenu(contenedor_principal, seleccion_categoria, *opciones_categoria)
    dropdown_categoria.grid(row=3, column=1, padx=10, pady=5)

    # Contenedor para los botones
    contenedor_botones = tk.Frame(ventana_eliminar_producto)
    contenedor_botones.pack()

    # Botón "Eliminar"
    boton_eliminar = tk.Button(contenedor_botones, text="Eliminar", width=10, command=eliminar_producto)
    boton_eliminar.pack(side="left", padx=5, pady=10)

    # Botón "Cancelar"
    boton_cancelar = tk.Button(contenedor_botones, text="Cancelar", width=10, command=ventana_eliminar_producto.destroy)
    boton_cancelar.pack(side="left", padx=5, pady=10)

    # Ejecutar el bucle principal de la ventana de eliminar producto
    ventana_eliminar_producto.mainloop()
    pass

# Función para abrir la ventana de buscar producto
def abrir_ventana_buscar_producto():
    # Función para buscar un producto en la base de datos
    def buscar_producto():
        # Obtener el valor ingresado por el usuario
        nombre_producto = entry_buscar.get()

        # Realizar la lógica de búsqueda en la base de datos
        # ...

        # Mostrar los resultados en una ventana emergente o en la consola
        # ...

    # Crear la ventana de buscar producto
    ventana_buscar_producto = tk.Toplevel(ventana_productos)
    ventana_buscar_producto.title("Buscar Producto")
    ventana_buscar_producto.geometry("400x300")

    # Contenedor principal
    contenedor_principal = tk.Frame(ventana_buscar_producto)
    contenedor_principal.pack(padx=20, pady=20)

    # Etiqueta "Buscar producto"
    label_buscar = tk.Label(contenedor_principal, text="Buscar producto:")
    label_buscar.grid(row=0, column=0, sticky="w")

    # Cuadro de entrada para buscar el producto
    entry_buscar = tk.Entry(contenedor_principal)
    entry_buscar.grid(row=0, column=1, padx=10, pady=5)

    # Contenedor para los botones
    contenedor_botones = tk.Frame(ventana_buscar_producto)
    contenedor_botones.pack()

    # Botón "Buscar"
    boton_buscar = tk.Button(contenedor_botones, text="Buscar", width=10, command=buscar_producto)
    boton_buscar.pack(side="left", padx=5, pady=10)

    # Botón "Cancelar"
    boton_cancelar = tk.Button(contenedor_botones, text="Cancelar", width=10, command=ventana_buscar_producto.destroy)
    boton_cancelar.pack(side="left", padx=5, pady=10)

    # Ejecutar el bucle principal de la ventana de buscar producto
    ventana_buscar_producto.mainloop()
    pass

# Función para generar informe de producto
def generar_informe_producto():
    def generar_informe():
        # Obtener los valores ingresados por el usuario
        nombre = entry_nombre.get()
        categoria = seleccion_categoria.get()

        # Validar los campos de entrada
        if nombre and categoria:
            # Realizar la lógica para generar el informe del producto
            # ...

            # Mostrar mensaje de éxito
            tk.messagebox.showinfo("Éxito", "El informe del producto se ha generado correctamente.")

            # Cerrar la ventana de generar informe del producto
            ventana_generar_informe_producto.destroy()
        else:
            # Mostrar mensaje de error
            tk.messagebox.showerror("Error", "Por favor, complete todos los campos.")

    # Crear la ventana de generar informe del producto
    ventana_generar_informe_producto = tk.Toplevel(ventana_productos)
    ventana_generar_informe_producto.title("Generar Informe del Producto")
    ventana_generar_informe_producto.geometry("400x200")

    # Contenedor principal
    contenedor_principal = tk.Frame(ventana_generar_informe_producto)
    contenedor_principal.pack(padx=20, pady=20)

    # Etiqueta "Nombre del producto"
    label_nombre = tk.Label(contenedor_principal, text="Nombre del producto:")
    label_nombre.grid(row=0, column=0, sticky="w")

    # Cuadro de entrada para el nombre del producto
    entry_nombre = tk.Entry(contenedor_principal)
    entry_nombre.grid(row=0, column=1, padx=10, pady=5)

    # Etiqueta "Categoría"
    label_categoria = tk.Label(contenedor_principal, text="Categoría:")
    label_categoria.grid(row=1, column=0, sticky="w")

    # Menú desplegable para seleccionar la categoría
    opciones_categoria = ["Categoría 1", "Categoría 2", "Categoría 3"]  # Ejemplo de opciones de categoría
    seleccion_categoria = tk.StringVar()
    dropdown_categoria = tk.OptionMenu(contenedor_principal, seleccion_categoria, *opciones_categoria)
    dropdown_categoria.grid(row=1, column=1, padx=10, pady=5)

    # Contenedor para los botones
    contenedor_botones = tk.Frame(ventana_generar_informe_producto)
    contenedor_botones.pack()

    # Botón "Generar Informe"
    boton_generar_informe = tk.Button(contenedor_botones, text="Generar Informe", width=15, command=generar_informe)
    boton_generar_informe.pack(side="left", padx=5, pady=10)

    # Botón "Cancelar"
    boton_cancelar = tk.Button(contenedor_botones, text="Cancelar", width=10,
                               command=ventana_generar_informe_producto.destroy)
    boton_cancelar.pack(side="left", padx=5, pady=10)

    # Ejecutar el bucle principal de la ventana de generar informe del producto
    ventana_generar_informe_producto.mainloop()
    pass

# Crear la ventana principal de gestión de productos
ventana_productos = tk.Tk()
ventana_productos.title("Gestión de Productos")
ventana_productos.geometry("800x600")

# Configurar el fondo y estilos
color_fondo = "#F5F5F5"
fuente_titulo = ("Arial", 24, "bold")

ventana_productos.configure(bg=color_fondo)

# Título de la ventana
titulo = tk.Label(ventana_productos, text="Gestión de Productos", font=fuente_titulo, fg="#1DA1F2", bg=color_fondo)
titulo.pack(pady=(30, 10))

# Contenedor para los botones
contenedor_botones = tk.Frame(ventana_productos, bg=color_fondo)
contenedor_botones.pack(pady=20)

# Estilos para los botones
estilo_botones = ttk.Style()
estilo_botones.configure('TButton', font=("Arial", 18))

# Botón Agregar Producto
boton_agregar_producto = ttk.Button(contenedor_botones, text="Agregar Producto", command=abrir_ventana_agregar_producto)
boton_agregar_producto.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Botón Actualizar Producto
boton_actualizar_producto = ttk.Button(contenedor_botones, text="Actualizar Producto", command=abrir_ventana_actualizar_producto)
boton_actualizar_producto.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Botón Eliminar Producto
boton_eliminar_producto = ttk.Button(contenedor_botones, text="Eliminar Producto", command=abrir_ventana_eliminar_producto)
boton_eliminar_producto.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Botón Buscar Producto
boton_buscar_producto = ttk.Button(contenedor_botones, text="Buscar Producto", command=abrir_ventana_buscar_producto)
boton_buscar_producto.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Botón Generar Informe de Producto
boton_generar_informe_producto = ttk.Button(contenedor_botones, text="Generar Informe de Producto", command=generar_informe_producto)
boton_generar_informe_producto.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Centrar el contenedor de botones en la ventana
contenedor_botones.pack(expand=True, fill=tk.BOTH)

# Ejecutar el bucle principal de la ventana
ventana_productos.mainloop()