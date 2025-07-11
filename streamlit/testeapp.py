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
with st.sidebar:
    st.image(
        "post_fiap.png"
        , caption="Pós-Tech FIAP | Tech Challenge Fase 4 | Grupo 5"
        , width=220
    )
    escolha = option_menu(
        "Tech Challenge: Fase 5",
        ["Exploração e Insights", "Deploy", "Conclusão", "Referências"],
        icons=["bar-chart-line", "gear", "check2-square", "book"],
        menu_icon="laptop",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "0px", "background-color": "#0e1117"},
            "icon": {"color": "white", "font-size": "18px"},
            "nav-link": {"color": "white", "font-size": "16px", "text-align": "left"},
            "nav-link-selected": {"background-color": "#6c63ff"},
        }
    )   

    st.title('Grupo 5 - FIAP')
    st.write('''Integrantes:
- Anderson Silva
- Kelvyn Candido
- Evandro Garbin
- Sandra Hoja
- Michael''')