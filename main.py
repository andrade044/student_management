import streamlit as st 
import utils
import pandas as pd 
import sqlite3


st.set_page_config(page_title="Controle de Alunos", 
                   layout='wide')
data_path = "alunos.db"
conn = sqlite3.connect(data_path)


col1, col2, col3 = st.columns([1, 1.45, 1])

with col2:
    

    with st.form(key="Conulta_aluno"):
        cpf = st.text_input("CPF aluno", placeholder="CPF ALuno")
        submit_button = st.form_submit_button(label="PESQUISAR")

        if submit_button:
            data = utils.get_filtered_data(cpf)
            if data.empty:
                st.warning(f"Não existe nenhum aluno com esse cpf **{cpf}**.")
            else:
                st.success(f'Consulta realizada, {len(data)} registros encontrados ')
                st.dataframe(data)