import pandas as pd

# Carregar o dataset original
dataset_path = "C:/Users/vinid/Downloads/openai-music-games-animes/datasets/spotify-millsongdata.csv"
spotify_data = pd.read_csv(dataset_path)

# Selecionar 100 amostras aleatórias
amostras = spotify_data.sample(n=100, random_state=42)

# Salvar as amostras em um novo arquivo
amostras.to_csv("spotify-amostras.csv", index=False)

print("Arquivo spotify-amostras.csv criado com sucesso!")
