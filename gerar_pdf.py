import os
import re
import markdown
from bs4 import BeautifulSoup
from fpdf import FPDF

class StudyPDF(FPDF):
    def header(self):
        # Arial bold 8
        self.set_font('Arial', 'B', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, self.safe('TJ-CE 2026 — Banco de Questões FCC (16/05 a 20/05)'), 0, 0, 'L')
        self.cell(0, 10, self.safe('Analista de TI'), 0, 1, 'R')
        self.line(10, 18, 200, 18)
        self.ln(5)

    def footer(self):
        # Posição a 1.5 cm do fim
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, self.safe(f'Página {self.page_no()}/{{nb}}'), 0, 0, 'C')

    def safe(self, text):
        if not text:
            return ""
        # Substituir aspas inteligentes e traços longos comuns do markdown
        text = text.replace('\u201c', '"').replace('\u201d', '"')
        text = text.replace('\u2018', "'").replace('\u2019', "'")
        text = text.replace('\u2013', '-').replace('\u2014', '-')
        text = text.replace('\u2022', '*')
        text = text.replace('\u2261', '==') # Equivalência lógica
        text = text.replace('\u2192', '->') # Condicional
        text = text.replace('\u2194', '<->') # Bicondicional
        text = text.replace('\u2227', '^') # E lógico
        text = text.replace('\u2228', 'v') # OU lógico
        text = text.replace('\u223c', '~') # Negação lógica
        text = text.replace('\u2260', '!=') # Diferente
        text = text.replace('\u2264', '<=') # Menor ou igual
        text = text.replace('\u2265', '>=') # Maior ou igual
        
        # Encodar para latin-1 substituindo caracteres incompatíveis
        return text.encode('latin-1', 'replace').decode('latin-1')

def generate_pdf():
    workspace_dir = r"c:\Users\Ruan Gomes\Downloads\TJC"
    questoes_dir = os.path.join(workspace_dir, "03_Baterias_Questoes_FCC")
    md_path = os.path.join(questoes_dir, "todas_questoes_fcc.md")
    pdf_path = os.path.join(questoes_dir, "todas_questoes_fcc.pdf")
    
    if not os.path.exists(md_path):
        print(f"Erro: Arquivo Markdown compilado não encontrado em {md_path}")
        return

    print("Lendo o compilado Markdown...")
    with open(md_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Converter Markdown para HTML
    print("Convertendo Markdown para HTML...")
    html_content = markdown.markdown(md_content)
    
    # Parsear com BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Configurar PDF
    print("Iniciando geração do PDF...")
    pdf = StudyPDF()
    pdf.alias_nb_pages()
    pdf.set_margins(10, 20, 10)
    pdf.add_page()
    
    # Processar elementos HTML sequencialmente
    elements = soup.find_all(recursive=False)
    
    in_details = False
    
    for el in elements:
        tag = el.name
        
        if tag == 'h1':
            pdf.ln(5)
            pdf.set_font('Arial', 'B', 16)
            pdf.set_text_color(15, 23, 42) # Dark blue/slate
            pdf.multi_cell(190, 8, pdf.safe(el.get_text()))
            pdf.ln(4)
            
        elif tag == 'h2':
            pdf.ln(4)
            pdf.set_font('Arial', 'B', 13)
            pdf.set_text_color(29, 78, 216) # Medium blue
            pdf.multi_cell(190, 7, pdf.safe(el.get_text()))
            pdf.ln(3)
            
        elif tag == 'h3':
            pdf.ln(3)
            pdf.set_font('Arial', 'B', 10)
            pdf.set_text_color(30, 41, 59) # Slate-800
            # Adicionar um pequeno recuo visual para perguntas
            title_text = el.get_text()
            pdf.multi_cell(190, 6, pdf.safe(title_text))
            pdf.ln(2)
            
        elif tag == 'p':
            pdf.set_font('Arial', '', 9.5)
            pdf.set_text_color(51, 65, 85) # Slate-700
            pdf.multi_cell(190, 4.5, pdf.safe(el.get_text()))
            pdf.ln(2)
            
        elif tag in ['ul', 'ol']:
            pdf.set_font('Arial', '', 9.5)
            pdf.set_text_color(51, 65, 85)
            for li in el.find_all('li'):
                # Identifica se é uma alternativa (começa com letra e parêntese) ou item normal
                li_text = li.get_text().strip()
                # Adiciona um pequeno recuo para as alternativas
                pdf.cell(5)
                pdf.multi_cell(185, 4.5, pdf.safe(li_text))
                pdf.ln(1.5)
            pdf.ln(1.5)
            
        elif tag == 'details':
            # Vamos estilizar o Gabarito e Justificativa em uma caixa
            pdf.set_font('Arial', 'B', 9.5)
            pdf.set_text_color(16, 124, 65) # Verde FCC para Gabarito
            
            summary = el.find('summary')
            summary_text = summary.get_text() if summary else "🔑 Gabarito e Justificativa"
            
            pdf.multi_cell(190, 5, pdf.safe(summary_text))
            pdf.ln(1)
            
            # Texto da justificativa
            pdf.set_font('Arial', '', 9)
            pdf.set_text_color(51, 65, 85)
            
            # Pega todo o texto do details exceto o summary
            details_paragraphs = el.find_all(['p', 'li'])
            for dp in details_paragraphs:
                if dp.name == 'summary':
                    continue
                dp_text = dp.get_text().strip()
                # Ignora a repetição do resumo se houver
                if dp_text == summary_text:
                    continue
                pdf.multi_cell(190, 4.5, pdf.safe(dp_text))
                pdf.ln(1.5)
            pdf.ln(3)
            
        elif tag == 'table':
            # Desenhar tabela de forma básica em PDF
            pdf.set_font('Arial', 'B', 8.5)
            pdf.set_text_color(30, 41, 59)
            
            headers = [th.get_text() for th in el.find_all('th')]
            rows = []
            for tr in el.find_all('tr'):
                cells = [td.get_text() for td in tr.find_all('td')]
                if cells:
                    rows.append(cells)
                    
            if headers:
                # Desenhar cabeçalho
                col_width = 190 / len(headers)
                for h in headers:
                    pdf.cell(col_width, 6, pdf.safe(h), border=1, align='C')
                pdf.ln()
                
                # Desenhar linhas
                pdf.set_font('Arial', '', 8)
                for r in rows:
                    for c in r:
                        pdf.cell(col_width, 5, pdf.safe(c), border=1)
                    pdf.ln()
            pdf.ln(3)

    print("Salvando PDF...")
    pdf.output(pdf_path)
    print(f"PDF gerado com sucesso em: {pdf_path}")

if __name__ == "__main__":
    generate_pdf()
