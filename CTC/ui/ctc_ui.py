# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ctccphRdj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1144, 770)
        self.actionActive_Trains = QAction(MainWindow)
        self.actionActive_Trains.setObjectName(u"actionActive_Trains")
        self.actionView_Active_Trains = QAction(MainWindow)
        self.actionView_Active_Trains.setObjectName(u"actionView_Active_Trains")
        self.actionTestbench = QAction(MainWindow)
        self.actionTestbench.setObjectName(u"actionTestbench")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setKerning(True)
        self.centralwidget.setFont(font)
        self.centralwidget.setAutoFillBackground(True)
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.header_layout = QWidget(self.centralwidget)
        self.header_layout.setObjectName(u"header_layout")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header_layout.sizePolicy().hasHeightForWidth())
        self.header_layout.setSizePolicy(sizePolicy)
        self.header_layout.setMaximumSize(QSize(16777215, 50))
        self.header_layout.setBaseSize(QSize(0, 16))
        self.menu = QHBoxLayout(self.header_layout)
        self.menu.setSpacing(0)
        self.menu.setObjectName(u"menu")
        self.menu.setContentsMargins(0, 0, 0, 0)
        self.header_icon = QLabel(self.header_layout)
        self.header_icon.setObjectName(u"header_icon")
        self.header_icon.setMaximumSize(QSize(55, 16777215))
        self.header_icon.setPixmap(QPixmap(u"images/AuroraLogo.jpg"))
        self.header_icon.setScaledContents(True)

        self.menu.addWidget(self.header_icon)

        self.header_ctc_label = QLabel(self.header_layout)
        self.header_ctc_label.setObjectName(u"header_ctc_label")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setKerning(True)
        self.header_ctc_label.setFont(font1)

        self.menu.addWidget(self.header_ctc_label)

        self.header_spacer = QSpacerItem(25, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.menu.addItem(self.header_spacer)

        self.header_simulation_label = QLabel(self.header_layout)
        self.header_simulation_label.setObjectName(u"header_simulation_label")
        self.header_simulation_label.setFont(font1)
        self.header_simulation_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.menu.addWidget(self.header_simulation_label)

        self.header_pause_button = QPushButton(self.header_layout)
        self.header_pause_button.setObjectName(u"header_pause_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_pause_button.sizePolicy().hasHeightForWidth())
        self.header_pause_button.setSizePolicy(sizePolicy1)
        self.header_pause_button.setMinimumSize(QSize(50, 50))
        self.header_pause_button.setIconSize(QSize(50, 50))

        self.menu.addWidget(self.header_pause_button)

        self.header_simulation_layout = QWidget(self.header_layout)
        self.header_simulation_layout.setObjectName(u"header_simulation_layout")
        self.gridLayout_4 = QGridLayout(self.header_simulation_layout)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.simulation_slider = QSlider(self.header_simulation_layout)
        self.simulation_slider.setObjectName(u"simulation_slider")
        self.simulation_slider.setMinimum(1)
        self.simulation_slider.setMaximum(10)
        self.simulation_slider.setValue(1)
        self.simulation_slider.setOrientation(Qt.Horizontal)
        self.simulation_slider.setTickPosition(QSlider.TicksBelow)

        self.gridLayout_4.addWidget(self.simulation_slider, 0, 0, 1, 3)

        self.simulation_10_label = QLabel(self.header_simulation_layout)
        self.simulation_10_label.setObjectName(u"simulation_10_label")
        self.simulation_10_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.simulation_10_label, 1, 2, 1, 1)

        self.simulation_1_label = QLabel(self.header_simulation_layout)
        self.simulation_1_label.setObjectName(u"simulation_1_label")
        self.simulation_1_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_4.addWidget(self.simulation_1_label, 1, 0, 1, 1)


        self.menu.addWidget(self.header_simulation_layout)

        self.header_time_display = QLabel(self.header_layout)
        self.header_time_display.setObjectName(u"header_time_display")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setKerning(True)
        self.header_time_display.setFont(font2)
        self.header_time_display.setFrameShape(QFrame.Box)

        self.menu.addWidget(self.header_time_display)


        self.gridLayout_3.addWidget(self.header_layout, 0, 0, 1, 1)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy2)
        self.SendTrains = QWidget()
        self.SendTrains.setObjectName(u"SendTrains")
        self.gridLayout_2 = QGridLayout(self.SendTrains)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.Send_Train_Layout = QGridLayout()
        self.Send_Train_Layout.setObjectName(u"Send_Train_Layout")
        self.Send_Train_Modes = QGridLayout()
        self.Send_Train_Modes.setObjectName(u"Send_Train_Modes")
        self.send_manual_button = QRadioButton(self.SendTrains)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.send_manual_button)
        self.send_manual_button.setObjectName(u"send_manual_button")

        self.Send_Train_Modes.addWidget(self.send_manual_button, 0, 1, 1, 1)

        self.Automatic_Layout = QWidget(self.SendTrains)
        self.Automatic_Layout.setObjectName(u"Automatic_Layout")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Automatic_Layout.sizePolicy().hasHeightForWidth())
        self.Automatic_Layout.setSizePolicy(sizePolicy3)
        self.Automatic_Layout.setMinimumSize(QSize(350, 0))
        self.gridLayout_5 = QGridLayout(self.Automatic_Layout)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.automatic_vert_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.automatic_vert_spacer, 0, 1, 1, 1)

        self.automatic_error_label = QLabel(self.Automatic_Layout)
        self.automatic_error_label.setObjectName(u"automatic_error_label")

        self.gridLayout_5.addWidget(self.automatic_error_label, 1, 1, 1, 1)

        self.automatic_upload_button = QPushButton(self.Automatic_Layout)
        self.automatic_upload_button.setObjectName(u"automatic_upload_button")

        self.gridLayout_5.addWidget(self.automatic_upload_button, 2, 1, 1, 1)


        self.Send_Train_Modes.addWidget(self.Automatic_Layout, 1, 0, 1, 2)

        self.send_automatic_button = QRadioButton(self.SendTrains)
        self.buttonGroup.addButton(self.send_automatic_button)
        self.send_automatic_button.setObjectName(u"send_automatic_button")
        self.send_automatic_button.setCheckable(True)
        self.send_automatic_button.setChecked(True)

        self.Send_Train_Modes.addWidget(self.send_automatic_button, 0, 0, 1, 1)

        self.Manual_Layout = QWidget(self.SendTrains)
        self.Manual_Layout.setObjectName(u"Manual_Layout")
        sizePolicy3.setHeightForWidth(self.Manual_Layout.sizePolicy().hasHeightForWidth())
        self.Manual_Layout.setSizePolicy(sizePolicy3)
        self.Manual_Layout.setMinimumSize(QSize(350, 0))
        self.Manual_Dispatch_Layout = QGridLayout(self.Manual_Layout)
        self.Manual_Dispatch_Layout.setObjectName(u"Manual_Dispatch_Layout")
        self.manual_train_block_input = QComboBox(self.Manual_Layout)
        self.manual_train_block_input.setObjectName(u"manual_train_block_input")
        self.manual_train_block_input.setEditable(True)
        self.manual_train_block_input.setInsertPolicy(QComboBox.NoInsert)

        self.Manual_Dispatch_Layout.addWidget(self.manual_train_block_input, 2, 0, 1, 1)

        self.manual_train_destination_button = QPushButton(self.Manual_Layout)
        self.manual_train_destination_button.setObjectName(u"manual_train_destination_button")

        self.Manual_Dispatch_Layout.addWidget(self.manual_train_destination_button, 5, 0, 1, 1)

        self.manual_train_dispatch_button = QPushButton(self.Manual_Layout)
        self.manual_train_dispatch_button.setObjectName(u"manual_train_dispatch_button")

        self.Manual_Dispatch_Layout.addWidget(self.manual_train_dispatch_button, 9, 0, 1, 1)

        self.manual_train_time_input = QDateTimeEdit(self.Manual_Layout)
        self.manual_train_time_input.setObjectName(u"manual_train_time_input")

        self.Manual_Dispatch_Layout.addWidget(self.manual_train_time_input, 4, 0, 1, 1)

        self.manual_train_line_input = QComboBox(self.Manual_Layout)
        self.manual_train_line_input.addItem("")
        self.manual_train_line_input.addItem("")
        self.manual_train_line_input.setObjectName(u"manual_train_line_input")
        self.manual_train_line_input.setEditable(True)
        self.manual_train_line_input.setInsertPolicy(QComboBox.NoInsert)
        self.manual_train_line_input.setPlaceholderText(u"Select Line")

        self.Manual_Dispatch_Layout.addWidget(self.manual_train_line_input, 0, 0, 1, 1)

        self.manual_error_label = QLabel(self.Manual_Layout)
        self.manual_error_label.setObjectName(u"manual_error_label")
        self.manual_error_label.setWordWrap(True)

        self.Manual_Dispatch_Layout.addWidget(self.manual_error_label, 7, 0, 1, 1)

        self.manual_reset_button = QPushButton(self.Manual_Layout)
        self.manual_reset_button.setObjectName(u"manual_reset_button")

        self.Manual_Dispatch_Layout.addWidget(self.manual_reset_button, 8, 0, 1, 1)

        self.manual_train_station_input = QComboBox(self.Manual_Layout)
        self.manual_train_station_input.setObjectName(u"manual_train_station_input")
        self.manual_train_station_input.setEditable(True)
        self.manual_train_station_input.setInsertPolicy(QComboBox.NoInsert)

        self.Manual_Dispatch_Layout.addWidget(self.manual_train_station_input, 1, 0, 1, 1)

        self.manual_route_table = QTableWidget(self.Manual_Layout)
        if (self.manual_route_table.columnCount() < 2):
            self.manual_route_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.manual_route_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.manual_route_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.manual_route_table.setObjectName(u"manual_route_table")
        self.manual_route_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.Manual_Dispatch_Layout.addWidget(self.manual_route_table, 6, 0, 1, 1)


        self.Send_Train_Modes.addWidget(self.Manual_Layout, 2, 0, 1, 2)


        self.Send_Train_Layout.addLayout(self.Send_Train_Modes, 0, 0, 1, 1)

        self.train_layout = QGridLayout()
        self.train_layout.setObjectName(u"train_layout")
        self.train_id_display = QLabel(self.SendTrains)
        self.train_id_display.setObjectName(u"train_id_display")

        self.train_layout.addWidget(self.train_id_display, 5, 1, 1, 1)

        self.train_dispatch_label = QLabel(self.SendTrains)
        self.train_dispatch_label.setObjectName(u"train_dispatch_label")

        self.train_layout.addWidget(self.train_dispatch_label, 2, 0, 1, 2)

        self.train_schedule_table = QTableWidget(self.SendTrains)
        if (self.train_schedule_table.columnCount() < 3):
            self.train_schedule_table.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.train_schedule_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.train_schedule_table.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.train_schedule_table.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.train_schedule_table.setObjectName(u"train_schedule_table")
        sizePolicy4 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.train_schedule_table.sizePolicy().hasHeightForWidth())
        self.train_schedule_table.setSizePolicy(sizePolicy4)
        self.train_schedule_table.setMinimumSize(QSize(400, 0))
        self.train_schedule_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.train_layout.addWidget(self.train_schedule_table, 1, 0, 1, 2)

        self.train_route_table = QTableWidget(self.SendTrains)
        if (self.train_route_table.columnCount() < 2):
            self.train_route_table.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.train_route_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.train_route_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.train_route_table.setObjectName(u"train_route_table")
        self.train_route_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.train_layout.addWidget(self.train_route_table, 10, 0, 1, 2)

        self.train_destination_display = QLabel(self.SendTrains)
        self.train_destination_display.setObjectName(u"train_destination_display")

        self.train_layout.addWidget(self.train_destination_display, 8, 1, 1, 1)

        self.train_line_label = QLabel(self.SendTrains)
        self.train_line_label.setObjectName(u"train_line_label")

        self.train_layout.addWidget(self.train_line_label, 6, 0, 1, 1)

        self.train_schedule_label = QLabel(self.SendTrains)
        self.train_schedule_label.setObjectName(u"train_schedule_label")

        self.train_layout.addWidget(self.train_schedule_label, 0, 0, 1, 2)

        self.train_dispatch_table = QTableWidget(self.SendTrains)
        if (self.train_dispatch_table.columnCount() < 3):
            self.train_dispatch_table.setColumnCount(3)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.train_dispatch_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.train_dispatch_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.train_dispatch_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        self.train_dispatch_table.setObjectName(u"train_dispatch_table")
        sizePolicy4.setHeightForWidth(self.train_dispatch_table.sizePolicy().hasHeightForWidth())
        self.train_dispatch_table.setSizePolicy(sizePolicy4)
        self.train_dispatch_table.setMinimumSize(QSize(400, 0))
        self.train_dispatch_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.train_layout.addWidget(self.train_dispatch_table, 3, 0, 1, 2)

        self.train_info_label = QLabel(self.SendTrains)
        self.train_info_label.setObjectName(u"train_info_label")

        self.train_layout.addWidget(self.train_info_label, 4, 0, 1, 2)

        self.train_route_label = QLabel(self.SendTrains)
        self.train_route_label.setObjectName(u"train_route_label")

        self.train_layout.addWidget(self.train_route_label, 9, 0, 1, 2)

        self.train_destination_label = QLabel(self.SendTrains)
        self.train_destination_label.setObjectName(u"train_destination_label")

        self.train_layout.addWidget(self.train_destination_label, 8, 0, 1, 1)

        self.train_line_display = QLabel(self.SendTrains)
        self.train_line_display.setObjectName(u"train_line_display")

        self.train_layout.addWidget(self.train_line_display, 6, 1, 1, 1)

        self.train_position_display = QLabel(self.SendTrains)
        self.train_position_display.setObjectName(u"train_position_display")

        self.train_layout.addWidget(self.train_position_display, 7, 1, 1, 1)

        self.train_id_label = QLabel(self.SendTrains)
        self.train_id_label.setObjectName(u"train_id_label")

        self.train_layout.addWidget(self.train_id_label, 5, 0, 1, 1)

        self.train_position_label = QLabel(self.SendTrains)
        self.train_position_label.setObjectName(u"train_position_label")

        self.train_layout.addWidget(self.train_position_label, 7, 0, 1, 1)


        self.Send_Train_Layout.addLayout(self.train_layout, 0, 1, 1, 1)

        self.Send_Block_Layout = QGridLayout()
        self.Send_Block_Layout.setObjectName(u"Send_Block_Layout")
        self.send_block_label = QLabel(self.SendTrains)
        self.send_block_label.setObjectName(u"send_block_label")
        self.send_block_label.setFont(font2)

        self.Send_Block_Layout.addWidget(self.send_block_label, 2, 0, 1, 1)

        self.block_line_input = QComboBox(self.SendTrains)
        self.block_line_input.addItem("")
        self.block_line_input.addItem("")
        self.block_line_input.setObjectName(u"block_line_input")

        self.Send_Block_Layout.addWidget(self.block_line_input, 3, 0, 1, 1)

        self.active_throughput_layout = QHBoxLayout()
        self.active_throughput_layout.setObjectName(u"active_throughput_layout")
        self.block_throughput_label = QLabel(self.SendTrains)
        self.block_throughput_label.setObjectName(u"block_throughput_label")

        self.active_throughput_layout.addWidget(self.block_throughput_label)

        self.block_throughput_display = QLabel(self.SendTrains)
        self.block_throughput_display.setObjectName(u"block_throughput_display")

        self.active_throughput_layout.addWidget(self.block_throughput_display)


        self.Send_Block_Layout.addLayout(self.active_throughput_layout, 1, 0, 1, 1)

        self.manual_block_table = QTableWidget(self.SendTrains)
        if (self.manual_block_table.columnCount() < 3):
            self.manual_block_table.setColumnCount(3)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.manual_block_table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.manual_block_table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.manual_block_table.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        self.manual_block_table.setObjectName(u"manual_block_table")
        sizePolicy2.setHeightForWidth(self.manual_block_table.sizePolicy().hasHeightForWidth())
        self.manual_block_table.setSizePolicy(sizePolicy2)
        self.manual_block_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.manual_block_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.manual_block_table.setSortingEnabled(True)
        self.manual_block_table.horizontalHeader().setCascadingSectionResizes(False)

        self.Send_Block_Layout.addWidget(self.manual_block_table, 5, 0, 1, 1)

        self.manual_block_layout = QWidget(self.SendTrains)
        self.manual_block_layout.setObjectName(u"manual_block_layout")
        self.Manual_Block_Layout = QGridLayout(self.manual_block_layout)
        self.Manual_Block_Layout.setObjectName(u"Manual_Block_Layout")
        self.Manual_Block_Layout.setVerticalSpacing(7)
        self.manual_block_switch_input = QComboBox(self.manual_block_layout)
        self.manual_block_switch_input.setObjectName(u"manual_block_switch_input")
        self.manual_block_switch_input.setMinimumSize(QSize(150, 0))
        self.manual_block_switch_input.setEditable(True)
        self.manual_block_switch_input.setInsertPolicy(QComboBox.NoInsert)

        self.Manual_Block_Layout.addWidget(self.manual_block_switch_input, 2, 0, 1, 1)

        self.manual_maintenance_layout = QGridLayout()
        self.manual_maintenance_layout.setObjectName(u"manual_maintenance_layout")
        self.manual_maintenance_layout.setVerticalSpacing(0)
        self.manual_block_close_button = QPushButton(self.manual_block_layout)
        self.manual_block_close_button.setObjectName(u"manual_block_close_button")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.manual_block_close_button.sizePolicy().hasHeightForWidth())
        self.manual_block_close_button.setSizePolicy(sizePolicy5)
        self.manual_block_close_button.setMinimumSize(QSize(283, 0))
        font3 = QFont()
        font3.setPointSize(12)
        font3.setKerning(True)
        self.manual_block_close_button.setFont(font3)

        self.manual_maintenance_layout.addWidget(self.manual_block_close_button, 0, 0, 1, 1)

        self.manual_block_open_button = QPushButton(self.manual_block_layout)
        self.manual_block_open_button.setObjectName(u"manual_block_open_button")
        self.manual_block_open_button.setMinimumSize(QSize(283, 0))
        self.manual_block_open_button.setFont(font3)

        self.manual_maintenance_layout.addWidget(self.manual_block_open_button, 1, 0, 1, 1)


        self.Manual_Block_Layout.addLayout(self.manual_maintenance_layout, 1, 0, 1, 1)


        self.Send_Block_Layout.addWidget(self.manual_block_layout, 6, 0, 1, 1)

        self.manual_block_input = QComboBox(self.SendTrains)
        self.manual_block_input.setObjectName(u"manual_block_input")
        self.manual_block_input.setMinimumSize(QSize(150, 0))
        self.manual_block_input.setEditable(True)
        self.manual_block_input.setInsertPolicy(QComboBox.NoInsert)

        self.Send_Block_Layout.addWidget(self.manual_block_input, 4, 0, 1, 1)


        self.Send_Train_Layout.addLayout(self.Send_Block_Layout, 0, 2, 1, 1)

        self.Send_Train_Layout.setColumnStretch(1, 1)
        self.Send_Train_Layout.setColumnStretch(2, 2)

        self.gridLayout_2.addLayout(self.Send_Train_Layout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.SendTrains, "")
        self.testBench = QWidget()
        self.testBench.setObjectName(u"testBench")
        self.gridLayout_10 = QGridLayout(self.testBench)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.tb_train_layout = QGridLayout()
        self.tb_train_layout.setObjectName(u"tb_train_layout")
        self.tb_train_input_layout = QGridLayout()
        self.tb_train_input_layout.setObjectName(u"tb_train_input_layout")
        self.tb_speed_input = QTextEdit(self.testBench)
        self.tb_speed_input.setObjectName(u"tb_speed_input")
        self.tb_speed_input.setMaximumSize(QSize(16777215, 50))

        self.tb_train_input_layout.addWidget(self.tb_speed_input, 1, 0, 1, 1)

        self.tb_position_input = QPushButton(self.testBench)
        self.tb_position_input.setObjectName(u"tb_position_input")

        self.tb_train_input_layout.addWidget(self.tb_position_input, 0, 0, 1, 1)

        self.tb_train_info_layout = QGridLayout()
        self.tb_train_info_layout.setObjectName(u"tb_train_info_layout")
        self.tb_train_info_layout.setContentsMargins(-1, -1, 15, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tb_authority_label = QLabel(self.testBench)
        self.tb_authority_label.setObjectName(u"tb_authority_label")

        self.gridLayout.addWidget(self.tb_authority_label, 0, 0, 1, 1)

        self.tb_authority_value = QLabel(self.testBench)
        self.tb_authority_value.setObjectName(u"tb_authority_value")

        self.gridLayout.addWidget(self.tb_authority_value, 0, 1, 1, 1)

        self.tb_speed_label = QLabel(self.testBench)
        self.tb_speed_label.setObjectName(u"tb_speed_label")

        self.gridLayout.addWidget(self.tb_speed_label, 1, 0, 1, 1)

        self.tb_speed_value = QLabel(self.testBench)
        self.tb_speed_value.setObjectName(u"tb_speed_value")

        self.gridLayout.addWidget(self.tb_speed_value, 1, 1, 1, 1)


        self.tb_train_info_layout.addLayout(self.gridLayout, 2, 0, 1, 1)

        self.tb_train_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tb_train_info_layout.addItem(self.tb_train_spacer, 3, 0, 1, 1)


        self.tb_train_input_layout.addLayout(self.tb_train_info_layout, 2, 0, 1, 1)


        self.tb_train_layout.addLayout(self.tb_train_input_layout, 1, 0, 1, 1)

        self.tb_train_layout.setColumnStretch(0, 1)

        self.gridLayout_10.addLayout(self.tb_train_layout, 0, 0, 1, 1)

        self.tb_block_layout = QGridLayout()
        self.tb_block_layout.setObjectName(u"tb_block_layout")
        self.tb_block_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.tb_block_layout.addItem(self.tb_block_spacer, 4, 0, 1, 1)

        self.tb_block_status_input = QComboBox(self.testBench)
        self.tb_block_status_input.addItem("")
        self.tb_block_status_input.addItem("")
        self.tb_block_status_input.setObjectName(u"tb_block_status_input")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tb_block_status_input.sizePolicy().hasHeightForWidth())
        self.tb_block_status_input.setSizePolicy(sizePolicy6)
        self.tb_block_status_input.setEditable(False)

        self.tb_block_layout.addWidget(self.tb_block_status_input, 2, 0, 1, 1)

        self.tb_error_label = QLabel(self.testBench)
        self.tb_error_label.setObjectName(u"tb_error_label")

        self.tb_block_layout.addWidget(self.tb_error_label, 5, 0, 1, 1)

        self.tb_block_input = QComboBox(self.testBench)
        self.tb_block_input.setObjectName(u"tb_block_input")
        self.tb_block_input.setEditable(True)

        self.tb_block_layout.addWidget(self.tb_block_input, 0, 0, 1, 1)

        self.tb_block_line_input = QComboBox(self.testBench)
        self.tb_block_line_input.setObjectName(u"tb_block_line_input")
        sizePolicy6.setHeightForWidth(self.tb_block_line_input.sizePolicy().hasHeightForWidth())
        self.tb_block_line_input.setSizePolicy(sizePolicy6)

        self.tb_block_layout.addWidget(self.tb_block_line_input, 1, 0, 1, 1)

        self.tb_occupancy_button = QPushButton(self.testBench)
        self.tb_occupancy_button.setObjectName(u"tb_occupancy_button")

        self.tb_block_layout.addWidget(self.tb_occupancy_button, 3, 0, 1, 1)

        self.tb_block_line_input1 = QComboBox(self.testBench)
        self.tb_block_line_input1.setObjectName(u"tb_block_line_input1")
        sizePolicy6.setHeightForWidth(self.tb_block_line_input1.sizePolicy().hasHeightForWidth())
        self.tb_block_line_input1.setSizePolicy(sizePolicy6)

        self.tb_block_layout.addWidget(self.tb_block_line_input1, 1, 0, 1, 1)


        self.gridLayout_10.addLayout(self.tb_block_layout, 0, 1, 1, 1)

        self.tabWidget.addTab(self.testBench, "")

        self.gridLayout_3.addWidget(self.tabWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.send_automatic_button.toggled.connect(self.Automatic_Layout.setVisible)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionActive_Trains.setText(QCoreApplication.translate("MainWindow", u"Send Trains", None))
        self.actionView_Active_Trains.setText(QCoreApplication.translate("MainWindow", u"View Active Trains", None))
        self.actionTestbench.setText(QCoreApplication.translate("MainWindow", u"Testbench", None))
        self.header_icon.setText("")
        self.header_ctc_label.setText(QCoreApplication.translate("MainWindow", u"CTC Office", None))
        self.header_simulation_label.setText(QCoreApplication.translate("MainWindow", u"Simulation Speed", None))
        self.header_pause_button.setText("")
        self.simulation_10_label.setText(QCoreApplication.translate("MainWindow", u"10x", None))
        self.simulation_1_label.setText(QCoreApplication.translate("MainWindow", u"1x", None))
        self.header_time_display.setText(QCoreApplication.translate("MainWindow", u"xx/xx/xxxx xx:xx:xx", None))
        self.send_manual_button.setText(QCoreApplication.translate("MainWindow", u"Manual Mode", None))
        self.automatic_error_label.setText(QCoreApplication.translate("MainWindow", u"Error Label", None))
        self.automatic_upload_button.setText(QCoreApplication.translate("MainWindow", u"Upload Train Schedule", None))
        self.send_automatic_button.setText(QCoreApplication.translate("MainWindow", u"Automatic Mode", None))
        self.manual_train_block_input.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Block", None))
        self.manual_train_destination_button.setText(QCoreApplication.translate("MainWindow", u"Add Desination", None))
        self.manual_train_dispatch_button.setText(QCoreApplication.translate("MainWindow", u"Dispatch Train", None))
        self.manual_train_time_input.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy hh:mm", None))
        self.manual_train_line_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.manual_train_line_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Red Line", None))

        self.manual_train_line_input.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Line", None))
        self.manual_error_label.setText(QCoreApplication.translate("MainWindow", u"Error Label", None))
        self.manual_reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset Route", None))
        self.manual_train_station_input.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Station", None))
        ___qtablewidgetitem = self.manual_route_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Station", None));
        ___qtablewidgetitem1 = self.manual_route_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Arrival Time", None));
        self.train_id_display.setText(QCoreApplication.translate("MainWindow", u"No Train Selected", None))
        self.train_dispatch_label.setText(QCoreApplication.translate("MainWindow", u"Dispatched Trains", None))
        ___qtablewidgetitem2 = self.train_schedule_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem3 = self.train_schedule_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem4 = self.train_schedule_table.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Departure Time", None));
        ___qtablewidgetitem5 = self.train_route_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem6 = self.train_route_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Arrival Time", None));
        self.train_destination_display.setText(QCoreApplication.translate("MainWindow", u"No Train Selected", None))
        self.train_line_label.setText(QCoreApplication.translate("MainWindow", u"Line", None))
        self.train_schedule_label.setText(QCoreApplication.translate("MainWindow", u"Scheduled Trains", None))
        ___qtablewidgetitem7 = self.train_dispatch_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Line", None));
        ___qtablewidgetitem8 = self.train_dispatch_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem9 = self.train_dispatch_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Departure Time", None));
        self.train_info_label.setText(QCoreApplication.translate("MainWindow", u"Train Information", None))
        self.train_route_label.setText(QCoreApplication.translate("MainWindow", u"Route", None))
        self.train_destination_label.setText(QCoreApplication.translate("MainWindow", u"Next Destination", None))
        self.train_line_display.setText(QCoreApplication.translate("MainWindow", u"No Train Selected", None))
        self.train_position_display.setText(QCoreApplication.translate("MainWindow", u"No Train Selected", None))
        self.train_id_label.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.train_position_label.setText(QCoreApplication.translate("MainWindow", u"Train Position", None))
        self.send_block_label.setText(QCoreApplication.translate("MainWindow", u"Blocks", None))
        self.block_line_input.setItemText(0, QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.block_line_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Red Line", None))

        self.block_throughput_label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Throughput</span></p></body></html>", None))
        self.block_throughput_display.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">220/hr</span></p></body></html>", None))
        ___qtablewidgetitem10 = self.manual_block_table.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Block", None));
        ___qtablewidgetitem11 = self.manual_block_table.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem12 = self.manual_block_table.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Infrastructure", None));
        self.manual_block_switch_input.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Switch State", None))
        self.manual_block_close_button.setText(QCoreApplication.translate("MainWindow", u"Put Block in Maintanence", None))
        self.manual_block_open_button.setText(QCoreApplication.translate("MainWindow", u"Take Block out of Maintanence", None))
        self.manual_block_input.setCurrentText(QCoreApplication.translate("MainWindow", u"Select Block", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SendTrains), QCoreApplication.translate("MainWindow", u"Send Trains", None))
        self.tb_speed_input.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Tickets</span></p></body></html>", None))
        self.tb_position_input.setText(QCoreApplication.translate("MainWindow", u"Send Tickets", None))
        self.tb_authority_label.setText(QCoreApplication.translate("MainWindow", u"Authority", None))
        self.tb_authority_value.setText(QCoreApplication.translate("MainWindow", u"200m", None))
        self.tb_speed_label.setText(QCoreApplication.translate("MainWindow", u"Suggested Speed", None))
        self.tb_speed_value.setText(QCoreApplication.translate("MainWindow", u"20m/s", None))
        self.tb_block_status_input.setItemText(0, "")
        self.tb_block_status_input.setItemText(1, QCoreApplication.translate("MainWindow", u"Fault", None))

        self.tb_block_status_input.setCurrentText("")
        self.tb_error_label.setText(QCoreApplication.translate("MainWindow", u"Error label", None))
        self.tb_occupancy_button.setText(QCoreApplication.translate("MainWindow", u"Toggle Block Occupancy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.testBench), QCoreApplication.translate("MainWindow", u"Testbench", None))
    # retranslateUi

