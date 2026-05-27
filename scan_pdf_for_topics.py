import sys
import os

pdf_path = r"c:\Users\Ruan Gomes\Downloads\TJC\edital-tj-ce-2026.PDF"
output_path = r"c:\Users\Ruan Gomes\Downloads\TJC\pdf_topics_result.txt"

try:
    import pypdf
    reader = pypdf.PdfReader(pdf_path)
except Exception as e:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"Error loading PDF library: {e}\n")
    sys.exit(1)

keywords = ["direito administrativo", "direito constitucional", "licitações", "14.133", "constitucional", "regimento interno"]

with open(output_path, "w", encoding="utf-8") as f:
    f.write("Searching PDF for disciplines...\n")
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if not text:
            continue
        text_lower = text.lower()
        found_keys = [k for k in keywords if k in text_lower]
        if found_keys:
            f.write(f"--- Page {i+1} matches {found_keys} ---\n")
            for line in text.splitlines():
                if any(k in line.lower() for k in keywords):
                    f.write(line + "\n")

print("Finished scanning for topics.")
