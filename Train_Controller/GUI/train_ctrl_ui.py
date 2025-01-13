# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'train_ctrl_v15.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QRadioButton, QSizePolicy, QSlider,
    QStatusBar, QTabWidget, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(749, 741)
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
        self.tabWidget.setGeometry(QRect(10, 80, 731, 601))
        self.tabWidget.setMinimumSize(QSize(0, 0))
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.drive_ctrl_box = QGroupBox(self.main)
        self.drive_ctrl_box.setObjectName(u"drive_ctrl_box")
        self.drive_ctrl_box.setGeometry(QRect(10, 60, 441, 151))
        self.input_speed_slider = QSlider(self.drive_ctrl_box)
        self.input_speed_slider.setObjectName(u"input_speed_slider")
        self.input_speed_slider.setGeometry(QRect(230, 70, 151, 22))
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
        self.current_speed_txt.setGeometry(QRect(10, 30, 91, 31))
        self.current_speed_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.current_speed_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.speed_limit_txt = QTextBrowser(self.drive_ctrl_box)
        self.speed_limit_txt.setObjectName(u"speed_limit_txt")
        self.speed_limit_txt.setGeometry(QRect(10, 100, 91, 31))
        self.speed_limit_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.speed_limit_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.input_speed_txt = QTextBrowser(self.drive_ctrl_box)
        self.input_speed_txt.setObjectName(u"input_speed_txt")
        self.input_speed_txt.setGeometry(QRect(220, 30, 111, 31))
        self.input_speed_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.input_speed_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.suggested_speed_txt = QTextBrowser(self.drive_ctrl_box)
        self.suggested_speed_txt.setObjectName(u"suggested_speed_txt")
        self.suggested_speed_txt.setGeometry(QRect(220, 100, 111, 31))
        self.suggested_speed_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.suggested_speed_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.mph_txt_3 = QLabel(self.drive_ctrl_box)
        self.mph_txt_3.setObjectName(u"mph_txt_3")
        self.mph_txt_3.setGeometry(QRect(170, 110, 31, 21))
        font2 = QFont()
        font2.setPointSize(11)
        self.mph_txt_3.setFont(font2)
        self.mph_txt_1 = QLabel(self.drive_ctrl_box)
        self.mph_txt_1.setObjectName(u"mph_txt_1")
        self.mph_txt_1.setGeometry(QRect(170, 40, 31, 21))
        self.mph_txt_1.setFont(font2)
        self.mph_txt_4 = QLabel(self.drive_ctrl_box)
        self.mph_txt_4.setObjectName(u"mph_txt_4")
        self.mph_txt_4.setGeometry(QRect(400, 110, 31, 21))
        self.mph_txt_4.setFont(font2)
        self.mph_txt_2 = QLabel(self.drive_ctrl_box)
        self.mph_txt_2.setObjectName(u"mph_txt_2")
        self.mph_txt_2.setGeometry(QRect(400, 40, 31, 21))
        self.mph_txt_2.setFont(font2)
        self.input_speed_display = QLabel(self.drive_ctrl_box)
        self.input_speed_display.setObjectName(u"input_speed_display")
        self.input_speed_display.setGeometry(QRect(330, 30, 71, 31))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.input_speed_display.setFont(font3)
        self.input_speed_display.setLayoutDirection(Qt.LeftToRight)
        self.input_speed_display.setFrameShape(QFrame.Panel)
        self.input_speed_display.setAlignment(Qt.AlignCenter)
        self.input_speed_display.setMargin(0)
        self.current_speed_display = QLabel(self.drive_ctrl_box)
        self.current_speed_display.setObjectName(u"current_speed_display")
        self.current_speed_display.setGeometry(QRect(100, 30, 71, 31))
        self.current_speed_display.setFont(font3)
        self.current_speed_display.setLayoutDirection(Qt.LeftToRight)
        self.current_speed_display.setFrameShape(QFrame.Panel)
        self.current_speed_display.setAlignment(Qt.AlignCenter)
        self.current_speed_display.setMargin(0)
        self.speed_limit_display = QLabel(self.drive_ctrl_box)
        self.speed_limit_display.setObjectName(u"speed_limit_display")
        self.speed_limit_display.setGeometry(QRect(100, 100, 71, 31))
        self.speed_limit_display.setFont(font3)
        self.speed_limit_display.setLayoutDirection(Qt.LeftToRight)
        self.speed_limit_display.setFrameShape(QFrame.Panel)
        self.speed_limit_display.setAlignment(Qt.AlignCenter)
        self.speed_limit_display.setMargin(0)
        self.suggested_speed_display = QLabel(self.drive_ctrl_box)
        self.suggested_speed_display.setObjectName(u"suggested_speed_display")
        self.suggested_speed_display.setGeometry(QRect(330, 100, 71, 31))
        self.suggested_speed_display.setFont(font3)
        self.suggested_speed_display.setLayoutDirection(Qt.LeftToRight)
        self.suggested_speed_display.setFrameShape(QFrame.Panel)
        self.suggested_speed_display.setAlignment(Qt.AlignCenter)
        self.suggested_speed_display.setMargin(0)
        self.brake_box = QGroupBox(self.main)
        self.brake_box.setObjectName(u"brake_box")
        self.brake_box.setGeometry(QRect(460, 289, 251, 271))
        self.e_brake_button = QPushButton(self.brake_box)
        self.e_brake_button.setObjectName(u"e_brake_button")
        self.e_brake_button.setGeometry(QRect(10, 110, 231, 71))
        font4 = QFont()
        font4.setPointSize(18)
        font4.setBold(True)
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        font4.setKerning(True)
        self.e_brake_button.setFont(font4)
        self.e_brake_button.setAutoFillBackground(True)
        self.engage_box = QGroupBox(self.brake_box)
        self.engage_box.setObjectName(u"engage_box")
        self.engage_box.setGeometry(QRect(10, 20, 231, 91))
        self.s_brake_txt = QTextBrowser(self.engage_box)
        self.s_brake_txt.setObjectName(u"s_brake_txt")
        self.s_brake_txt.setGeometry(QRect(10, 53, 111, 26))
        self.s_brake_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.s_brake_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.e_brake_txt = QTextBrowser(self.engage_box)
        self.e_brake_txt.setObjectName(u"e_brake_txt")
        self.e_brake_txt.setGeometry(QRect(10, 20, 111, 27))
        self.e_brake_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.e_brake_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.s_label_display = QLabel(self.engage_box)
        self.s_label_display.setObjectName(u"s_label_display")
        self.s_label_display.setGeometry(QRect(130, 50, 87, 27))
        font5 = QFont()
        font5.setPointSize(12)
        self.s_label_display.setFont(font5)
        self.e_label_display = QLabel(self.engage_box)
        self.e_label_display.setObjectName(u"e_label_display")
        self.e_label_display.setGeometry(QRect(130, 20, 87, 27))
        self.e_label_display.setFont(font5)
        self.e_label_display.setStyleSheet(u"text-align: center")
        self.s_brake_button = QPushButton(self.brake_box)
        self.s_brake_button.setObjectName(u"s_brake_button")
        self.s_brake_button.setGeometry(QRect(10, 190, 231, 71))
        font6 = QFont()
        font6.setPointSize(22)
        font6.setBold(True)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        font6.setKerning(True)
        self.s_brake_button.setFont(font6)
        self.s_brake_button.setAutoFillBackground(True)
        self.engineer_box = QGroupBox(self.main)
        self.engineer_box.setObjectName(u"engineer_box")
        self.engineer_box.setGeometry(QRect(460, 60, 221, 211))
        self.used_power_txt = QTextBrowser(self.engineer_box)
        self.used_power_txt.setObjectName(u"used_power_txt")
        self.used_power_txt.setGeometry(QRect(10, 20, 71, 31))
        font7 = QFont()
        font7.setPointSize(9)
        self.used_power_txt.setFont(font7)
        self.used_power_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.used_power_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kp_txt = QTextBrowser(self.engineer_box)
        self.kp_txt.setObjectName(u"kp_txt")
        self.kp_txt.setGeometry(QRect(10, 70, 81, 31))
        self.kp_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.kp_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ki_slider = QSlider(self.engineer_box)
        self.ki_slider.setObjectName(u"ki_slider")
        self.ki_slider.setGeometry(QRect(20, 180, 151, 22))
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
        self.kp_slider.setGeometry(QRect(20, 110, 151, 22))
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
        self.ki_txt_2.setGeometry(QRect(10, 140, 81, 31))
        self.ki_txt_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ki_txt_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.watt_txt = QLabel(self.engineer_box)
        self.watt_txt.setObjectName(u"watt_txt")
        self.watt_txt.setGeometry(QRect(200, 30, 16, 21))
        self.watt_txt.setFont(font2)
        self.used_power_display = QLabel(self.engineer_box)
        self.used_power_display.setObjectName(u"used_power_display")
        self.used_power_display.setGeometry(QRect(90, 20, 101, 31))
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        self.used_power_display.setFont(font8)
        self.used_power_display.setLayoutDirection(Qt.LeftToRight)
        self.used_power_display.setFrameShape(QFrame.Panel)
        self.used_power_display.setAlignment(Qt.AlignCenter)
        self.used_power_display.setMargin(0)
        self.kp_display = QLabel(self.engineer_box)
        self.kp_display.setObjectName(u"kp_display")
        self.kp_display.setGeometry(QRect(100, 70, 101, 31))
        self.kp_display.setFont(font8)
        self.kp_display.setLayoutDirection(Qt.LeftToRight)
        self.kp_display.setFrameShape(QFrame.Panel)
        self.kp_display.setAlignment(Qt.AlignCenter)
        self.kp_display.setMargin(0)
        self.ki_display = QLabel(self.engineer_box)
        self.ki_display.setObjectName(u"ki_display")
        self.ki_display.setGeometry(QRect(100, 140, 101, 31))
        self.ki_display.setFont(font8)
        self.ki_display.setLayoutDirection(Qt.LeftToRight)
        self.ki_display.setFrameShape(QFrame.Panel)
        self.ki_display.setAlignment(Qt.AlignCenter)
        self.ki_display.setMargin(0)
        self.door_box = QGroupBox(self.main)
        self.door_box.setObjectName(u"door_box")
        self.door_box.setGeometry(QRect(10, 380, 161, 91))
        self.right_txt = QTextBrowser(self.door_box)
        self.right_txt.setObjectName(u"right_txt")
        self.right_txt.setGeometry(QRect(10, 50, 61, 25))
        self.left_txt = QTextBrowser(self.door_box)
        self.left_txt.setObjectName(u"left_txt")
        self.left_txt.setGeometry(QRect(10, 20, 61, 26))
        font9 = QFont()
        font9.setPointSize(11)
        font9.setBold(True)
        self.left_txt.setFont(font9)
        self.left_button = QPushButton(self.door_box)
        self.left_button.setObjectName(u"left_button")
        self.left_button.setGeometry(QRect(80, 19, 71, 24))
        self.right_button = QPushButton(self.door_box)
        self.right_button.setObjectName(u"right_button")
        self.right_button.setGeometry(QRect(80, 50, 71, 24))
        self.light_box = QGroupBox(self.main)
        self.light_box.setObjectName(u"light_box")
        self.light_box.setGeometry(QRect(10, 480, 161, 81))
        self.interior_button = QPushButton(self.light_box)
        self.interior_button.setObjectName(u"interior_button")
        self.interior_button.setGeometry(QRect(90, 20, 61, 24))
        self.exterior_button = QPushButton(self.light_box)
        self.exterior_button.setObjectName(u"exterior_button")
        self.exterior_button.setGeometry(QRect(90, 51, 61, 24))
        self.exterior_txt = QTextBrowser(self.light_box)
        self.exterior_txt.setObjectName(u"exterior_txt")
        self.exterior_txt.setGeometry(QRect(10, 50, 71, 25))
        self.interior_txt = QTextBrowser(self.light_box)
        self.interior_txt.setObjectName(u"interior_txt")
        self.interior_txt.setGeometry(QRect(10, 18, 71, 26))
        self.fault_box = QGroupBox(self.main)
        self.fault_box.setObjectName(u"fault_box")
        self.fault_box.setGeometry(QRect(340, 380, 111, 181))
        self.signal_txt = QTextBrowser(self.fault_box)
        self.signal_txt.setObjectName(u"signal_txt")
        self.signal_txt.setGeometry(QRect(10, 20, 91, 41))
        self.signal_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.signal_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.engine_txt = QTextBrowser(self.fault_box)
        self.engine_txt.setObjectName(u"engine_txt")
        self.engine_txt.setGeometry(QRect(10, 70, 91, 41))
        self.engine_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.engine_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.brake_fail_txt = QTextBrowser(self.fault_box)
        self.brake_fail_txt.setObjectName(u"brake_fail_txt")
        self.brake_fail_txt.setGeometry(QRect(10, 120, 91, 41))
        self.brake_fail_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.brake_fail_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.station_box = QGroupBox(self.main)
        self.station_box.setObjectName(u"station_box")
        self.station_box.setGeometry(QRect(10, 220, 441, 151))
        self.location_txt = QTextBrowser(self.station_box)
        self.location_txt.setObjectName(u"location_txt")
        self.location_txt.setGeometry(QRect(10, 60, 211, 41))
        self.location_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.location_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.authority_txt = QTextBrowser(self.station_box)
        self.authority_txt.setObjectName(u"authority_txt")
        self.authority_txt.setGeometry(QRect(10, 18, 91, 36))
        self.station_button = QPushButton(self.station_box)
        self.station_button.setObjectName(u"station_button")
        self.station_button.setGeometry(QRect(230, 70, 191, 71))
        self.station_button.setFont(font8)
        self.ft_txt = QLabel(self.station_box)
        self.ft_txt.setObjectName(u"ft_txt")
        self.ft_txt.setGeometry(QRect(210, 30, 31, 21))
        self.ft_txt.setFont(font2)
        self.stop_box = QGroupBox(self.station_box)
        self.stop_box.setObjectName(u"stop_box")
        self.stop_box.setGeometry(QRect(230, 10, 201, 61))
        self.output_stop_display = QLabel(self.stop_box)
        self.output_stop_display.setObjectName(u"output_stop_display")
        self.output_stop_display.setGeometry(QRect(10, 20, 181, 31))
        self.output_stop_display.setFont(font8)
        self.output_stop_display.setLayoutDirection(Qt.LeftToRight)
        self.output_stop_display.setFrameShape(QFrame.Panel)
        self.output_stop_display.setAlignment(Qt.AlignCenter)
        self.output_stop_display.setMargin(0)
        self.authority_display = QLabel(self.station_box)
        self.authority_display.setObjectName(u"authority_display")
        self.authority_display.setGeometry(QRect(100, 20, 101, 31))
        self.authority_display.setFont(font8)
        self.authority_display.setLayoutDirection(Qt.RightToLeft)
        self.authority_display.setFrameShape(QFrame.Panel)
        self.authority_display.setFrameShadow(QFrame.Plain)
        self.authority_display.setAlignment(Qt.AlignCenter)
        self.authority_display.setMargin(0)
        self.station_display = QLabel(self.station_box)
        self.station_display.setObjectName(u"station_display")
        self.station_display.setGeometry(QRect(10, 110, 211, 31))
        self.station_display.setFont(font8)
        self.station_display.setLayoutDirection(Qt.LeftToRight)
        self.station_display.setFrameShape(QFrame.Panel)
        self.station_display.setAlignment(Qt.AlignCenter)
        self.station_display.setMargin(0)
        self.manual_button = QRadioButton(self.main)
        self.manual_button.setObjectName(u"manual_button")
        self.manual_button.setGeometry(QRect(610, 20, 101, 20))
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(True)
        self.manual_button.setFont(font10)
        self.temp_box = QGroupBox(self.main)
        self.temp_box.setObjectName(u"temp_box")
        self.temp_box.setGeometry(QRect(180, 380, 151, 181))
        self.f_txt = QLabel(self.temp_box)
        self.f_txt.setObjectName(u"f_txt")
        self.f_txt.setGeometry(QRect(80, 80, 31, 21))
        self.f_txt.setFont(font5)
        self.temp_slider = QSlider(self.temp_box)
        self.temp_slider.setObjectName(u"temp_slider")
        self.temp_slider.setGeometry(QRect(130, 20, 22, 141))
        self.temp_slider.setOrientation(Qt.Vertical)
        self.f_txt_2 = QLabel(self.temp_box)
        self.f_txt_2.setObjectName(u"f_txt_2")
        self.f_txt_2.setGeometry(QRect(80, 150, 31, 21))
        self.f_txt_2.setFont(font5)
        self.current_temp_txt = QTextBrowser(self.temp_box)
        self.current_temp_txt.setObjectName(u"current_temp_txt")
        self.current_temp_txt.setGeometry(QRect(10, 20, 111, 41))
        self.current_temp_txt.setFont(font9)
        self.current_temp_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.current_temp_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.set_temp_txt = QTextBrowser(self.temp_box)
        self.set_temp_txt.setObjectName(u"set_temp_txt")
        self.set_temp_txt.setGeometry(QRect(10, 110, 111, 26))
        self.set_temp_txt.setFont(font9)
        self.set_temp_txt.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.set_temp_txt.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.set_temp_display = QLabel(self.temp_box)
        self.set_temp_display.setObjectName(u"set_temp_display")
        self.set_temp_display.setGeometry(QRect(10, 140, 71, 31))
        self.set_temp_display.setFont(font3)
        self.set_temp_display.setLayoutDirection(Qt.LeftToRight)
        self.set_temp_display.setFrameShape(QFrame.Panel)
        self.set_temp_display.setAlignment(Qt.AlignCenter)
        self.set_temp_display.setMargin(0)
        self.current_temp_display = QLabel(self.temp_box)
        self.current_temp_display.setObjectName(u"current_temp_display")
        self.current_temp_display.setGeometry(QRect(10, 70, 71, 31))
        self.current_temp_display.setFont(font3)
        self.current_temp_display.setLayoutDirection(Qt.LeftToRight)
        self.current_temp_display.setFrameShape(QFrame.Panel)
        self.current_temp_display.setAlignment(Qt.AlignCenter)
        self.current_temp_display.setMargin(0)
        self.green_button = QPushButton(self.main)
        self.green_button.setObjectName(u"green_button")
        self.green_button.setGeometry(QRect(20, 10, 131, 41))
        font11 = QFont()
        font11.setPointSize(10)
        font11.setBold(True)
        font11.setUnderline(False)
        font11.setStrikeOut(False)
        font11.setKerning(True)
        self.green_button.setFont(font11)
        self.green_button.setAutoFillBackground(True)
        self.red_button = QPushButton(self.main)
        self.red_button.setObjectName(u"red_button")
        self.red_button.setGeometry(QRect(160, 10, 131, 41))
        self.red_button.setFont(font11)
        self.red_button.setAutoFillBackground(True)
        self.train_id = QLineEdit(self.main)
        self.train_id.setObjectName(u"train_id")
        self.train_id.setGeometry(QRect(300, 20, 81, 31))
        self.tabWidget.addTab(self.main, "")
        self.header_txt = QLabel(self.centralwidget)
        self.header_txt.setObjectName(u"header_txt")
        self.header_txt.setGeometry(QRect(0, -5, 751, 71))
        self.header_txt.setAutoFillBackground(True)
        self.header_txt.setPixmap(QPixmap(u"../../../../ECE 1140/Train Code/ECE1140.9/Train_Controller/images/yellow.png"))
        self.header_txt.setScaledContents(True)
        self.logo_txt = QLabel(self.centralwidget)
        self.logo_txt.setObjectName(u"logo_txt")
        self.logo_txt.setGeometry(QRect(10, 10, 71, 51))
        self.logo_txt.setAutoFillBackground(True)
        self.logo_txt.setPixmap(QPixmap(u"../../../../ECE 1140/Train Code/ECE1140.9/Train_Controller/images/AuroraLogo.jpg"))
        self.logo_txt.setScaledContents(True)
        self.simulation_speed_txt = QLabel(self.centralwidget)
        self.simulation_speed_txt.setObjectName(u"simulation_speed_txt")
        self.simulation_speed_txt.setGeometry(QRect(420, 0, 101, 39))
        self.date_time_display = QLabel(self.centralwidget)
        self.date_time_display.setObjectName(u"date_time_display")
        self.date_time_display.setGeometry(QRect(560, 10, 151, 39))
        self.time_slider = QSlider(self.centralwidget)
        self.time_slider.setObjectName(u"time_slider")
        self.time_slider.setGeometry(QRect(400, 30, 151, 22))
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
        self.pause_button.setGeometry(QRect(300, 10, 75, 41))
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
        self.menubar.setGeometry(QRect(0, 0, 749, 24))
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:696;\">Current Speed</span></p></body></html>", None))
        self.speed_limit_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:696;\">Speed Limit</span></p></body></html>", None))
        self.input_speed_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:696;\">Command Speed</span></p></body></html>", None))
        self.suggested_speed_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:696;\">Suggested Speed</span></p></body></html>", None))
        self.mph_txt_3.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.mph_txt_1.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.mph_txt_4.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.mph_txt_2.setText(QCoreApplication.translate("MainWindow", u"mph", None))
        self.input_speed_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.current_speed_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.speed_limit_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.suggested_speed_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:696;\">Serivice Brake</span></p></body></html>", None))
        self.e_brake_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:696;\">Emergency Brake</span></p></body></html>", None))
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
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:696;\">Power</span></p></body></html>", None))
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
        self.watt_txt.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.used_power_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.kp_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.ki_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">Signal Pick Up Failure</span></p></body></html>", None))
        self.engine_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-weight:600;\">Train Engine Failure</span></p></body></html>", None))
        self.brake_fail_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:11pt; font-weight:600;\">Brake Failure</span></p></body></html>", None))
        self.station_box.setTitle(QCoreApplication.translate("MainWindow", u"Station Control", None))
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:696;\">Authority</span></p></body></html>", None))
        self.station_button.setText(QCoreApplication.translate("MainWindow", u"Announce Stop", None))
        self.ft_txt.setText(QCoreApplication.translate("MainWindow", u"ft", None))
        self.stop_box.setTitle(QCoreApplication.translate("MainWindow", u"Next Station", None))
        self.output_stop_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.authority_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.station_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
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
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:696;\">Current Temperature</span></p></body></html>", None))
        self.set_temp_txt.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:11pt; font-weight:700; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:10pt; font-weight:600;\">Set Temperature</span></p></body></html>", None))
        self.set_temp_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.current_temp_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.green_button.setText(QCoreApplication.translate("MainWindow", u"Green Line", None))
        self.red_button.setText(QCoreApplication.translate("MainWindow", u"Red Line", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.main), QCoreApplication.translate("MainWindow", u"Main", None))
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

