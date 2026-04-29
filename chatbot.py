import json

def cargar_base_datos():
    try:
        with open("base_datos.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"preguntas": []}

def chatbot():
    datos = cargar_base_datos()
    print("==========================================")
    print("   CHATBOT INICIADO (MODO DOCKER-COMPOSE)  ")
    print("==========================================")
    
    while True:
        usuario = input("Tú: ").lower()
        if usuario in ['salir', 'exit', 'quit']:
            print("Chatbot: ¡Adiós!")
            break
        
        respuesta = "Lo siento, no entiendo esa pregunta."
        for p in datos["preguntas"]:
            if p["pregunta"].lower() in usuario:
                respuesta = p["respuesta"]
                break
        print(f"Chatbot: {respuesta}")

if __name__ == "__main__":
    chatbot()
