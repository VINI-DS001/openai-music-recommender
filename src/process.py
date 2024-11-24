import pandas as pd

# Carregar dataset de músicas
music_data = pd.read_csv("C:/Users/vinid/Downloads/openai-music-games-animes/datasets/tcc-ceds-music.csv")

def categorize_genre(row):
    # Mapeia os gêneros musicais para categorias temáticas
    if row['genre'] == "blues":
        return "melancólico"
    elif row['genre'] == "country":
        return "rústico"
    elif row['genre'] == "hip hop":
        return "urbano"
    elif row['genre'] == "jazz":
        return "sofisticado"
    elif row['genre'] == "pop":
        return "animado"
    elif row['genre'] == "reggae":
        return "praiano"
    elif row['genre'] == "rock":
        return "energético"
    else:
        return "outros"  # Categoria para casos inesperados

# Aplicar a função ao dataset
music_data['categoria'] = music_data.apply(categorize_genre, axis=1)

print(music_data['topic'].notnull().sum())  # Número de valores não nulos
print(music_data['topic'].head())  # Verifique as primeiras linhas para confirmar que são strings

# Exibir as primeiras linhas para verificar
print(music_data.head())

