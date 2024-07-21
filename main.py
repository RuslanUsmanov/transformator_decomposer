import sys
from pathlib import Path

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QErrorMessage,
    QFileDialog,
    QMainWindow,
    QTableView,
)

from core import service
from core.parameters import PassportParams, SourceParams
from ui.src.ui_mainwindow import Ui_MainWindow
from ui.src.ui_passport_params import Ui_Dialog as Ui_PassportParamsDialog
from ui.src.ui_source_params import Ui_Dialog as Ui_SourceParamsDialog


class PandasModel(QAbstractTableModel):
    def __init__(self, dataframe, parent=None):
        super(PandasModel, self).__init__()
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(
        self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole
    ):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as
        horizontal header data.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])

        return None


class TrasformatorDesomposer(QMainWindow):
    def __init__(self) -> None:
        super(TrasformatorDesomposer, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.source_params_window = QDialog()
        self.ui_source = Ui_SourceParamsDialog()
        self.ui_source.setupUi(self.source_params_window)

        self.passport_params_window = QDialog()
        self.ui_passport = Ui_PassportParamsDialog()
        self.ui_passport.setupUi(self.passport_params_window)

        self.data_select_window = QDialog()
        self.ui_select_data = Ui_DataSelectDialog()
        self.ui_select_data.setupUi(self.data_select_window)

        self.data_view_window = QDialog()
        self.ui_view_data = Ui_DataViewDialog()
        self.ui_view_data.setupUi(self.data_view_window)

        self._connect_handlers()
        self._init_data()
        self._update_passport_ui()

    def _init_data(self):
        self.dHandler = service.DataHandler()
        self._source_params = SourceParams()
        self._passport_params = PassportParams()
        self._ranges = None

    def _connect_handlers(self):
        """Подключение обработчиков к кнопкам и т.д."""
        self.ui.select_files_pushbutton.clicked.connect(
            self._open_select_files_dialog,
        )
        self.ui.source_params_action.triggered.connect(
            self.source_params_window.show,
        )
        self.ui.passport_params_action.triggered.connect(
            self.passport_params_window.show,
        )
        self.ui.data_view_pushbutton.clicked.connect(
            self.data_view_window.show,
        )
        self.ui.calculate_pushbutton.clicked.connect(
            self.data_select_window.show
        )
        self.ui.constr_radiobutton.clicked.connect(
            self._toggle_ranges
        )
        self.ui.no_constr_radiobutton.clicked.connect(
            self._toggle_ranges
        )

        # Dialog windows
        self.passport_params_window.accepted.connect(
            self._update_passport_params,
        )
        self.source_params_window.accepted.connect(
            self._update_source_params,
        )
        self.data_select_window.accepted.connect(
            self._calculate_all
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
        self._update_coeffs_ui(popt)
        self._update_metrics_ui(mertics)
        self._draw_plot()

        QGuiApplication.restoreOverrideCursor()

    def _update_coeffs_ui(self, popt):
        self.ui.c1_lineedit.setText(f"{float(popt[0]):.6f}")
        self.ui.a1_lineedit.setText(f"{float(popt[1]):.6f}")
        self.ui.c2_lineedit.setText(f"{float(popt[2]):.6f}")
        self.ui.a2_lineedit.setText(f"{float(popt[3]):.6f}")
        self.ui.c3_lineedit.setText(f"{float(popt[4]):.6f}")
        self.ui.a3_lineedit.setText(f"{float(popt[5]):.6f}")

    def _update_metrics_ui(self, metrics):
        self.ui.mae_lineedit.setText(f"{float(metrics["mae"]):.6f}")
        self.ui.mape_lineedit.setText(f"{float(metrics["mape"]):.6f}")
        self.ui.mdae_linedit.setText(f"{float(metrics["mdae"]):.6f}")
        self.ui.mse_lineedit.setText(f"{float(metrics["mse"]):.6f}")
        self.ui.r2_lineedit.setText(f"{float(metrics["r2"]):.6f}")

    def _update_passport_ui(self):
        self.ui.passport_type_lineedit.setText(self._passport_params.type)
        self.ui.passport_p_lineedit.setText(
            f"{self._passport_params.power:.6f}"
        )
        self.ui.passport_phase_lineedit.setText(
            f"{self._passport_params.phase_num}"
        )
        self.ui.passport_material_lineedit.setText(
            self._passport_params.material
        )
        self.ui.passport_u_lineedit.setText(
            f"{self._passport_params.voltage:.6f}"
        )

    def _draw_plot(self):
        self.ui.mpl_canvas.figure.clear()
        ax = self.ui.mpl_canvas.figure.subplots()
        ax.plot(
            self.dHandler.data.index,
            self.dHandler.data["dataset"],
            label="Исходный ряд"
        )
        ax.grid(True)
        self.ui.mpl_canvas.draw()

    def _update_passport_params(self):
        self._passport_params.type = self.ui_passport.type_lineedit.text()
        self._passport_params.material = (
            self.ui_passport.material_lineedit.text()
        )
        self._passport_params.power = float(
            self.ui_passport.power_lineedit.text()
        )
        self._passport_params.phase_num = int(
            self.ui_passport.num_phases_lineedit.text()
        )
        self._passport_params.voltage = float(
            self.ui_passport.u_lineedit.text()
        )

        self._update_passport_ui()

    def _update_source_params(self):
        self._source_params.R_meas = float(
            self.ui_source.r_meas_lineedit.text()
        )
        self._source_params.R_one = float(
            self.ui_source.r_one_lineedit.text()
        )
        self._source_params.K_u = float(
            self.ui_source.k_u_lineedit.text()
        )

    def _show_source_settings_window(self):
        self.source_params_window.show()

    def _show_passport_settings_window(self):
        self.passport_params_window.show()

    def _toggle_ranges(self):
        if self.ui.constr_radiobutton.isChecked():
            self.ui.from_points_lineedit.setDisabled(False)
            self.ui.to_points_lineedit.setDisabled(False)
        if self.ui.no_constr_radiobutton.isChecked():
            self.ui.from_points_lineedit.setDisabled(True)
            self.ui.to_points_lineedit.setDisabled(True)
            self.ui.from_points_lineedit.setText("")
            self.ui.to_points_lineedit.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrasformatorDesomposer()
    window.show()

    sys.exit(app.exec())
