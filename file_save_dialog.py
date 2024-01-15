from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog


class FileSaveDialog(QWidget):
    def __init__(self):
        super().__init__()

        self.path_name = None

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(self, "Zapisz plik", "", "Pliki tekstowe (*.txt);;Wszystkie pliki (*)", options=options)

        if file_name:
            self.path_name = file_name
