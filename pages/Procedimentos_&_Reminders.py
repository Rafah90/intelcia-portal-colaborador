import streamlit as st
import pandas as pd

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Portal do Colaborador", page_icon="📰",)

# TÍTULO VERMELHO
st.markdown("<h1 style='color:red'>Central de Procedimentos e Reminders 📰</h1>",unsafe_allow_html=True)

# SAUDAÇÃO COM ESPAÇO
st.markdown("Olá, Bem-vindo(a) ao seu portal de informações da operação SNS24!",unsafe_allow_html=True)
st.markdown("---")  # linha horizontal separando os textos

# FUNÇÃO PARA CARREGAR OS DADOS
@st.cache_data(ttl=60)
def carregar_dados():
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vShgrwD2B6WKm1b4u-drEj7TaFXceKZEGc3jqHQ2PRMsyjaCbHSROEYjClJaEHiHDGkACQSvmccfbov/pub?output=csv"
    df = pd.read_csv(url)
    return df

# CARREGAR PLANILHA
try:
    noticias = carregar_dados()
except Exception as e:
    st.error(f"Erro ao carregar dados do Google Sheets: {e}")
    st.stop()

# Verifica se as colunas necessárias existem
colunas_esperadas = ["Carimbo de data/hora", "Titulo da Informação", "Categoria", "Informação", "Data da Informação", "Imagem"]
if not all(col in noticias.columns for col in colunas_esperadas):
    st.error(f"A planilha deve conter as colunas: {', '.join(colunas_esperadas)}")
    st.stop()

# FILTRO LATERAL
categoria = st.sidebar.selectbox("Filtro das notícias por:",["TODAS CATEGORIAS"] + sorted(list(noticias["Categoria"].unique())))
if categoria != "TODAS CATEGORIAS":noticias = noticias[noticias["Categoria"] == categoria]

# INVERTER A ORDEM DAS NOTÍCIAS
noticias = noticias.iloc[::-1]  # agora a última linha aparece primeiro

# LAYOUT DAS INFORMAÇÕES EM 1 COLUNA SEM IMAGENS
for i, row in noticias.iterrows():
    with st.container():
        st.subheader(row["Titulo da Informação"])
        st.caption(f"{row['Categoria']} | {row['Data da Informação']}")
        st.write(row["Informação"])
        st.markdown("---")  # linha horizontal separando cada notícia
