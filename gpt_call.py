from groq import Groq
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv('OPENAI_API_KEY')

client_groq = Groq(
    api_key= groq_api_key,
)
client_openai = OpenAI(
    api_key=openai_api_key,
)

def groq_call(prompt):
    chat_completion = client_groq.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content
    

def gpt_call(prompt):
    chat_completion = client_openai.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-40",
    )
    return chat_completion.choices[0].message.content

def generate_variation(prompt, model='groq'):
    """Generates a variation of the given prompt using groq/GPT-4."""
    if model == 'groq':
        return groq_call(prompt)
    elif model == 'gpt':
        return gpt_call(prompt)
