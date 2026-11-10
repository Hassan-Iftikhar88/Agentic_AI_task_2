import json
from pathlib import Path
from datetime import datetime

FILE = Path(__file__).resolve().parent.parent / "outputs" / "saved_results" / "memory.json"


def load():
    if FILE.exists():
        try:
            return json.loads(FILE.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []


def remember(topic, platform, tone, idea):
    data = load()
    data.append({"topic": topic, "platform": platform, "tone": tone,
                 "idea": idea, "time": datetime.now().isoformat(timespec="seconds")})
    FILE.parent.mkdir(parents=True, exist_ok=True)
    FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def recent_summary(n=3):
    items = load()[-n:]
    if not items:
        return "None"
    return "; ".join(f"{i['topic']} ({i['platform']}, {i['tone']})" for i in items)
