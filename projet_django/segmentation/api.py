
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler
import os
import sys  


model_path = os.path.join(os.path.dirname(__file__), 'kmeans_model.pkl')
model = joblib.load(model_path)
scaler = StandardScaler()
scaler.mean_ = np.array([35.0, 60.0, 50.0])  # moyenne
scaler.scale_ = np.array([10.0, 20.0, 25.0])  #  écarts-types

def predire_segment(age, revenu, score):
    data = np.array([[age, revenu, score]])
    data_scaled = scaler.transform(data)
    cluster = model.predict(data_scaled)[0]
    
    segments = {
        0: 'Jeunes à fort achat',
        1: 'Seniors riches',
        2: 'Clients moyens',
        3: 'Jeunes peu engagés',
        4: 'Gros consommateurs'
    }
    return segments.get(cluster, "Segment  inconnu")


print(predire_segment(30, 70, 80))  # Exemple d'utilisation