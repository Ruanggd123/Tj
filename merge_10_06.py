import json
import os

questoes_dir = r"c:\Users\Ruan Gomes\Downloads\TJC\03_Baterias_Questoes_FCC"

b1 = json.load(open(os.path.join(questoes_dir, "dia_10_06_bloco_1.json"), "r", encoding="utf-8"))
b2 = json.load(open(os.path.join(questoes_dir, "dia_10_06_bloco_2.json"), "r", encoding="utf-8"))
b3 = json.load(open(os.path.join(questoes_dir, "dia_10_06_bloco_3.json"), "r", encoding="utf-8"))

merged = b1 + b2 + b3

todas_questoes_path = os.path.join(questoes_dir, "questoes.json")
with open(todas_questoes_path, "r", encoding="utf-8") as f:
    todas = json.load(f)

last_id = todas[-1]["id"] if len(todas) > 0 else 0

for item in merged:
    last_id += 1
    item["id"] = last_id
    item["day_id"] = "dia_10_06"
    item["day_title"] = "Quarta-feira 10/06"

with open(os.path.join(questoes_dir, "dia_10_06_questoes.json"), "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

todas.extend(merged)
with open(todas_questoes_path, "w", encoding="utf-8") as f:
    json.dump(todas, f, ensure_ascii=False, indent=2)

index_path = os.path.join(questoes_dir, "questoes_index.json")
with open(index_path, "r", encoding="utf-8") as f:
    index = json.load(f)

index = [x for x in index if x["day_id"] != "dia_10_06"]

index.append({
    "day_id": "dia_10_06",
    "day_title": "Quarta-feira 10/06",
    "filename": "dia_10_06_questoes.json",
    "count": len(merged)
})

with open(index_path, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print("Merge completo. questoes.json atualizado com", len(merged), "novas questoes.")
