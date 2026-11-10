from app.agent import run_agent

print("=== TrendPilot: Local Viral Content Agent ===")
topic = input("Enter your topic: ")
platform = input("Choose platform (LinkedIn/Instagram/X/YouTube Shorts): ")
tone = input("Choose tone (professional, funny, motivational...): ")
output_type = input("Choose output type (Post / Post + Reel Script): ")

try:
    r = run_agent(topic, platform, tone, output_type)
except RuntimeError as e:
    print("\nERROR:", e)
    raise SystemExit(1)

print("\n===== FINAL OUTPUT =====")
for k in ["topic", "platform", "idea", "audience", "hook", "caption", "hashtags",
          "reel_script", "title", "review", "saved_file"]:
    print(f"\n{k.upper()}:\n{r[k]}")
print("\nTools used:", " -> ".join(r["tools_used"]))
