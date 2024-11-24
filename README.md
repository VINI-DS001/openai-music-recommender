# Recomendador de Playlists de Trilha Sonora Baseadas em Preferências de Jogos ou Animes.

Equipe: Alec de Jesus, Felipe Leão, Henrique Lyrio, Mateus Pires, Rafael Miguez, Vinícius Souza

## Índice
- [Descrição do Projeto](#descrição-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação e Execução](#instalação-e-execução)
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

## Tecnologias utilizadas

As tecnologias da OpenAI escolhidas para o projeto incluem o GPT-4 com o objetivo de gerar descrições detalhadas de playlists com base nos animes/jogos informados pelo usuário. Ada v2 foi utilizada para agrupamento e classificação de dados musicais (ex.: identificar estilos musicais associados a cada título de anime/jogo). Por fim foi utilizado o DALL-E para gerar capas artísticas únicas para as playlists criadas, com base nos animes/jogos ou no gênero das músicas.

## Conjunto de Dados

O conjunto de dados original utilizado para criar o banco das músicas a serem recomendadas é constituído de um arquivo csv contendo aproximadamente 28 mil músicas, incluindo seus gêneros musicais, autores e ano de lançamento.

 - [Dataset: Musicas](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019)