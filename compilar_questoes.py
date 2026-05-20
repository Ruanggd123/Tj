import os
import re
import markdown

def compile_questions():
    print("Iniciando a compilação das questões...")
    workspace_dir = r"c:\Users\Ruan Gomes\Downloads\TJC"
    questoes_dir = os.path.join(workspace_dir, "03_Baterias_Questoes_FCC")
    
    files = [
        "dia_16_05_questoes.md",
        "dia_17_05_questoes.md",
        "dia_18_05_questoes.md",
        "dia_19_05_questoes.md",
        "dia_20_05_questoes.md"
    ]
    
    merged_markdown = []
    merged_markdown.append("# Compilado Geral de Questões FCC — TJ-CE 2026\n")
    merged_markdown.append("Este arquivo reúne as 225 questões (15 por tema, de 16/05 a 20/05) geradas com base no perfil da banca FCC para o cargo de Analista de TI.\n\n---\n")
    
    html_content_blocks = []
    
    for filename in files:
        filepath = os.path.join(questoes_dir, filename)
        if not os.path.exists(filepath):
            print(f"Erro: Arquivo {filename} não encontrado em {questoes_dir}")
            continue
            
        print(f"Lendo {filename}...")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Extrair data/título do dia
        day_match = re.search(r"Bateria de Questões FCC — (.*?)\n", content)
        day_title = day_match.group(1) if day_match else filename.replace(".md", "")
        
        # Adicionar ao markdown compilado
        # Remover o título principal do dia para não chocar, mas adicionar um cabeçalho estruturado
        clean_content = re.sub(r"^# Bateria de Questões FCC — (.*?)\n", "", content)
        merged_markdown.append(f"\n# {day_title}\n")
        merged_markdown.append(clean_content)
        merged_markdown.append("\n---\n")
        
        # Converter este dia específico para HTML
        day_html = markdown.markdown(clean_content)
        
        # Adicionar uma seção identificada por dia no HTML para permitir abas/filtros
        day_id = filename.replace("_questoes.md", "")
        html_content_blocks.append(f"""
        <section id="{day_id}" class="day-section active">
            <h2 class="day-header">{day_title}</h2>
            {day_html}
        </section>
        """)

    # Escrever arquivo Markdown compilado
    output_md_path = os.path.join(questoes_dir, "todas_questoes_fcc.md")
    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(merged_markdown))
    print(f"Arquivo compilado em Markdown criado: {output_md_path}")
    
    # Criar HTML interativo completo
    all_days_html = "\n".join(html_content_blocks)
    
    html_template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulador de Questões FCC — TJ-CE 2026</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-color: #0b0f19;
            --card-bg: #151d30;
            --text-color: #f1f5f9;
            --text-muted: #94a3b8;
            --accent-color: #3b82f6;
            --accent-hover: #2563eb;
            --success-color: #10b981;
            --border-color: #1e293b;
            --details-bg: #1e293b;
            --details-border: #334155;
            --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            background-color: var(--bg-color);
            color: var(--text-color);
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            padding: 0 0 80px 0;
        }}

        header {{
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border-bottom: 1px solid var(--border-color);
            padding: 40px 20px;
            text-align: center;
            position: relative;
        }}

        .header-container {{
            max-width: 1000px;
            margin: 0 auto;
        }}

        h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(to right, #60a5fa, #3b82f6, #a78bfa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}

        .subtitle {{
            color: var(--text-muted);
            font-size: 1.1rem;
            max-width: 600px;
            margin: 0 auto 20px auto;
        }}

        .stats-bar {{
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }}

        .stat-card {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 10px 20px;
            min-width: 120px;
            box-shadow: var(--shadow);
        }}

        .stat-val {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.5rem;
            font-weight: 700;
            color: var(--accent-color);
        }}

        .stat-lbl {{
            font-size: 0.8rem;
            color: var(--text-muted);
            text-transform: uppercase;
        }}

        /* Toolbar Fixa Superior */
        .toolbar {{
            position: sticky;
            top: 0;
            background-color: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-color);
            padding: 15px 20px;
            z-index: 100;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 4px 30px rgba(0, 0, 0, 0.3);
        }}

        .toolbar-container {{
            max-width: 1000px;
            margin: 0 auto;
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 15px;
        }}

        .filter-buttons {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}

        .btn {{
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            color: var(--text-color);
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 500;
            font-size: 0.9rem;
            transition: all 0.2s ease;
        }}

        .btn:hover {{
            background-color: var(--border-color);
            border-color: var(--text-muted);
        }}

        .btn.active {{
            background-color: var(--accent-color);
            border-color: var(--accent-color);
            color: white;
        }}

        .action-buttons {{
            display: flex;
            gap: 10px;
        }}

        .btn-action {{
            background-color: var(--accent-color);
            border: none;
            color: white;
            padding: 8px 16px;
            border-radius: 6px;
            font-weight: 600;
            cursor: pointer;
            transition: background-color 0.2s ease;
        }}

        .btn-action:hover {{
            background-color: var(--accent-hover);
        }}

        .btn-success {{
            background-color: var(--success-color);
        }}
        
        .btn-success:hover {{
            opacity: 0.9;
        }}

        /* Container Principal */
        main {{
            max-width: 1000px;
            margin: 30px auto;
            padding: 0 20px;
        }}

        .day-section {{
            margin-bottom: 40px;
            display: none;
        }}

        .day-section.active {{
            display: block;
            animation: fadeIn 0.3s ease-in-out;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .day-header {{
            font-family: 'Outfit', sans-serif;
            font-size: 2rem;
            border-bottom: 2px solid var(--accent-color);
            padding-bottom: 8px;
            margin: 40px 0 20px 0;
            color: #93c5fd;
        }}

        h2 {{
            font-family: 'Outfit', sans-serif;
            font-size: 1.5rem;
            margin: 30px 0 15px 0;
            color: #60a5fa;
        }}

        /* Estilização das Questões */
        h3 {{
            font-size: 1.1rem;
            font-weight: 600;
            margin: 25px 0 10px 0;
            background-color: #1e293b;
            padding: 12px 16px;
            border-left: 4px solid var(--accent-color);
            border-radius: 0 6px 6px 0;
        }}

        p {{
            margin-bottom: 15px;
            color: #cbd5e1;
            font-size: 1rem;
        }}

        ul, ol {{
            margin-left: 20px;
            margin-bottom: 20px;
            color: #cbd5e1;
        }}

        /* Render de listas de alternativas */
        p + ul, p + ol {{
            list-style: none;
            margin-left: 0;
        }}

        p + ul li, p + ol li {{
            background-color: rgba(30, 41, 59, 0.5);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 10px 15px;
            margin-bottom: 8px;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        p + ul li:hover, p + ol li:hover {{
            background-color: rgba(59, 130, 246, 0.1);
            border-color: var(--accent-color);
        }}

        /* Collapsible Details */
        details {{
            background-color: var(--details-bg);
            border: 1px solid var(--details-border);
            border-radius: 6px;
            margin: 15px 0 30px 0;
            overflow: hidden;
            transition: box-shadow 0.2s ease;
            box-shadow: var(--shadow);
        }}

        details[open] {{
            border-color: var(--success-color);
            box-shadow: 0 0 10px rgba(16, 185, 129, 0.2);
        }}

        summary {{
            padding: 12px 16px;
            font-weight: 600;
            cursor: pointer;
            user-select: none;
            outline: none;
            color: #a7f3d0;
            transition: background-color 0.2s ease;
        }}

        summary:hover {{
            background-color: rgba(16, 185, 129, 0.1);
        }}

        .details-content {{
            padding: 16px;
            border-top: 1px solid var(--details-border);
            background-color: rgba(15, 23, 42, 0.4);
        }}
        
        details p {{
            color: #e2e8f0;
        }}

        /* Estilo da Tabela do Direito PCD */
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            background-color: var(--card-bg);
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid var(--border-color);
        }}

        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }}

        th {{
            background-color: #1e293b;
            color: #60a5fa;
            font-weight: 600;
        }}

        tr:hover td {{
            background-color: rgba(30, 41, 59, 0.5);
        }}

        hr {{
            border: 0;
            height: 1px;
            background: var(--border-color);
            margin: 40px 0;
        }}

        /* Estilos de Impressão e PDF */
        @media print {{
            body {{
                background-color: white;
                color: black;
                padding: 0;
                font-size: 11pt;
            }}

            .toolbar, header, hr, .stats-bar, .filter-buttons, .action-buttons {{
                display: none !important;
            }}

            main {{
                margin: 0;
                padding: 0;
                max-width: 100%;
            }}

            .day-section {{
                display: block !important; /* Mostra tudo para imprimir */
                page-break-after: always;
            }}

            h3 {{
                background-color: #f1f5f9;
                color: black;
                border-left: 4px solid black;
                page-break-inside: avoid;
            }}

            p + ul li, p + ol li {{
                background-color: white;
                border: 1px solid #cbd5e1;
                color: black;
                page-break-inside: avoid;
            }}

            details {{
                background-color: white;
                border: 1px solid #cbd5e1;
                box-shadow: none;
                page-break-inside: avoid;
            }}

            details[open] {{
                box-shadow: none;
                border-color: black;
            }}

            summary {{
                color: black;
                font-weight: bold;
                border-bottom: 1px solid #cbd5e1;
            }}

            .details-content {{
                background-color: white;
                color: black;
            }}

            p, li, td, th {{
                color: black !important;
            }}
            
            table {{
                border-color: #cbd5e1;
                page-break-inside: avoid;
            }}
            
            th {{
                background-color: #f1f5f9;
                color: black;
            }}
        }}
    </style>
