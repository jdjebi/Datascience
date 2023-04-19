import mlflow
import configparser, os, pickle
import numpy as np

class VehiculeClassificaionModel:
    def __init__(self, config_path):

        config = configparser.ConfigParser()
        config.read(config_path)
        PATH_DATA_PREPROCESSOR = config.get('Paths', 'PATH_DATA_PREPROCESSOR')
        PATH_PROCESSED_SCHEMA = config.get('Paths', 'PATH_PROCESSED_SCHEMA')
        DIR_MLRUNS = config.get('Paths', 'DIR_MLRUNS')
        MODEL_NAME = config.get('Models', 'MODEL_NAME')
        MODEL_VERSION = config.getint('Models', 'MODEL_VERSION')

        mlflow.set_tracking_uri("file:" + os.path.abspath(DIR_MLRUNS))
        self.model = mlflow.pyfunc.load_model(model_uri=f"models:/{MODEL_NAME}/{MODEL_VERSION}")

        # Chargement du pre-traiteur
        with open(PATH_DATA_PREPROCESSOR, 'rb') as file:
            self.data_preprocessor = pickle.load(file)
        
        # Chargement du schema
        with open(PATH_PROCESSED_SCHEMA, 'rb') as file:
            self.data_schema = pickle.load(file)
            self.labels_map = self.data_schema["categories_map"]

    def predict(self, X):
        self.X_base = X.copy()
        X = self.preprocess(X)
        result = self.model.predict(X)
        return result

    def preprocess(self, X):
        X.loc[X.situationFamiliale == "C�libataire","situationFamiliale"] = "Célibataire"
        X = self.data_preprocessor.transform(X)        
        return X

    def postprocess(self, result):
        X =  self.X_base.copy()
        X["vehicule_categorie_id"] = result
        X["vehicule_categorie_label"] = X.vehicule_categorie_id.map(self.labels_map)
        return X
