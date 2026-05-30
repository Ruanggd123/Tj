import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

days = {
    "25": "Segunda-feira 25/05",
    "26": "Terça-feira 26/05",
    "27": "Quarta-feira 27/05",
    "28": "Quinta-feira 28/05",
    "29": "Sexta-feira 29/05"
}

base = r"c:\Users\Ruan Gomes\Downloads\TJC\03_Baterias_Questoes_FCC"
temp = os.path.join(base, "temp_parts")

for d, title in days.items():
    out_file = os.path.join(base, f"dia_{d}_05_questoes.md")
    print(f"Montando {out_file}...")
    with open(out_file, "w", encoding="utf-8") as out:
        out.write(f"# Bateria de Questões FCC — {title}\n\n")
        for t in ["1", "2", "3"]:
            in_file = os.path.join(temp, f"d{d}_t{t}.md")
            if os.path.exists(in_file):
                with open(in_file, "r", encoding="utf-8") as f:
                    out.write(f.read() + "\n\n")
            else:
                print(f"AVISO: Arquivo ausente: {in_file}")

print("Fusão completa!")
