import streamlit as st
import requests

API_URL = "https://debs-barros-flowise-ia.hf.space/api/v1/prediction/0e888b3d-5ad7-4dcd-9692-770e67561440"

# Consultar a API
def query(payload):
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

# Interface
st.title("OWASPIFY")
st.write("Digite uma pergunta:")

question = st.text_input("Pergunta:", "")

if st.button("Enviar"):
    if question:
        output = query({"question": question})  
        if "error" in output:
            st.error(f"Erro: {output['error']}")
        else:
            st.write("Resposta:", output.get("text", "Resposta não disponível")) 
    else:
        st.warning("Por favor, digite uma pergunta.")
