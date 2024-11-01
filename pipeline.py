from openai import OpenAI
from config import OPENAI_API_KEY

# Configura el cliente de OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_learning_path(career: str) -> str:
    prompt = f"Dame una línea de aprendizaje para ser {career}"
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
    print(generate_learning_path("desarrollador frontend"))
    print(generate_learning_path("analista de datos"))
    print(generate_learning_path("hacking ético"))
