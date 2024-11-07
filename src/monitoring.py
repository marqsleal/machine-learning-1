import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.outliers_influence import variance_inflation_factor


class DataMonitor:
    """
    Classe para análise e monitoramento de dados em um DataFrame.

    Métodos
    -------
    outliers_analysis(dataframe):
        Identifica e conta outliers em cada coluna numérica do DataFrame.

    multicolinearity_analysis(dataframe):
        Calcula o Fator de Inflação da Variância (VIF) para avaliar multicolinearidade nas colunas do DataFrame.
    """

    @staticmethod
    def outliers_analysis(dataframe):
        """
        Identifica e conta o número de outliers em cada coluna do DataFrame.

        Outliers são definidos como valores que estão além de 3 desvios padrão (Z-score > 3).

        Parâmetros
        ----------
        dataframe : pandas.DataFrame
            DataFrame com colunas numéricas para análise de outliers.

        Retorno
        -------
        pandas.Series
            Série com o número de outliers para cada coluna.
        """
        z_scores = stats.zscore(dataframe.select_dtypes(include=[np.number]))
        outliers = (abs(z_scores) > 3).sum()
        return outliers

    @staticmethod
    def multicolinearity_analysis(dataframe):
        """
        Calcula o Fator de Inflação da Variância (VIF) para detectar multicolinearidade entre variáveis.

        Parâmetros
        ----------
        dataframe : pandas.DataFrame
            DataFrame com colunas numéricas para análise de multicolinearidade.

        Retorno
        -------
        pandas.DataFrame
            DataFrame com cada coluna e seu respectivo VIF.
        """
        vif_data = pd.DataFrame()
        vif_data["feature"] = dataframe.columns
        vif_data["VIF"] = [variance_inflation_factor(dataframe.values, i) for i in range(dataframe.shape[1])]
        return vif_data

'''
Exemplo de uso das funções
df = seu DataFrame de dados
monitor = DataMonitor()
outliers = monitor.outliers_analysis(df)
vif = monitor.multicolinearity_analysis(df)

print("Análise de Outliers:")
print(outliers)
print("\nAnálise de Multicolinearidade (VIF):")
print(vif)
'''

