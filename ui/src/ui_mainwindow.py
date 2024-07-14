# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1366, 768)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.graphicsView = QGraphicsView(self.groupBox_6)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_9.addWidget(self.graphicsView)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer)

        self.pushButton_3 = QPushButton(self.groupBox_6)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_9.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_6)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_9.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox_6)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_9.addWidget(self.pushButton_5)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)


        self.horizontalLayout_9.addLayout(self.verticalLayout_9)


        self.gridLayout_5.addWidget(self.groupBox_6, 0, 1, 1, 1)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.groupBox_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.diapason_select_group = QGroupBox(self.centralwidget)
        self.diapason_select_group.setObjectName(u"diapason_select_group")
        self.horizontalLayout_4 = QHBoxLayout(self.diapason_select_group)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_7)

        self.no_constr_radiobutton = QRadioButton(self.diapason_select_group)
        self.no_constr_radiobutton.setObjectName(u"no_constr_radiobutton")
        self.no_constr_radiobutton.setEnabled(True)
        self.no_constr_radiobutton.setChecked(True)

        self.verticalLayout.addWidget(self.no_constr_radiobutton)

        self.constr_radiobutton = QRadioButton(self.diapason_select_group)
        self.constr_radiobutton.setObjectName(u"constr_radiobutton")

        self.verticalLayout.addWidget(self.constr_radiobutton)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_8)


        self.horizontalLayout_4.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.diapason_select_group)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.diapason_select_group)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.from_points_lineedit = QLineEdit(self.diapason_select_group)
        self.from_points_lineedit.setObjectName(u"from_points_lineedit")
        self.from_points_lineedit.setEnabled(False)
        self.from_points_lineedit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.from_points_lineedit)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.diapason_select_group)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.to_points_lineedit = QLineEdit(self.diapason_select_group)
        self.to_points_lineedit.setObjectName(u"to_points_lineedit")
        self.to_points_lineedit.setEnabled(False)
        self.to_points_lineedit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_3.addWidget(self.to_points_lineedit)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_4.addWidget(self.diapason_select_group)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.current_start_lineedit = QLineEdit(self.groupBox)
        self.current_start_lineedit.setObjectName(u"current_start_lineedit")
        self.current_start_lineedit.setMaximumSize(QSize(150, 16777215))
        self.current_start_lineedit.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.current_start_lineedit)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_5.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)


        self.verticalLayout_4.addWidget(self.groupBox)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_7)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_14.addWidget(self.label_16)

        self.c3_lineedit = QLineEdit(self.groupBox_3)
        self.c3_lineedit.setObjectName(u"c3_lineedit")
        self.c3_lineedit.setMaximumSize(QSize(250, 16777215))
        self.c3_lineedit.setReadOnly(True)

        self.horizontalLayout_14.addWidget(self.c3_lineedit)


        self.gridLayout.addLayout(self.horizontalLayout_14, 2, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_7.addWidget(self.label_8)

        self.c1_lineedit = QLineEdit(self.groupBox_3)
        self.c1_lineedit.setObjectName(u"c1_lineedit")
        self.c1_lineedit.setMaximumSize(QSize(250, 16777215))
        self.c1_lineedit.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.c1_lineedit)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_13.addWidget(self.label_15)

        self.c2_lineedit = QLineEdit(self.groupBox_3)
        self.c2_lineedit.setObjectName(u"c2_lineedit")
        self.c2_lineedit.setMaximumSize(QSize(250, 16777215))
        self.c2_lineedit.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.c2_lineedit)


        self.gridLayout.addLayout(self.horizontalLayout_13, 1, 0, 1, 1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_19 = QLabel(self.groupBox_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_17.addWidget(self.label_19)

        self.a3_lineedit = QLineEdit(self.groupBox_3)
        self.a3_lineedit.setObjectName(u"a3_lineedit")
        self.a3_lineedit.setMaximumSize(QSize(250, 16777215))
        self.a3_lineedit.setReadOnly(True)

        self.horizontalLayout_17.addWidget(self.a3_lineedit)


        self.gridLayout.addLayout(self.horizontalLayout_17, 2, 1, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_18 = QLabel(self.groupBox_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_16.addWidget(self.label_18)

        self.a2_lineedit = QLineEdit(self.groupBox_3)
        self.a2_lineedit.setObjectName(u"a2_lineedit")
        self.a2_lineedit.setMaximumSize(QSize(250, 16777215))
        self.a2_lineedit.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.a2_lineedit)


        self.gridLayout.addLayout(self.horizontalLayout_16, 1, 1, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_17 = QLabel(self.groupBox_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_15.addWidget(self.label_17)

        self.a1_lineedit = QLineEdit(self.groupBox_3)
        self.a1_lineedit.setObjectName(u"a1_lineedit")
        self.a1_lineedit.setMaximumSize(QSize(250, 16777215))
        self.a1_lineedit.setReadOnly(True)

        self.horizontalLayout_15.addWidget(self.a1_lineedit)


        self.gridLayout.addLayout(self.horizontalLayout_15, 0, 1, 1, 1)


        self.verticalLayout_5.addLayout(self.gridLayout)


        self.verticalLayout_8.addWidget(self.groupBox_3)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_25 = QLabel(self.groupBox_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_7.addWidget(self.label_25)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_5)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.label_20, 0, 0, 1, 1)

        self.mse_lineedit = QLineEdit(self.groupBox_4)
        self.mse_lineedit.setObjectName(u"mse_lineedit")
        self.mse_lineedit.setMaximumSize(QSize(250, 16777215))
        self.mse_lineedit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.mse_lineedit, 0, 1, 1, 1)

        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.label_21, 1, 0, 1, 1)

        self.mae_lineedit = QLineEdit(self.groupBox_4)
        self.mae_lineedit.setObjectName(u"mae_lineedit")
        self.mae_lineedit.setMaximumSize(QSize(250, 16777215))
        self.mae_lineedit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.mae_lineedit, 1, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.label_22, 2, 0, 1, 1)

        self.mape_lineedit = QLineEdit(self.groupBox_4)
        self.mape_lineedit.setObjectName(u"mape_lineedit")
        self.mape_lineedit.setMaximumSize(QSize(250, 16777215))
        self.mape_lineedit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.mape_lineedit, 2, 1, 1, 1)

        self.label_23 = QLabel(self.groupBox_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.label_23, 3, 0, 1, 1)

        self.mdae_linedit = QLineEdit(self.groupBox_4)
        self.mdae_linedit.setObjectName(u"mdae_linedit")
        self.mdae_linedit.setMaximumSize(QSize(250, 16777215))
        self.mdae_linedit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.mdae_linedit, 3, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_2.addWidget(self.label_24, 4, 0, 1, 1)

        self.r2_lineedit = QLineEdit(self.groupBox_4)
        self.r2_lineedit.setObjectName(u"r2_lineedit")
        self.r2_lineedit.setMaximumSize(QSize(250, 16777215))
        self.r2_lineedit.setReadOnly(True)

        self.gridLayout_2.addWidget(self.r2_lineedit, 4, 1, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_2)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_6)


        self.horizontalLayout_8.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_26 = QLabel(self.groupBox_5)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_6.addWidget(self.label_26)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_27 = QLabel(self.groupBox_5)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)

        self.kvkz_lineedit = QLineEdit(self.groupBox_5)
        self.kvkz_lineedit.setObjectName(u"kvkz_lineedit")
        self.kvkz_lineedit.setMaximumSize(QSize(250, 16777215))
        self.kvkz_lineedit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.kvkz_lineedit, 0, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_5)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(75, 16777215))

        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)

        self.kst_lineedit = QLineEdit(self.groupBox_5)
        self.kst_lineedit.setObjectName(u"kst_lineedit")
        self.kst_lineedit.setMaximumSize(QSize(250, 16777215))
        self.kst_lineedit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.kst_lineedit, 1, 1, 1, 1)


        self.verticalLayout_6.addLayout(self.gridLayout_3)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)


        self.horizontalLayout_8.addWidget(self.groupBox_5)


        self.verticalLayout_8.addLayout(self.horizontalLayout_8)


        self.gridLayout_5.addLayout(self.verticalLayout_8, 0, 0, 2, 1)

        self.groupBox_7 = QGroupBox(self.centralwidget)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMinimumSize(QSize(170, 0))
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.groupBox_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout_10.addWidget(self.label_9)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.passport_type_lineedit = QLineEdit(self.groupBox_7)
        self.passport_type_lineedit.setObjectName(u"passport_type_lineedit")
        self.passport_type_lineedit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.passport_type_lineedit, 0, 2, 1, 1)

        self.label_10 = QLabel(self.groupBox_7)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 0, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 3, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(154, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 3, 1, 1)

        self.passport_u_lineedit = QLineEdit(self.groupBox_7)
        self.passport_u_lineedit.setObjectName(u"passport_u_lineedit")
        self.passport_u_lineedit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.passport_u_lineedit, 2, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(170, 0))

        self.gridLayout_4.addWidget(self.label_14, 4, 1, 2, 1)

        self.label_13 = QLabel(self.groupBox_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(170, 0))

        self.gridLayout_4.addWidget(self.label_13, 3, 1, 1, 1)

        self.passport_phase_lineedit = QLineEdit(self.groupBox_7)
        self.passport_phase_lineedit.setObjectName(u"passport_phase_lineedit")
        self.passport_phase_lineedit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.passport_phase_lineedit, 3, 2, 2, 1)

        self.horizontalSpacer_4 = QSpacerItem(148, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 2, 3, 1, 1)

        self.label_11 = QLabel(self.groupBox_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(170, 0))

        self.gridLayout_4.addWidget(self.label_11, 1, 1, 1, 1)

        self.passport_p_lineedit = QLineEdit(self.groupBox_7)
        self.passport_p_lineedit.setObjectName(u"passport_p_lineedit")
        self.passport_p_lineedit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.passport_p_lineedit, 1, 2, 1, 1)

        self.label_12 = QLabel(self.groupBox_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(170, 0))

        self.gridLayout_4.addWidget(self.label_12, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 5, 3, 1, 1)

        self.passport_material_lineedit = QLineEdit(self.groupBox_7)
        self.passport_material_lineedit.setObjectName(u"passport_material_lineedit")
        self.passport_material_lineedit.setReadOnly(True)

        self.gridLayout_4.addWidget(self.passport_material_lineedit, 5, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_7, 2, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_9, 1, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_10, 3, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_11, 5, 0, 1, 1)


        self.verticalLayout_10.addLayout(self.gridLayout_4)


        self.gridLayout_5.addWidget(self.groupBox_7, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1366, 27))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SRK - \u043f\u043e\u0434\u0434\u0435\u0440\u0436\u043a\u0430 \u043f\u0440\u0438\u043d\u044f\u0442\u0438\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u0439 \u043f\u0440\u0438 \u043e\u0446\u0435\u043d\u043a\u0435 \u0441\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u044f \u0442\u0440\u0430\u043d\u0441\u0444\u043e\u0440\u043c\u0430\u0442\u043e\u0440\u043d\u043e\u0433\u043e \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.groupBox_6.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0435\u043d\u0438\u0435", None))
        self.groupBox_2.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u043a\u0430 \u0434\u0430\u043d\u043d\u044b\u0445", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0437\u043e\u0440", None))
        self.diapason_select_group.setTitle("")
        self.no_constr_radiobutton.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0437 \u043e\u0433\u0440\u0430\u043d\u0438\u0447\u0435\u043d\u0438\u0439", None))
        self.constr_radiobutton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0438\u0430\u043f\u0430\u0437\u043e\u043d", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0434\u0438\u0430\u043f\u0430\u0437\u043e\u043d\u0430:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0434\u043e", None))
        self.to_points_lineedit.setText(QCoreApplication.translate("MainWindow", u"90000", None))
        self.groupBox.setTitle("")
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0441\u043c\u043e\u0442\u0440 \u0442\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u043b\u044c\u043d\u044b\u0439 \u0442\u043e\u043a:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0410", None))
        self.groupBox_3.setTitle("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442\u044b \u0440\u0430\u0437\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"C3", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"C1", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"C2", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"A3", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"A2", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"A1", None))
        self.groupBox_4.setTitle("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0446\u0435\u043d\u043a\u0430 \u0440\u0430\u0437\u043b\u043e\u0436\u0435\u043d\u0438\u044f", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"MSE", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"MAE", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"MAPE", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"MdAE", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"R2 Score", None))
        self.groupBox_5.setTitle("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0438\u0442\u0435\u0440\u0438\u0439 \u043e\u0431\u043d\u0430\u0440\u0443\u0436\u0435\u043d\u0438\u044f \u0434\u0435\u0444\u0435\u043a\u0442\u0430", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0432\u043a\u0437", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0441\u0442", None))
        self.groupBox_7.setTitle("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0441\u043f\u043e\u0440\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0442\u0435\u0440\u0438\u0430\u043b \u043e\u0431\u043c\u043e\u0442\u043a\u0438", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0444\u0430\u0437", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0449\u043d\u043e\u0441\u0442\u044c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u043f\u0440\u044f\u0436\u0435\u043d\u0438\u0435 (U1/U2)", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430", None))
    # retranslateUi

