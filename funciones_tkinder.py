import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO
import requests
from Usuario import *

# URL de la imagen
url = "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"

# Descargar la imagen desde la URL
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Función para redimensionar la imagen según el tamaño de la ventana
def resize_image(event):
    new_width = event.width
    new_height = event.height
    resized_image = img.resize((new_width, new_height))
    new_image = ImageTk.PhotoImage(resized_image)
    canvas.image = new_image
    canvas.create_image(0, 0, anchor=tk.NW, image=new_image)

# Función de inicio de sesión
def login():
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Buscar el usuario en la lista
    for usuario in [usuario1, usuario2, usuario3]:
        if usuario.nombre_der_usuario == entered_username and usuario.verificar_contrasena(entered_password):
            # Inicio de sesión exitoso
            print("Inicio de sesión exitoso para:", usuario.nombre_der_usuario)
            abrir_ventana_principal(usuario.nombre_der_usuario)
            return

    # Si el bucle termina sin retorno, el inicio de sesión falló
    print("Inicio de sesión fallido. Usuario o contraseña incorrectos.")

# Función para abrir la ventana principal después del inicio de sesión exitoso
def abrir_ventana_principal(nombre_usuario):
    # Cerrar la ventana de inicio de sesión
    ventana.destroy()

    # Crear una nueva ventana principal
    ventana_principal = tk.Tk()
    ventana_principal.title(f"PlanetaryApp - Bienvenido, {nombre_usuario}")

    

    # Iniciar el bucle principal de la nueva ventana
    ventana_principal.mainloop()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("PlanetaryApp")

# Establecer el tamaño inicial de la ventana
ventana.geometry("900x600")  # Ancho x Altura

# Obtener el ancho y alto de la pantalla
screen_width = ventana.winfo_screenwidth()
screen_height = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (screen_width - 900) // 2
y = (screen_height - 600) // 2

# Centrar la ventana en la pantalla
ventana.geometry(f"900x600+{x}+{y}")

# Crear un Canvas para la imagen de fondo
canvas = tk.Canvas(ventana, width=900, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Enlazar la función resize_image al evento de cambio de tamaño de la ventana
ventana.bind("<Configure>", resize_image)

# Mostrar la imagen en el Canvas
photo = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Agregar campos de entrada y botón de inicio de sesión
username_label = tk.Label(ventana, text="Nombre de Usuario:")
username_label.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

username_entry = tk.Entry(ventana)
username_entry.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

password_label = tk.Label(ventana, text="Contraseña:")
password_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

password_entry = tk.Entry(ventana, show="*")  # Para ocultar la contraseña
password_entry.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

login_button = tk.Button(ventana, text="Iniciar Sesión", command=login)
login_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

ventana.mainloop()
