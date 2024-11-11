import streamlit as st
import pandas as pd
import mlflow


logged_model = 'src/models/mlartifacts/700678007511616763/48ffe9140fe84fd6ab247b80bce57ad2/artifacts/model'
loaded_model = mlflow.pyfunc.load_model(logged_model)

st.markdown("### Sistema de Aprovação de Crédito :credit_card:")

personal_loan = st.selectbox("Empréstimo Pessoal:", ["Sim", "Não"])
education = st.selectbox("Nível Educacional:", ["Ensino Médio", "Ensino Superior", "Pós-Graduação"])
securities_account = st.selectbox("Possui Conta de Títulos:", ["Sim", "Não"])
cd_account = st.selectbox("Possui Conta CD:", ["Sim", "Não"])
online = st.selectbox("Conta Online:", ["Sim", "Não"])
age_bracket_name = st.selectbox("Faixa Etária:", ["Baby boomers", "Generation X", "Generation Z", "Millennials"])

personal_loan = 1 if personal_loan == "Sim" else 0
securities_account = 1 if securities_account == "Sim" else 0
cd_account = 1 if cd_account == "Sim" else 0
online = 1 if online == "Sim" else 0

education_map = {"Ensino Médio": 1, "Ensino Superior": 2, "Pós-Graduação": 3}
education = education_map[education]

age_bracket_map = {
    "Baby boomers": [1, 0, 0, 0],
    "Generation X": [0, 1, 0, 0],
    "Generation Z": [0, 0, 1, 0],
    "Millennials": [0, 0, 0, 1]
}
age_bracket_encoded = age_bracket_map[age_bracket_name]

education_encoded = [1 if education == i else 0 for i in range(1, 4)]

input_data = pd.DataFrame([[
    personal_loan,
    education,
    securities_account,
    cd_account,
    online,
    *age_bracket_encoded,
    *education_encoded
]], columns=['personal_loan', 'education', 'securities_account',
             'cd_account', 'online', 'age_bracket_name_Baby boomers',
             'age_bracket_name_Generation X', 'age_bracket_name_Generation Z',
             'age_bracket_name_Millennials', 'education_1', 'education_2',
             'education_3'])

if st.button("Verificar Aprovação de Crédito"):
    prediction = loaded_model.predict(input_data)[0]
    
    if prediction == 1:
        st.success("Crédito Aprovado!")
    else:
        st.error("Crédito Negado.")
