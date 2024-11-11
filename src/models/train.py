import pandas as pd

import argparse

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow

import warnings
warnings.filterwarnings("ignore")

def parse_arg():
    parser = argparse.ArgumentParser(description='Credit System ML Predictor')
    parser.add_argument(
        '--n-estimators',
        type=int,
        default=100,
        help='The number of trees in the forest.'
    )
    parser.add_argument(
        '--criterion',
        type=str,
        default='entropy',
        help='''
        The function to measure the quality of a split. 
        Supported criteria are “gini” for the Gini impurity 
        and “log_loss” and “entropy” both for the Shannon 
        information gain;
    '''
    )

    parser.add_argument(
        '--max-depth',
        type=int,
        default=5,
        help='''
        The maximum depth of the tree. If None, then nodes are 
        expanded until all leaves are pure or until all leaves 
        contain less than min_samples_split samples.  
    '''
    )
    return parser.parse_args()

data = pd.read_csv('data/preprocessed/preprocessed_data.csv')
data_target = pd.read_csv('data/feature_store/data_with_new_features.csv')

features = ['personal_loan', 'education', 'securities_account',
            'cd_account', 'online', 'age_bracket_name_Baby boomers',
            'age_bracket_name_Generation X', 'age_bracket_name_Generation Z',
            'age_bracket_name_Millennials', 'education_1', 'education_2',
            'education_3']

X, y = data[features], data_target['credit_card']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

def main():
    args = parse_arg()
    rf_params = {'n_estimators': args.n_estimators,
                 'criterion': args.criterion,
                 'max_depth': args.max_depth}

    mlflow.set_tracking_uri('http://127.0.0.1:5000')
    mlflow.set_experiment('best-model-prototype')

    with mlflow.start_run(run_name='RandomForestClassifier-CreditApproval'):
        mlflow.sklearn.autolog()
        rf_model = RandomForestClassifier(**rf_params)
        rf_model.fit(X_train, y_train)
        y_pred = rf_model.predict(X_test)

        acc = accuracy_score(y_pred, y_test)
        print('Acurácia: {}'.format(acc))
        mlflow.log_metric('Acurácia', acc)

if __name__ == '__main__':
    main()
