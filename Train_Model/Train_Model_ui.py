# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Train_Model_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_TrainModel(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(992, 598)
        self.actionTrain_Model_Information = QAction(MainWindow)
        self.actionTrain_Model_Information.setObjectName(u"actionTrain_Model_Information")
        self.actionTestbench = QAction(MainWindow)
        self.actionTestbench.setObjectName(u"actionTestbench")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.centralwidget)
        self.header_widget.setObjectName(u"header_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_widget.sizePolicy().hasHeightForWidth())
        self.header_widget.setSizePolicy(sizePolicy)
        self.header_widget.setMinimumSize(QSize(0, 50))
        self.header_layout = QHBoxLayout(self.header_widget)
        self.header_layout.setObjectName(u"header_layout")
        self.AuroraIMG = QLabel(self.header_widget)
        self.AuroraIMG.setObjectName(u"AuroraIMG")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AuroraIMG.sizePolicy().hasHeightForWidth())
        self.AuroraIMG.setSizePolicy(sizePolicy1)
        self.AuroraIMG.setMinimumSize(QSize(40, 40))
        self.AuroraIMG.setMaximumSize(QSize(70, 40))
        self.AuroraIMG.setPixmap(QPixmap(u"images/AuroraLogo.png"))
        self.AuroraIMG.setScaledContents(True)

        self.header_layout.addWidget(self.AuroraIMG)

        self.LogoBrower = QTextBrowser(self.header_widget)
        self.LogoBrower.setObjectName(u"LogoBrower")
        sizePolicy1.setHeightForWidth(self.LogoBrower.sizePolicy().hasHeightForWidth())
        self.LogoBrower.setSizePolicy(sizePolicy1)
        self.LogoBrower.setMinimumSize(QSize(100, 40))
        self.LogoBrower.setMaximumSize(QSize(16777215, 40))
        self.LogoBrower.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.header_layout.addWidget(self.LogoBrower, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.redButton = QPushButton(self.header_widget)
        self.redButton.setObjectName(u"redButton")

        self.gridLayout.addWidget(self.redButton, 0, 1, 1, 1)

        self.TrainIdIn = QLineEdit(self.header_widget)
        self.TrainIdIn.setObjectName(u"TrainIdIn")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.TrainIdIn.sizePolicy().hasHeightForWidth())
        self.TrainIdIn.setSizePolicy(sizePolicy2)
        self.TrainIdIn.setMinimumSize(QSize(100, 0))
        self.TrainIdIn.setMaximumSize(QSize(50, 16777215))

        self.gridLayout.addWidget(self.TrainIdIn, 0, 2, 1, 1)

        self.greenButton = QPushButton(self.header_widget)
        self.greenButton.setObjectName(u"greenButton")

        self.gridLayout.addWidget(self.greenButton, 0, 0, 1, 1)


        self.header_layout.addLayout(self.gridLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.header_layout.addItem(self.horizontalSpacer)

        self.time_control = QHBoxLayout()
        self.time_control.setObjectName(u"time_control")
        self.simulation_speed_txt = QLabel(self.header_widget)
        self.simulation_speed_txt.setObjectName(u"simulation_speed_txt")

        self.time_control.addWidget(self.simulation_speed_txt)

        self.simSlider = QSlider(self.header_widget)
        self.simSlider.setObjectName(u"simSlider")
        self.simSlider.setMinimumSize(QSize(50, 0))
        self.simSlider.setMinimum(1)
        self.simSlider.setMaximum(10)
        self.simSlider.setPageStep(1)
        self.simSlider.setTracking(False)
        self.simSlider.setOrientation(Qt.Horizontal)
        self.simSlider.setTickPosition(QSlider.TicksBelow)
        self.simSlider.setTickInterval(1)

        self.time_control.addWidget(self.simSlider)

        self.pauseSim = QPushButton(self.header_widget)
        self.pauseSim.setObjectName(u"pauseSim")
        self.pauseSim.setMaximumSize(QSize(75, 16777215))

        self.time_control.addWidget(self.pauseSim)

        self.timeLabel = QLabel(self.header_widget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setMinimumSize(QSize(120, 0))
        self.timeLabel.setMaximumSize(QSize(120, 16777215))

        self.time_control.addWidget(self.timeLabel)


        self.header_layout.addLayout(self.time_control)


        self.gridLayout_2.addWidget(self.header_widget, 0, 0, 1, 1)

        self.TrainModelInformation = QTabWidget(self.centralwidget)
        self.TrainModelInformation.setObjectName(u"TrainModelInformation")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.TrainModelInformation.sizePolicy().hasHeightForWidth())
        self.TrainModelInformation.setSizePolicy(sizePolicy3)
        font = QFont()
        font.setPointSize(9)
        self.TrainModelInformation.setFont(font)
        self.Train_Model_Information = QWidget()
        self.Train_Model_Information.setObjectName(u"Train_Model_Information")
        self.gridLayout_8 = QGridLayout(self.Train_Model_Information)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetNoConstraint)
        self.train_left_layout = QGridLayout()
        self.train_left_layout.setObjectName(u"train_left_layout")
        self.train_left_layout.setVerticalSpacing(0)
        self.PhysicalData = QTableWidget(self.Train_Model_Information)
        if (self.PhysicalData.columnCount() < 1):
            self.PhysicalData.setColumnCount(1)
        __qtablewidgetitem = QTableWidgetItem()
        self.PhysicalData.setHorizontalHeaderItem(0, __qtablewidgetitem)
        if (self.PhysicalData.rowCount() < 9):
            self.PhysicalData.setRowCount(9)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(6, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(7, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.PhysicalData.setVerticalHeaderItem(8, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.PhysicalData.setItem(0, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.PhysicalData.setItem(1, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.PhysicalData.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.PhysicalData.setItem(3, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.PhysicalData.setItem(4, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.PhysicalData.setItem(5, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.PhysicalData.setItem(6, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.PhysicalData.setItem(7, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.PhysicalData.setItem(8, 0, __qtablewidgetitem18)
        self.PhysicalData.setObjectName(u"PhysicalData")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.PhysicalData.sizePolicy().hasHeightForWidth())
        self.PhysicalData.setSizePolicy(sizePolicy4)
        self.PhysicalData.setMinimumSize(QSize(250, 280))
        self.PhysicalData.setMaximumSize(QSize(250, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.PhysicalData.setFont(font1)
        self.PhysicalData.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.PhysicalData.setColumnCount(1)
        self.PhysicalData.horizontalHeader().setVisible(False)
        self.PhysicalData.horizontalHeader().setCascadingSectionResizes(True)
        self.PhysicalData.horizontalHeader().setMinimumSectionSize(55)
        self.PhysicalData.horizontalHeader().setDefaultSectionSize(100)
        self.PhysicalData.horizontalHeader().setStretchLastSection(True)
        self.PhysicalData.verticalHeader().setVisible(True)
        self.PhysicalData.verticalHeader().setCascadingSectionResizes(True)

        self.train_left_layout.addWidget(self.PhysicalData, 0, 0, 1, 1)

        self.DoorState = QTableWidget(self.Train_Model_Information)
        if (self.DoorState.columnCount() < 1):
            self.DoorState.setColumnCount(1)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.DoorState.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        if (self.DoorState.rowCount() < 2):
            self.DoorState.setRowCount(2)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.DoorState.setVerticalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.DoorState.setVerticalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.DoorState.setItem(0, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.DoorState.setItem(1, 0, __qtablewidgetitem23)
        self.DoorState.setObjectName(u"DoorState")
        sizePolicy1.setHeightForWidth(self.DoorState.sizePolicy().hasHeightForWidth())
        self.DoorState.setSizePolicy(sizePolicy1)
        self.DoorState.setMinimumSize(QSize(160, 90))
        self.DoorState.setMaximumSize(QSize(160, 90))
        self.DoorState.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.train_left_layout.addWidget(self.DoorState, 2, 0, 1, 1, Qt.AlignHCenter)

        self.LightsState = QTableWidget(self.Train_Model_Information)
        if (self.LightsState.columnCount() < 1):
            self.LightsState.setColumnCount(1)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.LightsState.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        if (self.LightsState.rowCount() < 2):
            self.LightsState.setRowCount(2)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.LightsState.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.LightsState.setVerticalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.LightsState.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.LightsState.setItem(1, 0, __qtablewidgetitem28)
        self.LightsState.setObjectName(u"LightsState")
        sizePolicy1.setHeightForWidth(self.LightsState.sizePolicy().hasHeightForWidth())
        self.LightsState.setSizePolicy(sizePolicy1)
        self.LightsState.setMinimumSize(QSize(160, 90))
        self.LightsState.setMaximumSize(QSize(160, 90))
        self.LightsState.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.train_left_layout.addWidget(self.LightsState, 5, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_left_layout.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.train_left_layout.addItem(self.verticalSpacer_5, 3, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.train_left_layout)

        self.mid_layout = QGridLayout()
        self.mid_layout.setObjectName(u"mid_layout")
        self.mid_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.EmergencyButton = QPushButton(self.Train_Model_Information)
        self.EmergencyButton.setObjectName(u"EmergencyButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.EmergencyButton.sizePolicy().hasHeightForWidth())
        self.EmergencyButton.setSizePolicy(sizePolicy5)
        self.EmergencyButton.setMinimumSize(QSize(400, 125))
        self.EmergencyButton.setMaximumSize(QSize(500, 125))
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        self.EmergencyButton.setFont(font2)

        self.mid_layout.addWidget(self.EmergencyButton, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mid_layout.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.train_info_layout = QHBoxLayout()
        self.train_info_layout.setObjectName(u"train_info_layout")
        self.TrainLine = QLabel(self.Train_Model_Information)
        self.TrainLine.setObjectName(u"TrainLine")

        self.train_info_layout.addWidget(self.TrainLine)

        self.TrainID = QLabel(self.Train_Model_Information)
        self.TrainID.setObjectName(u"TrainID")

        self.train_info_layout.addWidget(self.TrainID)


        self.mid_layout.addLayout(self.train_info_layout, 0, 0, 1, 1)

        self.Advertisment = QLabel(self.Train_Model_Information)
        self.Advertisment.setObjectName(u"Advertisment")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.Advertisment.sizePolicy().hasHeightForWidth())
        self.Advertisment.setSizePolicy(sizePolicy6)
        self.Advertisment.setMinimumSize(QSize(100, 200))
        self.Advertisment.setMaximumSize(QSize(300, 400))
        self.Advertisment.setPixmap(QPixmap(u"images/Ad_3.png"))
        self.Advertisment.setScaledContents(True)

        self.mid_layout.addWidget(self.Advertisment, 1, 0, 1, 1, Qt.AlignHCenter|Qt.AlignVCenter)

        self.BrakeState = QTableWidget(self.Train_Model_Information)
        if (self.BrakeState.columnCount() < 1):
            self.BrakeState.setColumnCount(1)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.BrakeState.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        if (self.BrakeState.rowCount() < 2):
            self.BrakeState.setRowCount(2)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.BrakeState.setVerticalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.BrakeState.setVerticalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.BrakeState.setItem(0, 0, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.BrakeState.setItem(1, 0, __qtablewidgetitem33)
        self.BrakeState.setObjectName(u"BrakeState")
        sizePolicy1.setHeightForWidth(self.BrakeState.sizePolicy().hasHeightForWidth())
        self.BrakeState.setSizePolicy(sizePolicy1)
        self.BrakeState.setMinimumSize(QSize(200, 95))
        self.BrakeState.setMaximumSize(QSize(200, 95))
        self.BrakeState.setFont(font)
        self.BrakeState.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.mid_layout.addWidget(self.BrakeState, 3, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mid_layout.addItem(self.verticalSpacer_6, 4, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mid_layout.addItem(self.verticalSpacer_7, 2, 0, 1, 1)


        self.horizontalLayout_2.addLayout(self.mid_layout)

        self.groupBox_3 = QGroupBox(self.Train_Model_Information)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy7)
        self.groupBox_3.setMinimumSize(QSize(300, 0))
        self.verticalLayoutWidget_5 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(10, 0, 302, 1105))
        self.verticalLayout_7 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Announcements = QLabel(self.verticalLayoutWidget_5)
        self.Announcements.setObjectName(u"Announcements")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.Announcements.sizePolicy().hasHeightForWidth())
        self.Announcements.setSizePolicy(sizePolicy8)
        self.Announcements.setMinimumSize(QSize(300, 40))
        self.Announcements.setMaximumSize(QSize(400, 50))
        self.Announcements.setFont(font)

        self.verticalLayout_7.addWidget(self.Announcements)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.murphyOutputsBlockTB_2 = QVBoxLayout()
        self.murphyOutputsBlockTB_2.setObjectName(u"murphyOutputsBlockTB_2")
        self.TestTrainEngine = QPushButton(self.verticalLayoutWidget_5)
        self.TestTrainEngine.setObjectName(u"TestTrainEngine")

        self.murphyOutputsBlockTB_2.addWidget(self.TestTrainEngine)

        self.TestBrake = QPushButton(self.verticalLayoutWidget_5)
        self.TestBrake.setObjectName(u"TestBrake")

        self.murphyOutputsBlockTB_2.addWidget(self.TestBrake)

        self.TestSignalPickup = QPushButton(self.verticalLayoutWidget_5)
        self.TestSignalPickup.setObjectName(u"TestSignalPickup")

        self.murphyOutputsBlockTB_2.addWidget(self.TestSignalPickup)


        self.gridLayout_5.addLayout(self.murphyOutputsBlockTB_2, 0, 1, 1, 1)

        self.murphylabelsBlock = QVBoxLayout()
        self.murphylabelsBlock.setObjectName(u"murphylabelsBlock")
        self.TrainEngineFailureLabel = QLabel(self.verticalLayoutWidget_5)
        self.TrainEngineFailureLabel.setObjectName(u"TrainEngineFailureLabel")

        self.murphylabelsBlock.addWidget(self.TrainEngineFailureLabel)

        self.SignalPickupFailureLabel = QLabel(self.verticalLayoutWidget_5)
        self.SignalPickupFailureLabel.setObjectName(u"SignalPickupFailureLabel")

        self.murphylabelsBlock.addWidget(self.SignalPickupFailureLabel)

        self.BrakeFailureLabel = QLabel(self.verticalLayoutWidget_5)
        self.BrakeFailureLabel.setObjectName(u"BrakeFailureLabel")

        self.murphylabelsBlock.addWidget(self.BrakeFailureLabel)


        self.gridLayout_5.addLayout(self.murphylabelsBlock, 0, 0, 1, 1)


        self.verticalLayout_7.addLayout(self.gridLayout_5)

        self.resetButton = QPushButton(self.verticalLayoutWidget_5)
        self.resetButton.setObjectName(u"resetButton")
        sizePolicy2.setHeightForWidth(self.resetButton.sizePolicy().hasHeightForWidth())
        self.resetButton.setSizePolicy(sizePolicy2)
        self.resetButton.setMinimumSize(QSize(200, 0))

        self.verticalLayout_7.addWidget(self.resetButton)

        self.FailureModes = QTableWidget(self.verticalLayoutWidget_5)
        if (self.FailureModes.columnCount() < 1):
            self.FailureModes.setColumnCount(1)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.FailureModes.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        if (self.FailureModes.rowCount() < 3):
            self.FailureModes.setRowCount(3)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.FailureModes.setVerticalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.FailureModes.setVerticalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.FailureModes.setVerticalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.FailureModes.setItem(0, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.FailureModes.setItem(1, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.FailureModes.setItem(2, 0, __qtablewidgetitem40)
        self.FailureModes.setObjectName(u"FailureModes")
        sizePolicy4.setHeightForWidth(self.FailureModes.sizePolicy().hasHeightForWidth())
        self.FailureModes.setSizePolicy(sizePolicy4)
        self.FailureModes.setMinimumSize(QSize(200, 120))
        self.FailureModes.setMaximumSize(QSize(200, 120))
        self.FailureModes.setFont(font)
        self.FailureModes.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.verticalLayout_7.addWidget(self.FailureModes, 0, Qt.AlignHCenter)

        self.TrainSize = QTableWidget(self.verticalLayoutWidget_5)
        if (self.TrainSize.columnCount() < 1):
            self.TrainSize.setColumnCount(1)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.TrainSize.setHorizontalHeaderItem(0, __qtablewidgetitem41)
        if (self.TrainSize.rowCount() < 7):
            self.TrainSize.setRowCount(7)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.TrainSize.setVerticalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.TrainSize.setVerticalHeaderItem(1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.TrainSize.setVerticalHeaderItem(2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.TrainSize.setVerticalHeaderItem(3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.TrainSize.setVerticalHeaderItem(4, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.TrainSize.setVerticalHeaderItem(5, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.TrainSize.setVerticalHeaderItem(6, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.TrainSize.setItem(0, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.TrainSize.setItem(1, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.TrainSize.setItem(2, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.TrainSize.setItem(3, 0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.TrainSize.setItem(4, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.TrainSize.setItem(5, 0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.TrainSize.setItem(6, 0, __qtablewidgetitem55)
        self.TrainSize.setObjectName(u"TrainSize")
        sizePolicy8.setHeightForWidth(self.TrainSize.sizePolicy().hasHeightForWidth())
        self.TrainSize.setSizePolicy(sizePolicy8)
        self.TrainSize.setMinimumSize(QSize(200, 225))
        self.TrainSize.setMaximumSize(QSize(200, 225))
        self.TrainSize.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.TrainSize.horizontalHeader().setVisible(False)
        self.TrainSize.horizontalHeader().setMinimumSectionSize(1)
        self.TrainSize.horizontalHeader().setDefaultSectionSize(175)

        self.verticalLayout_7.addWidget(self.TrainSize, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_2.addWidget(self.groupBox_3)


        self.gridLayout_8.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.TrainModelInformation.addTab(self.Train_Model_Information, "")

        self.gridLayout_2.addWidget(self.TrainModelInformation, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.actionTestbench.triggered.connect(self.TrainModelInformation.setFocus)
        self.actionTrain_Model_Information.triggered.connect(self.TrainModelInformation.setFocus)

        self.TrainModelInformation.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionTrain_Model_Information.setText(QCoreApplication.translate("MainWindow", u"Train Model Information", None))
        self.actionTestbench.setText(QCoreApplication.translate("MainWindow", u"Testbench", None))
        self.AuroraIMG.setText("")
        self.LogoBrower.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">Train Model</span></p></body></html>", None))
        self.redButton.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.greenButton.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.simulation_speed_txt.setText(QCoreApplication.translate("MainWindow", u"Simulation Speed", None))
        self.pauseSim.setText(QCoreApplication.translate("MainWindow", u"Pause Sim", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"00/00/0000 00:00", None))
        ___qtablewidgetitem = self.PhysicalData.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Train Data", None));
        ___qtablewidgetitem1 = self.PhysicalData.verticalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Power", None));
        ___qtablewidgetitem2 = self.PhysicalData.verticalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Current Speed", None));
        ___qtablewidgetitem3 = self.PhysicalData.verticalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Commanded Speed", None));
        ___qtablewidgetitem4 = self.PhysicalData.verticalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Speed Limit", None));
        ___qtablewidgetitem5 = self.PhysicalData.verticalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Acceleration", None));
        ___qtablewidgetitem6 = self.PhysicalData.verticalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Force", None));
        ___qtablewidgetitem7 = self.PhysicalData.verticalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Block Grade", None));
        ___qtablewidgetitem8 = self.PhysicalData.verticalHeaderItem(7)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Authority", None));
        ___qtablewidgetitem9 = self.PhysicalData.verticalHeaderItem(8)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None));

        __sortingEnabled = self.PhysicalData.isSortingEnabled()
        self.PhysicalData.setSortingEnabled(False)
        ___qtablewidgetitem10 = self.PhysicalData.item(0, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"60 W", None));
        ___qtablewidgetitem11 = self.PhysicalData.item(1, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"0 mph", None));
        ___qtablewidgetitem12 = self.PhysicalData.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"30 mph", None));
        ___qtablewidgetitem13 = self.PhysicalData.item(3, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"43 mph", None));
        ___qtablewidgetitem14 = self.PhysicalData.item(4, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"0.5 ft/s^2", None));
        ___qtablewidgetitem15 = self.PhysicalData.item(5, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"45136 lb", None));
        ___qtablewidgetitem16 = self.PhysicalData.item(6, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"0.5%", None));
        ___qtablewidgetitem17 = self.PhysicalData.item(7, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"0 ft", None));
        ___qtablewidgetitem18 = self.PhysicalData.item(8, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"0 mph", None));
        self.PhysicalData.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem19 = self.DoorState.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Door State", None));
        ___qtablewidgetitem20 = self.DoorState.verticalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Right", None));
        ___qtablewidgetitem21 = self.DoorState.verticalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Left", None));

        __sortingEnabled1 = self.DoorState.isSortingEnabled()
        self.DoorState.setSortingEnabled(False)
        ___qtablewidgetitem22 = self.DoorState.item(0, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Open", None));
        ___qtablewidgetitem23 = self.DoorState.item(1, 0)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Closed", None));
        self.DoorState.setSortingEnabled(__sortingEnabled1)

        ___qtablewidgetitem24 = self.LightsState.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Lights State", None));
        ___qtablewidgetitem25 = self.LightsState.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Internal", None));
        ___qtablewidgetitem26 = self.LightsState.verticalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"External", None));

        __sortingEnabled2 = self.LightsState.isSortingEnabled()
        self.LightsState.setSortingEnabled(False)
        ___qtablewidgetitem27 = self.LightsState.item(0, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"On", None));
        ___qtablewidgetitem28 = self.LightsState.item(1, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Off", None));
        self.LightsState.setSortingEnabled(__sortingEnabled2)

        self.EmergencyButton.setText(QCoreApplication.translate("MainWindow", u"Emergency Brake", None))
        self.TrainLine.setText(QCoreApplication.translate("MainWindow", u"Train Line: ", None))
        self.TrainID.setText(QCoreApplication.translate("MainWindow", u"Train ID: ", None))
        self.Advertisment.setText("")
        ___qtablewidgetitem29 = self.BrakeState.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Brake State", None));
        ___qtablewidgetitem30 = self.BrakeState.verticalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Emergency", None));
        ___qtablewidgetitem31 = self.BrakeState.verticalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Service", None));

        __sortingEnabled3 = self.BrakeState.isSortingEnabled()
        self.BrakeState.setSortingEnabled(False)
        ___qtablewidgetitem32 = self.BrakeState.item(0, 0)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Disengaged", None));
        ___qtablewidgetitem33 = self.BrakeState.item(1, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Disengaged", None));
        self.BrakeState.setSortingEnabled(__sortingEnabled3)

        self.groupBox_3.setTitle("")
        self.Announcements.setText(QCoreApplication.translate("MainWindow", u"Announcements: ", None))
        self.TestTrainEngine.setText(QCoreApplication.translate("MainWindow", u"Trigger Fault", None))
        self.TestBrake.setText(QCoreApplication.translate("MainWindow", u"Trigger Fault", None))
        self.TestSignalPickup.setText(QCoreApplication.translate("MainWindow", u"Trigger Fault", None))
        self.TrainEngineFailureLabel.setText(QCoreApplication.translate("MainWindow", u"Train Engine Failure", None))
        self.SignalPickupFailureLabel.setText(QCoreApplication.translate("MainWindow", u"Brake Failure", None))
        self.BrakeFailureLabel.setText(QCoreApplication.translate("MainWindow", u"Signal Pickup Failure", None))
        self.resetButton.setText(QCoreApplication.translate("MainWindow", u"Reset Faults", None))
        ___qtablewidgetitem34 = self.FailureModes.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Failure Modes", None));
        ___qtablewidgetitem35 = self.FailureModes.verticalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Train Engine ", None));
        ___qtablewidgetitem36 = self.FailureModes.verticalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Train Brake ", None));
        ___qtablewidgetitem37 = self.FailureModes.verticalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Signal Pickup ", None));

        __sortingEnabled4 = self.FailureModes.isSortingEnabled()
        self.FailureModes.setSortingEnabled(False)
        ___qtablewidgetitem38 = self.FailureModes.item(0, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Functioning", None));
        ___qtablewidgetitem39 = self.FailureModes.item(1, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Functioning", None));
        ___qtablewidgetitem40 = self.FailureModes.item(2, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Functioning", None));
        self.FailureModes.setSortingEnabled(__sortingEnabled4)

        ___qtablewidgetitem41 = self.TrainSize.horizontalHeaderItem(0)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Train Information", None));
        ___qtablewidgetitem42 = self.TrainSize.verticalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Crew Count", None));
        ___qtablewidgetitem43 = self.TrainSize.verticalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Passenger Count", None));
        ___qtablewidgetitem44 = self.TrainSize.verticalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Temperature", None));
        ___qtablewidgetitem45 = self.TrainSize.verticalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Weight", None));
        ___qtablewidgetitem46 = self.TrainSize.verticalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Length", None));
        ___qtablewidgetitem47 = self.TrainSize.verticalHeaderItem(5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Width", None));
        ___qtablewidgetitem48 = self.TrainSize.verticalHeaderItem(6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Height", None));

        __sortingEnabled5 = self.TrainSize.isSortingEnabled()
        self.TrainSize.setSortingEnabled(False)
        ___qtablewidgetitem49 = self.TrainSize.item(0, 0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem50 = self.TrainSize.item(1, 0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"120", None));
        ___qtablewidgetitem51 = self.TrainSize.item(2, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"75 \u00b0F", None));
        ___qtablewidgetitem52 = self.TrainSize.item(3, 0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"90272 lb", None));
        ___qtablewidgetitem53 = self.TrainSize.item(4, 0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"105.64 ft", None));
        ___qtablewidgetitem54 = self.TrainSize.item(5, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"8.69 ft", None));
        ___qtablewidgetitem55 = self.TrainSize.item(6, 0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"11.22 ft", None));
        self.TrainSize.setSortingEnabled(__sortingEnabled5)

        self.TrainModelInformation.setTabText(self.TrainModelInformation.indexOf(self.Train_Model_Information), QCoreApplication.translate("MainWindow", u"Train Model Information", None))
    # retranslateUi

