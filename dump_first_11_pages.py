import sys
import pypdf

pdf_path = r"c:\Users\Ruan Gomes\Downloads\TJC\edital-tj-ce-2026.PDF"
output_path = r"c:\Users\Ruan Gomes\Downloads\TJC\first_11_pages.txt"

try:
    reader = pypdf.PdfReader(pdf_path)
    print(f"Total pages: {len(reader.pages)}")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("Dumping pages 1 to 11 of the PDF:\n")
        # Extract pages 1 to 11 (indices 0 to 10)
        for page_num in range(min(11, len(reader.pages))):
            text = reader.pages[page_num].extract_text()
            f.write(f"\n================ PAGE {page_num + 1} ================\n")
            f.write(text)
    print("First 11 pages dumped successfully.")
except Exception as e:
    print(f"Error: {e}")
