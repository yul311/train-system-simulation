# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'train_ctrl_v12.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QLCDNumber,
    QLabel, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QScrollArea,
    QSizePolicy, QSlider, QStatusBar, QTabWidget,
    QTextBrowser, QWidget, QLineEdit)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1035, 783)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title_txt = QLabel(self.centralwidget)
        self.title_txt.setObjectName(u"title_txt")
        self.title_txt.setGeometry(QRect(90, 0, 211, 51))
        font1 = QFont()
        font1.setPointSize(20)
        self.title_txt.setFont(font1)
        self.title_txt.setAutoFillBackground(False)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 110, 1011, 611))
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.drive_ctrl_box = QGroupBox(self.main)
        self.drive_ctrl_box.setObjectName(u"drive_ctrl_box")
        self.drive_ctrl_box.setGeometry(QRect(20, 60, 491, 151))
        self.current_speed_display = QLCDNumber(self.drive_ctrl_box)
        self.current_speed_display.setObjectName(u"current_speed_display")
        self.current_speed_display.setGeometry(QRect(120, 30, 64, 31))
        self.input_speed_display = QLCDNumber(self.drive_ctrl_box)
        self.input_speed_display.setObjectName(u"input_speed_display")
        self.input_speed_display.setGeometry(QRect(350, 30, 64, 31))
        self.speed_limit_display = QLCDNumber(self.drive_ctrl_box)
        self.speed_limit_display.setObjectName(u"speed_limit_display")
        self.speed_limit_display.setGeometry(QRect(120, 100, 64, 31))
        self.suggested_speed_display = QLCDNumber(self.drive_ctrl_box)
        self.suggested_speed_display.setObjectName(u"suggested_speed_display")
        self.suggested_speed_display.setGeometry(QRect(350, 100, 64, 31))
        self.input_speed_slider = QSlider(self.drive_ctrl_box)
        self.input_speed_slider.setObjectName(u"input_speed_slider")
        self.input_speed_slider.setGeometry(QRect(250, 70, 151, 22))
        self.input_speed_slider.setMinimum(1)
        self.input_speed_slider.setMaximum(24)
        self.input_speed_slider.setPageStep(8)
        self.input_speed_slider.setSliderPosition(1)
        self.input_speed_slider.setOrientation(Qt.Horizontal)
        self.input_speed_slider.setInvertedAppearance(False)
        self.input_speed_slider.setTickPosition(QSlider.TicksBelow)
        self.input_speed_slider.setTickInterval(3)
        self.current_speed_txt = QTextBrowser(self.drive_ctrl_box)
        self.current_speed_txt.setObjectName(u"current_speed_txt")
        self.current_speed_txt.setGeometry(QRect(10, 30, 111, 31))
        self.current_speed_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.current_speed_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.speed_limit_txt = QTextBrowser(self.drive_ctrl_box)
        self.speed_limit_txt.setObjectName(u"speed_limit_txt")
        self.speed_limit_txt.setGeometry(QRect(10, 100, 111, 31))
        self.speed_limit_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.speed_limit_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.input_speed_txt = QTextBrowser(self.drive_ctrl_box)
        self.input_speed_txt.setObjectName(u"input_speed_txt")
        self.input_speed_txt.setGeometry(QRect(230, 30, 121, 31))
        self.input_speed_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.input_speed_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.suggested_speed_txt = QTextBrowser(self.drive_ctrl_box)
        self.suggested_speed_txt.setObjectName(u"suggested_speed_txt")
        self.suggested_speed_txt.setGeometry(QRect(230, 100, 121, 31))
        self.suggested_speed_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.suggested_speed_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mph_txt_3 = QLabel(self.drive_ctrl_box)
        self.mph_txt_3.setObjectName(u"mph_txt_3")
        self.mph_txt_3.setGeometry(QRect(190, 110, 31, 21))
        font2 = QFont()
        font2.setPointSize(11)
        self.mph_txt_3.setFont(font2)
        self.mph_txt_1 = QLabel(self.drive_ctrl_box)
        self.mph_txt_1.setObjectName(u"mph_txt_1")
        self.mph_txt_1.setGeometry(QRect(190, 40, 31, 21))
        self.mph_txt_1.setFont(font2)
        self.mph_txt_4 = QLabel(self.drive_ctrl_box)
        self.mph_txt_4.setObjectName(u"mph_txt_4")
        self.mph_txt_4.setGeometry(QRect(420, 110, 31, 21))
        self.mph_txt_4.setFont(font2)
        self.mph_txt_2 = QLabel(self.drive_ctrl_box)
        self.mph_txt_2.setObjectName(u"mph_txt_2")
        self.mph_txt_2.setGeometry(QRect(420, 40, 31, 21))
        self.mph_txt_2.setFont(font2)
        self.brake_box = QGroupBox(self.main)
        self.brake_box.setObjectName(u"brake_box")
        self.brake_box.setGeometry(QRect(540, 300, 451, 271))
        self.e_brake_button = QPushButton(self.brake_box)
        self.e_brake_button.setObjectName(u"e_brake_button")
        self.e_brake_button.setGeometry(QRect(10, 110, 431, 71))
        font3 = QFont()
        font3.setPointSize(27)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.e_brake_button.setFont(font3)
        self.e_brake_button.setAutoFillBackground(True)
        self.engage_box = QGroupBox(self.brake_box)
        self.engage_box.setObjectName(u"engage_box")
        self.engage_box.setGeometry(QRect(10, 20, 431, 91))
        self.s_brake_txt = QTextBrowser(self.engage_box)
        self.s_brake_txt.setObjectName(u"s_brake_txt")
        self.s_brake_txt.setGeometry(QRect(10, 53, 229, 26))
        self.s_brake_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.s_brake_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.e_brake_txt = QTextBrowser(self.engage_box)
        self.e_brake_txt.setObjectName(u"e_brake_txt")
        self.e_brake_txt.setGeometry(QRect(10, 20, 229, 27))
        self.e_brake_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.e_brake_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.s_label_display = QLabel(self.engage_box)
        self.s_label_display.setObjectName(u"s_label_display")
        self.s_label_display.setGeometry(QRect(280, 50, 87, 27))
        font4 = QFont()
        font4.setPointSize(12)
        self.s_label_display.setFont(font4)
        self.e_label_display = QLabel(self.engage_box)
        self.e_label_display.setObjectName(u"e_label_display")
        self.e_label_display.setGeometry(QRect(280, 20, 87, 27))
        self.e_label_display.setFont(font4)
        self.e_label_display.setStyleSheet(u"text-align: center")
        self.s_brake_button = QPushButton(self.brake_box)
        self.s_brake_button.setObjectName(u"s_brake_button")
        self.s_brake_button.setGeometry(QRect(10, 190, 431, 71))
        self.s_brake_button.setFont(font3)
        self.s_brake_button.setAutoFillBackground(True)
        self.engineer_box = QGroupBox(self.main)
        self.engineer_box.setObjectName(u"engineer_box")
        self.engineer_box.setGeometry(QRect(750, 60, 241, 231))
        self.used_power_display = QLCDNumber(self.engineer_box)
        self.used_power_display.setObjectName(u"used_power_display")
        self.used_power_display.setGeometry(QRect(110, 40, 64, 31))
        self.used_power_txt = QTextBrowser(self.engineer_box)
        self.used_power_txt.setObjectName(u"used_power_txt")
        self.used_power_txt.setGeometry(QRect(10, 40, 101, 31))
        self.used_power_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.used_power_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kp_txt = QTextBrowser(self.engineer_box)
        self.kp_txt.setObjectName(u"kp_txt")
        self.kp_txt.setGeometry(QRect(10, 90, 101, 31))
        self.kp_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kp_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kp_display = QLCDNumber(self.engineer_box)
        self.kp_display.setObjectName(u"kp_display")
        self.kp_display.setGeometry(QRect(160, 90, 64, 31))
        self.ki_display = QLCDNumber(self.engineer_box)
        self.ki_display.setObjectName(u"ki_display")
        self.ki_display.setGeometry(QRect(160, 160, 64, 31))
        self.ki_slider = QSlider(self.engineer_box)
        self.ki_slider.setObjectName(u"ki_slider")
        self.ki_slider.setGeometry(QRect(50, 190, 151, 22))
        self.ki_slider.setMinimum(1)
        self.ki_slider.setMaximum(24)
        self.ki_slider.setPageStep(8)
        self.ki_slider.setSliderPosition(1)
        self.ki_slider.setOrientation(Qt.Horizontal)
        self.ki_slider.setInvertedAppearance(False)
        self.ki_slider.setTickPosition(QSlider.TicksBelow)
        self.ki_slider.setTickInterval(3)
        self.kp_slider = QSlider(self.engineer_box)
        self.kp_slider.setObjectName(u"kp_slider")
        self.kp_slider.setGeometry(QRect(50, 130, 151, 22))
        self.kp_slider.setMinimum(1)
        self.kp_slider.setMaximum(24)
        self.kp_slider.setPageStep(8)
        self.kp_slider.setSliderPosition(1)
        self.kp_slider.setOrientation(Qt.Horizontal)
        self.kp_slider.setInvertedAppearance(False)
        self.kp_slider.setTickPosition(QSlider.TicksBelow)
        self.kp_slider.setTickInterval(3)
        self.ki_txt_2 = QTextBrowser(self.engineer_box)
        self.ki_txt_2.setObjectName(u"ki_txt_2")
        self.ki_txt_2.setGeometry(QRect(10, 160, 101, 31))
        self.ki_txt_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ki_txt_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.watt_txt = QLabel(self.engineer_box)
        self.watt_txt.setObjectName(u"watt_txt")
        self.watt_txt.setGeometry(QRect(180, 50, 51, 21))
        self.watt_txt.setFont(font2)
        self.door_box = QGroupBox(self.main)
        self.door_box.setObjectName(u"door_box")
        self.door_box.setGeometry(QRect(20, 380, 231, 91))
        self.right_txt = QTextBrowser(self.door_box)
        self.right_txt.setObjectName(u"right_txt")
        self.right_txt.setGeometry(QRect(10, 50, 77, 25))
        self.left_txt = QTextBrowser(self.door_box)
        self.left_txt.setObjectName(u"left_txt")
        self.left_txt.setGeometry(QRect(10, 20, 77, 26))
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.left_txt.setFont(font5)
        self.left_button = QPushButton(self.door_box)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setGeometry(QRect(120, 20, 107, 24))
        self.right_button = QPushButton(self.door_box)
        self.right_button.setObjectName(u"right_button")
        self.right_button.setGeometry(QRect(120, 51, 107, 24))
        self.light_box = QGroupBox(self.main)
        self.light_box.setObjectName(u"light_box")
        self.light_box.setGeometry(QRect(20, 480, 231, 81))
        self.interior_button = QPushButton(self.light_box)
        self.interior_button.setObjectName(u"interior_button")
        self.interior_button.setGeometry(QRect(120, 19, 107, 24))
        self.exterior_button = QPushButton(self.light_box)
        self.exterior_button.setObjectName(u"exterior_button")
        self.exterior_button.setGeometry(QRect(120, 50, 107, 24))
        self.exterior_txt = QTextBrowser(self.light_box)
        self.exterior_txt.setObjectName(u"exterior_txt")
        self.exterior_txt.setGeometry(QRect(20, 50, 77, 25))
        self.interior_txt = QTextBrowser(self.light_box)
        self.interior_txt.setObjectName(u"interior_txt")
        self.interior_txt.setGeometry(QRect(20, 18, 77, 26))
        self.fault_box = QGroupBox(self.main)
        self.fault_box.setObjectName(u"fault_box")
        self.fault_box.setGeometry(QRect(540, 60, 201, 231))
        self.signal_txt = QTextBrowser(self.fault_box)
        self.signal_txt.setObjectName(u"signal_txt")
        self.signal_txt.setGeometry(QRect(20, 30, 111, 52))
        self.signal_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.signal_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.engine_txt = QTextBrowser(self.fault_box)
        self.engine_txt.setObjectName(u"engine_txt")
        self.engine_txt.setGeometry(QRect(20, 100, 111, 52))
        self.engine_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.engine_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.brake_fail_txt = QTextBrowser(self.fault_box)
        self.brake_fail_txt.setObjectName(u"brake_fail_txt")
        self.brake_fail_txt.setGeometry(QRect(20, 170, 111, 52))
        self.brake_fail_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.brake_fail_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.signal_display = QLabel(self.fault_box)
        self.signal_display.setObjectName(u"signal_display")
        self.signal_display.setGeometry(QRect(140, 30, 81, 52))
        self.signal_display.setFont(font4)
        self.engine_display = QLabel(self.fault_box)
        self.engine_display.setObjectName(u"engine_display")
        self.engine_display.setGeometry(QRect(140, 100, 81, 52))
        self.engine_display.setFont(font4)
        self.brake_display = QLabel(self.fault_box)
        self.brake_display.setObjectName(u"brake_display")
        self.brake_display.setGeometry(QRect(140, 170, 81, 52))
        self.brake_display.setFont(font4)
        self.station_box = QGroupBox(self.main)
        self.station_box.setObjectName(u"station_box")
        self.station_box.setGeometry(QRect(20, 220, 491, 151))
        self.authority_display = QLCDNumber(self.station_box)
        self.authority_display.setObjectName(u"authority_display")
        self.authority_display.setGeometry(QRect(150, 20, 64, 36))
        self.station_display = QLabel(self.station_box)
        self.station_display.setObjectName(u"station_display")
        self.station_display.setGeometry(QRect(10, 100, 241, 41))
        self.station_display.setFont(font4)
        self.station_display.setStyleSheet(u"")
        self.location_txt = QTextBrowser(self.station_box)
        self.location_txt.setObjectName(u"location_txt")
        self.location_txt.setGeometry(QRect(10, 60, 241, 41))
        self.location_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.location_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.authority_txt = QTextBrowser(self.station_box)
        self.authority_txt.setObjectName(u"authority_txt")
        self.authority_txt.setGeometry(QRect(10, 18, 127, 36))
        self.station_button = QPushButton(self.station_box)
        self.station_button.setObjectName(u"station_button")
        self.station_button.setGeometry(QRect(280, 70, 191, 71))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        self.station_button.setFont(font6)
        self.ft_txt = QLabel(self.station_box)
        self.ft_txt.setObjectName(u"ft_txt")
        self.ft_txt.setGeometry(QRect(220, 30, 41, 21))
        self.ft_txt.setFont(font2)
        self.stop_box = QGroupBox(self.station_box)
        self.stop_box.setObjectName(u"stop_box")
        self.stop_box.setGeometry(QRect(270, 10, 211, 51))
        self.output_stop_display = QLabel(self.stop_box)
        self.output_stop_display.setObjectName(u"output_stop_display")
        self.output_stop_display.setGeometry(QRect(10, 10, 201, 31))
        self.output_stop_display.setFont(font)
        self.output_stop_display.setStyleSheet(u"")
        self.manual_button = QRadioButton(self.main)
        self.manual_button.setObjectName(u"manual_button")
        self.manual_button.setGeometry(QRect(818, 20, 151, 20))
        font7 = QFont()
        font7.setPointSize(14)
        font7.setBold(True)
        self.manual_button.setFont(font7)
        self.temp_box = QGroupBox(self.main)
        self.temp_box.setObjectName(u"temp_box")
        self.temp_box.setGeometry(QRect(260, 380, 251, 191))
        self.current_temp_display = QLCDNumber(self.temp_box)
        self.current_temp_display.setObjectName(u"current_temp_display")
        self.current_temp_display.setGeometry(QRect(20, 60, 64, 31))
        self.f_txt = QLabel(self.temp_box)
        self.f_txt.setObjectName(u"f_txt")
        self.f_txt.setGeometry(QRect(90, 70, 31, 21))
        self.f_txt.setFont(font4)
        self.temp_slider = QSlider(self.temp_box)
        self.temp_slider.setObjectName(u"temp_slider")
        self.temp_slider.setGeometry(QRect(220, 20, 22, 141))
        self.temp_slider.setOrientation(Qt.Vertical)
        self.f_txt_2 = QLabel(self.temp_box)
        self.f_txt_2.setObjectName(u"f_txt_2")
        self.f_txt_2.setGeometry(QRect(90, 140, 31, 21))
        self.f_txt_2.setFont(font4)

        self.temp_display = QLCDNumber(self.temp_box)
        self.temp_display.setObjectName(u"temp_display")
        self.temp_display.setGeometry(QRect(20, 130, 64, 31))
        self.current_temp_txt = QTextBrowser(self.temp_box)
        self.current_temp_txt.setObjectName(u"current_temp_txt")
        self.current_temp_txt.setGeometry(QRect(20, 20, 181, 31))
        self.current_temp_txt.setFont(font5)
        self.current_temp_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.current_temp_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.temp_txt = QTextBrowser(self.temp_box)
        self.temp_txt.setObjectName(u"temp_txt")
        self.temp_txt.setGeometry(QRect(20, 100, 181, 26))
        self.temp_txt.setFont(font5)
        self.temp_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.temp_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.green_button = QPushButton(self.main)
        self.green_button.setObjectName(u"green_button")
        self.green_button.setGeometry(QRect(20, 10, 131, 41))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setUnderline(False)
        font8.setStrikeOut(False)
        font8.setKerning(True)
        self.green_button.setFont(font8)
        self.green_button.setAutoFillBackground(True)
        self.blue_button = QPushButton(self.main)
        self.blue_button.setObjectName(u"blue_button")
        self.blue_button.setGeometry(QRect(160, 10, 131, 41))
        self.blue_button.setFont(font8)
        self.blue_button.setAutoFillBackground(True)
        self.red_button = QPushButton(self.main)
        self.red_button.setObjectName(u"red_button")
        self.red_button.setGeometry(QRect(300, 10, 131, 41))
        self.red_button.setFont(font8)
        self.red_button.setAutoFillBackground(True)
        self.train_id = QLineEdit(self.main)
        self.train_id.setObjectName(u"train_id")
        self.train_id.setGeometry(QRect(450, 10, 61, 41))

        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 59, 39))

        self.tabWidget.addTab(self.main, "")
        self.testbench = QWidget()
        self.testbench.setObjectName(u"testbench")
        self.tb_pass_brake_box = QGroupBox(self.testbench)
        self.tb_pass_brake_box.setObjectName(u"tb_pass_brake_box")
        self.tb_pass_brake_box.setGeometry(QRect(490, 250, 491, 111))
        self.tb_e_brake_button = QPushButton(self.tb_pass_brake_box)
        self.tb_e_brake_button.setObjectName(u"tb_e_brake_button")
        self.tb_e_brake_button.setGeometry(QRect(20, 20, 431, 71))
        self.tb_e_brake_button.setFont(font3)
        self.tb_e_brake_button.setAutoFillBackground(True)
        self.tb_drive_control_box = QGroupBox(self.testbench)
        self.tb_drive_control_box.setObjectName(u"tb_drive_control_box")
        self.tb_drive_control_box.setGeometry(QRect(740, 90, 241, 151))
        self.tb_current_speed_display = QLCDNumber(self.tb_drive_control_box)
        self.tb_current_speed_display.setObjectName(u"tb_current_speed_display")
        self.tb_current_speed_display.setGeometry(QRect(130, 30, 64, 31))
        self.tb_current_speed_txt = QTextBrowser(self.tb_drive_control_box)
        self.tb_current_speed_txt.setObjectName(u"tb_current_speed_txt")
        self.tb_current_speed_txt.setGeometry(QRect(10, 30, 120, 31))
        self.tb_current_speed_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_current_speed_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_speed_limit_txt = QTextBrowser(self.tb_drive_control_box)
        self.tb_speed_limit_txt.setObjectName(u"tb_speed_limit_txt")
        self.tb_speed_limit_txt.setGeometry(QRect(10, 70, 120, 31))
        self.tb_speed_limit_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_speed_limit_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_suggested_speed_txt = QTextBrowser(self.tb_drive_control_box)
        self.tb_suggested_speed_txt.setObjectName(u"tb_suggested_speed_txt")
        self.tb_suggested_speed_txt.setGeometry(QRect(10, 110, 120, 31))
        self.tb_suggested_speed_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_suggested_speed_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_mph_txt_2 = QLabel(self.tb_drive_control_box)
        self.tb_mph_txt_2.setObjectName(u"tb_mph_txt_2")
        self.tb_mph_txt_2.setGeometry(QRect(200, 80, 41, 21))
        self.tb_mph_txt_2.setFont(font2)
        self.tb_mph_txt_1 = QLabel(self.tb_drive_control_box)
        self.tb_mph_txt_1.setObjectName(u"tb_mph_txt_1")
        self.tb_mph_txt_1.setGeometry(QRect(200, 40, 41, 21))
        self.tb_mph_txt_1.setFont(font2)
        self.tb_mph_txt_3 = QLabel(self.tb_drive_control_box)
        self.tb_mph_txt_3.setObjectName(u"tb_mph_txt_3")
        self.tb_mph_txt_3.setGeometry(QRect(200, 120, 41, 21))
        self.tb_mph_txt_3.setFont(font2)
        self.tb_speed_limit_display = QPlainTextEdit(self.tb_drive_control_box)
        self.tb_speed_limit_display.setObjectName(u"tb_speed_limit_display")
        self.tb_speed_limit_display.setGeometry(QRect(130, 70, 65, 31))
        font9 = QFont()
        font9.setPointSize(15)
        self.tb_speed_limit_display.setFont(font9)
        self.tb_speed_limit_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_speed_limit_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_suggested_speed_display = QPlainTextEdit(self.tb_drive_control_box)
        self.tb_suggested_speed_display.setObjectName(u"tb_suggested_speed_display")
        self.tb_suggested_speed_display.setGeometry(QRect(130, 110, 65, 31))
        self.tb_suggested_speed_display.setFont(font9)
        self.tb_suggested_speed_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_suggested_speed_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_fault_box = QGroupBox(self.testbench)
        self.tb_fault_box.setObjectName(u"tb_fault_box")
        self.tb_fault_box.setGeometry(QRect(490, 10, 241, 231))
        self.tb_signal_txt = QTextBrowser(self.tb_fault_box)
        self.tb_signal_txt.setObjectName(u"tb_signal_txt")
        self.tb_signal_txt.setGeometry(QRect(10, 30, 111, 52))
        self.tb_signal_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_signal_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_engine_txt = QTextBrowser(self.tb_fault_box)
        self.tb_engine_txt.setObjectName(u"tb_engine_txt")
        self.tb_engine_txt.setGeometry(QRect(10, 100, 111, 52))
        self.tb_engine_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_engine_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_brake_txt = QTextBrowser(self.tb_fault_box)
        self.tb_brake_txt.setObjectName(u"tb_brake_txt")
        self.tb_brake_txt.setGeometry(QRect(10, 170, 111, 52))
        self.tb_brake_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_brake_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_signal_display = QCheckBox(self.tb_fault_box)
        self.tb_signal_display.setObjectName(u"tb_signal_display")
        self.tb_signal_display.setGeometry(QRect(130, 40, 101, 31))
        self.tb_signal_display.setFont(font)
        self.tb_engine_display = QCheckBox(self.tb_fault_box)
        self.tb_engine_display.setObjectName(u"tb_engine_display")
        self.tb_engine_display.setGeometry(QRect(130, 110, 101, 31))
        self.tb_engine_display.setFont(font)
        self.tb_brake_display = QCheckBox(self.tb_fault_box)
        self.tb_brake_display.setObjectName(u"tb_brake_display")
        self.tb_brake_display.setGeometry(QRect(130, 180, 101, 31))
        self.tb_brake_display.setFont(font)
        self.tb_engineer_box = QGroupBox(self.testbench)
        self.tb_engineer_box.setObjectName(u"tb_engineer_box")
        self.tb_engineer_box.setGeometry(QRect(740, 10, 241, 71))
        self.tb_power_display = QLCDNumber(self.tb_engineer_box)
        self.tb_power_display.setObjectName(u"tb_power_display")
        self.tb_power_display.setGeometry(QRect(120, 30, 64, 31))
        self.tb_power_txt = QTextBrowser(self.tb_engineer_box)
        self.tb_power_txt.setObjectName(u"tb_power_txt")
        self.tb_power_txt.setGeometry(QRect(10, 30, 101, 31))
        self.tb_power_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_power_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_watt_txt = QLabel(self.tb_engineer_box)
        self.tb_watt_txt.setObjectName(u"tb_watt_txt")
        self.tb_watt_txt.setGeometry(QRect(190, 40, 41, 21))
        self.tb_watt_txt.setFont(font2)
        self.tb_engage_box = QGroupBox(self.testbench)
        self.tb_engage_box.setObjectName(u"tb_engage_box")
        self.tb_engage_box.setGeometry(QRect(10, 10, 471, 561))
        self.tb_temp_box = QGroupBox(self.tb_engage_box)
        self.tb_temp_box.setObjectName(u"tb_temp_box")
        self.tb_temp_box.setGeometry(QRect(10, 20, 251, 101))
        self.tb_temp_display = QLCDNumber(self.tb_temp_box)
        self.tb_temp_display.setObjectName(u"tb_temp_display")
        self.tb_temp_display.setGeometry(QRect(20, 60, 64, 31))
        self.tb_f_txt = QLabel(self.tb_temp_box)
        self.tb_f_txt.setObjectName(u"tb_f_txt")
        self.tb_f_txt.setGeometry(QRect(90, 70, 31, 21))
        self.tb_f_txt.setFont(font4)
        self.tb_current_temp_txt = QTextBrowser(self.tb_temp_box)
        self.tb_current_temp_txt.setObjectName(u"tb_current_temp_txt")
        self.tb_current_temp_txt.setGeometry(QRect(20, 20, 211, 30))
        font10 = QFont()
        font10.setPointSize(13)
        font10.setBold(True)
        self.tb_current_temp_txt.setFont(font10)
        self.tb_current_temp_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_current_temp_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_model_input_box = QGroupBox(self.tb_engage_box)
        self.tb_model_input_box.setObjectName(u"tb_model_input_box")
        self.tb_model_input_box.setEnabled(True)
        self.tb_model_input_box.setGeometry(QRect(10, 130, 251, 221))
        self.tb_acceleration_txt = QTextBrowser(self.tb_model_input_box)
        self.tb_acceleration_txt.setObjectName(u"tb_acceleration_txt")
        self.tb_acceleration_txt.setGeometry(QRect(10, 60, 120, 31))
        self.tb_acceleration_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_acceleration_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_acceleration_display = QPlainTextEdit(self.tb_model_input_box)
        self.tb_acceleration_display.setObjectName(u"tb_acceleration_display")
        self.tb_acceleration_display.setGeometry(QRect(130, 60, 65, 31))
        self.tb_acceleration_display.setFont(font9)
        self.tb_acceleration_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_acceleration_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_ft_per_s_txt = QLabel(self.tb_model_input_box)
        self.tb_ft_per_s_txt.setObjectName(u"tb_ft_per_s_txt")
        self.tb_ft_per_s_txt.setGeometry(QRect(200, 70, 41, 21))
        self.tb_ft_per_s_txt.setFont(font2)
        self.tb_force_txt = QTextBrowser(self.tb_model_input_box)
        self.tb_force_txt.setObjectName(u"tb_force_txt")
        self.tb_force_txt.setGeometry(QRect(10, 20, 120, 31))
        self.tb_force_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_force_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_newtons_txt = QLabel(self.tb_model_input_box)
        self.tb_newtons_txt.setObjectName(u"tb_newtons_txt")
        self.tb_newtons_txt.setGeometry(QRect(200, 30, 41, 21))
        self.tb_newtons_txt.setFont(font2)
        self.tb_elevation_txt = QTextBrowser(self.tb_model_input_box)
        self.tb_elevation_txt.setObjectName(u"tb_elevation_txt")
        self.tb_elevation_txt.setGeometry(QRect(10, 100, 120, 31))
        self.tb_elevation_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_elevation_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_ft_txt_1 = QLabel(self.tb_model_input_box)
        self.tb_ft_txt_1.setObjectName(u"tb_ft_txt_1")
        self.tb_ft_txt_1.setGeometry(QRect(200, 110, 41, 21))
        self.tb_ft_txt_1.setFont(font2)
        self.tb_elevation_display = QPlainTextEdit(self.tb_model_input_box)
        self.tb_elevation_display.setObjectName(u"tb_elevation_display")
        self.tb_elevation_display.setGeometry(QRect(130, 100, 65, 31))
        self.tb_elevation_display.setFont(font9)
        self.tb_elevation_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_elevation_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_slope_txt = QTextBrowser(self.tb_model_input_box)
        self.tb_slope_txt.setObjectName(u"tb_slope_txt")
        self.tb_slope_txt.setGeometry(QRect(10, 140, 120, 31))
        self.tb_slope_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_slope_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_capacity_display = QPlainTextEdit(self.tb_model_input_box)
        self.tb_capacity_display.setObjectName(u"tb_capacity_display")
        self.tb_capacity_display.setGeometry(QRect(130, 180, 65, 31))
        self.tb_capacity_display.setFont(font9)
        self.tb_capacity_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_capacity_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_capacity_txt = QTextBrowser(self.tb_model_input_box)
        self.tb_capacity_txt.setObjectName(u"tb_capacity_txt")
        self.tb_capacity_txt.setGeometry(QRect(10, 180, 120, 31))
        self.tb_capacity_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_capacity_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_degree_txt = QLabel(self.tb_model_input_box)
        self.tb_degree_txt.setObjectName(u"tb_degree_txt")
        self.tb_degree_txt.setGeometry(QRect(200, 150, 51, 21))
        self.tb_degree_txt.setFont(font2)
        self.tb_force_display = QPlainTextEdit(self.tb_model_input_box)
        self.tb_force_display.setObjectName(u"tb_force_display")
        self.tb_force_display.setGeometry(QRect(130, 20, 65, 31))
        self.tb_force_display.setFont(font9)
        self.tb_force_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_force_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_slope_display = QPlainTextEdit(self.tb_model_input_box)
        self.tb_slope_display.setObjectName(u"tb_slope_display")
        self.tb_slope_display.setGeometry(QRect(130, 140, 65, 31))
        self.tb_slope_display.setFont(font9)
        self.tb_slope_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_slope_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_door_box = QGroupBox(self.tb_engage_box)
        self.tb_door_box.setObjectName(u"tb_door_box")
        self.tb_door_box.setGeometry(QRect(270, 20, 191, 101))
        self.tb_right_txt = QTextBrowser(self.tb_door_box)
        self.tb_right_txt.setObjectName(u"tb_right_txt")
        self.tb_right_txt.setGeometry(QRect(10, 60, 91, 31))
        self.tb_right_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_right_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_left_txt = QTextBrowser(self.tb_door_box)
        self.tb_left_txt.setObjectName(u"tb_left_txt")
        self.tb_left_txt.setGeometry(QRect(10, 20, 91, 31))
        self.tb_left_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_left_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_right_display = QLabel(self.tb_door_box)
        self.tb_right_display.setObjectName(u"tb_right_display")
        self.tb_right_display.setGeometry(QRect(110, 60, 71, 31))
        font11 = QFont()
        font11.setPointSize(14)
        self.tb_right_display.setFont(font11)
        self.tb_left_display = QLabel(self.tb_door_box)
        self.tb_left_display.setObjectName(u"tb_left_display")
        self.tb_left_display.setGeometry(QRect(110, 20, 71, 31))
        self.tb_left_display.setFont(font11)
        self.tb_light_box = QGroupBox(self.tb_engage_box)
        self.tb_light_box.setObjectName(u"tb_light_box")
        self.tb_light_box.setGeometry(QRect(270, 130, 191, 101))
        self.tb_exterior_txt = QTextBrowser(self.tb_light_box)
        self.tb_exterior_txt.setObjectName(u"tb_exterior_txt")
        self.tb_exterior_txt.setGeometry(QRect(10, 60, 91, 31))
        self.tb_exterior_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_exterior_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_interior_txt = QTextBrowser(self.tb_light_box)
        self.tb_interior_txt.setObjectName(u"tb_interior_txt")
        self.tb_interior_txt.setGeometry(QRect(10, 20, 91, 31))
        self.tb_interior_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_interior_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_interior_display = QLabel(self.tb_light_box)
        self.tb_interior_display.setObjectName(u"tb_interior_display")
        self.tb_interior_display.setGeometry(QRect(110, 20, 64, 31))
        self.tb_interior_display.setFont(font11)
        self.tb_exterior_display = QLabel(self.tb_light_box)
        self.tb_exterior_display.setObjectName(u"tb_exterior_display")
        self.tb_exterior_display.setGeometry(QRect(110, 60, 71, 31))
        self.tb_exterior_display.setFont(font11)
        self.tb_brake_box = QGroupBox(self.tb_engage_box)
        self.tb_brake_box.setObjectName(u"tb_brake_box")
        self.tb_brake_box.setGeometry(QRect(270, 240, 191, 91))
        self.tb_s_display = QTextBrowser(self.tb_brake_box)
        self.tb_s_display.setObjectName(u"tb_s_display")
        self.tb_s_display.setGeometry(QRect(10, 53, 171, 26))
        self.tb_s_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_s_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_e_display = QTextBrowser(self.tb_brake_box)
        self.tb_e_display.setObjectName(u"tb_e_display")
        self.tb_e_display.setGeometry(QRect(10, 20, 171, 27))
        self.tb_e_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_e_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_load_data_display = QPushButton(self.tb_engage_box)
        self.tb_load_data_display.setObjectName(u"tb_load_data_display")
        self.tb_load_data_display.setEnabled(True)
        self.tb_load_data_display.setGeometry(QRect(10, 420, 451, 131))
        font12 = QFont()
        font12.setPointSize(29)
        font12.setBold(False)
        font12.setItalic(True)
        font12.setUnderline(True)
        self.tb_load_data_display.setFont(font12)
        self.tb_station_control_box = QGroupBox(self.testbench)
        self.tb_station_control_box.setObjectName(u"tb_station_control_box")
        self.tb_station_control_box.setEnabled(True)
        self.tb_station_control_box.setGeometry(QRect(490, 360, 491, 211))
        self.tb_authority_txt = QTextBrowser(self.tb_station_control_box)
        self.tb_authority_txt.setObjectName(u"tb_authority_txt")
        self.tb_authority_txt.setEnabled(True)
        self.tb_authority_txt.setGeometry(QRect(10, 80, 341, 36))
        self.tb_authority_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_authority_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_ft_txt_2 = QLabel(self.tb_station_control_box)
        self.tb_ft_txt_2.setObjectName(u"tb_ft_txt_2")
        self.tb_ft_txt_2.setEnabled(True)
        self.tb_ft_txt_2.setGeometry(QRect(440, 90, 31, 21))
        self.tb_ft_txt_2.setFont(font2)
        self.tb_authority_display = QPlainTextEdit(self.tb_station_control_box)
        self.tb_authority_display.setObjectName(u"tb_authority_display")
        self.tb_authority_display.setEnabled(True)
        self.tb_authority_display.setGeometry(QRect(370, 80, 64, 36))
        self.tb_authority_display.setFont(font9)
        self.tb_authority_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_authority_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_station_txt = QTextBrowser(self.tb_station_control_box)
        self.tb_station_txt.setObjectName(u"tb_station_txt")
        self.tb_station_txt.setEnabled(True)
        self.tb_station_txt.setGeometry(QRect(10, 120, 471, 41))
        self.tb_station_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_station_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_station_display = QPlainTextEdit(self.tb_station_control_box)
        self.tb_station_display.setObjectName(u"tb_station_display")
        self.tb_station_display.setEnabled(True)
        self.tb_station_display.setGeometry(QRect(10, 170, 471, 36))
        self.tb_station_display.setFont(font9)
        self.tb_station_display.setMidLineWidth(0)
        self.tb_station_display.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_station_display.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tb_stop_box = QGroupBox(self.tb_station_control_box)
        self.tb_stop_box.setObjectName(u"tb_stop_box")
        self.tb_stop_box.setGeometry(QRect(20, 20, 221, 51))
        self.tb_stop_display = QLabel(self.tb_stop_box)
        self.tb_stop_display.setObjectName(u"tb_stop_display")
        self.tb_stop_display.setGeometry(QRect(10, 20, 171, 21))
        font13 = QFont()
        font13.setPointSize(12)
        font13.setUnderline(True)
        self.tb_stop_display.setFont(font13)
        self.tb_stop_display.setStyleSheet(u"")
        self.tabWidget.addTab(self.testbench, "")
        self.tb_drive_control_box.raise_()
        self.tb_fault_box.raise_()
        self.tb_engineer_box.raise_()
        self.tb_pass_brake_box.raise_()
        self.tb_engage_box.raise_()
        self.tb_station_control_box.raise_()
        self.header_txt = QLabel(self.centralwidget)
        self.header_txt.setObjectName(u"header_txt")
        self.header_txt.setGeometry(QRect(0, -5, 1031, 71))
        self.header_txt.setAutoFillBackground(True)
        self.header_txt.setPixmap(QPixmap(u"../images/yellow.png"))
        self.header_txt.setScaledContents(True)
        self.logo_txt = QLabel(self.centralwidget)
        self.logo_txt.setObjectName(u"logo_txt")
        self.logo_txt.setGeometry(QRect(10, 10, 71, 51))
        self.logo_txt.setAutoFillBackground(True)
        self.logo_txt.setPixmap(QPixmap(u"../images/AuroraLogo.jpg"))
        self.logo_txt.setScaledContents(True)
        self.simulation_speed_txt = QLabel(self.centralwidget)
        self.simulation_speed_txt.setObjectName(u"simulation_speed_txt")
        self.simulation_speed_txt.setGeometry(QRect(720, 0, 101, 39))
        self.date_time_display = QLabel(self.centralwidget)
        self.date_time_display.setObjectName(u"date_time_display")
        self.date_time_display.setGeometry(QRect(880, 10, 131, 39))
        self.time_slider = QSlider(self.centralwidget)
        self.time_slider.setObjectName(u"time_slider")
        self.time_slider.setGeometry(QRect(700, 30, 151, 22))
        self.time_slider.setMinimum(1)
        self.time_slider.setMaximum(24)
        self.time_slider.setPageStep(8)
        self.time_slider.setSliderPosition(1)
        self.time_slider.setOrientation(Qt.Horizontal)
        self.time_slider.setInvertedAppearance(False)
        self.time_slider.setTickPosition(QSlider.TicksBelow)
        self.time_slider.setTickInterval(3)
        self.pause_button = QPushButton(self.centralwidget)
        self.pause_button.setObjectName(u"pause_button")
        self.pause_button.setGeometry(QRect(600, 10, 75, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.header_txt.raise_()
        self.tabWidget.raise_()
        self.title_txt.raise_()
        self.logo_txt.raise_()
        self.simulation_speed_txt.raise_()
        self.date_time_display.raise_()
        self.time_slider.raise_()
        self.pause_button.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1035, 24))
        self.menuMain = QMenu(self.menubar)
        self.menuMain.setObjectName(u"menuMain")
        self.menuTestBench = QMenu(self.menubar)
        self.menuTestBench.setObjectName(u"menuTestBench")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMain.menuAction())
        self.menubar.addAction(self.menuTestBench.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuTestBench.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_txt.setText(QCoreApplication.translate("MainWindow", u"Train Controller", None))
        self.drive_ctrl_box.setTitle(QCoreApplication.translate("MainWindow", u"Driver Control", None))
        self.current_speed_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:696;\">Current Speed</span></p></body></html>", None))
        self.speed_limit_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:696;\">Speed Limit</span></p></body></html>", None))
        self.input_speed_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:696;\">Manual Speed</span></p></body></html>", None))
        self.suggested_speed_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:696;\">Suggested Speed</span></p></body></html>", None))
        self.mph_txt_3.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.mph_txt_1.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.mph_txt_4.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.mph_txt_2.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.brake_box.setTitle(QCoreApplication.translate("MainWindow", u"Brakes", None))
        self.e_brake_button.setText(QCoreApplication.translate("MainWindow", u"Emergency Brake", None))
        self.engage_box.setTitle(QCoreApplication.translate("MainWindow", u"Engagement", None))
        self.s_brake_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:696;\">Serivice Brake</span></p></body></html>", None))
        self.e_brake_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:696;\">Emergency Brake</span></p></body></html>", None))
        self.s_label_display.setText(QCoreApplication.translate("MainWindow", u"Disengaged", None))
        self.e_label_display.setText(QCoreApplication.translate("MainWindow", u"Disengaged", None))
        self.s_brake_button.setText(QCoreApplication.translate("MainWindow", u"Service Brake", None))
        self.engineer_box.setTitle(QCoreApplication.translate("MainWindow", u"Engineer Control", None))
        self.used_power_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:696;\">Used Power</span></p></body></html>", None))
        self.kp_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Kp</span></p></body></html>", None))
        self.ki_txt_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Ki</span></p></body></html>", None))
        self.watt_txt.setText(QCoreApplication.translate("MainWindow", u"Watts", None))
        self.door_box.setTitle(QCoreApplication.translate("MainWindow", u"Doors", None))
        self.right_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:696;\">Right</span></p></body></html>", None))
        self.left_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:696;\">Left</span></p></body></html>", None))
        self.left_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.right_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.light_box.setTitle(QCoreApplication.translate("MainWindow", u"Lights", None))
        self.interior_button.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.exterior_button.setText(QCoreApplication.translate("MainWindow", u"On", None))
        self.exterior_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:696;\">Exterior</span></p></body></html>", None))
        self.interior_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:696;\">Interior</span></p></body></html>", None))
        self.fault_box.setTitle(QCoreApplication.translate("MainWindow", u"Faults", None))
        self.signal_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600;\">Signal Pick Up Failure</span></p></body></html>", None))
        self.engine_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">Train Engine Failure</span></p></body></html>", None))
        self.brake_fail_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">Brake Failure</span></p></body></html>", None))
        self.signal_display.setText(QCoreApplication.translate("MainWindow", u"Good", None))
        self.engine_display.setText(QCoreApplication.translate("MainWindow", u"Good", None))
        self.brake_display.setText(QCoreApplication.translate("MainWindow", u"Good", None))
        self.station_box.setTitle(QCoreApplication.translate("MainWindow", u"Station Control", None))
        self.station_display.setText(QCoreApplication.translate("MainWindow", u"Pennsylvanian", None))
        self.location_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:696;\">Current Station</span></p></body></html>", None))
        self.authority_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:696;\">Authority</span></p></body></html>", None))
        self.station_button.setText(QCoreApplication.translate("MainWindow", u"Announce Stop", None))
        self.ft_txt.setText(QCoreApplication.translate("MainWindow", u"miles", None))
        self.stop_box.setTitle(QCoreApplication.translate("MainWindow", u"Next Station", None))
        self.output_stop_display.setText(QCoreApplication.translate("MainWindow", u"Pennsylvanian", None))
        self.manual_button.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.temp_box.setTitle(QCoreApplication.translate("MainWindow", u"Cabin Temperature", None))
        self.f_txt.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.f_txt_2.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.current_temp_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:696;\">Current Temperature</span></p></body></html>", None))
        self.temp_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600;\">Set Temperature</span></p></body></html>", None))
        self.green_button.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.blue_button.setText(QCoreApplication.translate("MainWindow", u"Blue Line", None))
        self.red_button.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QCoreApplication.translate("MainWindow", u"Main", None))
        self.tb_pass_brake_box.setTitle(QCoreApplication.translate("MainWindow", u"Passenger Emergency Brake", None))
        self.tb_e_brake_button.setText(QCoreApplication.translate("MainWindow", u"Emergency Brake", None))
        self.tb_drive_control_box.setTitle(QCoreApplication.translate("MainWindow", u"Driver Control", None))
        self.tb_current_speed_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:696;\">Current Speed</span></p></body></html>", None))
        self.tb_speed_limit_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:696;\">Speed Limit</span></p></body></html>", None))
        self.tb_suggested_speed_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:696;\">Suggested Speed</span></p></body></html>", None))
        self.tb_mph_txt_2.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.tb_mph_txt_1.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.tb_mph_txt_3.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.tb_speed_limit_display.setPlainText("")
        self.tb_suggested_speed_display.setPlainText("")
        self.tb_fault_box.setTitle(QCoreApplication.translate("MainWindow", u"Faults", None))
        self.tb_signal_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:600;\">Signal Pick Up Failure</span></p></body></html>", None))
        self.tb_engine_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">Train Engine Failure</span></p></body></html>", None))
        self.tb_brake_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-size:8.25pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">Brake Failure</span></p></body></html>", None))
        self.tb_signal_display.setText(QCoreApplication.translate("MainWindow", u"Signal Fault", None))
        self.tb_engine_display.setText(QCoreApplication.translate("MainWindow", u"Engine Fault", None))
        self.tb_brake_display.setText(QCoreApplication.translate("MainWindow", u"Brake Fault", None))
        self.tb_engineer_box.setTitle(QCoreApplication.translate("MainWindow", u"Engineer Control", None))
        self.tb_power_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:696;\">Used Power</span></p></body></html>", None))
        self.tb_watt_txt.setText(QCoreApplication.translate("MainWindow", u"Watts", None))
        self.tb_engage_box.setTitle(QCoreApplication.translate("MainWindow", u"Engagements", None))
        self.tb_temp_box.setTitle(QCoreApplication.translate("MainWindow", u"Cabin Temperature", None))
        self.tb_f_txt.setText(QCoreApplication.translate("MainWindow", u"\u00b0F", None))
        self.tb_current_temp_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:13pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:696;\">Current Temperature</span></p></body></html>", None))
        self.tb_model_input_box.setTitle(QCoreApplication.translate("MainWindow", u"Train Model Input", None))
        self.tb_acceleration_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Acceleration</span></p></body></html>", None))
        self.tb_acceleration_display.setPlainText("")
        self.tb_ft_per_s_txt.setText(QCoreApplication.translate("MainWindow", u"ft/s^2", None))
        self.tb_force_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Force</span></p></body></html>", None))
        self.tb_newtons_txt.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.tb_elevation_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Elevation</span></p></body></html>", None))
        self.tb_ft_txt_1.setText(QCoreApplication.translate("MainWindow", u"ft", None))
        self.tb_elevation_display.setPlainText("")
        self.tb_slope_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Slope</span></p></body></html>", None))
        self.tb_capacity_display.setPlainText("")
        self.tb_capacity_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Capacity</span></p></body></html>", None))
        self.tb_degree_txt.setText(QCoreApplication.translate("MainWindow", u"degree", None))
        self.tb_force_display.setPlainText("")
        self.tb_slope_display.setPlainText("")
        self.tb_door_box.setTitle(QCoreApplication.translate("MainWindow", u"Door Control", None))
        self.tb_right_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Right</span></p></body></html>", None))
        self.tb_left_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Left</span></p></body></html>", None))
        self.tb_right_display.setText(QCoreApplication.translate("MainWindow", u"Closed", None))
        self.tb_left_display.setText(QCoreApplication.translate("MainWindow", u"Closed", None))
        self.tb_light_box.setTitle(QCoreApplication.translate("MainWindow", u"Light Control", None))
        self.tb_exterior_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Exterior</span></p></body></html>", None))
        self.tb_interior_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:12pt; font-weight:696;\">Interior</span></p></body></html>", None))
        self.tb_interior_display.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.tb_exterior_display.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.tb_brake_box.setTitle(QCoreApplication.translate("MainWindow", u"Brake Engagement", None))
        self.tb_s_display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:696;\">Service Brake</span></p></body></html>", None))
        self.tb_e_display.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:9pt; font-weight:696;\">Emergency Brake</span></p></body></html>", None))
        self.tb_load_data_display.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.tb_station_control_box.setTitle(QCoreApplication.translate("MainWindow", u"Station Control", None))
        self.tb_authority_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:696;\">Authority</span></p></body></html>", None))
        self.tb_ft_txt_2.setText(QCoreApplication.translate("MainWindow", u"mi", None))
        self.tb_authority_display.setPlainText("")
        self.tb_station_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:696;\">Next Station</span></p></body></html>", None))
        self.tb_station_display.setPlainText(QCoreApplication.translate("MainWindow", u"Enter Train Station ", None))
        self.tb_stop_box.setTitle(QCoreApplication.translate("MainWindow", u"Station Output", None))
        self.tb_stop_display.setText(QCoreApplication.translate("MainWindow", u"....", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.testbench), QCoreApplication.translate("MainWindow", u"Testbench", None))
        self.header_txt.setText("")
        self.logo_txt.setText("")
        self.simulation_speed_txt.setText(QCoreApplication.translate("MainWindow", u"Simulation Speed", None))
        self.date_time_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pause_button.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.menuMain.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuTestBench.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

