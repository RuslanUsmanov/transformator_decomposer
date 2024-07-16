import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
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
            filter="Файл данных (*.txt *.csv)",
            dir=str(Path.home())
        )
        if not filenames:
            return

        QGuiApplication.setOverrideCursor(Qt.WaitCursor)

        try:
            self.dHandler.read_from_file(filenames)
        except Exception as ex:
            QGuiApplication.restoreOverrideCursor()
            msg_box = QErrorMessage(self)
            msg_box.setWindowTitle("Ошибка")
            msg_box.showMessage(f"Ошибка во время чтения файла:\n{repr(ex)}")
            return

        self.ui.current_start_lineedit.setText(
            f"{float(self.dHandler.data["dataset"][0]):.6f}"
        )
        popt = self.dHandler.get_coefficients()
        mertics = self.dHandler.get_metrics(popt)
        self._update_coeffs(popt)
        self._update_metrics(mertics)
        self._draw_plot()

        QGuiApplication.restoreOverrideCursor()

    def _update_coeffs(self, popt):
        self.ui.c1_lineedit.setText(f"{float(popt[0]):.6f}")
        self.ui.a1_lineedit.setText(f"{float(popt[1]):.6f}")
        self.ui.c2_lineedit.setText(f"{float(popt[2]):.6f}")
        self.ui.a2_lineedit.setText(f"{float(popt[3]):.6f}")
        self.ui.c3_lineedit.setText(f"{float(popt[4]):.6f}")
        self.ui.a3_lineedit.setText(f"{float(popt[5]):.6f}")

    def _update_metrics(self, metrics):
        self.ui.mae_lineedit.setText(f"{float(metrics["mae"]):.6f}")
        self.ui.mape_lineedit.setText(f"{float(metrics["mape"]):.6f}")
        self.ui.mdae_linedit.setText(f"{float(metrics["mdae"]):.6f}")
        self.ui.mse_lineedit.setText(f"{float(metrics["mse"]):.6f}")
        self.ui.r2_lineedit.setText(f"{float(metrics["r2"]):.6f}")

    def _draw_plot(self):
        self.ui.mpl_canvas.figure.clear()
        ax = self.ui.mpl_canvas.figure.subplots()
        ax.plot(self.dHandler.data.index, self.dHandler.data["dataset"])
        ax.grid(True)
        self.ui.mpl_canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrasformatorDesomposer()
    window.show()

    sys.exit(app.exec())
