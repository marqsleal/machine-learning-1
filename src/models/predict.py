import mlflow
logged_model = 'src/models/mlartifacts/700678007511616763/48ffe9140fe84fd6ab247b80bce57ad2/artifacts/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd

data = pd.read_csv('data/preprocessed/preprocessed_data.csv')
features = ['personal_loan', 'education', 'securities_account',
            'cd_account', 'online', 'age_bracket_name_Baby boomers',
            'age_bracket_name_Generation X', 'age_bracket_name_Generation Z',
            'age_bracket_name_Millennials', 'education_1', 'education_2',
            'education_3']

predicted = loaded_model.predict(data[features])

data['predicted'] = predicted
data.to_csv('reports/approval_results.csv', index=False)
