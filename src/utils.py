import os
import sys
import numpy as np
import pandas as pd
import dill
import pickle
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import r2_score



from src.exception import CustomException

#for creating the file and dumpp it
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path,'wb') as file_obj:
            #used to store the pickel file in harddisk
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_model(X_train, y_train,X_test, y_test, models, param):
    try:
        X_train, X_test, y_train, y_test = train_test_split(
            X_train, y_train , test_size = 0.2, random_state = 42
        )
        report = {}

        for i in range(len(list(models))):

            model = list(models.values())[i]
            para = param[list(models.keys())[i]]

            gs = GridSearchCV(model, para, cv =3)
            gs.fit(X_train, y_train)

            #selecting the best parameters
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        raise CustomException(e, sys)
    

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        raise CustomException(e, sys)
