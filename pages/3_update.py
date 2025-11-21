import streamlit as st 
import utils
import pandas as pd 

if 'aluno_data' not in st.session_state:
    st.session_state.aluno_data = pd.DataFrame() 
if 'cpf_pesquisado' not in st.session_state:
    st.session_state.cpf_pesquisado = ""

st.set_page_config(page_title="Cadastro de Alunos",
                   layout='wide')

col1, col2, col3 = st.columns([1, 1.45, 1])

with col2:
    
    with st.form(key="Consulta_form"):
        st.subheader('Pesquisar Aluno')
        search_cpf = st.text_input("CPF do Aluno", placeholder="Digite o CPF ou parte dele")
        search_button = st.form_submit_button(label="PESQUISAR")

        if search_button:
        
            data = utils.get_filtered_data(search_cpf) 
            
            if data.empty:
                st.session_state.aluno_data = pd.DataFrame()
                st.error(" Aluno não encontrado ou CPF inválido.")
            elif len(data) > 1:
            
                st.warning("Múltiplos resultados encontrados. Refine a pesquisa.")
                st.dataframe(data)
                st.session_state.aluno_data = pd.DataFrame()
            else:
              
                st.session_state.aluno_data = data.iloc[0]
                st.session_state.cpf_pesquisado = data.iloc[0]['cpf']
                st.success(f"Aluno **{st.session_state.aluno_data['nome_completo']}** pronto para edição.")

 
    if not st.session_state.aluno_data.empty:
        aluno = st.session_state.aluno_data
        
        with st.form(key="Atualizacao_form"):
            st.subheader(f'Atualizar: {aluno["nome_completo"]}')

          
            name = st.text_input('Nome completo', value=aluno['nome_completo'])
            
       
            cpf_key = st.text_input('CPF (Chave)', value=aluno['cpf'], disabled=True) 
            
            phone = st.text_input('TELEFONE', value=aluno['telefone'])
            
            
            rotation = st.selectbox('Turno', options=['Manhã', 'Tarde','Noite'], 
                                    index=['Manhã', 'Tarde','Noite'].index(
                                        aluno['turno']))

            payment = st.selectbox('Forma de Pagamento', 
                                   options=['Ainda não especificado',
                                            'Avista', 'Parcelado'], 
                                   index=['Ainda não especificado',
                                          'Avista', 'Parcelado'].index(aluno['pagamento']))

            process_part = st.selectbox('Parte do processo', 
                                        options=['Teorico', 'Prático A', 
                                                 'Pratico B', 'Prático D'], 
                                        index=['Teorico', 'Prático A', 'Pratico B', 
                                               'Prático D'].index(aluno['parte_processo']))
            
            update_button = st.form_submit_button(label="ATUALIZAR DADOS")

            if update_button:
                
                utils.update_student(
                    cpf=aluno['cpf'], 
                    new_name=name, 
                    new_phone=phone, 
                    new_rotation=rotation, 
                    new_payment=payment, 
                    new_process_part=process_part
                )
                st.success("✨ Cadastro atualizado com sucesso!")
                
                st.session_state.aluno_data = pd.DataFrame() 
                st.rerun()