# -*- coding: utf-8 -*-

###############################################################################
# Form generated from reading UI file 'ui_source_params.ui'
#
# Created by: Qt User Interface Compiler version 6.7.2
#
# WARNING! All changes made in this file will be lost when recompiling UI file!
###############################################################################

from PySide6.QtCore import QCoreApplication, QLocale, QMetaObject, QSize, Qt
from PySide6.QtGui import QDoubleValidator, QFont
from PySide6.QtWidgets import (
    QDialogButtonBox,
    QGridLayout,
    QLabel,
    QLineEdit,
    QSizePolicy,
    QVBoxLayout,
)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName("Dialog")
        Dialog.resize(220, 170)
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(220)
        sizePolicy.setVerticalStretch(170)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(220, 170))
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)

        self.only_double = QDoubleValidator()
        self.only_double.setLocale(
            QLocale(QLocale.English, QLocale.UnitedStates)
        )

        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.r_meas_lineedit = QLineEdit(Dialog)
        self.r_meas_lineedit.setObjectName("r_meas_lineedit")
        self.r_meas_lineedit.setInputMethodHints(
            Qt.InputMethodHint.ImhPreferNumbers
        )
        self.r_meas_lineedit.setValidator(self.only_double)

        self.gridLayout.addWidget(self.r_meas_lineedit, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.k_u_lineedit = QLineEdit(Dialog)
        self.k_u_lineedit.setObjectName("k_u_lineedit")
        self.k_u_lineedit.setInputMethodHints(
            Qt.InputMethodHint.ImhPreferNumbers
        )
        self.k_u_lineedit.setValidator(self.only_double)

        self.gridLayout.addWidget(self.k_u_lineedit, 1, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.r_one_lineedit = QLineEdit(Dialog)
        self.r_one_lineedit.setObjectName("r_one_lineedit")
        self.r_one_lineedit.setInputMethodHints(
            Qt.InputMethodHint.ImhPreferNumbers
        )
        self.r_one_lineedit.setValidator(self.only_double)

        self.gridLayout.addWidget(self.r_one_lineedit, 2, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

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

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate(
                "Dialog",
                "\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435",  # noqa: E501
                None,
            )
        )
        self.label.setText(
            QCoreApplication.translate("Dialog", "R\u0438\u0437\u043c", None)
        )
        self.r_meas_lineedit.setText(
            QCoreApplication.translate("Dialog", "352.8", None)
        )
        self.label_2.setText(QCoreApplication.translate("Dialog", "Ku", None))
        self.k_u_lineedit.setText(
            QCoreApplication.translate("Dialog", "2000", None)
        )
        self.label_3.setText(QCoreApplication.translate("Dialog", "R1", None))
        self.r_one_lineedit.setText(
            QCoreApplication.translate("Dialog", "0.683", None)
        )

    # retranslateUi
