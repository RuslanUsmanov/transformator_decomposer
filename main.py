import os
import sys
from pathlib import Path

from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QErrorMessage,
    QFileDialog,
    QMainWindow,
    QTableView,
)

from core import service
from core.decompose import calc_kst, calc_kvkz, func
from core.parameters import PassportParams, SourceParams
from ui.src.ui_data_select import Ui_Dialog as Ui_DataSelectDialog
from ui.src.ui_data_view import Ui_Dialog as Ui_DataViewDialog
from ui.src.ui_drow_select import Ui_Dialog as Ui_DrowSelectDialog
from ui.src.ui_mainwindow import Ui_MainWindow
from ui.src.ui_passport_params import Ui_Dialog as Ui_PassportParamsDialog
from ui.src.ui_source_params import Ui_Dialog as Ui_SourceParamsDialog

basedir = os.path.dirname(__file__)


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

        self.drow_select_window = QDialog()
        self.ui_drow_select = Ui_DrowSelectDialog()
        self.ui_drow_select.setupUi(self.drow_select_window)

        self._connect_handlers()
        self._init_data()
        self._update_passport_ui()

    def _init_data(self):
        """Инициализация переменных."""
        self.datasets: dict[str, service.DataSet] = {}
        self.plots: dict[str, service.Plot] = {}
        self._source_params = SourceParams()
        self._passport_params = PassportParams()

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
        self.ui.draw_plot_pushutton.clicked.connect(
            self.drow_select_window.show
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
        self.drow_select_window.accepted.connect(
            self._redraw_plots
        )

    def _open_select_files_dialog(self):
        """Получает список файлов и выполняет их преобразование в DataFrame."""
        filenames, _ = QFileDialog.getOpenFileNames(
            self,
            caption="Выберите файлы",
            filter="Файл данных (*.txt *.csv)",
            dir=str(Path.home())
        )
        if not filenames:
            return

        QGuiApplication.setOverrideCursor(Qt.WaitCursor)
        self.datasets = {}
        self.plots = {}

        try:
            self.datasets = service.read_data_from_files(filenames)
        except Exception as ex:
            QGuiApplication.restoreOverrideCursor()
            msg_box = QErrorMessage(self)
            msg_box.setWindowTitle("Ошибка")
            msg_box.showMessage(f"Ошибка во время чтения файла:\n{repr(ex)}")
            return

        self._clear_all()

        self._update_data_view_tables()
        self._update_data_select_list()
        self._update_plots_after_load()
        self.ui.data_view_pushbutton.setEnabled(True)
        self.ui.draw_plot_pushutton.setEnabled(True)
        self.ui.calculate_pushbutton.setEnabled(True)
        QGuiApplication.restoreOverrideCursor()

    def _update_data_view_tables(self):
        for filename, dataset in self.datasets.items():
            model = PandasModel(dataset.dataset)
            view = QTableView()
            self.ui_view_data.tab_widget.addTab(view, filename)
            view.setModel(model)

    def _update_data_select_list(self):
        self.ui_select_data.dataset_listwidget.addItems(
            name for name in self.datasets.keys()
        )

    def _update_coeffs_ui(self, popt_1, popt_2):
        self.ui.c1_lineedit_1.setText(f"{float(popt_1[0]):.6f}")
        self.ui.a1_lineedit_1.setText(f"{float(popt_1[1]):.6f}")
        self.ui.c2_lineedit_1.setText(f"{float(popt_1[2]):.6f}")
        self.ui.a2_lineedit_1.setText(f"{float(popt_1[3]):.6f}")
        self.ui.c3_lineedit_1.setText(f"{float(popt_1[4]):.6f}")
        self.ui.a3_lineedit_1.setText(f"{float(popt_1[5]):.6f}")

        self.ui.c1_lineedit_2.setText(f"{float(popt_2[0]):.6f}")
        self.ui.a1_lineedit_2.setText(f"{float(popt_2[1]):.6f}")
        self.ui.c2_lineedit_2.setText(f"{float(popt_2[2]):.6f}")
        self.ui.a2_lineedit_2.setText(f"{float(popt_2[3]):.6f}")
        self.ui.c3_lineedit_2.setText(f"{float(popt_2[4]):.6f}")
        self.ui.a3_lineedit_2.setText(f"{float(popt_2[5]):.6f}")

    def _clear_all(self):
        self.ui.mae_lineedit_1.setText("")
        self.ui.mape_lineedit_1.setText("")
        self.ui.mdae_linedit_1.setText("")
        self.ui.mse_lineedit_1.setText("")
        self.ui.r2_lineedit_1.setText("")

        self.ui.mae_lineedit_2.setText("")
        self.ui.mape_lineedit_2.setText("")
        self.ui.mdae_linedit_2.setText("")
        self.ui.mse_lineedit_2.setText("")
        self.ui.r2_lineedit_2.setText("")

        self.ui.c1_lineedit_1.setText("")
        self.ui.a1_lineedit_1.setText("")
        self.ui.c2_lineedit_1.setText("")
        self.ui.a2_lineedit_1.setText("")
        self.ui.c3_lineedit_1.setText("")
        self.ui.a3_lineedit_1.setText("")

        self.ui.c1_lineedit_2.setText("")
        self.ui.a1_lineedit_2.setText("")
        self.ui.c2_lineedit_2.setText("")
        self.ui.a2_lineedit_2.setText("")
        self.ui.c3_lineedit_2.setText("")
        self.ui.a3_lineedit_2.setText("")

        self.ui.kst_lineedit.setText("")
        self.ui.kvkz_lineedit.setText("")

        self.ui.current_start_lineedit_0.setText("")
        self.ui.current_start_lineedit_1.setText("")
        self.ui.file_0_label.setText("Файл 1")
        self.ui.file_1_label.setText("Файл 2")

        self.ui.decomp_tabwidget.setTabText(0, "График 1")
        self.ui.decomp_tabwidget.setTabText(1, "График 2")

        self.ui.metrics_tabwidget.setTabText(0, "График 1")
        self.ui.metrics_tabwidget.setTabText(1, "График 2")

        self.ui.mpl_canvas.figure.clear()

        self.ui_view_data.tab_widget.clear()

        self.ui_select_data.dataset_listwidget.clear()
        self.ui_drow_select.datadrow_listwidget.clear()

        self.ui.mpl_canvas.figure.clear()

    def _update_metrics_ui(
        self,
        metrics_1: dict[str, int],
        metrics_2: dict[str, int],
    ):
        self.ui.mae_lineedit_1.setText(f"{float(metrics_1["mae"]):.6f}")
        self.ui.mape_lineedit_1.setText(f"{float(metrics_1["mape"]):.6f}")
        self.ui.mdae_linedit_1.setText(f"{float(metrics_1["mdae"]):.6f}")
        self.ui.mse_lineedit_1.setText(f"{float(metrics_1["mse"]):.6f}")
        self.ui.r2_lineedit_1.setText(f"{float(metrics_1["r2"]):.6f}")

        self.ui.mae_lineedit_2.setText(f"{float(metrics_2["mae"]):.6f}")
        self.ui.mape_lineedit_2.setText(f"{float(metrics_2["mape"]):.6f}")
        self.ui.mdae_linedit_2.setText(f"{float(metrics_2["mdae"]):.6f}")
        self.ui.mse_lineedit_2.setText(f"{float(metrics_2["mse"]):.6f}")
        self.ui.r2_lineedit_2.setText(f"{float(metrics_2["r2"]):.6f}")

    def _update_passport_ui(self):
        self.ui.passport_type_lineedit.setText(self._passport_params.type)
        self.ui.passport_p_lineedit.setText(self._passport_params.power)
        self.ui.passport_phase_lineedit.setText(
            self._passport_params.phase_num
        )
        self.ui.passport_material_lineedit.setText(
            self._passport_params.material
        )
        self.ui.passport_u_lineedit.setText(self._passport_params.voltage)

    def _update_plots_after_load(self):
        for name in self.datasets.keys():
            self.plots[name + " исходный ряд"] = service.Plot(
                x=self.datasets[name].dataset["time"].to_numpy(),
                y=self.datasets[name].dataset["dataset"].to_numpy(),
                label=name + " исходный ряд",
            )
        self._update_plots_select()

    def _update_plots_select(self):
        self.ui_drow_select.datadrow_listwidget.clear()
        self.ui_drow_select.datadrow_listwidget.addItems(
            name for name in self.plots.keys()
        )

    def _redraw_plots(self):
        self.ui.mpl_canvas.figure.clear()
        selected_plots = [
            item.text()
            for item in self.ui_drow_select.datadrow_listwidget.selectedItems()
        ]

        ax = self.ui.mpl_canvas.figure.subplots()
        for plot in selected_plots:
            ax.plot(
                self.plots[plot].x,
                self.plots[plot].y,
                label=self.plots[plot].label,
            )
        ax.legend()
        ax.grid(True)
        self.ui.mpl_canvas.draw()

    def _update_passport_params(self):
        self._passport_params.type = self.ui_passport.type_lineedit.text()
        self._passport_params.material = (
            self.ui_passport.material_lineedit.text()
        )
        self._passport_params.power = (
            self.ui_passport.power_lineedit.text()
        )
        self._passport_params.phase_num = (
            self.ui_passport.num_phases_lineedit.text()
        )
        self._passport_params.voltage = (
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

    def _toggle_ranges(self):
        if self.ui.constr_radiobutton.isChecked():
            self.ui.from_points_lineedit.setDisabled(False)
            self.ui.to_points_lineedit.setDisabled(False)
        if self.ui.no_constr_radiobutton.isChecked():
            self.ui.from_points_lineedit.setDisabled(True)
            self.ui.to_points_lineedit.setDisabled(True)
            self.ui.from_points_lineedit.setText("")
            self.ui.to_points_lineedit.setText("")

    def _update_tab_names(self, names):
        self.ui.file_0_label.setText(names[0])
        self.ui.current_start_lineedit_0.setText(
            f"{self.datasets[names[0]].dataset_scaled["dataset"][0]:.6f}"
        )
        self.ui.file_1_label.setText(names[1])
        self.ui.current_start_lineedit_1.setText(
            f"{self.datasets[names[1]].dataset_scaled["dataset"][0]:.6f}"
        )
        for i in range(len(names)):
            self.ui.decomp_tabwidget.setTabText(i, names[i])
            self.ui.metrics_tabwidget.setTabText(i, names[i])

    def _update_criteria_coeffs(self, popt_1, popt_2):
        kvkz = calc_kvkz(popt_1, popt_2)
        self.ui.kvkz_lineedit.setText(f"{kvkz:.6f}")

        kst = calc_kst(popt_1, popt_2)
        if kst:
            self.ui.kst_lineedit.setText(f"{kst:.6f}")
        else:
            self.ui.kst_lineedit.setText("Условие не выполнено.")

    def _calculate_all(self):
        QGuiApplication.setOverrideCursor(Qt.WaitCursor)
        if self.ui.constr_radiobutton.isChecked():
            from_points = int(self.ui.from_points_lineedit.text())
            to_points = int(self.ui.to_points_lineedit.text())
            if from_points >= to_points:
                QGuiApplication.restoreOverrideCursor()
                msg_box = QErrorMessage(self)
                msg_box.setWindowTitle("Ошибка")
                msg_box.showMessage("Некорректный диапазон.")
                return
        else:
            from_points = None
            to_points = None

        selected_names = [
            item.text()
            for item in self.ui_select_data.dataset_listwidget.selectedItems()
        ]

        if len(selected_names) != 2:
            QGuiApplication.restoreOverrideCursor()
            msg_box = QErrorMessage(self)
            msg_box.setWindowTitle("Ошибка")
            msg_box.showMessage("Необходимо выбрать два набора данных.")
            return

        self.datasets[selected_names[0]].scale_dataset(
            self._source_params,
            from_points,
            to_points,
        )
        self.datasets[selected_names[1]].scale_dataset(
            self._source_params,
            from_points,
            to_points,
        )
        try:
            popt_1 = self.datasets[selected_names[0]].get_coefficients()
            popt_2 = self.datasets[selected_names[1]].get_coefficients()
        except Exception as ex:
            QGuiApplication.restoreOverrideCursor()
            msg_box = QErrorMessage(self)
            msg_box.setWindowTitle("Ошибка")
            msg_box.showMessage(f"Ошибка вычисления: {repr(ex)}")
            return

        metrics_1 = self.datasets[selected_names[0]].get_metrics(popt_1)
        metrics_2 = self.datasets[selected_names[1]].get_metrics(popt_1)

        self.plots[selected_names[0] + " данные"] = service.Plot(
            x=self.datasets[
                selected_names[0]
            ].dataset_scaled["time"].to_numpy(),
            y=self.datasets[
                selected_names[0]
            ].dataset_scaled["dataset"].to_numpy(),
            label=selected_names[0] + " данные"
        )
        self.plots[selected_names[1] + " данные"] = service.Plot(
            x=self.datasets[
                selected_names[1]
            ].dataset_scaled["time"].to_numpy(),
            y=self.datasets[
                selected_names[1]
            ].dataset_scaled["dataset"].to_numpy(),
            label=selected_names[1] + " данные"
        )

        self.plots[selected_names[0] + " функция"] = service.Plot(
            x=self.datasets[
                selected_names[0]
            ].dataset_scaled["time"].to_numpy(),
            y=func(
                self.datasets[
                    selected_names[0]
                ].dataset_scaled["time"].to_numpy(),
                *popt_1,
            ),
            label=selected_names[0] + " функция"
        )
        self.plots[selected_names[1] + " функция"] = service.Plot(
            x=self.datasets[
                selected_names[1]
            ].dataset_scaled["time"].to_numpy(),
            y=func(
                self.datasets[
                    selected_names[1]
                ].dataset_scaled["time"].to_numpy(),
                *popt_2,
            ),
            label=selected_names[1] + " функция"
        )

        self._update_coeffs_ui(popt_1, popt_2)
        self._update_metrics_ui(metrics_1,  metrics_2)
        self._update_criteria_coeffs(popt_1, popt_2)

        self._update_tab_names(selected_names)
        self._update_plots_select()
        QGuiApplication.restoreOverrideCursor()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(
        QIcon(os.path.join(basedir, "ui/resources/logo/app_logo.ico"))
    )
    window = TrasformatorDesomposer()
    window.show()

    sys.exit(app.exec())
