import pandas as pd
import numpy as np


# step-1: load data

try:
    df = pd.read_csv('data/external/bankloan.csv')
    print('Dados carregados com sucesso.')
except Exception as load_error:
    print('{}: Erro ao caregar os dados. Erro tipo 001.'.format(load_error))

# step-2: standardizing columns

try:
    rename_columns = {
                    'Age': 'age',
                    'Experience': 'experience',
                    'Income': 'income',
                    'ZIP.Code': 'zip_code',
                    'Family': 'family',
                    'CCAvg': 'cc_avg',
                    'Education': 'education',
                    'Mortgage': 'mortgage',
                    'Personal.Loan': 'personal_loan',
                    'Securities.Account': 'securities_account',
                    'CD.Account': 'cd_account',
                    'Online': 'online',
                    'CreditCard': 'credit_card'
                    
                    }

    df = df.rename(columns=rename_columns)
    print('Colunas padronizadas')
except Exception as standardize_columns_error:
    print('{}: Erro ao padronizar colunas. Erro tipo 002.'.format(standardize_columns_error))

# step-3: creating new features

df.loc[df['experience'] < 0, 'experience'] = 0

def age_bracket(age: int) -> int:
    if age >= 78:
        return 5
    elif age >= 59:
        return 4
    elif age >= 43:
        return 3
    elif age >= 27:
        return 2
    else:
        return 1


def age_bracket_str(age_bracket: int) -> str:
    if age_bracket == 1:
        return 'Generation Z'
    elif age_bracket == 2:
        return 'Millennials'
    elif age_bracket == 3:
        return 'Generation X'
    elif age_bracket == 4:
        return 'Baby boomers'
    else:
        return 'Silent generation'


# Avaliar métrica usada para crédito, placeholde
def age_bracket_credit_expected(age_bracket: int) -> int:
    if age_bracket == 1:
        return 665
    elif age_bracket == 2:
        return 687
    elif age_bracket == 3:
        return 710
    elif age_bracket == 4:
        return 746
    else:
        return 750


try:
    df['age_bracket'] = df['age'].apply(age_bracket)
    df['age_bracket_name'] = df['age_bracket'].apply(age_bracket_str)
    df['income_per_family_member'] = df['income'] / (df['family'] + 1)
    df['cc_to_income_ratio'] = df['cc_avg'] / df['income']
    df['debt_to_income_ratio'] = (df['cc_avg'] + df['mortgage']) / df['income']
    df['financial_maturity_index'] = (df['income'] / df['cc_avg'])
    print('Novas features adicionadas.')
except Exception as feature_eng_error:
    print('{}: Ocorreu um erro ao criar novas features. Erro tipo 003.'.format(feature_eng_error))

# step-4: to treat infinity values
try:
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    print('Não há valores infinitos.')
except Exception as inf_error:
    print('{}: Ocorreu um erro ao tratar os valores tendendo ao infinito. Erro tipo 004.'.format(inf_error))

# step-5: saving data with new features
df.to_csv('data/feature_store/data_with_new_features.csv', index=False)
