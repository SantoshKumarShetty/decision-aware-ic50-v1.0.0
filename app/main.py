
from fastapi import FastAPI, Depends
import numpy as np
from pathlib import Path
from app.auth import authenticate
from app.schemas import IC50Request, IC50Response, DecisionRequest, DecisionResponse
from app.audit import log_event
from app.decision_logic import evaluate_decision
from ic50_models.base import IC50Model

MODEL_PATH = Path("models/ic50_model.pkl")
if not MODEL_PATH.exists():
    raise RuntimeError("No IC50 model found. Provide models/ic50_model.pkl before running.")

app = FastAPI(title="Decision-Aware IC50 Platform", version="1.0.0")
ic50_model = IC50Model.load(str(MODEL_PATH))

@app.post("/predict/ic50", response_model=IC50Response)
def predict_ic50(req: IC50Request):
    samples = ic50_model.predict_distribution(req.features)
    return IC50Response(
        median=float(np.median(samples)),
        lower=float(np.quantile(samples, 0.05)),
        upper=float(np.quantile(samples, 0.95)),
        samples=samples.tolist()
    )

@app.post("/decision/evaluate", response_model=DecisionResponse)
def decision_endpoint(req: DecisionRequest, actor: str = Depends(authenticate)):
    decision = evaluate_decision(req)
    log_event("DECISION_EVALUATED", actor, decision.model_dump())
    return decision
