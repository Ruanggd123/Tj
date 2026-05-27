import os
import re
import random
import subprocess
import sys

def replace_references(text, mapping):
    # Temporary placeholders to prevent double-mapping issues
    def repl_word(match):
        word = match.group(1)
        letter = match.group(2)
        return f"{word} __TEMP_{letter}__"
    
    text = re.sub(r"\b(alternativa|opção|letra|opções|opção|alternativas)\s+([A-E])\b", repl_word, text, flags=re.IGNORECASE)
    
    def repl_bold_colon(match):
        letter = match.group(1)
        return f"**__TEMP_{letter}__**:"
    text = re.sub(r"\*\*([A-E])\*\*:", repl_bold_colon, text)
    
    def repl_bold_status(match):
        letter = match.group(1)
        status = match.group(2)
        return f"**__TEMP_{letter}__ ({status})**"
    text = re.sub(r"\*\*([A-E])\s*\((Correta|Incorreta)\)\*\*", repl_bold_status, text, flags=re.IGNORECASE)

    def repl_status(match):
        letter = match.group(1)
        status = match.group(2)
        return f"__TEMP_{letter}__ ({status})"
    text = re.sub(r"\b([A-E])\s*\((Correta|Incorreta)\)", repl_status, text, flags=re.IGNORECASE)
    
    def repl_paren(match):
        letter = match.group(1)
        return f"(__TEMP_{letter}__) "
    text = re.sub(r"\(([A-E])\)", repl_paren, text)
    
    def repl_paren_close(match):
        letter = match.group(1)
        return f"__TEMP_{letter}__)"
    text = re.sub(r"\b([A-E])\)", repl_paren_close, text)

    for k in ['A', 'B', 'C', 'D', 'E']:
        text = text.replace(f"__TEMP_{k}__", mapping[k])
        
    return text

def shuffle_file(filepath):
    print(f"Embaralhando alternativas em: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Divide o arquivo pelos blocos de questões
    parts = re.split(r"(?m)^### Questão ", content)
    header = parts[0]
    questions_parts = parts[1:]
    
    num_questions = len(questions_parts)
    print(f"Encontradas {num_questions} questões.")
    
    # Distribui as respostas corretas uniformemente (ex: 9 de cada letra para 45 questões)
    base_targets = ['A', 'B', 'C', 'D', 'E']
    targets = []
    for i in range(num_questions):
        targets.append(base_targets[i % 5])
    
    # Semente fixa por arquivo para garantir reproducibilidade
    random.seed(os.path.basename(filepath))
    random.shuffle(targets)
    
    new_parts = [header]
    
    for i, part in enumerate(questions_parts):
        # Cada parte começa com o número da questão e fonte, ex: 1 (FCC)\n...
        first_line_match = re.match(r"^(\d+)\s*\((.*?)\)", part)
        if not first_line_match:
            new_parts.append("### Questão " + part)
            continue
            
        q_num = first_line_match.group(1).strip()
        q_source = first_line_match.group(2).strip()
        q_body = part[first_line_match.end():].lstrip()
        
        # Extrai os detalhes de gabarito e explicação
        details_match = re.search(r"<details>([\s\S]*?)\*\*Gabarito:\s*([A-E])\*\*([\s\S]*?)</details>", q_body)
        if not details_match:
            new_parts.append("### Questão " + part)
            continue
            
        details_inner_before = details_match.group(1) # Spacing/summary before Gabarito
        current_ans = details_match.group(2).strip()
        explanation = details_match.group(3) # Explanation text after Gabarito
        
        # Separa o enunciado das opções
        q_text_options = q_body[:details_match.start()].strip()
        
        # Encontra onde começam as opções
        a_match = re.search(r"(?m)^A\)", q_text_options)
        if a_match:
            statement = q_text_options[:a_match.start()].strip()
            options_text = q_text_options[a_match.start():].strip()
        else:
            statement = q_text_options
            options_text = ""
            
        # Mapeia as opções
        options_dict = {}
        opt_matches = list(re.finditer(r"([A-E])\)\s*(.*?)(?=\n[A-E]\)|$)", options_text, re.DOTALL))
        for opt_m in opt_matches:
            options_dict[opt_m.group(1)] = opt_m.group(2).strip()
            
        if len(options_dict) < 5:
            new_parts.append("### Questão " + part)
            continue
            
        target = targets[i]
        
        # Cria a bijeção (mapeamento)
        mapping = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E'}
        if current_ans != target:
            mapping[current_ans] = target
            mapping[target] = current_ans
            
        # Cria as novas opções com base no mapeamento
        new_options = {}
        for old_key, new_key in mapping.items():
            new_options[new_key] = options_dict[old_key]
            
        # Atualiza referências na explicação
        updated_explanation = replace_references(explanation, mapping)
        
        # O que vem depois do </details>
        after_details = q_body[details_match.end():]
            
        # Reconstrói a questão
        new_q_block = f"### Questão {q_num} ({q_source})\n"
        if statement:
            new_q_block += statement + "\n"
        for k in ['A', 'B', 'C', 'D', 'E']:
            new_q_block += f"{k}) {new_options[k]}\n"
        new_q_block += "\n"
        new_q_block += f"<details>{details_inner_before}**Gabarito: {target}**{updated_explanation}</details>"
        new_q_block += after_details
        
        new_parts.append(new_q_block)
        
    # Salva o arquivo markdown de volta
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write("".join(new_parts).strip() + "\n")
    print(f"Arquivo {filepath} atualizado com sucesso.")

def main():
    workspace_dir = r"c:\Users\Ruan Gomes\Downloads\TJC"
    questoes_dir = os.path.join(workspace_dir, "03_Baterias_Questoes_FCC")
    
    days = ['dia_22_05_questoes.md', 'dia_25_05_questoes.md', 'dia_26_05_questoes.md', 'dia_27_05_questoes.md']
    
    for filename in days:
        filepath = os.path.join(questoes_dir, filename)
        if os.path.exists(filepath):
            shuffle_file(filepath)
        else:
            print(f"Aviso: arquivo não encontrado: {filepath}")
            
    # Executa o script de compilação
    print("\nExecutando 'compilar_questoes.py' para regenerar os JSONs...")
    comp_script = os.path.join(workspace_dir, "compilar_questoes.py")
    subprocess.check_call([sys.executable, comp_script])

if __name__ == "__main__":
    main()
