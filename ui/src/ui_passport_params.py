# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_passport_params.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(375, 230)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(375, 230))
        Dialog.setMaximumSize(QSize(375, 230))
        font = QFont()
        font.setPointSize(12)
        Dialog.setFont(font)
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.type_lineedit = QLineEdit(Dialog)
        self.type_lineedit.setObjectName(u"type_lineedit")

        self.gridLayout.addWidget(self.type_lineedit, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.power_lineedit = QLineEdit(Dialog)
        self.power_lineedit.setObjectName(u"power_lineedit")

        self.gridLayout.addWidget(self.power_lineedit, 1, 1, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.u_lineedit = QLineEdit(Dialog)
        self.u_lineedit.setObjectName(u"u_lineedit")

        self.gridLayout.addWidget(self.u_lineedit, 2, 1, 1, 1)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.num_phases_lineedit = QLineEdit(Dialog)
        self.num_phases_lineedit.setObjectName(u"num_phases_lineedit")

        self.gridLayout.addWidget(self.num_phases_lineedit, 3, 1, 1, 1)

        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.material_lineedit = QLineEdit(Dialog)
        self.material_lineedit.setObjectName(u"material_lineedit")

        self.gridLayout.addWidget(self.material_lineedit, 4, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0422\u0438\u043f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 (U1/U2)", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u0430\u0437", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b \u043e\u0431\u043c\u043e\u0442\u043a\u0438", None))
    # retranslateUi

