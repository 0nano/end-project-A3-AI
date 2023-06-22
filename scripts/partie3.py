import sys
import pandas as pd
from sklearn.cluster import KMeans
import json
import numpy as np


# Fonction de prédiction de gravité d'accident
def predict_accident_gravity(accident_info, classification_method, best_model_svm, best_model_rf, best_model_mlp):
    # Utiliser la méthode de classification spécifiée
    if classification_method == "SVM":
        prediction = best_model_svm.predict(accident_info)
    elif classification_method == "RF":
        prediction = best_model_rf.predict(accident_info)
    elif classification_method == "MLP":
        prediction = best_model_mlp.predict(accident_info)
    else:
        #Méthode de classification non prise en charge
        return None
    
    # Créer un dictionnaire contenant la prédiction de gravité
    result = {"gravitée": prediction}
    
  # Conversion du dictionnaire en JSON
json_output = json.dumps(result)
print(json_output)
