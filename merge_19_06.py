import json
import os

questoes_dir = r"c:\Users\Ruan Gomes\Downloads\TJC\03_Baterias_Questoes_FCC"

b1_pt1 = json.load(open(os.path.join(questoes_dir, "dia_19_06_bloco_1_pt1.json"), "r", encoding="utf-8"))
b1_pt2 = json.load(open(os.path.join(questoes_dir, "dia_19_06_bloco_1_pt2.json"), "r", encoding="utf-8"))
b2_pt1 = json.load(open(os.path.join(questoes_dir, "dia_19_06_bloco_2_pt1.json"), "r", encoding="utf-8"))
b2_pt2 = json.load(open(os.path.join(questoes_dir, "dia_19_06_bloco_2_pt2.json"), "r", encoding="utf-8"))
b3 = json.load(open(os.path.join(questoes_dir, "dia_19_06_bloco_3.json"), "r", encoding="utf-8"))

merged = b1_pt1 + b1_pt2 + b2_pt1 + b2_pt2 + b3

todas_questoes_path = os.path.join(questoes_dir, "questoes.json")
with open(todas_questoes_path, "r", encoding="utf-8") as f:
    todas = json.load(f)

last_id = todas[-1]["id"] if len(todas) > 0 else 0

for item in merged:
    last_id += 1
    item["id"] = last_id
    item["day_id"] = "dia_19_06"
    item["day_title"] = "Sexta-feira 19/06"

with open(os.path.join(questoes_dir, "dia_19_06_questoes.json"), "w", encoding="utf-8") as f:
    json.dump(merged, f, ensure_ascii=False, indent=2)

todas.extend(merged)
with open(todas_questoes_path, "w", encoding="utf-8") as f:
    json.dump(todas, f, ensure_ascii=False, indent=2)

index_path = os.path.join(questoes_dir, "questoes_index.json")
with open(index_path, "r", encoding="utf-8") as f:
    index = json.load(f)

index = [x for x in index if x["day_id"] != "dia_19_06"]

index.append({
    "day_id": "dia_19_06",
    "day_title": "Sexta-feira 19/06",
    "filename": "dia_19_06_questoes.json",
    "count": len(merged)
})

with open(index_path, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print("Merge completo. questoes.json atualizado com", len(merged), "novas questoes.")
