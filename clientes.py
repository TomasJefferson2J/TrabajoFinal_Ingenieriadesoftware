import tkinter as tk
from tkinter import ttk

# Función para abrir la ventana de agregar cliente
def abrir_ventana_agregar_cliente():
    ventana_agregar_cliente = tk.Toplevel(ventana_clientes)
    ventana_agregar_cliente.title("Agregar Cliente")
    ventana_agregar_cliente.geometry("600x500")

    # Etiquetas y campos de entrada
    etiqueta_nombre = ttk.Label(ventana_agregar_cliente, text="Nombre:")
    etiqueta_nombre.pack(pady=10)
    campo_nombre = ttk.Entry(ventana_agregar_cliente)
    campo_nombre.pack(pady=5)

    etiqueta_apellido = ttk.Label(ventana_agregar_cliente, text="Apellido:")
    etiqueta_apellido.pack(pady=10)
    campo_apellido = ttk.Entry(ventana_agregar_cliente)
    campo_apellido.pack(pady=5)

    etiqueta_direccion = ttk.Label(ventana_agregar_cliente, text="Dirección:")
    etiqueta_direccion.pack(pady=10)
    campo_direccion = ttk.Entry(ventana_agregar_cliente)
    campo_direccion.pack(pady=5)

    etiqueta_numero_documento = ttk.Label(ventana_agregar_cliente, text="Número de Documento:")
    etiqueta_numero_documento.pack(pady=10)
    campo_numero_documento = ttk.Entry(ventana_agregar_cliente)
    campo_numero_documento.pack(pady=5)

    etiqueta_tipo_documento = ttk.Label(ventana_agregar_cliente, text="Tipo de Documento:")
    etiqueta_tipo_documento.pack(pady=10)
    opciones_tipo_documento = ["RUC", "DNI", "SIN documento"]
    combo_tipo_documento = ttk.Combobox(ventana_agregar_cliente, values=opciones_tipo_documento)
    combo_tipo_documento.pack(pady=5)

    # Botones Guardar y Cancelar
    boton_guardar = ttk.Button(ventana_agregar_cliente, text="Guardar")
    boton_guardar.pack(pady=10)

    boton_cancelar = ttk.Button(ventana_agregar_cliente, text="Cancelar", command=ventana_agregar_cliente.destroy)
    boton_cancelar.pack(pady=5)
    pass
# Función para abrir la ventana de actualizar cliente
def abrir_ventana_actualizar_cliente():
    # Lógica para abrir la ventana de actualizar cliente
    def guardar_actualizacion():
        # Lógica para guardar los cambios realizados al cliente

        # Cerrar la ventana de actualización
        ventana_actualizar_cliente.destroy()

    def cancelar_actualizacion():
        # Cerrar la ventana de actualización sin aplicar cambios
        ventana_actualizar_cliente.destroy()

    # Obtener los valores actuales del cliente que se desea actualizar
    # client_data = obtener_datos_cliente(id_cliente)
    # Por simplicidad, utilizaremos valores de ejemplo
    client_data = {
        'nombre': 'Juan',
        'apellido': 'Pérez',
        'direccion': 'Calle Principal 123',
        'tipo_documento': 'DNI',
        'numero_documento': '12345678'
    }

    # Crear la ventana de actualización de cliente
    ventana_actualizar_cliente = tk.Toplevel()
    ventana_actualizar_cliente.title("Actualizar Cliente")

    # Etiquetas de campo
    tk.Label(ventana_actualizar_cliente, text="Nombre:").grid(row=0, column=0, sticky=tk.E)
    tk.Label(ventana_actualizar_cliente, text="Apellido:").grid(row=1, column=0, sticky=tk.E)
    tk.Label(ventana_actualizar_cliente, text="Dirección:").grid(row=2, column=0, sticky=tk.E)
    tk.Label(ventana_actualizar_cliente, text="Tipo de Documento:").grid(row=3, column=0, sticky=tk.E)
    tk.Label(ventana_actualizar_cliente, text="Número de Documento:").grid(row=4, column=0, sticky=tk.E)

    # Campos de entrada de texto
    entry_nombre = tk.Entry(ventana_actualizar_cliente)
    entry_nombre.insert(0, client_data['nombre'])
    entry_nombre.grid(row=0, column=1)

    entry_apellido = tk.Entry(ventana_actualizar_cliente)
    entry_apellido.insert(0, client_data['apellido'])
    entry_apellido.grid(row=1, column=1)

    entry_direccion = tk.Entry(ventana_actualizar_cliente)
    entry_direccion.insert(0, client_data['direccion'])
    entry_direccion.grid(row=2, column=1)

    # Menú desplegable para el tipo de documento
    combo_tipo_documento = ttk.Combobox(ventana_actualizar_cliente, values=['RUC', 'DNI', 'SIN documento'])
    combo_tipo_documento.set(client_data['tipo_documento'])
    combo_tipo_documento.grid(row=3, column=1)

    entry_numero_documento = tk.Entry(ventana_actualizar_cliente)
    entry_numero_documento.insert(0, client_data['numero_documento'])
    entry_numero_documento.grid(row=4, column=1)

    # Botones de acción
    boton_guardar = ttk.Button(ventana_actualizar_cliente, text="Guardar", command=guardar_actualizacion)
    boton_guardar.grid(row=5, column=0, pady=10, padx=10)

    boton_cancelar = ttk.Button(ventana_actualizar_cliente, text="Cancelar", command=cancelar_actualizacion)
    boton_cancelar.grid(row=5, column=1, pady=10, padx=10)
    pass

