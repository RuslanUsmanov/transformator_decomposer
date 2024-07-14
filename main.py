import os
import sys

from PySide6.QtWidgets import (
    QApplication,
    QErrorMessage,
    QFileDialog,
    QMainWindow,
)

from core import service
from ui.src.ui_mainwindow import Ui_MainWindow


class TrasformatorDesomposer(QMainWindow):
    def __init__(self) -> None:
        super(TrasformatorDesomposer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dHandler = service.DataHandler()

        self.ui.select_files_pushbutton.clicked.connect(
            self.open_select_files_dialog
        )

    def open_select_files_dialog(self):
        filenames, _ = QFileDialog.getOpenFileName(
            self,
            caption="Выберите файлы",
            filter="Файл данных (*.txt *.csv *.dat)",
            dir=f"{os.getenv("HOME")}",
        )
        if not filenames:
            return

        try:
            self.dHandler.read_from_file(filenames)
        except Exception as ex:
            msg_box = QErrorMessage(self)
            msg_box.setWindowTitle("Ошибка")
            msg_box.showMessage(f"Ошибка во время чтения файла:\n{repr(ex)}")
            return

        self.update_coeffs()

    def update_coeffs(self):
        popt = self.dHandler.get_coefficients()
        self.ui.c1_lineedit.setText(str(popt[0]))
        self.ui.a1_lineedit.setText(str(popt[1]))
        self.ui.c2_lineedit.setText(str(popt[2]))
        self.ui.a2_lineedit.setText(str(popt[3]))
        self.ui.c3_lineedit.setText(str(popt[4]))
        self.ui.a3_lineedit.setText(str(popt[5]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrasformatorDesomposer()
    window.show()

    sys.exit(app.exec())
