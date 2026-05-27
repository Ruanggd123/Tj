import sys
import os

pdf_path = r"c:\Users\Ruan Gomes\Downloads\TJC\edital-tj-ce-2026.PDF"
output_path = r"c:\Users\Ruan Gomes\Downloads\TJC\syllabus_pages.txt"

try:
    import pypdf
    reader = pypdf.PdfReader(pdf_path)
except Exception as e:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Error loading PDF library: {e}\n")
    sys.exit(1)

with open(output_path, "w", encoding="utf-8") as f:
    f.write("Dumping pages 12 to 24 of the PDF:\n")
    for page_num in range(11, len(reader.pages)):
        text = reader.pages[page_num].extract_text()
        f.write(f"\n================ PAGE {page_num + 1} ================\n")
        f.write(text)

print("Pages dumped successfully.")
