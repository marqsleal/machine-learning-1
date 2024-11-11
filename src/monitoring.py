import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
import xgboost
from sklearn.model_selection import train_test_split
import numpy as np
import scipy.stats as stats
from statsmodels.stats.outliers_influence import variance_inflation_factor


data = pd.read_csv('data/preprocessed/preprocessed_data_combined.csv')

features = ['personal_loan','securities_account','cd_account','online',
            'cat__age_bracket_name_Baby boomers','cat__age_bracket_name_Generation X',
            'cat__age_bracket_name_Generation Z','cat__age_bracket_name_Millennials',
            'cat__education_ensino_medio','cat__education_ensino_superior',
            'cat__education_pos_graduacao']

X, y = data[features], data['credit_card']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

xgb_params = {'learning_rate': 0.01,
                'max_depth': 3,
                'n_estimators': 100}

xgb_model = xgboost.XGBClassifier(**xgb_params)
xgb_model.fit(X_train, y_train)
y_pred_xgb = xgb_model.predict(X_test)

class Monitor:
    @staticmethod
    def outliers_analysis(dataframe):
        z_scores = stats.zscore(dataframe.select_dtypes(include=[np.number]))
        outliers = (abs(z_scores) > 3).sum()
        return outliers


    @staticmethod
    def multicolinearity_analysis(dataframe):
        vif_data = pd.DataFrame()
        vif_data["feature"] = dataframe.columns
        vif_data["VIF"] = [variance_inflation_factor(dataframe.values, i) for i in range(dataframe.shape[1])]
        return vif_data


monitor = Monitor()

st.title("Monitoramento de Métricas e Dados")

st.subheader("Análise de Outliers")
outliers = monitor.outliers_analysis(data)
fig, ax = plt.subplots()
outliers.plot(kind='bar', ax=ax)
ax.set_title("Número de Outliers por Coluna")
st.pyplot(fig)

st.subheader("Análise de Multicolinearidade")
vif_data = monitor.multicolinearity_analysis(X)
fig, ax = plt.subplots()
sns.barplot(x='VIF', y='feature', data=vif_data, ax=ax)
ax.set_title("VIF por Feature")
st.pyplot(fig)

st.subheader("Relatório de Classificação")
classif_report = classification_report(y_test, y_pred, output_dict=True)
report_df = pd.DataFrame(classif_report).transpose()
st.write(report_df)

st.subheader("Matriz de Confusão")
conf_matrix = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", ax=ax)
ax.set_title("Matriz de Confusão")
ax.set_xlabel("Predito")
ax.set_ylabel("Verdadeiro")
st.pyplot(fig)
