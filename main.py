import sys

from PySide6.QtWidgets import QApplication, QMainWindow

from ui.src.ui_mainwindow import Ui_MainWindow


class TrasformatorDesomposer(QMainWindow):
    def __init__(self) -> None:
        super(TrasformatorDesomposer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrasformatorDesomposer()
    window.show()

    sys.exit(app.exec())
