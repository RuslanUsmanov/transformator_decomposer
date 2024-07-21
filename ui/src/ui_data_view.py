# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'ui_data_view.ui'
#
# Created by: Qt User Interface Compiler version 6.7.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QDialogButtonBox, QTabWidget, QVBoxLayout


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(650, 650)
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_widget = QTabWidget(Dialog)
        self.tab_widget.setObjectName("tab_widget")

        self.verticalLayout.addWidget(self.tab_widget)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.StandardButton.Cancel
            | QDialogButtonBox.StandardButton.Ok
        )

        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.tab_widget.setCurrentIndex(-1)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate(
                "Dialog",
                "\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0434\u0430\u043d\u043d\u044b\u0445",  # noqa: E501
                None,
            )
        )

    # retranslateUi
