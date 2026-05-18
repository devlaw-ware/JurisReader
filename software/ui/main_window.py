from PySide6.QtWidgets import (
    QWidget,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QFileDialog,
    QLabel,
    QProgressBar
)

from PySide6.QtCore import (
    QThread,
    Signal,
    QTimer
)

from software.services.extraction_service import (
    extract_dates,
    extract_values
)

from software.services.pdf_service import extract_text

from software.services.ai_service import summarize_text


class SummaryThread(QThread):

    finished = Signal(str)

    def __init__(self, text):

        super().__init__()

        self.text = text

    def run(self):

        summary = summarize_text(self.text)

        self.finished.emit(summary)


class MainWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Juris_Reader")

        self.resize(800, 600)

        self.button = QPushButton("Abrir PDF")

        self.summary_button = QPushButton(
            "Gerar Resumo do Processo"
        )

        self.status_label = QLabel(
            "Ao gerar o resumo, aguarde até sua conclusão."
        )

        self.progress_bar = QProgressBar()

        self.text_area = QTextEdit()

        self.info_area = QTextEdit()

        layout = QVBoxLayout()

        layout.addWidget(self.button)

        layout.addWidget(self.summary_button)

        layout.addWidget(self.status_label)

        layout.addWidget(self.progress_bar)

        layout.addWidget(self.text_area)

        layout.addWidget(self.info_area)

        self.setLayout(layout)

        self.button.clicked.connect(self.open_pdf)

        self.summary_button.clicked.connect(
            self.generate_summary
        )

    def open_pdf(self):

        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar PDF",
            "",
            "PDF Files (*.pdf)"
        )

        if file_path:

            text = extract_text(file_path)

            self.current_text = text

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

            self.status_label.setText(
                "Gerando resumo..."
            )

            self.progress = 0

            self.progress_bar.setValue(0)

            self.timer = QTimer()

            self.timer.timeout.connect(
                self.update_progress
            )

            self.timer.start(100)

            self.thread = SummaryThread(
                self.current_text
            )

            self.thread.finished.connect(
                self.show_summary
            )

            self.thread.start()

    def update_progress(self):

        if self.progress < 95:

            self.progress += 1

            self.progress_bar.setValue(
                self.progress
            )

    def show_summary(self, summary):

        self.timer.stop()

        self.progress_bar.setValue(100)

        self.text_area.setText(summary)

        self.status_label.setText(
            "Resumo concluído."
        )