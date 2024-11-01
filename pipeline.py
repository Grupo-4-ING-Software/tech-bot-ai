from prompts import PROMPTS
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_learning_path(career: str) -> str:
    # Obtiene el prompt específico o el genérico
    prompt = PROMPTS.get(career.lower(), PROMPTS["default"]).format(career=career)
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
    print(generate_learning_path("desarrollador frontend"))  # Debería usar el prompt personalizado
    print(generate_learning_path("analista de datos"))      # Debería usar el prompt personalizado
    print(generate_learning_path("ingeniero de software"))  # Debería usar el prompt genérico
