# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Menu.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QFrame, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_menu(object):
    def setupUi(self, menu):
        if not menu.objectName():
            menu.setObjectName(u"menu")
        menu.resize(281, 501)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(menu.sizePolicy().hasHeightForWidth())
        menu.setSizePolicy(sizePolicy)
        menu.setDocumentMode(True)
        menu.setDockNestingEnabled(False)
        self.simulationSpeedBlock = QWidget(menu)
        self.simulationSpeedBlock.setObjectName(u"simulationSpeedBlock")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.simulationSpeedBlock.sizePolicy().hasHeightForWidth())
        self.simulationSpeedBlock.setSizePolicy(sizePolicy1)
        self.trackmodelheaderLabel = QLabel(self.simulationSpeedBlock)
        self.trackmodelheaderLabel.setObjectName(u"trackmodelheaderLabel")
        self.trackmodelheaderLabel.setGeometry(QRect(110, 0, 181, 51))
        font = QFont()
        font.setPointSize(20)
        self.trackmodelheaderLabel.setFont(font)
        self.image = QLabel(self.simulationSpeedBlock)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(0, 0, 71, 51))
        self.image.setPixmap(QPixmap(u"API/AuroraLogo.jpg"))
        self.image.setScaledContents(True)
        self.yellow = QLabel(self.simulationSpeedBlock)
        self.yellow.setObjectName(u"yellow")
        self.yellow.setGeometry(QRect(0, 0, 281, 51))
        self.yellow.setFrameShape(QFrame.WinPanel)
        self.yellow.setPixmap(QPixmap(u"API/yellow.png"))
        self.yellow.setScaledContents(True)
        self.ctc_button = QPushButton(self.simulationSpeedBlock)
        self.ctc_button.setObjectName(u"ctc_button")
        self.ctc_button.setGeometry(QRect(10, 60, 261, 41))
        self.wayside_button = QPushButton(self.simulationSpeedBlock)
        self.wayside_button.setObjectName(u"wayside_button")
        self.wayside_button.setGeometry(QRect(10, 110, 261, 41))
        self.track_model_button = QPushButton(self.simulationSpeedBlock)
        self.track_model_button.setObjectName(u"track_model_button")
        self.track_model_button.setGeometry(QRect(10, 160, 261, 41))
        self.train_model_button = QPushButton(self.simulationSpeedBlock)
        self.train_model_button.setObjectName(u"train_model_button")
        self.train_model_button.setGeometry(QRect(10, 210, 261, 41))
        self.train_controller_button = QPushButton(self.simulationSpeedBlock)
        self.train_controller_button.setObjectName(u"train_controller_button")
        self.train_controller_button.setGeometry(QRect(10, 260, 261, 41))
        self.line = QFrame(self.simulationSpeedBlock)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(10, 300, 261, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.commandLinkButton = QCommandLinkButton(self.simulationSpeedBlock)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(10, 320, 261, 41))
        menu.setCentralWidget(self.simulationSpeedBlock)
        self.yellow.raise_()
        self.trackmodelheaderLabel.raise_()
        self.image.raise_()
        self.ctc_button.raise_()
        self.wayside_button.raise_()
        self.track_model_button.raise_()
        self.train_model_button.raise_()
        self.train_controller_button.raise_()
        self.line.raise_()
        self.commandLinkButton.raise_()
        self.menubar = QMenuBar(menu)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 281, 22))
        self.menubar.setDefaultUp(True)
        self.menuTraick_Model = QMenu(self.menubar)
        self.menuTraick_Model.setObjectName(u"menuTraick_Model")
        self.menuFault_List = QMenu(self.menubar)
        self.menuFault_List.setObjectName(u"menuFault_List")
        self.menuFault_List.setTearOffEnabled(False)
        self.menuFault_List.setSeparatorsCollapsible(True)
        self.menuTestBench = QMenu(self.menubar)
        self.menuTestBench.setObjectName(u"menuTestBench")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        menu.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(menu)
        self.statusbar.setObjectName(u"statusbar")
        menu.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTraick_Model.menuAction())
        self.menubar.addAction(self.menuFault_List.menuAction())
        self.menubar.addAction(self.menuTestBench.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(menu)

        QMetaObject.connectSlotsByName(menu)
    # setupUi

    def retranslateUi(self, menu):
        menu.setWindowTitle(QCoreApplication.translate("menu", u"Launcher", None))
        self.trackmodelheaderLabel.setText(QCoreApplication.translate("menu", u"Launcher", None))
        self.image.setText("")
        self.yellow.setText("")
        self.ctc_button.setText(QCoreApplication.translate("menu", u"CTC", None))
        self.wayside_button.setText(QCoreApplication.translate("menu", u"Wayside Controller", None))
        self.track_model_button.setText(QCoreApplication.translate("menu", u"Track Model", None))
        self.train_model_button.setText(QCoreApplication.translate("menu", u"Train Model", None))
        self.train_controller_button.setText(QCoreApplication.translate("menu", u"Train Controller", None))
        self.commandLinkButton.setText(QCoreApplication.translate("menu", u"Start System", None))
        self.menuTraick_Model.setTitle(QCoreApplication.translate("menu", u"File", None))
        self.menuFault_List.setTitle(QCoreApplication.translate("menu", u"Edit", None))
        self.menuTestBench.setTitle(QCoreApplication.translate("menu", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("menu", u"Help", None))
    # retranslateUi

