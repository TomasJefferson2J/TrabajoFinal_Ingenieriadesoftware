import tkinter as tk
from tkinter import ttk

def main():
    # Crear la ventana principal
    ventana_resumen = tk.Tk()

    # Configurar el tamaño y el título de la ventana
    ventana_resumen.geometry("800x600")
    ventana_resumen.title("Resumen de Ventas")

    # Título: Agrega un título o encabezado para identificar la sección de resumen de ventas.
    titulo = tk.Label(ventana_resumen, text="Resumen de Ventas", font=("Arial", 24, "bold"))
    titulo.pack(pady=20)

    # Selección del año: Permite al usuario seleccionar un año específico para ver el resumen de ventas correspondiente a ese año.
    etiqueta_seleccion = tk.Label(ventana_resumen, text="Selecciona el año:")
    etiqueta_seleccion.pack()

    combo_anio = tk.StringVar()
    combo_anio.set("2023")  # Valor por defecto
    opciones_anio = ["2021", "2022", "2023"]  # Opciones disponibles
    menu_anio = tk.OptionMenu(ventana_resumen, combo_anio, *opciones_anio)
    menu_anio.pack(pady=10)

    # Resumen de ventas por mes: Muestra una tabla o lista desglosada por meses, donde se muestra la información de ventas para cada mes del año seleccionado.
    tabla_ventas = tk.Label(ventana_resumen, text="Mes \t Ventas")
    tabla_ventas.pack()

    # Generar datos ficticios para mostrar en la tabla
    ventas_por_mes = [
        ("Enero", 200),
        ("Febrero", 300),
        ("Marzo", 400),
        ("Abril", 500),
        ("Mayo", 600),
        ("Junio", 700),
        ("Julio", 800),
        ("Agosto", 900),
        ("Septiembre", 1000),
        ("Octubre", 1100),
        ("Noviembre", 1200),
        ("Diciembre", 1300),
    ]

    for mes, ventas in ventas_por_mes:
        etiqueta_mes = tk.Label(ventana_resumen, text=f"{mes}\t{ventas}")
        etiqueta_mes.pack()

    # Estadísticas generales: Proporciona un resumen de estadísticas generales, como el total de ventas del año seleccionado, el promedio de ventas mensuales, el mes con más ventas, el mes con menos ventas, etc.
    total_ventas = sum(ventas for _, ventas in ventas_por_mes)
    promedio_ventas = total_ventas / len(ventas_por_mes)
    mes_max_ventas = max(ventas_por_mes, key=lambda x: x[1])[0]
    mes_min_ventas = min(ventas_por_mes, key=lambda x: x[1])[0]

    estadisticas = tk.Label(ventana_resumen,
                            text=f"Total ventas: {total_ventas}\nPromedio ventas: {promedio_ventas:.2f}\nMes con más ventas: {mes_max_ventas}\nMes con menos ventas: {mes_min_ventas}")
    estadisticas.pack(pady=10)

    # Cuadros en blanco en lugar de los gráficos porque no funciona el matplotlib
    cuadro_en_blanco = tk.Label(ventana_resumen, width=400, height=300, relief="solid", bg="white")
    cuadro_en_blanco.pack(pady=10)



    # Iniciar el bucle principal de la aplicación
    ventana_resumen.mainloop()


# Punto de entrada del programa
if __name__ == "__main__":
    main()





