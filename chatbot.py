import json

def cargar_base_datos():
    try:
        with open("base_datos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"preguntas": []}

def buscar_respuesta_json(pregunta, base_datos):
    palabras_pregunta = set(pregunta.lower().split())
    for item in base_datos['preguntas']:
        palabras_clave = set(item['pregunta'].lower().split())
        if palabras_clave.intersection(palabras_pregunta):
            respuesta = item['respuesta']
            url = item.get('url', 'No disponible')
            return f"{respuesta}\nMás información: {url}"
    return "Lo siento, no tengo una respuesta para esa pregunta."

# Cargar datos
base_datos = cargar_base_datos()

print("\n========================================")
print("   CHATBOT INICIADO (MODO TERMINAL)   ")
print("========================================\n")
print("Escribe tu pregunta o 'salir' para finalizar.\n")

while True:
    usuario = input("Tú: ")
    if usuario.lower() in ["salir", "exit", "quit"]:
        print("Chatbot: ¡Adiós!")
        break
    
    respuesta = buscar_respuesta_json(usuario, base_datos)
    print(f"Chatbot: {respuesta}\n")
