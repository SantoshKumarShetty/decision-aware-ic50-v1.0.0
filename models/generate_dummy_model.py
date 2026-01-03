
from sklearn.ensemble import RandomForestRegressor
import numpy as np, joblib, os

X = np.random.rand(100, 5)
y = np.random.rand(100) * 500

model = RandomForestRegressor(n_estimators=10)
model.fit(X, y)

os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/ic50_model.pkl")
print("Dummy IC50 model generated.")
