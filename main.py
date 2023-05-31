# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import tkinter as tk
from tkinter import messagebox
import subprocess

def iniciar_sesion():
    usuario = campo_usuario.get()
    contrasena = campo_contrasena.get()

    # Verificar las credenciales ingresadas
    if usuario == "tom" and contrasena == "12":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
        ventana_login.destroy()  # Cerrar la ventana de login
        abrir_dashboard()  # Mostrar el panel de control
    else:
        messagebox.showerror("Error de inicio de sesión", "Credenciales inválidas")

def abrir_dashboard():
    # Importar y ejecutar el archivo dashboard.py
    import dashboard
    dashboard.mostrar_dashboard()

# Crear una instancia de la ventana de login
ventana_login = tk.Tk()
ventana_login.title("Aplicación de Ventas")
ventana_login.geometry("360x480")

# Fondo de la ventana

# Marco para centrar los elementos
marco = tk.Frame(ventana_login, bg="white")
marco.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=300, height=300)

# Logo de la aplicación
logo = tk.Label(marco, text="Logo de la aplicación", font=("Arial", 16, "bold"), fg="#1DA1F2", bg="white")
logo.pack(pady=(40, 20))

# Campo de entrada para usuario
campo_usuario = tk.Entry(marco, font=("Arial", 12), bg="#F0F0F0")
campo_usuario.insert(0, "Usuario")
campo_usuario.pack(pady=10)

# Campo de entrada para contraseña
campo_contrasena = tk.Entry(marco, font=("Arial", 12), show="*", bg="#F0F0F0")
campo_contrasena.insert(0, "Contraseña")
campo_contrasena.pack(pady=10)

# Botón de inicio de sesión
boton_login = tk.Button(marco, text="Iniciar sesión", font=("Arial", 14, "bold"), bg="#1DA1F2", fg="white", command=iniciar_sesion)
boton_login.pack(pady=10)

# Ejecutar el bucle principal de la ventana de login
ventana_login.mainloop()





