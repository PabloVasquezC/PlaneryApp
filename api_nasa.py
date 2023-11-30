import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

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

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("PlanetaryApp")

# Establecer el tamaño inicial de la ventana
ventana.geometry("900x600")  # Ancho x Altura

# Crear un Canvas para la imagen de fondo
canvas = tk.Canvas(ventana, width=900, height=600)
canvas.pack(fill=tk.BOTH, expand=True)

# Enlazar la función resize_image al evento de cambio de tamaño de la ventana
ventana.bind("<Configure>", resize_image)

# Mostrar la imagen en el Canvas
photo = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Iniciar el bucle principal de la aplicación
ventana.mainloop()
