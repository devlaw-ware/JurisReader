from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QFileDialog
)

from software.services.extraction_service import extract_dates, extract_values
from software.services.pdf_service import extract_text
from software.services.ai_service import summarize_text 


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Juris_Reader")
        self.resize(800, 600)

        self.button = QPushButton("Abrir PDF")
        self.summary_button = QPushButton("Gerar Resumo do Processo")  #Button create to generate summary of the text extracted from the pdf file

        self.text_area = QTextEdit()
        self.info_area = QTextEdit()

        layout = QVBoxLayout()

        layout.addWidget(self.button)
        layout.addWidget(self.summary_button) #Add the summary button to the layout
        layout.addWidget(self.text_area)
        layout.addWidget(self.info_area)

        self.setLayout(layout)

        self.button.clicked.connect(self.open_pdf)
        self.summary_button.clicked.connect(self.generate_summary) #Connect the summary button to the generate_summary method 

    def open_pdf(self):
        
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar PDF",
            "",
            "PDF Files (*.pdf)"
        )
        

        if file_path:

            text = extract_text(file_path)
            self.current_text = text #Store the extracted text in a variable to be used later for generating the summary
            self.text_area.setText(text)
            dates = extract_dates(text)
            values = extract_values(text)
            
            info_text = f"""
DATAS:

{'\n'.join(dates)}

VALORES:

{'\n'.join(values)}
"""

        self.info_area.setText(info_text)

    def generate_summary(self):

        if hasattr(self, 'current_text'):
            summary = summarize_text(self.current_text) #Generate the summary using the current text extracted from the pdf file
            self.text_area.setText(summary) #Display the summary in the text areas
    