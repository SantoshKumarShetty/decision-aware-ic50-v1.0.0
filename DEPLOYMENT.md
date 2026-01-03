
# Deployment Guide

## What is required to run

1. Python 3.11+
2. A trained IC50 model artifact at:
   models/ic50_model.pkl
3. API keys configured in app/auth.py or via environment
4. Docker (optional but recommended)

To generate a dummy model for testing only:
```
python models/generate_dummy_model.py
```

## What is intentionally omitted

- No pretrained IC50 model (domain-specific by design)
- No causal guarantees
- No clinical claims
- No default thresholds for real biology

This repository provides architecture, not biological truth.
