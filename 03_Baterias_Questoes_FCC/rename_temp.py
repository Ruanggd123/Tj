import os

temp_dir = r"c:\Users\Ruan Gomes\Downloads\TJC\03_Baterias_Questoes_FCC\temp_parts"

renames = [
    ("d27_t2.md", "d31_t3.md"), # Testes -> Day 31
    ("d27_t3.md", "d32_t1.md"), # Dir Adm -> Day 32
    ("d25_t2.md", "d30_t1.md"), # UX/UI -> Day 30
    ("d25_t3.md", "d30_t2.md"), # ITIL -> Day 30
    ("d26_t1.md", "d30_t3.md"), # Arquitetura -> Day 30
    ("d26_t2.md", "d31_t1.md"), # DevOps -> Day 31
    ("d26_t3.md", "d31_t2.md"), # Dir Const -> Day 31
]

for old, new in renames:
    old_path = os.path.join(temp_dir, old)
    new_path = os.path.join(temp_dir, new)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renomeado {old} para {new}")

# Rename Java to correct slot (from T1 to T2)
java_old = os.path.join(temp_dir, "d27_t1.md")
java_new = os.path.join(temp_dir, "d27_t2.md")
if os.path.exists(java_old):
    os.rename(java_old, java_new)
    print("Renomeado d27_t1.md para d27_t2.md")
