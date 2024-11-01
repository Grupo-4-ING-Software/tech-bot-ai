import re
from prompts import PROMPTS
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def normalize_input(career: str) -> str:
    """Normaliza el input del usuario para mejorar la búsqueda en el diccionario de prompts."""
    normalized_career = re.sub(r'[^a-zA-Z\s]', '', career).lower().strip()
    return normalized_career

def generate_learning_path(career: str) -> str:
    career_normalized = normalize_input(career)
    prompt = PROMPTS.get(career_normalized, PROMPTS["default"]).format(career=career)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    learning_path = response.choices[0].message.content.strip()
    return learning_path
if __name__ == "__main__":
    print(generate_learning_path("Desarrollador Front-end"))
    print(generate_learning_path("Frontend Developer"))
    print(generate_learning_path("analista de datos"))
