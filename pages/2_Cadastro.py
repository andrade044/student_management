import streamlit as st 
import utils

st.set_page_config(page_title="Cadastro de Alunos",
                   layout='wide')

col1, col2, col3 = st.columns([1, 1.45, 1])

with col2:
    
    with st.form(key="Cadastro_form"):
        st.subheader('Informações pessoais')

        name = st.text_input('Nome completo',
                         placeholder='Nome Completo')

        cpf = st.text_input('CPF', label_visibility='visible',
                         placeholder='CPF',)
        
        phone = st.text_input('TELEFONE',
                         placeholder='TELEFONE')
        
        rotation = st.selectbox('Turno',options=['Manhã', 'Tarde','Noite'])

        payment = st.selectbox('Forma de Pagamento', 
                               options=['Ainda não especificado',
                                        'Avista', 'Parcelado'])

        process_part = st.selectbox('Parte do processo', 
                                    options=['Teorico', 'Prático A', 
                                             'Pratico B', 'Prático D'])

        submit_button = st.form_submit_button(label='Cadastrar')

        if submit_button:
            
            if not name or not cpf or not phone:
                st.error('Nome, CPF ou Telefone são campos obrigatórios')
            else:
                try:
                    utils.register_student(cpf=cpf,
                                        name=name,
                                        phone=phone,
                                        rotation=rotation,
                                        payment=payment,
                                        process_part=process_part)        
                    st.success('Aluno cadastrado')
                except Exception as e:
                    if "UNIQUE constraint failed: alunos.cpf" in str(e):
                        st.error("CPF já existe")
                    else:
                        st.error('Erro desconhecido')