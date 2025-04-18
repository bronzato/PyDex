import streamlit as st
import pandas as pd

st.markdown("# Python Pokedex")
st.sidebar.markdown("Python Pokedex")

if "data" not in st.session_state:
    df_data = pd.read_csv("dataset/pokemon.csv")
    st.session_state["data"] = df_data

st.markdown(
    """🧬 Pokédex Completa – Do Pokémon #001 ao #721
Bem-vindo à sua nova fonte definitiva de informações sobre Pokémon! Esta base de dados cobre todas as criaturas das Gerações I a VI, incluindo formas alternativas, mega evoluções e variações especiais. Explore os dados detalhados de mais de 700 Pokémon, com informações que abrangem:

📛 Nome e Número na Pokédex Nacional

🧪 Tipos Primário e Secundário

🧬 Atributos de Batalha: HP, Ataque, Defesa, Ataque Especial, Defesa Especial e Velocidade

🧠 Valor Total de Status (Base Stats Total)

⚡ Geração de Origem (de Kanto a Kalos)

⭐ Indicador de Lendário

Você encontrará desde os clássicos como Bulbasaur, Charizard e Mewtwo, até os lendários como Rayquaza, Arceus e Xerneas, com dados consistentes e atualizados para análise, comparações, ou apenas para matar a curiosidade.
""")