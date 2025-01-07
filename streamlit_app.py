import streamlit as st
import pickle
import numpy as np
import pandas as pd
import joblib
from io import BytesIO
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill

# --- Page Configuration ---
st.set_page_config(
    page_title="Concrete Strength Prediction with Confidence Intervals (v2.0)",
    page_icon="https://raw.githubusercontent.com/dimasbetioli/concrete-ia-app/refs/heads/main/mult.png",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --- Add Image Header ---
st.image(
    "https://raw.githubusercontent.com/dimasbetioli/concrete-ia-app/refs/heads/main/topo.png",
    use_container_width=True,
)

# --- Main Title ---
st.markdown(
    "<h1 style='text-align: center; color: #2196F3; font-size: 30px;'> PROJECT - AI Applied to Predicting Concrete Strength at 28 Days (v2.0)</h1>",
    unsafe_allow_html=True,
)

# --- Introduction ---
st.markdown(
    '<h3 style="text-align: center; color: #2C2C2C; font-size: 14px; margin-bottom: 20px;">Team led by Prof André C.P.L.F. de Carvalho</h3>',
    unsafe_allow_html=True,
)

# --- Input Options: Manual or Excel File ---
st.markdown(
    """
    <p style="text-align: center; font-size: 16px; color: #2C2C2C;">
    <span style="font-size: 30px; color: #4CAF50;">&#8595;</span> Choose whether to enter data manually or upload an Excel file <span style="font-size: 30px; color: #4CAF50;">&#8595;</span>
    </p>
    """,
    unsafe_allow_html=True,
)

# --- Session State for User Choices ---
if 'tipo_entrada' not in st.session_state:
    st.session_state.tipo_entrada = None

# --- Center and Align Buttons Side-by-Side ---
col1, col2 = st.columns(2)
with col1:
    if st.button("Enter Data Manually"):
        st.session_state.tipo_entrada = "Enter Manually"

with col2:
    if st.button("Upload Excel File"):
        st.session_state.tipo_entrada = "Upload Excel"

# --- Add Space Above Button ---
st.markdown("<div style='margin-top: 30px;'></div>", unsafe_allow_html=True)

# --- Conditional Logic Based on User Choice ---
if st.session_state.tipo_entrada == "Enter Manually":
    st.write("You chose to enter data manually.")

    # --- Input Options ---
    opcao = st.radio(
        "Choose input configuration:",
        [
            "CT_Cimento e CT_Agua (Cement and Water)",
            "CT_Cimento, CT_Agua, e resistências reais (3d, 7d, 28d) (Cement, Water, and Real Strengths)",
            "CT_Cimento, CT_Agua, resistências reais, e Fc_7d (Cement, Water, Real Strengths, and Fc_7d)",
            "CT_Cimento, CT_Agua, resistências reais, Fc_7d, e aditivos (Cement, Water, Real Strengths, Fc_7d, and Additives)",
            "Todas as variáveis (All Variables)"
        ]
    )

    entradas = []
    model_path = ""

    # --- Session State for Inputs ---
    if 'entradas' not in st.session_state:
        st.session_state.entradas = []

    if opcao == "CT_Cimento e CT_Agua (Cement and Water)":
        model_path = "models/model_quant_0.500_set1.pkl"
        st.session_state.entradas = [
            # ... (inputs conforme a versão anterior)
        ]

    # Botão para calcular
    if st.button("Calcular Resistência"):
        if all(isinstance(v, (int, float)) and v > 0 for v in st.session_state.entradas):  # Verifica se são números positivos
            try:
                model_mediana = joblib.load(model_path)
                model_inf = joblib.load(model_path.replace("0.500", "0.025")) #Carrega o modelo de quantil inferior
                model_sup = joblib.load(model_path.replace("0.500", "0.975")) #Carrega o modelo de quantil superior

                entrada = np.array([st.session_state.entradas])
                mediana = model_mediana.predict(entrada)[0]
                inferior = model_inf.predict(entrada)[0]
                superior = model_sup.predict(entrada)[0]

                st.success(f"A resistência prevista do concreto aos 28 dias é: **{mediana:.2f} MPa**")
                st.write(f"Intervalo de confiança de 95%: [{inferior:.2f} MPa, {superior:.2f} MPa]")

            except FileNotFoundError:
                st.error("Modelo não encontrado. Verifique o caminho do modelo.")
            except Exception as e:
                st.error(f"Erro ao carregar o modelo ou realizar a predição: {e}")
        else:
            st.error("Por favor, insira valores numéricos positivos válidos para todas as variáveis.")


elif st.session_state.tipo_entrada == "Upload Excel":
    # ...(resto do código para upload de excel conforme a versão anterior)

    if uploaded_file is not None:
        #...(resto do código para processar excel conforme a versão anterior)

        try:
            #...(resto do código para escolher modelo conforme a opção escolhida)

            # Carregar os modelos (mediana, inferior e superior)
            model_mediana = joblib.load(model_path)
            model_inf = joblib.load(model_path.replace("0.500", "0.025"))
            model_sup = joblib.load(model_path.replace("0.500", "0.975"))

            # Selecionar as colunas relevantes e preparar os dados para previsão
            input_data = df[selected_columns]
            X = input_data.values

            # Fazer as previsões para mediana e intervalo
            previsoes_mediana = model_mediana.predict(X)
            previsoes_inferior = model_inf.predict(X)
            previsoes_superior = model_sup.predict(X)

            # Adicionar as previsões ao DataFrame
            input_data["Previsão (Mediana)"] = previsoes_mediana
            input_data["Limite Inferior (95%)"] = previsoes_inferior
            input_data["Limite Superior (95%)"] = previsoes_superior

            #...(resto do código para exibir e salvar o excel conforme a versão anterior)

        except FileNotFoundError:
            st.error("Modelo não encontrado. Verifique o caminho do modelo.")
        except Exception as e:
            st.error(f"Erro ao realizar a previsão: {e}")
