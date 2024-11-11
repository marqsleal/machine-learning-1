import mlflow
logged_model = 'src/models/mlartifacts/748753631065908979/05ca3b89e6bb461084eb01860798b4c4/artifacts/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd

data = pd.read_csv('data/preprocessed/preprocessed_data_combined.csv')

features = ['personal_loan','securities_account','cd_account','online',
            'cat__age_bracket_name_Baby boomers','cat__age_bracket_name_Generation X',
            'cat__age_bracket_name_Generation Z','cat__age_bracket_name_Millennials',
            'cat__education_ensino_medio','cat__education_ensino_superior',
            'cat__education_pos_graduacao']

predicted = loaded_model.predict(data[features])

data['predicted'] = predicted
data.to_csv('reports/approval_results.csv', index=False)
