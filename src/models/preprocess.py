import pandas as pd
import numpy as np

from sklearn.preprocessing import OneHotEncoder, StandardScaler

try:
    df = pd.read_csv('data/feature_store/data_with_new_features.csv')
    print('1/4')
except FileNotFoundError as error:
    print()

numerical = ['age', 'experience', 'income', 'family', 'mortgage', 'cc_avg']

categorical = ['age_bracket_name', 'personal_loan', 'education_degree', 
               'securities_account', 'cd_account', 'online', 'credit_card']

df_numerical = df[numerical].copy()
df_categorical = df[categorical].copy()

cat_features_list = df_categorical.columns.tolist()
cat_features = [cat_features_list[0], cat_features_list[3]]
num_features = df_numerical.columns.tolist()[:-1]

scaler = StandardScaler()
encoder = OneHotEncoder(handle_unknown='ignore')
num_scaled = scaler.fit_transform(df_numerical[num_features])
cat_encoded = encoder.fit_transform(df_categorical[cat_features])

# PRECISO TERMINAR ISSO......