import os

def setup_study_env():
    base_dir = r"c:\Users\Ruan Gomes\Downloads\TJC"
    folders = [
        "01_Editais_e_Calendario",
        "02_Conhecimentos_Gerais/01_Portugues",
        "02_Conhecimentos_Gerais/02_RLM",
        "02_Conhecimentos_Gerais/03_Direito_Administrativo",
        "02_Conhecimentos_Gerais/04_Direito_Constitucional",
        "02_Conhecimentos_Gerais/05_Legislação_TJCE",
        "03_Conhecimentos_Especificos_TI/01_Engenharia_de_Software",
        "03_Conhecimentos_Especificos_TI/02_Banco_de_Dados",
        "03_Conhecimentos_Especificos_TI/03_Infraestrutura_e_Redes",
        "03_Conhecimentos_Especificos_TI/04_Seguranca_da_Informacao",
        "03_Conhecimentos_Especificos_TI/05_Governanca_TI",
        "04_Provas_Anteriores",
        "05_Redacao",
        "06_Mapas_Mentais_e_Flashcards"
    ]

    print(f"--- Iniciando configuração do ambiente de estudos em: {base_dir} ---")
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Criado diretório base: {base_dir}")

    for folder in folders:
        path = os.path.join(base_dir, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Pasta criada: {folder}")
        else:
            print(f"Pasta já existe: {folder}")

    print("\n--- Estrutura de pastas concluída com sucesso! ---")

if __name__ == "__main__":
    setup_study_env()
