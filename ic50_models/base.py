
from abc import ABC, abstractmethod
import numpy as np

class IC50Model(ABC):
    @abstractmethod
    def predict_distribution(self, features: dict) -> np.ndarray:
        pass

    @staticmethod
    def load(path: str):
        from ic50_models.sklearn_model import SklearnIC50Model
        return SklearnIC50Model.load(path)