# Función para abrir la ventana de eliminar cliente
def abrir_ventana_eliminar_cliente():
    def eliminar_cliente():
        numero_documento = campo_documento.get()
        # Lógica para eliminar el cliente con el número de documento especificado
        # ...

        mensaje = tk.messagebox.showinfo("Eliminar Cliente", "El cliente ha sido eliminado correctamente.")
        ventana_eliminar.destroy()

    ventana_eliminar = tk.Toplevel()
    ventana_eliminar.title("Eliminar Cliente")
    ventana_eliminar.geometry("400x300")
    ventana_eliminar.configure(bg="#F5F5F5")

    titulo = tk.Label(ventana_eliminar, text="Eliminar Cliente", font=("Arial", 20, "bold"), fg="#1DA1F2", bg="#F5F5F5")
    titulo.pack(pady=(30, 10))

    contenedor_eliminar = tk.Frame(ventana_eliminar, bg="#F5F5F5")
    contenedor_eliminar.pack(pady=20)

    label_documento = tk.Label(contenedor_eliminar, text="Número de Documento:", font=("Arial", 14), bg="#F5F5F5")
    label_documento.pack()
    campo_documento = tk.Entry(contenedor_eliminar, font=("Arial", 14))
    campo_documento.pack(pady=10)

    boton_eliminar = ttk.Button(contenedor_eliminar, text="Eliminar", command=eliminar_cliente)
    boton_eliminar.pack(pady=10, ipadx=20, ipady=5)

    contenedor_eliminar.pack(expand=True, fill=tk.BOTH)

    ventana_eliminar.mainloop()
    pass

# Función para abrir la ventana de buscar cliente
def abrir_ventana_buscar_cliente():
    def buscar_cliente():
        numero_documento = campo_documento.get()
        # Lógica para buscar el cliente con el número de documento especificado
        # ...

        # Mostrar los resultados de la búsqueda en una ventana emergente
        ventana_resultados = tk.Toplevel()
        ventana_resultados.title("Resultados de Búsqueda")
        ventana_resultados.geometry("400x300")
        ventana_resultados.configure(bg="#F5F5F5")

        titulo_resultados = tk.Label(ventana_resultados, text="Resultados de Búsqueda", font=("Arial", 20, "bold"),
                                     fg="#1DA1F2", bg="#F5F5F5")
        titulo_resultados.pack(pady=(30, 10))

        # Aquí puedes mostrar los resultados de la búsqueda en etiquetas o en una tabla
        # Puedes ajustar esta parte según tus necesidades específicas

    ventana_buscar = tk.Toplevel()
    ventana_buscar.title("Buscar Cliente")
    ventana_buscar.geometry("400x300")
    ventana_buscar.configure(bg="#F5F5F5")

    titulo = tk.Label(ventana_buscar, text="Buscar Cliente", font=("Arial", 20, "bold"), fg="#1DA1F2", bg="#F5F5F5")
    titulo.pack(pady=(30, 10))

    contenedor_buscar = tk.Frame(ventana_buscar, bg="#F5F5F5")
    contenedor_buscar.pack(pady=20)

    label_documento = tk.Label(contenedor_buscar, text="Número de Documento:", font=("Arial", 14), bg="#F5F5F5")
    label_documento.pack()
    campo_documento = tk.Entry(contenedor_buscar, font=("Arial", 14))
    campo_documento.pack(pady=10)

    boton_buscar = ttk.Button(contenedor_buscar, text="Buscar", command=buscar_cliente)
    boton_buscar.pack(pady=10, ipadx=20, ipady=5)

    contenedor_buscar.pack(expand=True, fill=tk.BOTH)

    ventana_buscar.mainloop()
    pass

