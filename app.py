import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados
df = pd.read_excel("base_academica.xlsx")

st.set_page_config(page_title="Dashboard Acadêmico", layout="wide")
st.title("📊 Dashboard Acadêmico - Gestão Universitária")

st.sidebar.header("🎯 Filtros")
anos = ["Todos"] + sorted(df["Ano Inscrição"].unique().tolist())
ano = st.sidebar.selectbox("Ano de Inscrição", anos)

# Aplicar filtro
if ano != "Todos":
    df = df[df["Ano Inscrição"] == ano]

# Métricas principais
st.subheader("📌 Indicadores Gerais")
col1, col2, col3 = st.columns(3)
col1.metric("📚 Nota Média", round(df["Nota Média"].mean(), 2))
col2.metric("📅 Frequência Média (%)", round(df["Frequência (%)"].mean(), 2))
col3.metric("⏱️ Horas de Estudo", round(df["Horas de Estudo Semanais"].mean(), 2))

# Gráfico de notas
st.subheader("📈 Distribuição das Notas Médias")
fig, ax = plt.subplots()
ax.hist(df["Nota Média"], bins=10, color='skyblue', edgecolor='black')
ax.set_title("Distribuição das Notas Médias")
ax.set_xlabel("Nota Média")
ax.set_ylabel("Número de Alunos")
st.pyplot(fig)

# Rendimento Acadêmico
st.subheader("📋 Classificação por Rendimento")
rendimento = df["Rendimento Acadêmico (Classificação)"].value_counts()
st.bar_chart(rendimento)

# Correlação entre Estudo e Notas
st.subheader("🔍 Relação: Estudo vs Nota Final")
fig2, ax2 = plt.subplots()
ax2.scatter(df["Horas de Estudo Semanais"], df["Nota Última Avaliação"], alpha=0.7)
ax2.set_xlabel("Horas de Estudo Semanais")
ax2.set_ylabel("Nota Última Avaliação")
ax2.set_title("Estudo x Nota Final")
st.pyplot(fig2)
