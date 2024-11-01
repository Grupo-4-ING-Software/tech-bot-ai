import json
from openai import OpenAI
from config import OPENAI_API_KEY
from prompts import PROMPTS

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_learning_path(career: str) -> dict:
    prompt = f"Por favor, enumera los conceptos clave para aprender como {career}, comenzando con el número 1 y explicando cada concepto brevemente."
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Procesa la respuesta en un formato de lista
    raw_output = response.choices[0].message.content.strip()
    lines = raw_output.split("\n")
    nodes = []

    for line in lines:
        if line.strip() and line[0].isdigit():  
            parts = line.split(".", 1)
            if len(parts) == 2:
                name = parts[1].strip().split(" ", 1)[0]  
                description = parts[1].strip()  
                nodes.append({"name": name, "description": description})

    # Estructura del JSON final
    roadmap_json = {
        "roadmap": {
            "tip": "Make sure to build as many projects as possible for each node of the roadmap.",
            "nodes": nodes,
            "importantNote": "You should be able to find an intern or Junior Frontend Developer job after learning these key concepts. Start applying for jobs and keep learning."
        }
    }

    return roadmap_json

if __name__ == "__main__":
    career = input("What career would you like to generate a learning path for? ")
    learning_path = generate_learning_path(career)
    print(json.dumps(learning_path, indent=2))