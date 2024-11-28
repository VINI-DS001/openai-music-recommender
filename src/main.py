from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import os
import openai

# Carregar variáveis do arquivo .env
load_dotenv()

# Acessar a chave da API
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

# Função para gerar a descrição da playlist com GPT-4
def generate_playlist_description(anime_or_game):
    prompt = f"Crie uma descrição para uma playlist inspirada em {anime_or_game}. A playlist deve refletir emoções épicas e uma atmosfera grandiosa."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']

# Função para classificar músicas com base na similaridade das letras
def classify_songs(query, dataset):
    # Criar embedding do query
    embeddings = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=query
    )
    query_embedding = embeddings['data'][0]['embedding']  # vetor de embedding do query

    # Gerar embeddings para as letras das músicas
    music_embeddings = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=dataset['text'].tolist()  # Convertendo a coluna 'text' para lista
    )

    # Adicionar coluna com os embeddings das músicas
    dataset['embedding'] = [embedding['embedding'] for embedding in music_embeddings['data']]

    # Calcular a similaridade para cada letra de música
    dataset['similaridade'] = dataset['embedding'].apply(
        lambda desc_embedding: cosine_similarity([query_embedding], [desc_embedding])[0][0]
    )

    # Retornar as 5 músicas mais similares
    return dataset.sort_values('similaridade', ascending=False).head(5)

# Função para gerar a capa da playlist com DALL-E
def generate_playlist_cover(theme):
    response = openai.Image.create(
        prompt=f"Arte digital para uma playlist épica inspirada em {theme}, com cores vibrantes e temática de fantasia.",
        n=1,
        size="512x512"
    )
    return response['data'][0]['url']

# Código principal
if __name__ == "__main__":
    # Carregar o dataset de amostras
    dataset_path = "spotify-amostras.csv"
    music_data = pd.read_csv(dataset_path)

    # Pedir o nome do anime ou jogo ao usuário
    anime_or_game = input("Digite o nome do anime ou jogo: ")

    # Gerar a descrição da playlist
    description = generate_playlist_description(anime_or_game)
    print("\nDescrição da Playlist:")
    print(description)

    # Classificar músicas e gerar a playlist
    print("\nClassificação de músicas baseada no tema...")
    top_songs = classify_songs(anime_or_game, music_data)

    # Exibir as 5 músicas selecionadas
    print("\nMúsicas selecionadas para a playlist:")
    print(top_songs[['artist', 'song', 'link']])

    # Gerar a capa da playlist
    print("\nGerando a capa da playlist...")
    image_url = generate_playlist_cover(anime_or_game)
    print("Capa gerada:", image_url)
