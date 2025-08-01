import streamlit as st
import dados


st.title("Filmes")

nome= st.text_input("Nome do filme : ")
ano= st.number_input("Ano de lançamento: ",min_value=2000 , max_value=2025)
nota= st.slider("Pontuação do filme: ", min_value=0.0 , max_value=10.0 )

if st.button('Adicionar'):
    dados.inserir_dados(nome,ano,nota)
    st.success('Filme registrado')
elif st.button('Cancelar'):
    pass
    
    
filmes= dados.lista_dados()
st.header("Lista de Filmes")
st.table(filmes)