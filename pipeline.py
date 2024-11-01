import json
import openai
from openai import OpenAI
from config import OPENAI_API_KEY
from prompts import PROMPTS

client = OpenAI(api_key=OPENAI_API_KEY)

def is_relevant_input(career: str) -> bool:
    """Verifica si la entrada del usuario es relevante para carreras tecnológicas."""
    keywords = [
        "tecnología", "programador", "desarrollador", "ingeniero", "científico", "analista", "consultor",
        "frontend", "backend", "full stack", "devops", "ciberseguridad", "hacking", "machine learning",
        "data scientist", "cloud", "software", "QA", "tester", "arquitecto de software", "redes",
        "sistemas", "infraestructura", "robotics", "inteligencia artificial", "iot", "blockchain"
    ]
    return any(keyword in career.lower() for keyword in keywords)

def generate_learning_path(career: str) -> dict:
    if not is_relevant_input(career):
        return {
            "message": "🤖 Hola, soy *TechBot* y estoy aquí para ayudarte a convertirte en un experto en carreras tecnológicas. Si necesitas información sobre roles como desarrollador, analista de datos, o ingeniero, ¡estoy listo para ayudarte! 🚀"
        }

    try:
        prompt = f"Enumera los conceptos fundamentales que un {career} debe aprender, y proporciona una breve descripción de cada uno."
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        raw_output = response.choices[0].message.content.strip()
        lines = raw_output.split("\n")
        nodes = []

        for line in lines:
            if line.strip() and line[0].isdigit():  # Verifica si la línea comienza con un número
                parts = line.split(".", 1)
                if len(parts) == 2:
                    name = parts[1].strip().split(" ", 1)[0]
                    description = parts[1].strip()
                    nodes.append({"name": name, "description": description})

        roadmap_json = {
            "roadmap": {
                "tip": "Make sure to build as many projects as possible for each node of the roadmap.",
                "nodes": nodes,
                "importantNote": "You should be able to find an intern or Junior Frontend Developer job after learning these key concepts. Start applying for jobs and keep learning."
            }
        }

        return roadmap_json

    except openai.APIError as e:
        return {"error": f"Error en la solicitud a OpenAI: {str(e)}"}
    except json.JSONDecodeError:
        return {"error": "Error al procesar la respuesta de OpenAI. La respuesta no estaba en un formato válido."}
    except Exception as e:
        return {"error": f"Se produjo un error inesperado: {str(e)}"}

if __name__ == "__main__":
    career = input("What career would you like to generate a learning path for? ")
    learning_path = generate_learning_path(career)
    print(json.dumps(learning_path, indent=2))