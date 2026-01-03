
import numpy as np
from app.schemas import DecisionRequest, DecisionResponse

SAFE_UPPER_BOUND = 300.0

def evaluate_decision(req: DecisionRequest) -> DecisionResponse:
    if not any(np.quantile(x, 0.95) < SAFE_UPPER_BOUND for x in req.cell_line_ic50):
        return DecisionResponse(
            decision="STOP",
            forbidden_actions=["escalation"],
            rationale={"baseline": "Fails cell-line falsification"}
        )

    variability = np.var([np.median(x) for x in req.tumoroid_ic50])
    if variability < 0.05:
        return DecisionResponse(
            decision="STRATIFIED_FOLLOWUP",
            allowed_actions=["mutation_conditioned_followup"],
            forbidden_actions=["generalization", "patient_prediction"],
            rationale={"status": "Robust conditional signal"}
        )

    return DecisionResponse(
        decision="EXPLORATORY_ONLY",
        forbidden_actions=["claims", "escalation"],
        rationale={"status": "Fragile stratification"}
    )
