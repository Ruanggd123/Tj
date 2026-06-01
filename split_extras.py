import json
import subprocess
import os

def generate_md(json_data, day_title):
    md_lines = []
    md_lines.append(f"# {day_title}")
    md_lines.append("")
    for i, q in enumerate(json_data):
        md_lines.append(f"### Questão {i+1} ({q['source']})")
        md_lines.append(f"**Tema:** {q['theme']}\n")
        if q.get('context'):
            md_lines.append(f"**Contexto:**\n> {q['context']}\n")
        md_lines.append(f"{q['statement']}\n")
        for key, value in q['options'].items():
            md_lines.append(f"{key}) {value}")
        md_lines.append("")
        md_lines.append(f"<details><summary>🔑 Ver Gabarito e Explicação</summary>\n")
        md_lines.append(f"**Gabarito: {q['answer']}**\n")
        md_lines.append(f"{q['explanation']}")
        md_lines.append("</details>\n")
        md_lines.append("---\n")
    return "\n".join(md_lines)

# Read the original deleted JSON
output = subprocess.check_output(['git', 'show', ':03_Baterias_Questoes_FCC/dia_30_05_questoes.json']).decode('utf-8')
data = json.loads(output)

q_17_06 = []
q_24_06 = []

for q in data:
    theme = q['theme']
    if 'UX' in theme or 'Governan' in theme:
        q_17_06.append(q)
    elif 'Arquitetura' in theme:
        q_24_06.append(q)

def save_files(basename, day_title, q_list):
    if not q_list: return
    # Update day info
    for q in q_list:
        q['day_id'] = basename
        q['day_title'] = day_title
    
    # Write JSON
    with open(f"03_Baterias_Questoes_FCC/{basename}.json", "w", encoding="utf-8") as f:
        json.dump(q_list, f, ensure_ascii=False, indent=2)
    
    # Write MD
    md_content = generate_md(q_list, day_title)
    with open(f"03_Baterias_Questoes_FCC/{basename}.md", "w", encoding="utf-8") as f:
        f.write(md_content)

save_files("dia_17_06_questoes_extra", "Quarta-feira 17/06 (Bateria Extra Ouro - UX/Acessibilidade e Governança)", q_17_06)
save_files("dia_24_06_questoes_extra", "Quarta-feira 24/06 (Bateria Extra Ouro - Arquitetura de Software)", q_24_06)

print(f"Created dia_17_06_questoes_extra with {len(q_17_06)} questions.")
print(f"Created dia_24_06_questoes_extra with {len(q_24_06)} questions.")
