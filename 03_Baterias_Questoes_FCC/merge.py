import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

days = {
    "25": "Segunda-feira 25/05",
    "26": "Terça-feira 26/05",
    "27": "Quarta-feira 27/05",
    "28": "Quinta-feira 28/05",
    "29": "Sexta-feira 29/05",
    "30": "Sábado 30/05 (Bateria Extra Ouro)",
    "31": "Domingo 31/05 (Bateria Extra Diamante)",
    "32": "Segunda-feira 01/06 (Bateria Extra Mestre)"
}

base = r"c:\Users\Ruan Gomes\Downloads\TJC\03_Baterias_Questoes_FCC"
temp = os.path.join(base, "temp_parts")

for d, title in days.items():
    out_file = os.path.join(base, f"dia_{d}_05_questoes.md")
    print(f"Montando {out_file}...")
    with open(out_file, "w", encoding="utf-8") as out:
        out.write(f"# Bateria de Questões FCC — {title}\n\n")
        
        # O Dia 32 tem apenas 1 tema extra, mas o loop até 3 resolve isso por não encontrar os demais.
        for t in ["1", "2", "3"]:
            in_file = os.path.join(temp, f"d{d}_t{t}.md")
            if os.path.exists(in_file):
                with open(in_file, "r", encoding="utf-8") as f:
                    out.write(f.read() + "\n\n")
            else:
                if d not in ["32"]: # Não emite aviso para o 32 porque já sabemos que tem só 1 tema.
                    print(f"AVISO: Arquivo ausente: {in_file}")

print("Fusão completa de todos os dias e baterias extras!")
