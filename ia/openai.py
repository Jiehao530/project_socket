import openai
import os 
from dotenv import load_dotenv

load_dotenv("../.env")

KEY_IA = os.getenv("OPENAI_KEY")

openai.api_key = KEY_IA

def get_response_ia(message):
    try:
        response_ia = openai.chat.completions.create(model="gpt-4.1", messages=[{"role": "user", "content": message}])
        return response_ia.choices[0].message.content
    
    except Exception as error:
        print(f"OpenAI API error: {error}")
        return "Sorry, an error occurred with the AI."