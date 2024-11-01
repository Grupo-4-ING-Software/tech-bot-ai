import openai
from openai import OpenAI
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY
client = OpenAI(
    api_key=OPENAI_API_KEY,
)

def test_openai_connection():
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "Dame una línea de aprendizaje para ser desarrollador frontend"
            }
        ]
    )
    print(response.choices[0].message.content.strip())

if __name__ == "__main__":
    test_openai_connection()
