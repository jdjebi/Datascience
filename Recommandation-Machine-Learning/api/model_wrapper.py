import configparser, pickle

class VehiculeClassificaionModel:
    def __init__(self, config_path):

        config = configparser.ConfigParser()
        config.read(config_path)
        PATH_MODEL = config.get('Paths', 'PATH_MODEL')
        PATH_DATA_PREPROCESSOR = config.get('Paths', 'PATH_DATA_PREPROCESSOR')
        PATH_MODEL_SCHEMA = config.get('Paths', 'PATH_PROCESSED_SCHEMA')

        # Chargement du modèle
        with open(PATH_MODEL, 'rb') as file:
            self.model = pickle.load(file)

        # Chargement du pre-traiteur
        with open(PATH_DATA_PREPROCESSOR, 'rb') as file:
            self.data_preprocessor = pickle.load(file)
        
        # Chargement du schema
        with open(PATH_MODEL_SCHEMA, 'rb') as file:
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
