from pypdf import PdfReader

class FileParser:
    def __init__(self) -> None:
        pass
    
    def convert_pdf_to_text(pdf_file):
        reader = PdfReader(pdf_file)
        page = reader.pages[0]
        full_text = ''
        for page in reader.pages:
            full_text = full_text + page.extract_text()
        return full_text