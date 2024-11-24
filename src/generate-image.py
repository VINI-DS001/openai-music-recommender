from dotenv import load_dotenv
import os

import openai

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar a chave
openai_api_key = os.getenv("OPENAI_API_KEY")

# Configurar a API key
openai.api_key = openai_api_key

def generate_playlist_cover(theme):
    response = openai.Image.create(
        prompt=f"Arte digital para uma playlist épica inspirada em {theme}, com cores vibrantes e temática de fantasia.",
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

image_url = generate_playlist_cover("League of Legends")
print("Capa gerada:", image_url)
