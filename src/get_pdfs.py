from pathlib import Path
import pdfplumber as pdftool

exam_test_folder_path = Path("data/pdfs")

for file in exam_test_folder_path.glob('*.pdf'):

    with pdftool.open(file) as test_pdf_file:
        for n_pag, pag in enumerate(test_pdf_file.pages, 1):
            print("----Page number: ", n_pag)
            data = pag.extract_text()
            
    
