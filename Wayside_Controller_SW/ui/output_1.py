# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wayside_controller.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1265, 810)
        self.actionSwitch_Control = QAction(MainWindow)
        self.actionSwitch_Control.setObjectName(u"actionSwitch_Control")
        self.actionSignal_Control = QAction(MainWindow)
        self.actionSignal_Control.setObjectName(u"actionSignal_Control")
        self.actionCrossing_Control = QAction(MainWindow)
        self.actionCrossing_Control.setObjectName(u"actionCrossing_Control")
        self.actionTestbench = QAction(MainWindow)
        self.actionTestbench.setObjectName(u"actionTestbench")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QSize(0, 2))
        self.tab_1 = QWidget()
        self.tab_1.setObjectName(u"tab_1")
        self.gridLayout_4 = QGridLayout(self.tab_1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.switch_table = QTableWidget(self.tab_1)
        if (self.switch_table.columnCount() < 4):
            self.switch_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.switch_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.switch_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.switch_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.switch_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.switch_table.setObjectName(u"switch_table")
        self.switch_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.switch_table.setColumnCount(4)
        self.switch_table.horizontalHeader().setStretchLastSection(True)
        self.switch_table.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.switch_table)

        self.label_10 = QLabel(self.tab_1)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_2.addWidget(self.label_10)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.PLC_label = QLabel(self.tab_1)
        self.PLC_label.setObjectName(u"PLC_label")

        self.horizontalLayout_2.addWidget(self.PLC_label)

        self.PLC_download = QPushButton(self.tab_1)
        self.PLC_download.setObjectName(u"PLC_download")

        self.horizontalLayout_2.addWidget(self.PLC_download)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.PLC_upload = QPushButton(self.tab_1)
        self.PLC_upload.setObjectName(u"PLC_upload")

        self.verticalLayout_2.addWidget(self.PLC_upload)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.switch_label = QLabel(self.tab_1)
        self.switch_label.setObjectName(u"switch_label")

        self.verticalLayout_4.addWidget(self.switch_label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.state1_block_label = QLabel(self.tab_1)
        self.state1_block_label.setObjectName(u"state1_block_label")

        self.horizontalLayout_4.addWidget(self.state1_block_label)

        self.state2_block_label = QLabel(self.tab_1)
        self.state2_block_label.setObjectName(u"state2_block_label")

        self.horizontalLayout_4.addWidget(self.state2_block_label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.switch_graphic = QLabel(self.tab_1)
        self.switch_graphic.setObjectName(u"switch_graphic")
        self.switch_graphic.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.switch_graphic.sizePolicy().hasHeightForWidth())
        self.switch_graphic.setSizePolicy(sizePolicy1)
        self.switch_graphic.setMaximumSize(QSize(300, 300))
        self.switch_graphic.setPixmap(QPixmap(u"../../../.designer/backup/img/Track Ctl Graphics state1.png"))
        self.switch_graphic.setScaledContents(True)
        self.switch_graphic.setIndent(-5)

        self.verticalLayout_4.addWidget(self.switch_graphic)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.owner_block_label = QLabel(self.tab_1)
        self.owner_block_label.setObjectName(u"owner_block_label")

        self.horizontalLayout_5.addWidget(self.owner_block_label)

        self.switch_toggle = QPushButton(self.tab_1)
        self.switch_toggle.setObjectName(u"switch_toggle")

        self.horizontalLayout_5.addWidget(self.switch_toggle)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.block_table_1 = QTableWidget(self.tab_1)
        if (self.block_table_1.columnCount() < 4):
            self.block_table_1.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.block_table_1.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.block_table_1.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.block_table_1.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.block_table_1.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.block_table_1.setObjectName(u"block_table_1")
        self.block_table_1.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.block_table_1.verticalHeader().setVisible(False)

        self.gridLayout_3.addWidget(self.block_table_1, 0, 2, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.signal_table = QTableWidget(self.tab_2)
        if (self.signal_table.columnCount() < 2):
            self.signal_table.setColumnCount(2)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.signal_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.signal_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        self.signal_table.setObjectName(u"signal_table")
        self.signal_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.signal_table.setColumnCount(2)
        self.signal_table.horizontalHeader().setStretchLastSection(True)
        self.signal_table.verticalHeader().setVisible(False)
        self.signal_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.signal_table)


        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.signal_label = QLabel(self.tab_2)
        self.signal_label.setObjectName(u"signal_label")

        self.verticalLayout_5.addWidget(self.signal_label)

        self.signal_graphic = QLabel(self.tab_2)
        self.signal_graphic.setObjectName(u"signal_graphic")
        self.signal_graphic.setMaximumSize(QSize(200, 300))
        self.signal_graphic.setPixmap(QPixmap(u"../../../.designer/backup/img/Track Ctl Graphics red.png"))
        self.signal_graphic.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.signal_graphic)

        self.signal_toggle = QPushButton(self.tab_2)
        self.signal_toggle.setObjectName(u"signal_toggle")

        self.verticalLayout_5.addWidget(self.signal_toggle)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.block_table_2 = QTableWidget(self.tab_2)
        if (self.block_table_2.columnCount() < 4):
            self.block_table_2.setColumnCount(4)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.block_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.block_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.block_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.block_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        self.block_table_2.setObjectName(u"block_table_2")
        self.block_table_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.block_table_2.verticalHeader().setVisible(False)

        self.horizontalLayout_6.addWidget(self.block_table_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout = QGridLayout(self.tab_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.crossing_table = QTableWidget(self.tab_3)
        if (self.crossing_table.columnCount() < 2):
            self.crossing_table.setColumnCount(2)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.crossing_table.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.crossing_table.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        self.crossing_table.setObjectName(u"crossing_table")
        self.crossing_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.crossing_table.setColumnCount(2)
        self.crossing_table.horizontalHeader().setStretchLastSection(True)
        self.crossing_table.verticalHeader().setVisible(False)

        self.verticalLayout_6.addWidget(self.crossing_table)


        self.horizontalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.crossing_label = QLabel(self.tab_3)
        self.crossing_label.setObjectName(u"crossing_label")

        self.verticalLayout_7.addWidget(self.crossing_label)

        self.crossing_graphic = QLabel(self.tab_3)
        self.crossing_graphic.setObjectName(u"crossing_graphic")
        self.crossing_graphic.setMaximumSize(QSize(300, 200))
        self.crossing_graphic.setToolTipDuration(8)
        self.crossing_graphic.setPixmap(QPixmap(u"../../../.designer/backup/img/rrc_open.png"))
        self.crossing_graphic.setScaledContents(True)

        self.verticalLayout_7.addWidget(self.crossing_graphic)

        self.crossing_toggle = QPushButton(self.tab_3)
        self.crossing_toggle.setObjectName(u"crossing_toggle")

        self.verticalLayout_7.addWidget(self.crossing_toggle)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_7)

        self.block_table_3 = QTableWidget(self.tab_3)
        if (self.block_table_3.columnCount() < 4):
            self.block_table_3.setColumnCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.block_table_3.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.block_table_3.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.block_table_3.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.block_table_3.setHorizontalHeaderItem(3, __qtablewidgetitem19)
        self.block_table_3.setObjectName(u"block_table_3")
        self.block_table_3.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.block_table_3.verticalHeader().setVisible(False)

        self.horizontalLayout_7.addWidget(self.block_table_3)


        self.gridLayout.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout_7 = QGridLayout(self.tab_4)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox = QGroupBox(self.tab_4)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.tb_occ = QCheckBox(self.groupBox)
        self.tb_occ.setObjectName(u"tb_occ")
        self.tb_occ.setGeometry(QRect(30, 30, 111, 20))

        self.gridLayout_6.addWidget(self.groupBox, 1, 0, 1, 1)

        self.tb_block_label = QLabel(self.tab_4)
        self.tb_block_label.setObjectName(u"tb_block_label")

        self.gridLayout_6.addWidget(self.tb_block_label, 0, 0, 1, 2)

        self.tb_block_table = QTableWidget(self.tab_4)
        if (self.tb_block_table.columnCount() < 8):
            self.tb_block_table.setColumnCount(8)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_block_table.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_block_table.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_block_table.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_block_table.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_block_table.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tb_block_table.setHorizontalHeaderItem(5, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tb_block_table.setHorizontalHeaderItem(6, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tb_block_table.setHorizontalHeaderItem(7, __qtablewidgetitem27)
        self.tb_block_table.setObjectName(u"tb_block_table")
        self.tb_block_table.setMaximumSize(QSize(700, 16777215))
        self.tb_block_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_block_table.verticalHeader().setVisible(False)

        self.gridLayout_6.addWidget(self.tb_block_table, 0, 2, 3, 1)

        self.groupBox_2 = QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.tb_dis = QCheckBox(self.groupBox_2)
        self.tb_dis.setObjectName(u"tb_dis")
        self.tb_dis.setGeometry(QRect(30, 30, 221, 20))

        self.gridLayout_6.addWidget(self.groupBox_2, 1, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_5.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.header_layout = QWidget(self.centralwidget)
        self.header_layout.setObjectName(u"header_layout")
        self.header_layout.setMaximumSize(QSize(16777215, 70))
        self.header_layout.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.header_layout)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.header_layout)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setMaximumSize(QSize(52, 52))
        self.label.setPixmap(QPixmap(u"../../../.designer/backup/AuroraLogo.jpg"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_3 = QLabel(self.header_layout)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.node_select = QComboBox(self.header_layout)
        self.node_select.setObjectName(u"node_select")

        self.horizontalLayout.addWidget(self.node_select)

        self.pause_button = QPushButton(self.header_layout)
        self.pause_button.setObjectName(u"pause_button")
        icon = QIcon()
        icon.addFile(u"../Other/pause_button.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_button.setIcon(icon)
        self.pause_button.setIconSize(QSize(48, 48))
        self.pause_button.setCheckable(True)

        self.horizontalLayout.addWidget(self.pause_button)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.header_layout)
        self.label_6.setObjectName(u"label_6")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy5)
        self.label_6.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout.addWidget(self.label_6)

        self.horizontalSlider = QSlider(self.header_layout)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(5)
        sizePolicy6.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy6)
        self.horizontalSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setSingleStep(1)
        self.horizontalSlider.setPageStep(2)
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.horizontalSlider.setInvertedAppearance(False)
        self.horizontalSlider.setInvertedControls(False)
        self.horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(2)

        self.verticalLayout.addWidget(self.horizontalSlider)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label_4 = QLabel(self.header_layout)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)

        self.checkBox = QCheckBox(self.header_layout)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoRepeatDelay(298)

        self.horizontalLayout.addWidget(self.checkBox)


        self.gridLayout_5.addWidget(self.header_layout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1265, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuView.addAction(self.actionSwitch_Control)
        self.menuView.addAction(self.actionSignal_Control)
        self.menuView.addAction(self.actionCrossing_Control)
        self.menuView.addAction(self.actionTestbench)

        self.retranslateUi(MainWindow)
        self.actionSwitch_Control.triggered.connect(self.tabWidget.setFocus)
        self.actionSignal_Control.triggered.connect(self.tabWidget.setFocus)
        self.actionCrossing_Control.triggered.connect(self.tabWidget.setFocus)
        self.actionTestbench.triggered.connect(self.tabWidget.setFocus)
        self.switch_table.clicked.connect(self.switch_label.update)

        self.tabWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionSwitch_Control.setText(QCoreApplication.translate("MainWindow", u"Switch Control", None))
        self.actionSignal_Control.setText(QCoreApplication.translate("MainWindow", u"Signal Control", None))
        self.actionCrossing_Control.setText(QCoreApplication.translate("MainWindow", u"Crossing Control", None))
        self.actionTestbench.setText(QCoreApplication.translate("MainWindow", u"Testbench", None))
        ___qtablewidgetitem = self.switch_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Block", None));
        ___qtablewidgetitem1 = self.switch_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Primary Block", None));
        ___qtablewidgetitem2 = self.switch_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Secondary Block", None));
        ___qtablewidgetitem3 = self.switch_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Current Connection", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Switch Logic Program</span></p></body></html>", None))
        self.PLC_label.setText(QCoreApplication.translate("MainWindow", u"sample_file.eds", None))
        self.PLC_download.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.PLC_upload.setText(QCoreApplication.translate("MainWindow", u"Upload PLC File", None))
        self.switch_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Switch [SWITCH ID]</span></p></body></html>", None))
        self.state1_block_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">[STATE 1 BLOCK]</p></body></html>", None))
        self.state2_block_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">[STATE 2 BLOCK]</p></body></html>", None))
        self.switch_graphic.setText("")
        self.owner_block_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">[OWNER BLOCK]</p></body></html>", None))
        self.switch_toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle Switch", None))
        ___qtablewidgetitem4 = self.block_table_1.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Block ID", None));
        ___qtablewidgetitem5 = self.block_table_1.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem6 = self.block_table_1.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem7 = self.block_table_1.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), QCoreApplication.translate("MainWindow", u"Switch Control", None))
        ___qtablewidgetitem8 = self.signal_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Block", None));
        ___qtablewidgetitem9 = self.signal_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"State", None));
        self.signal_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Signal [SIGNAL ID]</span></p></body></html>", None))
        self.signal_graphic.setText("")
        self.signal_toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle Light", None))
        ___qtablewidgetitem10 = self.block_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Block ID", None));
        ___qtablewidgetitem11 = self.block_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem12 = self.block_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem13 = self.block_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Signal Control", None))
        ___qtablewidgetitem14 = self.crossing_table.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Block", None));
        ___qtablewidgetitem15 = self.crossing_table.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"State", None));
        self.crossing_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Crossing [CROSSING ID]</span></p></body></html>", None))
        self.crossing_graphic.setText("")
        self.crossing_toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle Crossing", None))
        ___qtablewidgetitem16 = self.block_table_3.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Block ID", None));
        ___qtablewidgetitem17 = self.block_table_3.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem18 = self.block_table_3.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem19 = self.block_table_3.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Crossing Control", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Track Model Inputs", None))
        self.tb_occ.setText(QCoreApplication.translate("MainWindow", u"Occupy Block", None))
        self.tb_block_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Block []</span></p></body></html>", None))
        ___qtablewidgetitem20 = self.tb_block_table.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Block ID", None));
        ___qtablewidgetitem21 = self.tb_block_table.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Section", None));
        ___qtablewidgetitem22 = self.tb_block_table.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem23 = self.tb_block_table.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Occupancy", None));
        ___qtablewidgetitem24 = self.tb_block_table.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Switch", None));
        ___qtablewidgetitem25 = self.tb_block_table.horizontalHeaderItem(5)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Signal", None));
        ___qtablewidgetitem26 = self.tb_block_table.horizontalHeaderItem(6)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Crossing", None));
        ___qtablewidgetitem27 = self.tb_block_table.horizontalHeaderItem(7)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Vital Authority", None));
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"CTC Office Inputs", None))
        self.tb_dis.setText(QCoreApplication.translate("MainWindow", u"Place under maintenance", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Testbench", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Wayside Controller</span></p></body></html>", None))
        self.pause_button.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Simulation speed</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Simulation time\n"
"MM/DD/YYYY hh:mm:ss", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Manual Mode", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

