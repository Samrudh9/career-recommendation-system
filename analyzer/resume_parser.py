import pdfplumber

def extract_text_from_pdf(pdf_file_path):
    """Extracts text from a PDF file given its path."""
    text = ""
    with pdfplumber.open(pdf_file_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text