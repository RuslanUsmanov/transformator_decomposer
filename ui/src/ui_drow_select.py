# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'ui_drow_select.ui'
#
# Created by: Qt User Interface Compiler version 6.7.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QAbstractItemView,
    QDialogButtonBox,
    QListView,
    QListWidget,
    QVBoxLayout,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(408, 391)
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.datadrow_listwidget = QListWidget(Dialog)
        self.datadrow_listwidget.setObjectName("datadrow_listwidget")
        self.datadrow_listwidget.setSelectionMode(
            QAbstractItemView.SelectionMode.MultiSelection
        )
        self.datadrow_listwidget.setViewMode(QListView.ViewMode.ListMode)
        self.datadrow_listwidget.setSelectionRectVisible(False)

        self.verticalLayout.addWidget(self.datadrow_listwidget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate(
                "Dialog",
                "\u0412\u044b\u0431\u043e\u0440 \u0434\u0430\u043d\u043d\u044b\u0445 \u0434\u043b\u044f \u0433\u0440\u0430\u0444\u0438\u043a\u0430",  # noqa: E501
                None,
            )
        )

    # retranslateUi
