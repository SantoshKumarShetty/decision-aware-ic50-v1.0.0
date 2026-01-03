
from pydantic import BaseModel
from typing import Dict, List

class IC50Request(BaseModel):
    features: Dict[str, float]

class IC50Response(BaseModel):
    median: float
    lower: float
    upper: float
    samples: List[float]

class DecisionRequest(BaseModel):
    cell_line_ic50: List[List[float]]
    tumoroid_ic50: List[List[float]]
    mutations: Dict[str, Dict[str, bool]]
    gene: str

class DecisionResponse(BaseModel):
    decision: str
    allowed_actions: List[str] = []
    forbidden_actions: List[str] = []
    rationale: Dict[str, str] = {}
