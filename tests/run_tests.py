import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from app.agent import run_agent

CASES = [
    ("YOLOv8 helmet detection", "LinkedIn", "Professional", "Post"),
    ("AI internship experience", "LinkedIn", "Motivational", "Post"),
    ("Python learning journey", "Instagram", "Funny", "Reel Script"),
    ("Machine learning project", "X/Twitter", "Short and catchy", "Post"),
    ("Data annotation struggles", "LinkedIn", "Humorous", "Post"),
    ("Model failed in production", "Instagram", "Meme style", "Reel Script"),
    ("Final year project", "LinkedIn", "Professional", "Post"),
    ("Computer vision project", "YouTube Shorts", "Exciting", "Reel Script"),
    ("Debugging FastAPI", "X/Twitter", "Funny", "Post"),
    ("Open-source contribution", "LinkedIn", "Inspirational", "Post"),
]

rows = [
    "# Test Cases",
    "",
    "| # | Topic | Platform | Tone | Tools used | Saved file | Score | Useful? | Notes |",
    "|---|---|---|---|---|---|---|---|---|",
]
for i, (t, p, tone, o) in enumerate(CASES, 1):
    print(f"\n########## TEST {i}/10: {t} ({p}) ##########")
    try:
        r = run_agent(t, p, tone, o)
        rows.append(
            f"| {i} | {t} | {p} | {tone} | {', '.join(r['tools_used'])} | "
            f"{r['saved_file']} | {r['score']}/10 | TBD | |")
    except Exception as e:
        rows.append(f"| {i} | {t} | {p} | {tone} | ERROR | - | - | No | {e} |")

out = Path(__file__).with_name("test_cases.md")
out.write_text("\n".join(rows) + "\n", encoding="utf-8")
print("\nDone: tests/test_cases.md  -> now open each saved file and replace TBD with Yes/No + a note.")
