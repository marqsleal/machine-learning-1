"""
Este script realiza o pré-processamento de dados para um conjunto de características numéricas e categóricas.

Passos do pré-processamento:

1. Carregamento dos dados:
   - O arquivo CSV contendo as características é carregado em um DataFrame.

2. Separação dos dados:
   - O DataFrame é dividido em dois conjuntos: `df_numerical` contendo variáveis numéricas e `df_categorical` contendo variáveis categóricas.

3. Pré-processamento:
   - Uma transformação logarítmica é aplicada à coluna 'mortgage' utilizando a função `np.log1p` para tratamento de outliers.
   - As variáveis categóricas 'age_bracket_name' e 'education' são codificadas usando o `OneHotEncoder` do `sklearn`, com o parâmetro `handle_unknown='ignore'` para lidar com valores desconhecidos durante a transformação.

4. Concatação e salvamento:
   - As variáveis codificadas são unidas aos DataFrames numérico e categórico.
   - O DataFrame resultante é salvo em um arquivo CSV de pré-processamento.

Exceções:
- O código está preparado para lidar com erros ao carregar, separar, pré-processar e salvar os dados, imprimindo mensagens de erro específicas.

Notas:
- O código pressupõe que o arquivo CSV de entrada está no caminho correto e que as colunas indicadas existem no DataFrame.
- O processo de pré-processamento é simplificado e pode ser ajustado conforme necessário.
"""


import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.preprocessing import OneHotEncoder

# step-1: load data
try:
    df = pd.read_csv('data/feature_store/data_with_new_features.csv')
    print('Dados carregados com sucesso.')
except FileNotFoundError as load_error:
    print('{}: Erro ao carregar arquivo. Verifique o caminho do diretório.'.format(load_error))

# step-2: split dataframes
try:
    numerical = ['age', 'experience', 'income', 'family', 'mortgage']

    categorical = ['age_bracket_name', 'personal_loan', 'education', 
                'securities_account', 'cd_account', 'online']

    df_numerical = df[numerical].copy()
    df_categorical = df[categorical].copy()
    print('Separação de Dataframes: categóricos e numéricos.')
except Exception as split_df_error:
    print('{}: Ocorreu um erro ao separar os dataframes.'.format(split_df_error))

# step-3: preprocess
try:
    df_categorical['mortgage_log'] = np.log1p(df['mortgage'])
    encoder = OneHotEncoder(handle_unknown='ignore')
    X_encoded = encoder.fit_transform(df[['age_bracket_name', 'education']])
    print('Dados pré-processados com sucesso')
except Exception as err:
    print('{}: ocorreu um erro ao preprocessar os dados.'.format(err))

# step-4: concat and save dataset
try:
    df_encoded = pd.DataFrame(X_encoded.toarray(), columns=encoder.get_feature_names_out(['age_bracket_name', 'education']))

    df_categorical.reset_index(drop=True, inplace=True)
    df_numerical.reset_index(drop=True, inplace=True)

    df_preprocessed = pd.concat([df_categorical, df_numerical, df_encoded], axis=1)
    df_preprocessed.to_csv('data/preprocessed/preprocessed_data', index=False)
    print('Dados salvos com sucesso')
except FileNotFoundError as save_error:
    print('{}: Ocorreu um erro ao salvar o arquivo. Verifique o caminho do diretório'.format(save_error))
    