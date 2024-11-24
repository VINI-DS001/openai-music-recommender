from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from process import music_data
import os

import openai

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar a chave
openai_api_key = os.getenv("OPENAI_API_KEY")

# Configurar a API key
openai.api_key = openai_api_key

def generate_playlist_description(anime_or_game):
    prompt = f"Crie uma descrição para uma playlist inspirada em {anime_or_game}. A playlist deve refletir emoções épicas e uma atmosfera grandiosa."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

description = generate_playlist_description("League of Legends")
print(description)

def classify_songs(query, dataset):
    # Criar embedding do query
    embeddings = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=query
    )
    query_embedding = embeddings['data'][0]['embedding']  # vetor de embedding do query
    
    # Gerar embeddings para as descrições das músicas no dataset
    music_embeddings = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=dataset['topic'].tolist()  # Convertendo a coluna 'topic' para lista
    )
    
    # Adicionar coluna com os embeddings das músicas
    dataset['embedding'] = [embedding['embedding'] for embedding in music_embeddings['data']]
    
    # Calcular a similaridade para cada descrição de música
    dataset['similaridade'] = dataset['embedding'].apply(
        lambda desc_embedding: cosine_similarity([query_embedding], [desc_embedding])[0][0]
    )
    
    # Retornar as 10 músicas mais similares
    return dataset.sort_values('similaridade', ascending=False).head(10)

