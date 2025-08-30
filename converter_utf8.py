import json

with open("lgpd_summary_by_topic.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("lgpd_summary_by_topic.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("OK: arquivo convertido para UTF-8.")
