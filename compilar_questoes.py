import os
import re
import json

def parse_markdown_to_json():
    print("Iniciando a compilação das questões para JSON...")
    workspace_dir = r"c:\Users\Ruan Gomes\Downloads\TJC"
    questoes_dir = os.path.join(workspace_dir, "03_Baterias_Questoes_FCC")
    
    pattern = re.compile(r"^dia_(\d{2})_(\d{2})_questoes\.md$")
    found_files = []
    for filename in os.listdir(questoes_dir):
        m = pattern.match(filename)
        if m:
            day = int(m.group(1))
            month = int(m.group(2))
            found_files.append((day, month, filename))
            
    found_files.sort(key=lambda x: (x[1], x[0]))
    
    if not found_files:
        print("Erro: Nenhum arquivo de questões encontrado em", questoes_dir)
        return

    index_data = []
    all_questions = []
    question_id_counter = 1
    
    for day, month, filename in found_files:
        filepath = os.path.join(questoes_dir, filename)
        day_id = filename.replace("_questoes.md", "")
        
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        day_match = re.search(r"Bateria de Questões FCC — (.*?)\n", content)
        day_title = day_match.group(1).strip() if day_match else f"Dia {day:02d}/{month:02d}"
        
        day_questions = []
        
        # Split by Themes
        theme_splits = re.split(r"(?m)^## 📝 TEMA \d+: (.*?)$", content)
        
        # The first part is the header, subsequent parts are pairs of (Theme Title, Content)
        for i in range(1, len(theme_splits), 2):
            theme_title = theme_splits[i].strip()
            theme_content = theme_splits[i+1]
            
            # Use positive lookahead to split by '### ' while keeping it in the block
            blocks = re.split(r"(?m)^### ", theme_content)
            
            current_context = ""
            
            for block in blocks:
                block = block.strip()
                if not block:
                    continue
                    
                if block.startswith("Texto"):
                    # This block is a reading text / context
                    # We remove the trailing '---' if it exists
                    context_clean = re.sub(r"(?m)^---$", "", block).strip()
                    current_context = "### " + context_clean
                    
                elif block.startswith("Questão"):
                    # This block is a question
                    # Parse the first line to get the source
                    first_line_match = re.match(r"^Questão \d+ \((.*?)\)", block)
                    if not first_line_match:
                        continue
                    q_source = first_line_match.group(1).strip()
                    
                    # Remove the first line
                    q_content = block[first_line_match.end():].strip()
                    
                    details_match = re.search(r"<details>[\s\S]*?\*\*Gabarito:\s*([A-E])\*\*([\s\S]*?)</details>", q_content)
                    if not details_match:
                        continue
                        
                    answer = details_match.group(1).strip()
                    explanation_raw = details_match.group(2).strip()
                    
                    # Question text and options
                    q_text_options = q_content[:details_match.start()].strip()
                    
                    a_match = re.search(r"(?m)^A\)", q_text_options)
                    if a_match:
                        statement = q_text_options[:a_match.start()].strip()
                        options_text = q_text_options[a_match.start():].strip()
                    else:
                        statement = q_text_options
                        options_text = ""
                    
                    options_dict = {}
                    opt_matches = list(re.finditer(r"([A-E])\)\s*(.*?)(?=\n[A-E]\)|$)", options_text, re.DOTALL))
                    for opt_m in opt_matches:
                        options_dict[opt_m.group(1)] = opt_m.group(2).strip()
                    
                    question_obj = {
                        "id": question_id_counter,
                        "day_id": day_id,
                        "day_title": day_title,
                        "theme": theme_title,
                        "context": current_context,
                        "source": q_source,
                        "statement": statement,
                        "options": options_dict,
                        "answer": answer,
                        "explanation": explanation_raw
                    }
                    day_questions.append(question_obj)
                    all_questions.append(question_obj)
                    question_id_counter += 1
        
        # Save individual day JSON
        day_json_filename = f"{day_id}_questoes.json"
        day_json_path = os.path.join(questoes_dir, day_json_filename)
        with open(day_json_path, "w", encoding="utf-8") as f:
            json.dump(day_questions, f, ensure_ascii=False, indent=2)
            
        index_data.append({
            "day_id": day_id,
            "day_title": day_title,
            "filename": day_json_filename,
            "count": len(day_questions)
        })

    # Save index JSON
    index_json_path = os.path.join(questoes_dir, "questoes_index.json")
    with open(index_json_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

    # Save to a unified file as legacy backup
    output_json_path = os.path.join(questoes_dir, "questoes.json")
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
        
    print(f"Index de questões criado: {index_json_path} com {len(index_data)} dias.")
    print(f"Arquivo JSON unificado criado/atualizado: {output_json_path} com {len(all_questions)} questões.")

if __name__ == "__main__":
    parse_markdown_to_json()