</head>
<body>

    <header>
        <div class="header-container">
            <h1>Simulador FCC — TJ-CE 2026</h1>
            <p class="subtitle">Banco Completo de Questões comentadas de Engenharia de Software, Banco de Dados, Redes, Segurança, RLM, Português e Direito da PCD.</p>
            <div class="stats-bar">
                <div class="stat-card">
                    <div class="stat-val">225</div>
                    <div class="stat-lbl">Questões</div>
                </div>
                <div class="stat-card">
                    <div class="stat-val">5 dias</div>
                    <div class="stat-lbl">Estudados</div>
                </div>
                <div class="stat-card">
                    <div class="stat-val">100%</div>
                    <div class="stat-lbl">Gabaritadas</div>
                </div>
            </div>
        </div>
    </header>

    <div class="toolbar">
        <div class="toolbar-container">
            <div class="filter-buttons">
                <button class="btn active" onclick="filterDay('all', this)">Ver Todas</button>
                <button class="btn" onclick="filterDay('dia_16_05', this)">Dia 16/05</button>
                <button class="btn" onclick="filterDay('dia_17_05', this)">Dia 17/05</button>
                <button class="btn" onclick="filterDay('dia_18_05', this)">Dia 18/05</button>
                <button class="btn" onclick="filterDay('dia_19_05', this)">Dia 19/05</button>
                <button class="btn" onclick="filterDay('dia_20_05', this)">Dia 20/05</button>
            </div>
            
            <div class="action-buttons">
                <button class="btn-action" onclick="toggleAll(true)">Expandir Respostas</button>
                <button class="btn-action" onclick="toggleAll(false)">Colapsar Respostas</button>
                <button class="btn-action btn-success" onclick="window.print()">Gerar PDF / Imprimir</button>
            </div>
        </div>
    </div>

    <main>
        {all_days_html}
    </main>

    <script>
        // Função para filtrar o dia exibido
        function filterDay(dayId, btn) {{
            // Atualizar botões ativos
            document.querySelectorAll('.filter-buttons .btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Mostrar/ocultar seções
            const sections = document.querySelectorAll('.day-section');
            if (dayId === 'all') {{
                sections.forEach(s => s.classList.add('active'));
            }} else {{
                sections.forEach(s => {{
                    if (s.id === dayId) {{
                        s.classList.add('active');
                    }} else {{
                        s.classList.remove('active');
                    }}
                }});
            }}
        }}

        // Função para expandir ou colapsar todas as respostas
        function toggleAll(open) {{
            const details = document.querySelectorAll('details');
            details.forEach(d => {{
                if (open) {{
                    d.setAttribute('open', '');
                }} else {{
                    d.removeAttribute('open');
                }}
            }});
        }}
        
        // Colocar a classe details-content dentro dos details
        document.querySelectorAll('details').forEach(d => {{
            const summary = d.querySelector('summary');
            const nodes = Array.from(d.childNodes).filter(node => node !== summary);
            const wrapper = document.createElement('div');
            wrapper.className = 'details-content';
            nodes.forEach(n => wrapper.appendChild(n));
            d.appendChild(wrapper);
        }});
    </script>
</body>
</html>
"""
    
    output_html_path = os.path.join(questoes_dir, "todas_questoes_fcc.html")
    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Arquivo HTML interativo criado: {output_html_path}")
    print("Processo concluído com sucesso!")

if __name__ == "__main__":
    compile_questions()
