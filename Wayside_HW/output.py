# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'waysideHardwareTest.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCommandLinkButton,
    QFrame, QGroupBox, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1400, 781)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(920, 10, 160, 51))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalSlider = QSlider(self.verticalLayoutWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(5)
        sizePolicy1.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy1)
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(24)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(8)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(4)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 10, 301, 51))
        self.yellow = QLabel(self.centralwidget)
        self.yellow.setObjectName(u"yellow")
        self.yellow.setGeometry(QRect(10, 10, 1361, 51))
        self.yellow.setFrameShape(QFrame.WinPanel)
        self.yellow.setPixmap(QPixmap(u"../../../../../../../Downloads/images/yellow.png"))
        self.yellow.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(1100, 10, 131, 51))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 55, 50))
        self.label.setPixmap(QPixmap(u"../../../../../.designer/backup/AuroraLogo.jpg"))
        self.label.setScaledContents(True)
        self.node_select = QComboBox(self.centralwidget)
        self.node_select.setObjectName(u"node_select")
        self.node_select.setGeometry(QRect(660, 20, 231, 31))
        self.checkBox = QCheckBox(self.centralwidget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(1240, 10, 91, 51))
        self.checkBox.setAutoRepeatDelay(298)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-90, 10, 1511, 50))
        self.label_2.setPixmap(QPixmap(u"../../../../../.designer/backup/img/yellow.png"))
        self.label_2.setScaledContents(True)
        self.tb_disp_go = QCommandLinkButton(self.centralwidget)
        self.tb_disp_go.setObjectName(u"tb_disp_go")
        self.tb_disp_go.setGeometry(QRect(450, 310, 181, 41))
        self.ManualLineInput_5 = QComboBox(self.centralwidget)
        self.ManualLineInput_5.setObjectName(u"ManualLineInput_5")
        self.ManualLineInput_5.setGeometry(QRect(25, 129, 340, 22))
        self.ManualLineInput_5.setEditable(True)
        self.ManualLineInput_5.setInsertPolicy(QComboBox.NoInsert)
        self.ManualLineInput_5.setPlaceholderText(u"Select Line")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(725, 149, 211, 16))
        self.dispatch_label = QLabel(self.centralwidget)
        self.dispatch_label.setObjectName(u"dispatch_label")
        self.dispatch_label.setGeometry(QRect(725, 129, 251, 16))
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 190, 341, 421))
        self.tb_occ = QCheckBox(self.groupBox)
        self.tb_occ.setObjectName(u"tb_occ")
        self.tb_occ.setGeometry(QRect(30, 30, 111, 20))
        self.tb_fault = QPushButton(self.groupBox)
        self.tb_fault.setObjectName(u"tb_fault")
        self.tb_fault.setGeometry(QRect(20, 60, 181, 28))
        self.tb_dis = QCheckBox(self.centralwidget)
        self.tb_dis.setObjectName(u"tb_dis")
        self.tb_dis.setGeometry(QRect(45, 149, 111, 20))
        self.tb_disp_to = QComboBox(self.centralwidget)
        self.tb_disp_to.setObjectName(u"tb_disp_to")
        self.tb_disp_to.setGeometry(QRect(450, 250, 160, 22))
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tb_disp_to.sizePolicy().hasHeightForWidth())
        self.tb_disp_to.setSizePolicy(sizePolicy2)
        self.tb_disp_to.setEditable(True)
        self.tb_disp_to.setInsertPolicy(QComboBox.NoInsert)
        self.tb_disp_to.setPlaceholderText(u"Select Line")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(480, 290, 91, 16))
        self.block_table_4 = QTableWidget(self.centralwidget)
        if (self.block_table_4.columnCount() < 4):
            self.block_table_4.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.block_table_4.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.block_table_4.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.block_table_4.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.block_table_4.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.block_table_4.setObjectName(u"block_table_4")
        self.block_table_4.setGeometry(QRect(725, 189, 409, 661))
        self.tb_disp_from = QComboBox(self.centralwidget)
        self.tb_disp_from.setObjectName(u"tb_disp_from")
        self.tb_disp_from.setGeometry(QRect(450, 190, 165, 22))
        sizePolicy2.setHeightForWidth(self.tb_disp_from.sizePolicy().hasHeightForWidth())
        self.tb_disp_from.setSizePolicy(sizePolicy2)
        self.tb_disp_from.setEditable(True)
        self.tb_disp_from.setInsertPolicy(QComboBox.NoInsert)
        self.tb_disp_from.setPlaceholderText(u"Select Line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1400, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Simulation speed</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Wayside Controller</span></p></body></html>", None))
        self.yellow.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Simulation time\n"
"MM/DD/YYYY hh:mm:ss", None))
        self.label.setText("")
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Manual Mode", None))
        self.label_2.setText("")
        self.tb_disp_go.setText(QCoreApplication.translate("MainWindow", u"Dispatch", None))
        self.ManualLineInput_5.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Block", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Switch state: [] to []", None))
        self.dispatch_label.setText(QCoreApplication.translate("MainWindow", u"Dispatched train from [] to []", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Track Model Inputs", None))
        self.tb_occ.setText(QCoreApplication.translate("MainWindow", u"Occupy Block", None))
        self.tb_fault.setText(QCoreApplication.translate("MainWindow", u"Trigger Fault in Block", None))
        self.tb_dis.setText(QCoreApplication.translate("MainWindow", u"Disable Block", None))
        self.tb_disp_to.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Block", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Dispatch train", None))
        ___qtablewidgetitem = self.block_table_4.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Block ID", None));
        ___qtablewidgetitem1 = self.block_table_4.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem2 = self.block_table_4.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem3 = self.block_table_4.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None));
        self.tb_disp_from.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Block", None))
    # retranslateUi

