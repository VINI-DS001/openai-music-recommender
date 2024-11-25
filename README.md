# Recomendador de Playlists de Trilha Sonora Baseadas em Preferências de Jogos ou Animes.

Equipe: Alec de Jesus, Felipe Leão, Henrique Lyrio, Mateus Pires, Rafael Miguez, Vinícius Souza

## Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Execução](#instalação-e-execução)
- [Funcionalidades](#funcionalidades)
- [Conjunto de Dados](#conjunto-de-dados)

## Descrição do Projeto

Este repositório contém os códigos e documentação do projeto final da Unidade 03 da matéria Tópicos Avançados em Inteligência Computacional, no qual treinamos um modelo utilizando a API da OpenAI para criar um recomendador de playlists de músicas baseadas nas preferências em jogos ou animes de uma pessoa, além de criar uma capa personalizada para a playlist.

## Tecnologias Utilizadas
- Python 3.x
- Bibliotecas: `openai 0.28`, `scikit-learn`, `pandas`, `python-dotenv`
- Git/GitHub para controle de versão e colaboração

## Instalação e Execução

Para rodar o projeto localmente:

1. Clone o repositório:
    ```bash
    git clone https://github.com/VINI-DS001/openai-music-recommender.git
    ```

2. Instale as dependências:
    ```bash
    pip install openai==0.28
    ```

    ```bash
    pip install pandas
    ```

    ```bash
    pip install scikit-learn
    ```

    ```bash
    pip install python-dotenv
    ```

## Funcionalidades

Análise e Geração de Descrição Temática:
A aplicação utiliza o modelo GPT-4 da OpenAI para analisar títulos de animes ou jogos inseridos pelo usuário. Em seguida, gera uma descrição temática que ressoe com o universo do título, seja ele de anime ou jogo.

Sugestão de Músicas:
A IA sugere músicas de um banco de dados de acordo com o estilo do anime/jogo inserido pelo usuário. As sugestões são baseadas em gênero musical, clima e vibe do título escolhido.

Classificação de Músicas Relevantes:
A Ada v2, outro modelo da OpenAI, classifica músicas com base na sua relevância para o estilo do anime/jogo. Com isso, a IA é capaz de montar playlists personalizadas, selecionando músicas que melhor se encaixam no universo do título selecionado.

Criação de Capa de Playlist:
A aplicação usa o modelo DALL-E para gerar uma capa artística exclusiva para a playlist sugerida. A imagem é criada com uma estética que combina com o estilo visual do anime ou jogo escolhido.

## Conjunto de Dados

O conjunto de dados original utilizado para criar o banco das músicas a serem recomendadas é constituído de um arquivo csv contendo aproximadamente 28 mil músicas, incluindo seus gêneros musicais, autores e ano de lançamento.

 - [Dataset: Musicas](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019)