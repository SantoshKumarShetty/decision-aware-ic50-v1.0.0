
import joblib, numpy as np
from ic50_models.base import IC50Model

class SklearnIC50Model(IC50Model):
    def __init__(self, model):
        self.model = model

    def predict_distribution(self, features: dict) -> np.ndarray:
        X = np.array([features[k] for k in sorted(features.keys())]).reshape(1, -1)
        return np.array([est.predict(X)[0] for est in self.model.estimators_])

    @staticmethod
    def load(path: str):
        model = joblib.load(path)
        return SklearnIC50Model(model)
