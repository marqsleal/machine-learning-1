import pandas as pd

import argparse

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import xgboost
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
import mlflow

import warnings
warnings.filterwarnings("ignore")

def parse_arg():
    parser = argparse.ArgumentParser(description='Credit System ML Predictor')
    parser.add_argument(
        '--learning-rate',
        type=float,
        default=0.01,
        help="""
    In machine learning and statistics, the learning rate is a tuning parameter
    in an optimization algorithm that determines the step size at each iteration
    while moving toward a minimum of a loss function.
    """
    )
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
        default=3,
        help='''
        The maximum depth of the tree. If None, then nodes are 
        expanded until all leaves are pure or until all leaves 
        contain less than min_samples_split samples.  
    '''
    )
    parser.add_argument(
        '--random-state',
        type=int,
        default=42,
        help='''
        Controls both the randomness of the bootstrapping of the 
        samples used when building trees (if bootstrap=True) and 
        the sampling of the features to consider when looking for 
        the best split at each node (if max_features < n_features). 
    '''
    )
    parser.add_argument(
        '--class-weight',
        type=dict,
        default=None,
        help='''
        Weights associated with classes in the form "class_label: weight". 
        If not given, all classes are supposed to have weight one. 
        For multi-output problems, a list of dicts can be provided in the 
        same order as the columns of y. 
    '''
    )
    parser.add_argument(
        '--max-features',
        type=str,
        default='sqrt',
        help='''
        The number of features to consider when looking for the best split
    '''
    )


    return parser.parse_args()

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

def main():
    args = parse_arg()

    xgb_params = {'learning_rate': args.learning_rate,
                  'max_depth': args.max_depth,
                  'n_estimators': args.n_estimators}
    
    mlflow.set_tracking_uri('http://127.0.0.1:5000')
    mlflow.set_experiment('xgb-classifier')

    with mlflow.start_run(run_name='XGBClassifier-CreditApproval'):
        mlflow.xgboost.autolog()
        xgb_model = xgboost.XGBClassifier(**xgb_params)
        xgb_model.fit(X_train, y_train)
        y_pred_xgb = xgb_model.predict(X_test)

        acc = accuracy_score(y_pred_xgb, y_test)
        precision = precision_score(y_pred_xgb, y_test)
        recall = recall_score(y_pred_xgb, y_test)
        f1 = f1_score(y_pred_xgb, y_test)
        print('>>> Acurácia do XGBClassifier: {}'.format(acc))
        print('>>> Precisão do XGBClassifier: {}'.format(precision))
        print('>>> Revocação do XGBClassifier: {}'.format(recall))
        print('>>> F1 Score do XGBClassifier: {}'.format(f1))
        mlflow.log_metric('Acurácia', acc)
        mlflow.log_metric('Precisão', precision)
        mlflow.log_metric('Revocação', recall)
        mlflow.log_metric('F1 Score', f1)

if __name__ == '__main__':
    main()
