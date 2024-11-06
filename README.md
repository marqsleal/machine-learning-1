## Machine Learning I - Santander Coders 2024: Trilha de Ciência de Dados

![Python](https://img.shields.io/badge/Python-3776AB.svg?style=for-the-badge&logo=Python&logoColor=white)![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=for-the-badge&logo=pandas&logoColor=white)![Numpy](https://img.shields.io/badge/NumPy-013243.svg?style=for-the-badge&logo=NumPy&logoColor=white)![Sklearn](https://img.shields.io/badge/scikitlearn-F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)![Mlflow](https://img.shields.io/badge/MLflow-0194E2.svg?style=for-the-badge&logo=MLflow&logoColor=white)

![Docker](https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white)![GithubActions](https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=for-the-badge&logo=GitHub-Actions&logoColor=white)![GoogleCloud](https://img.shields.io/badge/Google%20Cloud-4285F4.svg?style=for-the-badge&logo=Google-Cloud&logoColor=white)


### Sobre o Projeto

Este projeto visa desenvolver um sistema preditivo para auxiliar na avaliação de crédito. Utilizando algoritmos de Machine Learning, o projeto tem dois objetivos principais: prever o score de crédito de um cliente, em um problema de regressão, e construir um modelo de classificação para determinar a aprovação ou não de crédito para clientes específicos. Este projeto pode ajudar a tomar decisões mais rápidas e assertivas, reduzindo o risco de inadimplência e otimizando a alocação de crédito.

### O Conjunto de Dados

Os dados consistem em informações pessoais e financeiras dos clientes, detalhando características relevantes para avaliação de crédito. As principais colunas dos dados incluem:

```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 14 columns):
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   ID                  5000 non-null   int64  
 1   Age                 5000 non-null   int64  
 2   Experience          5000 non-null   int64  
 3   Income              5000 non-null   int64  
 4   ZIP.Code            5000 non-null   int64  
 5   Family              5000 non-null   int64  
 6   CCAvg               5000 non-null   float64
 7   Education           5000 non-null   int64  
 8   Mortgage            5000 non-null   int64  
 9   Personal.Loan       5000 non-null   int64  
 10  Securities.Account  5000 non-null   int64  
 11  CD.Account          5000 non-null   int64  
 12  Online              5000 non-null   int64  
 13  CreditCard          5000 non-null   int64  
dtypes: float64(1), int64(13)
memory usage: 547.0 KB

```

### Problema de Negócio

O setor de crédito apresenta um risco significativo para instituições financeiras, que buscam minimizar a concessão de crédito para clientes de alto risco. O problema de negócio que este projeto pretende resolver é: como prever o score de crédito dos clientes e, com base nesse score e em outras variáveis, decidir se um cliente deve ou não receber aprovação de crédito. Uma avaliação de crédito mais precisa permite que a instituição tome decisões mais informadas e minimize o risco de inadimplência, além de melhorar a experiência dos clientes de baixo risco com um processo de aprovação mais ágil.

### Objetivos

1. **Prever o Score de Crédito**: Desenvolver um modelo de regressão que preveja o score de crédito dos clientes, levando em conta variáveis demográficas e financeiras. O objetivo é fornecer uma estimativa do score para clientes atuais e potenciais.

2. **Decidir a Aprovação de Crédito**: Desenvolver um modelo de classificação que determine se um cliente deve ou não receber aprovação de crédito. Esse modelo será alimentado pelo score de crédito previsto e outras variáveis relevantes.

3. **Melhorar o Processo de Avaliação de Crédito**: Automatizar o processo de análise de crédito com base em dados históricos e algoritmos preditivos, permitindo decisões mais rápidas e embasadas para aprovação de crédito.

Autores: Mille, Mileno, Maria, Gabriel, Juan
