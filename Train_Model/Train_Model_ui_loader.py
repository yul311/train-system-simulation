
import sys
import os
import math
import random

from Train_Model.services.conversion import *
import Train_Model.Train_Model_ui as ui
from Train_Model.classes.Train_Model import TrainModel
from datetime import datetime
from Main.simulation_time import sim

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QTimer)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextBrowser, QVBoxLayout, QWidget)
from PySide6 import QtWidgets

from Track_Model.Controller import greenLine, redLine

class TrainModelUI(QMainWindow):

    time: QTimer
    currentTime: int = 0
    
    def __init__(self): #, tm: TrainModel):
        super().__init__()
        self.ui = ui.Ui_TrainModel()
        self.ui.setupUi(self)
        self.selected_train = None
        self.train_id = None
        
        icon = QIcon(os.path.join(os.getcwd(),"Other","AuroraLogo.jpg"))
        self.setWindowIcon(icon)
        self.setWindowTitle("Train Model")

        self.green_select = False
        self.red_select = False

        self.timer = QTimer()
        self.timer.timeout.connect(self.__timeout__)
        self.timer.start(100)

        self.adtimer = QTimer()
        self.adtimer.timeout.connect(self.update_ad)
        self.adtimer.start(5000)

        self.color_ui()
        self.table_setup()
        self.connect_buttons()

        #time
        #self.ui.label_2.setText(self.time.strftime("%d/%m/%y %H:%M:%S"))

        #setting images
        IMAGE_PATH = os.path.join(os.getcwd(),"Train_Model", "images","AuroraLogo.png")
        self.ui.AuroraIMG.setPixmap(QPixmap(IMAGE_PATH))

        IMAGE_PATH_AD1 = os.path.join(os.getcwd(),"Train_Model", "images","Ad_1.png")
        self.ui.Advertisment.setPixmap(QPixmap(IMAGE_PATH_AD1))

    def __timeout__(self):
        time = sim.get_curr_string()
        self.update_clock(time)

    #color things on my ui
    def color_ui(self):
        self.ui.EmergencyButton.setStyleSheet("background-color: red;")
        self.ui.LogoBrower.setStyleSheet("background-color: #F2CD6D;")
        self.ui.header_widget.setAutoFillBackground(True)
        p = self.ui.header_widget.palette()
        p.setColor(self.ui.header_widget.backgroundRole(), QColor(242, 205, 109, 255))
        self.ui.header_widget.setPalette(p)

    def table_setup(self):
        header = self.ui.PhysicalData.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.PhysicalData.setHorizontalHeader(header)

        header = self.ui.LightsState.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.LightsState.setHorizontalHeader(header)


    #connecting buttons
    def connect_buttons(self):
        #self.ui.TestTrack_Model_Input.clicked.connect(self.updateOutputs)
        #self.ui.TestTrain_Controller_Input.clicked.connect(self.updateOutputs)
        self.ui.TestTrainEngine.clicked.connect(self.trigger_engine_failure)
        #self.ui.TestTrainEngine_tb.clicked.connect(self.trigger_engine_failure)
        self.ui.TestBrake.clicked.connect(self.trigger_brake_failure)
        #self.ui.TestBrake_tb.clicked.connect(self.trigger_brake_failure)
        self.ui.TestSignalPickup.clicked.connect(self.trigger_signal_pickup_failure)
        #self.ui.TestSignalPickup_tb.clicked.connect(self.trigger_signal_pickup_failure)
        self.ui.resetButton.clicked.connect(self.reset_faults)
        #self.ui.resetButton_tb.clicked.connect(self.reset_faults)
        self.ui.EmergencyButton.clicked.connect(self.set_emergency_brake)
        self.ui.greenButton.clicked.connect(self.update_train_green)
        self.ui.redButton.clicked.connect(self.update_train_red)
        self.ui.pauseSim.clicked.connect(self.pauseSim)
        self.ui.simSlider.valueChanged.connect(self.change_sim_speed)

    #clock function

    def update_clock(self, time: str):
        self.ui.timeLabel.setText(QCoreApplication.translate("MainWindow", u"Simulation Time:\n"f"{time}", None))

        if (self.selected_train):
            self.update_announcements()
            self.update_brake_states()
            self.update_door_states()
            self.update_light_states()
            self.update_train_info()
            self.update_physical_data()

    def pauseSim(self):
        if sim.running:
            sim.stop()
        else: 
            sim.start()

    def change_sim_speed(self, value: int):
        sim.set_sim_speed(value)

    def trigger_engine_failure(self):
            try:
                if (self.selected_train != None or self.selected_train != 0):
                    self.selected_train.model.failures.set_engine_failure()
                    self.ui.FailureModes.setItem(0,0,QTableWidgetItem(str("Failing")))
                    #self.ui.FailureModes_tb.setItem(0,0,QTableWidgetItem(str("Failing")))
                    self.selected_train.model.ctrl_link.send_failures(self.selected_train.model.failures.get_brake_failure_state(), self.selected_train.model.failures.get_engine_failure_state(), self.selected_train.model.failures.get_signal_pickup_failure_state())
                    self.update_failure_states()
                else:
                    Exception ("Train does not exist")
            except AttributeError:
                print("Train does not exist")
            except KeyError:
                print("Train does not exist")

    def trigger_brake_failure(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                self.selected_train.model.failures.set_brake_failure()
                self.selected_train.model.ctrl_link.send_failures(self.selected_train.model.failures.get_brake_failure_state(), self.selected_train.model.failures.get_engine_failure_state(), self.selected_train.model.failures.get_signal_pickup_failure_state())
                self.selected_train.model.brakes.disable_brakes()
                self.ui.FailureModes.setItem(0,1,QTableWidgetItem(str("Failing")))
                #self.ui.FailureModes_tb.setItem(0,1,QTableWidgetItem(str("Failing")))
                self.update_failure_states()
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist")
        
    def trigger_signal_pickup_failure(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                self.selected_train.model.failures.set_signal_pickup_failure()
                self.ui.FailureModes.setItem(0,2,QTableWidgetItem(str("Failing")))
                #self.ui.FailureModes_tb.setItem(0,2,QTableWidgetItem(str("Failing")))
                self.selected_train.model.ctrl_link.send_failures(self.selected_train.model.failures.get_brake_failure_state(), self.selected_train.model.failures.get_engine_failure_state(), self.selected_train.model.failures.get_signal_pickup_failure_state())
                self.update_failure_states()
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist")

    def reset_faults(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                self.selected_train.model.failures.reset_faults()
                self.selected_train.model.ctrl_link.send_failures(self.selected_train.model.failures.get_brake_failure_state(), self.selected_train.model.failures.get_engine_failure_state(), self.selected_train.model.failures.get_signal_pickup_failure_state())
                self.update_failure_states()
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist")

    def set_emergency_brake(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                if(self.selected_train.model.failures.get_brake_failure_state() == False):
                    self.selected_train.model.brakes.set_emergency_brake(True)
                    self.selected_train.model.ctrl_link.send_passenger_emergency_brake(True)
                    #self.selected_train.model.ctrl_link.send_passenger_emergency_brake(self.selected_train.model.brakes.get_emergency_brake_state())
                    self.ui.BrakeState.setItem(0,0,QTableWidgetItem(str("Engaged")))
                    #self.ui.BrakeState_tb.setItem(0,0,QTableWidgetItem(str("Engaged")))
                else:
                    raise Exception ("Train brake failure is raised")
            else:
                Exception ("Train does not exist 1")
        except AttributeError:
            print("Train does not exist 2")
        except KeyError:
            print("Train does not exist 3")
         

    def update_train_green(self):
        if (self.ui.TrainIdIn.text() != ''):
            self.train_id = int(self.ui.TrainIdIn.text())
            try:
                self.selected_train = greenLine.trains[self.train_id]
                self.green_select = True
                self.red_select = False
                self.ui.TrainLine.setText("Train Line: Green")
                self.ui.TrainID.setText("Train ID: "+ str(self.train_id))
            except KeyError:
                print("Train being selected does not exist on green line")

    def update_train_red(self):
        if (self.ui.TrainIdIn.text() != ''):
            self.train_id = int(self.ui.TrainIdIn.text())

            try:
                self.selected_train = redLine.trains[self.train_id]
                self.red_select = True
                self.green_select = False
                self.blue_select = False
                self.ui.TrainLine.setText("Train Line: Red")
                self.ui.TrainID.setText("Train ID: "+ str(self.train_id))
            except KeyError:
                print("Train being selected does not exist on red line")
            
    def update_train_blue(self):
        if (self.ui.TrainIdIn.text() != ''):
            self.train_id = int(self.ui.TrainIdIn.text())
            try:
                self.selected_train = blueLine.trains[self.train_id]
                self.blue_select = True
                self.red_select = False
                self.green_select = False
                self.ui.TrainLine.setText("Train Line: Blue")
                self.ui.TrainID.setText("Train ID: "+ str(self.train_id))
            except KeyError:
                print("Train being selected does not exist on blue line")
           
    def update_physical_data(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                # convert all shits to imperial
                #authority maybe i should remove authority and not display it
                auth = str(str(meters_feet(self.selected_train.model.authority))+" ft")
                #self.ui.PhysicalData_tb.setItem(0,0,QTableWidgetItem(str(auth)))
                self.ui.PhysicalData.setItem(0,0,QTableWidgetItem(str(auth)))

                #power
                power_zero_condition = self.selected_train.model.failures.get_brake_failure_state() or self.selected_train.model.failures.get_engine_failure_state() or self.selected_train.model.failures.get_signal_pickup_failure_state() or self.selected_train.model.brakes.get_service_brake_state() or self.selected_train.model.brakes.get_emergency_brake_state()
                if(power_zero_condition == True):
                    power_display = str("0 W")
                    #self.ui.PhysicalData_tb.setItem(0,0,QTableWidgetItem(str(power_display)))
                    self.ui.PhysicalData.setItem(0,0,QTableWidgetItem(str(power_display)))
                else:
                    power_round = round(self.selected_train.model.power_command, 2)
                    power_display = str(str(power_round) + " W")
                    #self.ui.PhysicalData_tb.setItem(0,0,QTableWidgetItem(str(power_display)))
                    self.ui.PhysicalData.setItem(0,0,QTableWidgetItem(str(power_display)))

                #current speed
                speed_display = str(str(meter_sec_miles_hour(self.selected_train.model.current_speed)) + " mph")
                #self.ui.PhysicalData_tb.setItem(0,1,QTableWidgetItem(str(speed_display)))
                self.ui.PhysicalData.setItem(0,1,QTableWidgetItem(str(speed_display)))

                #commanded speed 
                com_speed_display = str(str(meter_sec_miles_hour(self.selected_train.model.commanded_speed)) + " mph")
                #self.ui.PhysicalData_tb.setItem(0,2,QTableWidgetItem(str(com_speed_display)))
                self.ui.PhysicalData.setItem(0,2,QTableWidgetItem(str(com_speed_display)))

                #speed limit
                speed_limit_display = str(str(meter_sec_miles_hour(self.selected_train.model.speed_limit)) + " mph")
                #self.ui.PhysicalData_tb.setItem(0,3,QTableWidgetItem(str(speed_limit_display)))
                self.ui.PhysicalData.setItem(0,3,QTableWidgetItem(str(speed_limit_display)))

                #acceleration
                acc_display = str(str(mpssquared_fpssquared(self.selected_train.model.acceleration))+" ft/s^2")
                #self.ui.PhysicalData_tb.setItem(0,4,QTableWidgetItem(str(acc_display)))
                self.ui.PhysicalData.setItem(0,4,QTableWidgetItem(str(acc_display)))

                #force 
                force_display = str(str(newton_poundforce(self.selected_train.model.force)) + " lb")
                #self.ui.PhysicalData_tb.setItem(0,5,QTableWidgetItem(str(force_display)))
                self.ui.PhysicalData.setItem(0,5,QTableWidgetItem(str(force_display)))

                #temperature
                #temp_display = str(str(celcius_fahrenheit(self.selected_train.model.current_temperature)) + " °F")
                #self.ui.PhysicalData_tb.setItem(0,8, QTableWidgetItem(str(temp_display)))

                #block grade
                block_display = str(str(str(self.selected_train.model.block_Grade)+" %"))
                self.ui.PhysicalData.setItem(0,6,QTableWidgetItem(str(block_display)))
                #self.ui.PhysicalData_tb.setItem(0,6,QTableWidgetItem(str(block_display)))

                #authority
                auth_display = str(str(meters_feet(self.selected_train.model.authority))+" ft")
                self.ui.PhysicalData.setItem(0,7,QTableWidgetItem(str(auth_display)))

                #suggested speed
                suggested_speed_display = str(str(meter_sec_miles_hour(self.selected_train.model.suggested_speed))+" mph")
                self.ui.PhysicalData.setItem(0,8,QTableWidgetItem(str(suggested_speed_display)))
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist")
        

    def update_light_states(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                if(self.selected_train.model.lights.get_internal_lights_state() == True):
                    #self.ui.LightsState_tb.setItem(0,0,QTableWidgetItem(str("On")))
                    self.ui.LightsState.setItem(0,0,QTableWidgetItem(str("On")))
                else:
                    #self.ui.LightsState_tb.setItem(0,0,QTableWidgetItem(str("Off")))
                    self.ui.LightsState.setItem(0,0,QTableWidgetItem(str("Off")))
                if(self.selected_train.model.lights.get_external_lights_state() == True):
                    #self.ui.LightsState_tb.setItem(0,1,QTableWidgetItem(str("On")))
                    self.ui.LightsState.setItem(0,1,QTableWidgetItem(str("On")))
                else:
                    #self.ui.LightsState_tb.setItem(0,1,QTableWidgetItem(str("Off")))
                    self.ui.LightsState.setItem(0,1,QTableWidgetItem(str("Off")))
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist")

    def update_door_states(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                if(self.selected_train.model.doors.get_left_door_state()==True):
                    #self.ui.DoorState_tb.setItem(0,1,QTableWidgetItem(str("Open")))
                    self.ui.DoorState.setItem(0,1,QTableWidgetItem(str("Open")))
                else:
                    #self.ui.DoorState_tb.setItem(0,1,QTableWidgetItem(str("Closed")))
                    self.ui.DoorState.setItem(0,1,QTableWidgetItem(str("Closed")))

                if(self.selected_train.model.doors.get_right_door_state()==True):
                    self.ui.DoorState.setItem(0,0,QTableWidgetItem(str("Open")))
                    #self.ui.DoorState_tb.setItem(0,0,QTableWidgetItem(str("Open")))
                else:
                    self.ui.DoorState.setItem(0,0,QTableWidgetItem(str("Closed")))
                    #self.ui.DoorState_tb.setItem(0,0,QTableWidgetItem(str("Closed")))
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist")

    def update_brake_states(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                if(self.selected_train.model.brakes.get_emergency_brake_state()==True):
                    #self.ui.BrakeState_tb.setItem(0,0,QTableWidgetItem(str("Engaged")))
                    self.ui.BrakeState.setItem(0,0,QTableWidgetItem(str("Engaged")))
                else:
                    #self.ui.BrakeState_tb.setItem(0,0,QTableWidgetItem(str("Disengaged")))
                    self.ui.BrakeState.setItem(0,0,QTableWidgetItem(str("Disengaged")))
                    
                if(self.selected_train.model.brakes.get_service_brake_state()==True):
                    #self.ui.BrakeState_tb.setItem(0,1,QTableWidgetItem(str("Engaged")))
                    self.ui.BrakeState.setItem(0,1,QTableWidgetItem(str("Engaged")))
                else:
                    #self.ui.BrakeState_tb.setItem(0,1,QTableWidgetItem(str("Disengaged")))
                    self.ui.BrakeState.setItem(0,1,QTableWidgetItem(str("Disengaged")))
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist")

    def update_failure_states(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                if(self.selected_train.model.failures.get_engine_failure_state() == True):
                    self.ui.FailureModes.setItem(0,0,QTableWidgetItem(str("Failing")))
                    #self.ui.FailureModes_tb.setItem(0,0,QTableWidgetItem(str("Failing")))
                else:
                    self.ui.FailureModes.setItem(0,0,QTableWidgetItem(str("Functioning")))
                    #self.ui.FailureModes_tb.setItem(0,0,QTableWidgetItem(str("Functioning")))

                if(self.selected_train.model.failures.get_brake_failure_state() == True):
                    self.ui.FailureModes.setItem(0,1,QTableWidgetItem(str("Failing")))
                    #self.ui.FailureModes_tb.setItem(0,1,QTableWidgetItem(str("Failing")))
                else:
                    self.ui.FailureModes.setItem(0,1,QTableWidgetItem(str("Functioning")))
                    #self.ui.FailureModes_tb.setItem(0,1,QTableWidgetItem(str("Functioning")))

                if(self.selected_train.model.failures.get_signal_pickup_failure_state() == True):
                    self.ui.FailureModes.setItem(0,2,QTableWidgetItem(str("Failing")))
                    #self.ui.FailureModes_tb.setItem(0,2,QTableWidgetItem(str("Failing")))
                else:
                    self.ui.FailureModes.setItem(0,2,QTableWidgetItem(str("Functioning")))
                    #self.ui.FailureModes_tb.setItem(0,2,QTableWidgetItem(str("Functioning")))
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist")

    def update_announcements(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                #self.ui.Announcements_tb.setText("Announcements: "+ self.selected_train.model.announcements)
                self.ui.Announcements.setText("Announcements: "+ self.selected_train.model.announcements)
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist brake")

    def update_train_info(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                self.ui.TrainSize.setItem(0,0, QTableWidgetItem(str(self.selected_train.model.num_crew)))
                self.ui.TrainSize.setItem(0,1, QTableWidgetItem(str(self.selected_train.model.num_passenger)))
                temp_display = str(str(celcius_fahrenheit(self.selected_train.model.current_temperature)) + " °F")
                self.ui.TrainSize.setItem(0,2, QTableWidgetItem(str(temp_display)))
                weight_display = str(str(kilograms_pounds(self.selected_train.model.total_mass)) +" lb")
                self.ui.TrainSize.setItem(0,3, QTableWidgetItem(str(weight_display)))
                
                #lenght, weight, height
                #self.ui.TrainSize.setItem(0,4, QTableWidgetItem(str(str(self.selected_train.total_mass)+" ft")))
                #self.ui.TrainSize.setItem(0,5, QTableWidgetItem(str(str(self.selected_train.total_mass)+" ft")))
                #self.ui.TrainSize.setItem(0,6, QTableWidgetItem(str(str(self.selected_train.total_mass)+" ft")))
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist brake")

    def update_ad(self):
        # Displaying and updating ad
        IMAGE_PATH_AD1 = os.path.join(os.getcwd(),"Train_Model", "images","Ad_1.png")
        IMAGE_PATH_AD2 = os.path.join(os.getcwd(),"Train_Model", "images","Ad_2.png")
        IMAGE_PATH_AD3 = os.path.join(os.getcwd(),"Train_Model", "images","Ad_3.png")

        adchoose = random.randint(1,4)
        if adchoose == 1:
            self.ui.Advertisment.setPixmap(QPixmap(IMAGE_PATH_AD1))
        elif adchoose == 2:
            self.ui.Advertisment.setPixmap(QPixmap(IMAGE_PATH_AD2))
        elif adchoose == 3:
            self.ui.Advertisment.setPixmap(QPixmap(IMAGE_PATH_AD3))

    def updateOutputs(self):
        try:
            if (self.selected_train != None or self.selected_train != 0):
                #authority input in ft need to change to m
                if (self.ui.AuthorityIn.text() != ''):
                    #self.ui.PhysicalData_tb.setItem(0,0,QTableWidgetItem(str(self.ui.AuthorityIn.text()+" ft")))
                    self.ui.PhysicalData.setItem(0,0,QTableWidgetItem(str(self.ui.AuthorityIn.text()+" ft")))
                    self.selected_train.model.authority = feets_meters(float(self.ui.AuthorityIn.text()))

                #speed limit input in mph need to change to m/s
                if (self.ui.SpeedLimitIn.text() != ''):
                    #self.ui.PhysicalData_tb.setItem(0,4,QTableWidgetItem(str(self.ui.SpeedLimitIn.text()+" mph")))
                    self.ui.PhysicalData.setItem(0,4,QTableWidgetItem(str(self.ui.SpeedLimitIn.text()+" mph")))
                    self.selected_train.model.speed_limit = mph_mps(float(self.ui.SpeedLimitIn.text()))

                #block grade input
                if (self.ui.BlockGradeIn.text() != ''):
                    #self.ui.PhysicalData_tb.setItem(0,9,QTableWidgetItem(str(self.ui.BlockGradeIn.text()+" %")))
                    self.ui.PhysicalData.setItem(0,8,QTableWidgetItem(str(self.ui.BlockGradeIn.text()+" %")))
                    self.selected_train.model.block_Grade = float(self.ui.BlockGradeIn.text())

                #power input in w
                if (self.ui.PowerIn.text() != ''):
                    #self.ui.PhysicalData_tb.setItem(0,1,QTableWidgetItem(str(self.ui.PowerIn.text()+" W")))
                    self.ui.PhysicalData.setItem(0,1,QTableWidgetItem(str(self.ui.PowerIn.text()+" W")))
                    self.selected_train.model.power_command = float(self.ui.PowerIn.text())

                #commanded speed input in mph need to change to m/s
                if (self.ui.SuggestedSpeedIn.text() != ''):
                    #self.ui.PhysicalData_tb.setItem(0,3,QTableWidgetItem(str(self.ui.SuggestedSpeedIn.text()+" mph")))
                    self.ui.PhysicalData.setItem(0,3,QTableWidgetItem(str(self.ui.SuggestedSpeedIn.text()+" mph")))
                    self.selected_train.model.commanded_speed = mph_mps(float(self.ui.SuggestedSpeedIn.text()))

                #temperature input in fahrenheit to celsius
                if (self.ui.TemperatureIn.text() != ''):
                    self.selected_train.model.temperature_command = fahrenheit_celcius(int(self.ui.TemperatureIn.text()))

                #announcement input
                if (self.ui.AnnouncementIn.text() != ''):
                    #self.ui.Announcements_tb.setText("Announcements: "+ self.ui.AnnouncementIn.text())
                    self.ui.Announcements.setText("Announcements: "+ self.ui.AnnouncementIn.text())
                    self.selected_train.model.announcements = self.ui.AnnouncementIn.text()

                #changing output based on door state
                if(self.ui.LeftDoorCheck.isChecked()==True):
                    #self.ui.DoorState_tb.setItem(0,1,QTableWidgetItem(str("Open")))
                    self.ui.DoorState.setItem(0,1,QTableWidgetItem(str("Open")))
                    self.selected_train.model.doors.set_left_door(True)
                else:
                    #self.ui.DoorState_tb.setItem(0,1,QTableWidgetItem(str("Closed")))
                    self.ui.DoorState.setItem(0,1,QTableWidgetItem(str("Closed")))
                    self.selected_train.model.doors.set_left_door(False)
                if(self.ui.RightDoorCheck.isChecked()==True):
                    self.ui.DoorState.setItem(0,0,QTableWidgetItem(str("Open")))
                    #self.ui.DoorState_tb.setItem(0,0,QTableWidgetItem(str("Open")))
                    self.selected_train.model.doors.set_right_door(True)
                else:
                    self.ui.DoorState.setItem(0,0,QTableWidgetItem(str("Closed")))
                    #self.ui.DoorState_tb.setItem(0,0,QTableWidgetItem(str("Closed")))
                    self.selected_train.model.doors.set_right_door(False)

                #changing output based on light state
                if(self.ui.InternalLightsCheck.isChecked()==True):
                    #self.ui.LightsState_tb.setItem(0,0,QTableWidgetItem(str("On")))
                    self.ui.LightsState.setItem(0,0,QTableWidgetItem(str("On")))
                    self.selected_train.model.lights.set_internal_lights(True)
                else:
                    #self.ui.LightsState_tb.setItem(0,0,QTableWidgetItem(str("Off")))
                    self.ui.LightsState.setItem(0,0,QTableWidgetItem(str("Off")))
                    self.selected_train.model.lights.set_internal_lights(False)
                if(self.ui.ExternalLightsCheck.isChecked()==True):
                    #self.ui.LightsState_tb.setItem(0,1,QTableWidgetItem(str("On")))
                    self.ui.LightsState.setItem(0,1,QTableWidgetItem(str("On")))
                    self.selected_train.model.lights.set_external_lights(True)
                else:
                    #self.ui.LightsState_tb.setItem(0,1,QTableWidgetItem(str("Off")))
                    self.ui.LightsState.setItem(0,1,QTableWidgetItem(str("Off")))
                    self.selected_train.model.lights.set_external_lights(False)

                #changing output based on brake state
                if(self.ui.EBrakeCheck.isChecked()==True):
                    #self.ui.BrakeState_tb.setItem(0,0,QTableWidgetItem(str("Engaged")))
                    self.ui.BrakeState.setItem(0,0,QTableWidgetItem(str("Engaged")))
                    self.selected_train.model.brakes.set_emergency_brake(True)
                else:
                    #self.ui.BrakeState_tb.setItem(0,0,QTableWidgetItem(str("Disengaged")))
                    self.ui.BrakeState.setItem(0,0,QTableWidgetItem(str("Disengaged")))
                    self.selected_train.model.brakes.set_emergency_brake(False)
                if(self.ui.ServiceBrakeCheck.isChecked()==True):
                    #self.ui.BrakeState_tb.setItem(0,1,QTableWidgetItem(str("Engaged")))
                    self.ui.BrakeState.setItem(0,1,QTableWidgetItem(str("Engaged")))
                    self.selected_train.model.brakes.set_service_brake(True)
                else:
                    #self.ui.BrakeState_tb.setItem(0,1,QTableWidgetItem(str("Disengaged")))
                    self.ui.BrakeState.setItem(0,1,QTableWidgetItem(str("Disengaged")))
                    self.selected_train.model.brakes.set_service_brake(False)
            else:
                Exception ("Train does not exist")
        except AttributeError:
            print("Train does not exist")
        except KeyError:
            print("Train does not exist brake")

#---------------------------------------------------------------
# Displaying the GUI
#---------------------------------------------------------------
def main():
    app = QApplication(sys.argv)
    form  = TrainModelUI()
    form.show()
    sys.exit(app.exec())

if __name__ == '__main__':

    main()