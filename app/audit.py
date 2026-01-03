
import json, datetime
from pathlib import Path
AUDIT_FILE = Path("audit.log")

def log_event(event, actor, payload):
    record = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "event": event,
        "actor": actor,
        "payload": payload
    }
    with AUDIT_FILE.open("a") as f:
        f.write(json.dumps(record) + "\n")
