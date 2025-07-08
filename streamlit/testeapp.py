import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="Sistema de Recomendação de Talentos",
    page_icon=":bookmark_tabs:",
    layout="wide"
)
st.title("\U0001F4D1 Dashboard de Matching entre Vagas e Candidatos")
st.subheader("\U0001F50E Selecione uma vaga na aba lateral para visualizar os candidatos mais compatíveis")


st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            overflow-y: hidden;
        }
        .stProgress > div > div > div > div {
            background-color: #6c63ff;
        }
        .warning-box {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