# Función para generar informe de cliente
def generar_informe_cliente():
    def generar_informe():
        cliente_id = campo_cliente_id.get()
        # Lógica para generar el informe del cliente con el ID especificado
        # ...

        # Mostrar el informe en una ventana emergente
        ventana_informe = tk.Toplevel()
        ventana_informe.title("Informe del Cliente")
        ventana_informe.geometry("600x400")
        ventana_informe.configure(bg="#F5F5F5")

        titulo_informe = tk.Label(ventana_informe, text="Informe del Cliente", font=("Arial", 20, "bold"), fg="#1DA1F2",
                                  bg="#F5F5F5")
        titulo_informe.pack(pady=(30, 10))

        # Aquí puedes mostrar el informe del cliente en etiquetas, texto enriquecido o cualquier otro formato
        # Puedes ajustar esta parte según tus necesidades específicas

    ventana_generar_informe = tk.Toplevel()
    ventana_generar_informe.title("Generar Informe de Cliente")
    ventana_generar_informe.geometry("400x300")
    ventana_generar_informe.configure(bg="#F5F5F5")

    titulo = tk.Label(ventana_generar_informe, text="Generar Informe de Cliente", font=("Arial", 20, "bold"),
                      fg="#1DA1F2", bg="#F5F5F5")
    titulo.pack(pady=(30, 10))

    contenedor_generar_informe = tk.Frame(ventana_generar_informe, bg="#F5F5F5")
    contenedor_generar_informe.pack(pady=20)

    label_cliente_id = tk.Label(contenedor_generar_informe, text="ID del Cliente:", font=("Arial", 14), bg="#F5F5F5")
    label_cliente_id.pack()
    campo_cliente_id = tk.Entry(contenedor_generar_informe, font=("Arial", 14))
    campo_cliente_id.pack(pady=10)

    boton_generar = ttk.Button(contenedor_generar_informe, text="Generar Informe", command=generar_informe)
    boton_generar.pack(pady=10, ipadx=20, ipady=5)

    contenedor_generar_informe.pack(expand=True, fill=tk.BOTH)

    ventana_generar_informe.mainloop()
    pass

# Crear la ventana principal de gestión de clientes
ventana_clientes = tk.Tk()
ventana_clientes.title("Gestión de Clientes")
ventana_clientes.geometry("800x600")

# Configurar el fondo y estilos
color_fondo = "#F5F5F5"
fuente_titulo = ("Arial", 24, "bold")

ventana_clientes.configure(bg=color_fondo)

# Título de la ventana
titulo = tk.Label(ventana_clientes, text="Gestión de Clientes", font=fuente_titulo, fg="#1DA1F2", bg=color_fondo)
titulo.pack(pady=(30, 10))

# Contenedor para los botones
contenedor_botones = tk.Frame(ventana_clientes, bg=color_fondo)
contenedor_botones.pack(pady=20)

# Estilos para los botones
estilo_botones = ttk.Style()
estilo_botones.configure('TButton', font=("Arial", 18))

# Botón Agregar Cliente
boton_agregar_cliente = ttk.Button(contenedor_botones, text="Agregar Cliente", command=abrir_ventana_agregar_cliente)
boton_agregar_cliente.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Botón Actualizar Cliente
boton_actualizar_cliente = ttk.Button(contenedor_botones, text="Actualizar Cliente", command=abrir_ventana_actualizar_cliente)
boton_actualizar_cliente.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Botón Eliminar Cliente
boton_eliminar_cliente = ttk.Button(contenedor_botones, text="Eliminar Cliente", command=abrir_ventana_eliminar_cliente)
boton_eliminar_cliente.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Botón Buscar Cliente
boton_buscar_cliente = ttk.Button(contenedor_botones, text="Buscar Cliente", command=abrir_ventana_buscar_cliente)
boton_buscar_cliente.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Botón Generar Informe de Cliente
boton_generar_informe_cliente = ttk.Button(contenedor_botones, text="Generar Informe de Cliente", command=generar_informe_cliente)
boton_generar_informe_cliente.pack(pady=10, padx=50, ipadx=20, ipady=5, fill=tk.BOTH)

# Centrar el contenedor de botones en la ventana
contenedor_botones.pack(expand=True, fill=tk.BOTH)

# Ejecutar el bucle principal de la ventana
ventana_clientes.mainloop()
