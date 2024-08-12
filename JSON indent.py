import json

with open("origin.json", "r") as f1:
  with open("ideal.json", "w", encoding="utf-8") as f2:
    f2.write(json.dumps(json.load(f1), indent=4, ensure_ascii=False))
