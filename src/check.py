import pandas as pd

# Carregar o arquivo de amostras
amostras_carregadas = pd.read_csv("spotify-amostras.csv")

# Exibir o cabeçalho do arquivo (primeiras 5 colunas para verificação)
print("Header do arquivo (primeiras 5 colunas):")
print(amostras_carregadas.columns)

# Exibir as 5 primeiras amostras do arquivo
print("\nPrimeiras 5 amostras do arquivo:")
print(amostras_carregadas.head())
