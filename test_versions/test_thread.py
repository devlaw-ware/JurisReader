import sys
import time

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QLabel,
    QProgressBar
)

from PySide6.QtCore import (
    QThread,
    Signal,
    QTimer
)


class WorkerThread(QThread):

    finished = Signal(str)

    def run(self):

        time.sleep(5)

        self.finished.emit(
            "Resumo gerado com sucesso!"
        )


class Window(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "Teste Thread"
        )

        self.resize(400, 200)

        self.button = QPushButton(
            "Gerar Resumo"
        )

        self.label = QLabel(
            "Pronto"
        )

        self.progress_bar = QProgressBar()

        layout = QVBoxLayout()

        layout.addWidget(self.button)

        layout.addWidget(self.label)

        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

        self.button.clicked.connect(
            self.start_summary
        )

    def start_summary(self):

        self.label.setText(
            "Gerando resumo..."
        )

        self.progress = 0

        self.progress_bar.setValue(0)

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_progress
        )

        self.timer.start(100)

        self.thread = WorkerThread()

        self.thread.finished.connect(
            self.finish_summary
        )

        self.thread.start()

    def update_progress(self):

        if self.progress < 95:

            self.progress += 1

            self.progress_bar.setValue(
                self.progress
            )

    def finish_summary(self, message):

        self.timer.stop()

        self.progress_bar.setValue(100)

        self.label.setText(message)


app = QApplication(sys.argv)

window = Window()

window.show()

sys.exit(app.exec())