import streamlit as st
import altair as alt


df_data = st.session_state["data"]

st.set_page_config(
    page_title="Pokémon Data",
    page_icon=":dragon:",
    layout="wide"
)


type1 = df_data["Type 1"].unique()
slc_type1 = st.sidebar.selectbox("Tipo 1", type1)
df_data_type1 = df_data[df_data["Type 1"] == slc_type1]
slc_type2 = st.sidebar.selectbox("Tipo 2", df_data_type1["Type 2"].unique())
df_data_type2 = df_data_type1[df_data_type1["Type 2"] == slc_type2]
slc_name = st.sidebar.selectbox("Pokémon", df_data_type2["Name"].unique())
df_data_name = df_data_type2[df_data_type2["Name"] == slc_name]
pokemon_id = df_data_type2[df_data_type2["Name"] == slc_name]["#"].values[0]

st.image(
    f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{pokemon_id}.png",
    width=200,
)
st.title(df_data_name["Name"].values[0])
st.markdown(f"**Geração:** {df_data_name['Generation'].values[0]}")
st.markdown(f"**Tipo Principal:** {df_data_name['Type 1'].values[0]}")
st.markdown(f"**Tipo Secundário:** {df_data_name['Type 2'].values[0]}")
st.divider()
col1, col2, col3, col4, col5, col6 = st.columns(6)

col1.metric(label="HP", value=df_data_name['HP'].values[0])
col2.metric(label="Attack", value=df_data_name['Attack'].values[0])
col3.metric(label="Defense", value=df_data_name['Defense'].values[0])
col4.metric(label="Speed", value=df_data_name['Speed'].values[0])
col5.metric(label="Special Attack", value=df_data_name['Sp. Atk'].values[0])
col6.metric(label="Special Defense", value=df_data_name['Sp. Def'].values[0])

df_stats = df_data_name[["HP", "Attack", "Defense", "Speed", "Sp. Atk", "Sp. Def"]].T
df_stats.columns = ["Valor"]
df_stats = df_stats.reset_index().rename(columns={"index": "Stat"})

chart = alt.Chart(df_stats).mark_bar().encode(
    x=alt.X('Valor:Q', scale=alt.Scale(domain=[0, 300])),
    y=alt.Y('Stat:N', sort='-y'),
    tooltip=['Stat', 'Valor']
).properties(
    height=250,
)
st.altair_chart(chart, use_container_width=True)