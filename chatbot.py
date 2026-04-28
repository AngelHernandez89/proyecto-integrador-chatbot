import json
import tkinter as tk
from tkinter import scrolledtext

# Cargar base de datos desde un archivo JSON
def cargar_base_datos():
    try:
        with open("base_datos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"preguntas": []}

# Buscar respuesta en la base de datos JSON basándose en palabras clave
def buscar_respuesta_json(pregunta, base_datos):
    palabras_pregunta = set(pregunta.lower().split())  # Convertir pregunta a conjunto de palabras clave
    for item in base_datos['preguntas']:
        palabras_clave = set(item['pregunta'].lower().split())  # Convertir las palabras clave a conjunto
        if palabras_clave.intersection(palabras_pregunta):  # Comprobar coincidencias
            respuesta = item['respuesta']
            url = item.get('url', 'No disponible')
            return f"{respuesta}\nMás información: {url}"
    return "Lo siento, no tengo una respuesta para esa pregunta."

# Función principal del chatbot
def obtener_respuesta():
    pregunta = entrada_usuario.get()
    if pregunta.strip() == "":
        return

    # Buscar en la base de datos
    respuesta = buscar_respuesta_json(pregunta, base_datos)
    
    # Mostrar la respuesta en la interfaz
    historial_texto.insert(tk.END, f"Tú: {pregunta}\nChatbot: {respuesta}\n\n")
    entrada_usuario.delete(0, tk.END)

# Cargar base de datos al iniciar
base_datos = cargar_base_datos()

# Interfaz gráfica con Tkinter
root = tk.Tk()
root.title("Chatbot con Tkinter y Base de Datos")

# Área de texto con desplazamiento
historial_texto = scrolledtext.ScrolledText(root, width=50, height=20, wrap=tk.WORD)
historial_texto.pack(pady=10)

# Campo de entrada y botón
entrada_usuario = tk.Entry(root, width=50)
entrada_usuario.pack(pady=5)

boton_enviar = tk.Button(root, text="Enviar", command=obtener_respuesta)
boton_enviar.pack(pady=5)

# Ejecutar la interfaz gráfica
root.mainloop()
