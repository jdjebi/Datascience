# Data Scientist Junior en MSc Big Data à l'ESTIA

Ce dépôt GitHub contient des projets de Data Science sur lesquels j'ai travaillé au cours de mon parcours professionnel et académique. Les projets sont organisés par type et sont décrits brièvement ci-dessous. 

Voici une liste de mes projets, classés par type :

| Projet | Type | Outils | Meilleur modèle | Précision |
| ------ | ---- | ------ | ---------------| --------- |
| Analyse et classification de critiques de films | NLP | Scikit-Learn, NLTK, Gensim, Spacy | Regression logistique | 89% |
| Détection de médicaments défectueux | Deep Learning | TensorFlow, PyTorch | CNN avec TensorFlow | 92% |
| Analyse de la clientèle d'un concessionnaire et recommandation de véhicules | Machine Learning | Scikit-Learn, Hadoop/Spark, MongoDB, Oracle, HDFS, Mlflow, Docker, Flask | Clustering : KMeans, Recommandation : RandomForest | Clustering : 72%, Recommandation : 74%  |
| Prédiction de l'affluence sur des lignes de bus | Machine Learning/ Deep Learning | Scikit-Learn, Keras | RandomForestRegressor | 50% |
| Prédiction des salaires à partir des descriptions de postes | NLP | Scikit-Learn | Ridge | 81% |


Chaque projet comprend un résumé, des détails sur les outils utilisés et un lien vers le code sur Github. N'hésitez pas à y jeter un coup d'œil !

## Projet de NLP

### Analyse et classification de critiques de films, NLP
ESTIA, Bidart
- Nettoyage et tokenisation des données
- Mise en place d'un pipeline de transformation des données
- Entraînement d'un modèle de classification, précision de 89%
Outils: Scikit-Learn, NLTK, Gensim, Spacy
Source: https://github.com/jdjebi/Datascience/tree/main/Analyse-de-sentiments-NLP

### Prédiction des salaires à partir des descriptions de postes
- Nettoyage et tokenisation des descriptions
- Entraînement d'un modèle de prédiction de salaire basé sur la vectorisation de mots avec un modèle TfidVectorizer (Précision du modèle 81%)
Outils: Scikit-Learn, TfidVectorizer
Source: https://github.com/jdjebi/Datascience/tree/main/Prediction-de-salaire

## Projet de Deep Learning

### Détection de médicaments défectueux, Deep Learning
AI4Industry, Proditec
- Génération de 30000 images à partir de 1000 via la Data Augmentation
- Définition de deux modèles de type CNN avec PyTorch et Tensorflow
- Entraînement des modèles et comparaison des résultats
- Test du meilleur modèle sur les données de test, précision 92%
Outils: TensorFlow, PyTorch
Source: https://github.com/jdjebi/Datascience/tree/main/Detection-medicaments-defecteux-Deep-Learning

## Projets de Machine Learning

### Analyse de la clientèle d'un concessionnaire et recommandation de véhicules, Machine Learning
- Construction d'un Datalake pour l'analyse de la clientèle
- Nettoyage et transformation des données du Datalake
- Exploration et visualisation des données des clients et du catalogue de véhicules
- Entraînement d'un modèle de clustering des véhicules, précision 72%
- Entraînement d'un modèle de recommandation, précision de 74%
- Déploiement du meilleur modèle sous forme d'API
Outils: Scikit-Learn, Hadoop/Spark, MongoDB, Oracle, HDFS, Mlflow, Docker, Flask
Source: https://github.com/jdjebi/Datascience/tree/main/Recommandation-Machine-Learning

N'hésitez pas à me contacter si vous avez des questions ou des commentaires sur l'un de ces projets. 

### Détection de médicaments défectueux, Deep Learning
- Étude de la série temporelle de l'activité des bus de 2019 à 2023
- Entraînement d'un modèle prédiction de l'affluence pour chaque ligne de bus, pour les 3 prochains jours avec une précision de 80%
Outils: TensorFlow, PyTorch
Source: https://github.com/jdjebi/Datascience/tree/main/Prediction-affluence-bus-Machine%20Learning-Deep%20Learning

