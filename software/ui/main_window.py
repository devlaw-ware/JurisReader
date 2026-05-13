from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QFileDialog
)

from software.services.pdf_service import extract_text


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("JurisReader")
        self.resize(800, 600)

        self.button = QPushButton("Abrir PDF")

        self.text_area = QTextEdit()

        layout = QVBoxLayout()

        layout.addWidget(self.button)
        layout.addWidget(self.text_area)

        self.setLayout(layout)

        self.button.clicked.connect(self.open_pdf)

    def open_pdf(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar PDF",
            "",
            "PDF Files (*.pdf)"
        )

        if file_path:

            text = extract_text(file_path)

            self.text_area.setText(text)