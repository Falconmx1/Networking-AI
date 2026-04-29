"""Entrenamiento de modelos IA con datos de red"""
import numpy as np
import pickle
import os
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class NetworkModelTrainer:
    def __init__(self, model_path='models/'):
        self.model_path = model_path
        os.makedirs(model_path, exist_ok=True)
        
    def train_isolation_forest(self, training_data):
        """Entrena modelo Isolation Forest"""
        # training_data debería ser lista de vectores de características
        X = np.array(training_data)
        
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        model = IsolationForest(contamination=0.1, random_state=42)
        model.fit(X_scaled)
        
        # Guardar modelo
        with open(f'{self.model_path}/isolation_forest.pkl', 'wb') as f:
            pickle.dump({'model': model, 'scaler': scaler}, f)
        
        return model
    
    def generate_synthetic_traffic(self, n_samples=1000):
        """Genera datos sintéticos para entrenamiento"""
        # Tráfico normal
        normal = np.random.normal(100, 30, (int(n_samples*0.9), 4))
        
        # Tráfico anómalo
        anomalous = np.random.normal(500, 150, (int(n_samples*0.1), 4))
        
        return np.vstack([normal, anomalous])
    
    def load_model(self):
        """Carga modelo entrenado"""
        model_file = f'{self.model_path}/isolation_forest.pkl'
        if os.path.exists(model_file):
            with open(model_file, 'rb') as f:
                return pickle.load(f)
        return None
