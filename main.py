from software.services.pdf_service import extract_text

pdf_path = "docs/teste.pdf"

text = extract_text(pdf_path)

print(text)
 