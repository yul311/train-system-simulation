import sys
import os
import math
import GUI.ctrl_ui as ui
import time
import numpy as np 
from scipy.signal import TransferFunction, freqz
from typing import Optional
from PySide6.QtWidgets import (QApplication, QMainWindow, QSlider, QScrollArea, QPushButton, QLCDNumber, QTableWidgetItem, QMessageBox, QGraphicsView,
                               QGraphicsRectItem, QGraphicsScene, QHBoxLayout, QWidget, QLabel, QGraphicsItem, QVBoxLayout)
from PySide6.QtCore import QFile, Slot,QDate, QTime, QTimer, QDateTime, Qt, QEvent, QRectF
from PySide6.QtGui import QPalette, QColor, QIntValidator, QBrush, QPen, QPixmap
from PySide6.QtUiTools import QUiLoader
from beacon_decoder import BeaconDecoder

from Track_Model.Controller import greenLine, blueLine #redLine


item = BeaconDecoder()  

class main(QMainWindow):
    #--------------------------------------------------------------------------
    # Delay
    #--------------------------------------------------------------------------
    start_time = QDateTime()
    m_secs_passed = 0
    simulation_speed = 1
    interval = 1000
    
    model_values: BeaconDecoder()
    
    
    #--------------------------------------------------------------------------
    # Main
    #--------------------------------------------------------------------------
    def __init__(self, item, parent=None):
        
        #speed_limit = items.speed_limit
        #suggested_speed = items.suggested_speed
        #authority = items.authority
        
        super(main, self).__init__(parent)
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.trainid = None
        self.selected_train = None
        
        self.start_time = QDateTime.currentDateTime()
        update_timer = QTimer(self)
        update_timer.timeout.connect(self.time_update)
        update_timer.setInterval(self.interval)
        update_timer.setSingleShot(False)
        update_timer.start()       
        
        #self.ui.logo_txt.setPixmap(QPixmap(os.path.join(os.getcwd(), "Train_Controller/images/AuroraLogo.jpg")))
        #self.ui.header_txt.setPixmap(QPixmap(os.path.join(os.getcwd(), "Train_Controller/images/yellow.png")))
         
        validator = QIntValidator()
        self.ui.train_id.setValidator(validator)
        
    #--------------------------------------------------------------------------
    # Train ID
    #--------------------------------------------------------------------------
        self.ui.blue_button.clicked.connect(self.update_blue)
        self.ui.green_button.clicked.connect(self.update_green)
        self.ui.red_button.clicked.connect(self.update_red)
            
    #--------------------------------------------------------------------------
    # Authority
    #--------------------------------------------------------------------------
         
    
        
    #--------------------------------------------------------------------------
    # Automation
    #--------------------------------------------------------------------------
        self.ui.manual_button.clicked.connect(self.Automation)
        #self.ui.tb_load_data_display.clicked.connect(self.LoadData) 
       
    #--------------------------------------------------------------------------
    # Speed Control
    #--------------------------------------------------------------------------
        self.model_values = item
            
        # setting the speed limit 
        self.ui.speed_limit_display.display(92)
        
        # input speed control 
        self.ui.input_speed_slider.setMinimum(0)
        self.ui.input_speed_slider.setMaximum(100)
        self.ui.input_speed_slider.setRange(0, 43)
        self.ui.input_speed_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.input_speed_slider.setTickInterval(10)
        self.ui.original_input_speed = self.ui.input_speed_slider.styleSheet()
        
        self.ui.input_speed_slider.valueChanged.connect(self.time_update)
        self.ui.input_speed_slider.valueChanged.connect(self.SpeedControl)
        
        # test        
        self.previous_speed = self.ui.input_speed_display.value()
        self.ui.input_speed_slider.show()
        
        # suggested speed
        self.ui.suggested_speed_display.display(37377)
        
    #--------------------------------------------------------------------------
    # Station Control
    #--------------------------------------------------------------------------
    
        self.ui.authority_display.display(333)
        self.ui.original_station = self.ui.station_button.styleSheet()
        
        # announcing the stops
        self.ui.output_stop_display.setText("...")
        self.ui.output_stop_display.setStyleSheet("text-align: center;")
        self.ui.station_button.clicked.connect(self.AnnounceStop)
        
        
    #--------------------------------------------------------------------------
    # Emergency Brake
    #--------------------------------------------------------------------------
        self.ui.tb_e_display.setStyleSheet("background-color: grey;")
    
        self.ui.e_label_display.setStyleSheet("background-color: grey;")
        self.ui.e_brake_button.setStyleSheet("background-color: red;")
        self.ui.original_e_button = self.ui.e_brake_button.styleSheet()
        self.ui.original_e_label = self.ui.e_label_display.styleSheet()
        self.ui.e_brake_button.clicked.connect(self.EmergencyState)
        self.ui.tb_e_brake_button.clicked.connect(self.EmergencyState)
        
    #--------------------------------------------------------------------------
    # Service Brake
    #--------------------------------------------------------------------------
        self.ui.tb_s_display.setStyleSheet("background-color: grey;")
    
        self.ui.s_label_display.setStyleSheet("background-color: grey;")
        self.ui.s_slider.setMinimum(0)
        self.ui.s_slider.setMaximum(100)
        self.ui.s_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.s_slider.setTickInterval(10)
        self.ui.original_s_slider = self.ui.s_slider.styleSheet()
        self.ui.original_s_label = self.ui.s_label_display.styleSheet()
        self.ui.s_slider.valueChanged.connect(self.ServiceState)
        self.ui.s_slider.show()
        
    #--------------------------------------------------------------------------
    # Light Control
    #--------------------------------------------------------------------------
    
        self.ui.interior_button.setStyleSheet("background-color: green;")
        self.ui.original_interior = self.ui.interior_button.styleSheet()
        self.ui.interior_button.clicked.connect(self.InteriorLight)
        
        
        self.ui.exterior_button.setStyleSheet("background-color: grey;")
        self.ui.exterior_button.setText("Off")
        self.ui.original_exterior = self.ui.exterior_button.styleSheet()
        self.ui.exterior_button.clicked.connect(self.ExteriorLight)
    
    #--------------------------------------------------------------------------
    # Door Control
    #--------------------------------------------------------------------------
    
        self.ui.left_button.setStyleSheet("background-color: grey;")
        self.ui.left_button.setText("Close")
        self.ui.original_left = self.ui.left_button.styleSheet()
        self.ui.left_button.clicked.connect(self.LeftDoor)
        
        self.ui.right_button.setStyleSheet("background-color: grey;")
        self.ui.right_button.setText("Close")
        self.ui.original_right = self.ui.right_button.styleSheet()
        self.ui.right_button.clicked.connect(self.RightDoor)

    #--------------------------------------------------------------------------
    # Temperature Control
    #--------------------------------------------------------------------------

        self.ui.temp_slider.setMinimum(0)
        self.ui.temp_slider.setMaximum(100)
        self.ui.temp_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.temp_slider.setTickInterval(10)
        self.ui.original_temp_slider = self.ui.temp_slider.styleSheet()
        
        
        #self.ui.temp_slider.valueChanged.connect(self.time_update)
        self.ui.temp_slider.valueChanged.connect(self.TempControl)
        
        
        #test
        self.previous_temp = self.ui.temp_slider.value()
        
        self.ui.temp_slider.valueChanged.connect(self.time_update)
        self.ui.temp_slider.show()
        
    #--------------------------------------------------------------------------
    # Tunnel Control
    #--------------------------------------------------------------------------
        #self.ui.original_tunnel = self.ui.tunnel_display.styleSheet()
        #self.ui.tunnel_display.clicked.connect(self.TunnelControl)
        
    #--------------------------------------------------------------------------
    # Power Control
    #--------------------------------------------------------------------------

        self.ui.original_kp = self.ui.kp_slider.styleSheet()
        self.ui.original_ki = self.ui.ki_slider.styleSheet()
        
        self.ui.kp_display.display(0)
        self.ui.ki_display.display(0)
        
        self.ui.kp_slider.setMinimum(0)
        self.ui.kp_slider.setMaximum(100)
        self.ui.kp_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.kp_slider.setTickInterval(10)
        self.ui.kp_slider.valueChanged.connect(self.KpPower)
        self.ui.kp_slider.show()
        
        self.ui.ki_slider.setMinimum(0)
        self.ui.ki_slider.setMaximum(100)
        self.ui.ki_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.ki_slider.setTickInterval(10)
        self.ui.ki_slider.valueChanged.connect(self.KiPower)
        self.ui.ki_slider.show()
    
    #--------------------------------------------------------------------------
    # Faults
    #--------------------------------------------------------------------------
        self.ui.signal_display.setStyleSheet("background-color: green;")
        self.ui.tb_signal_display.clicked.connect(self.SignalFault)
        
        self.ui.engine_display.setStyleSheet("background-color: green;")
        self.ui.tb_engine_display.clicked.connect(self.EngineFault)
        
        self.ui.brake_display.setStyleSheet("background-color: green;")
        self.ui.tb_brake_display.clicked.connect(self.BrakeFault)
        
    
        
    #--------------------------------------------------------------------------
    # Trains
    #--------------------------------------------------------------------------
    def update_blue(self):
         if (self.ui.train_id.text() != ""):
            self.trainid = int(self.ui.train_id.text())
            try:
                self.selected_train = blueLine.trains[self.trainid].controller
                print(self.trainid)
            except KeyError:
                print("Train being selected does not exist")
    
    def update_red(self):
        pass
    
    def update_green(self):
        #print('button pressed')
        if (self.ui.train_id.text() != ""):
            self.trainid = int(self.ui.train_id.text())
            try:
                self.selected_train = greenLine.trains[self.trainid].controller
                #print(self.selected_train.get_line())
                #print(self.trainid)
            except KeyError:
                print("Train being selected does not exist")
            #print(self.trainid)




    #--------------------------------------------------------------------------
    # Update
    #--------------------------------------------------------------------------
    
    # load the parameters
    def LoadData(self):
        global speed_limit
        global suggested_speed
        global authority
        
        if (self.ui.tb_speed_limit_display.toPlainText()):
           
            speed_limit = int(self.ui.tb_speed_limit_display.toPlainText()) 
            
            #setting the speed limit 
            self.ui.speed_limit_display.display(speed_limit)
            
            # input speed control 
            self.ui.input_speed_slider.setMinimum(0)
            self.ui.input_speed_slider.setMaximum(100)
            self.ui.input_speed_slider.setRange(0, speed_limit)
            self.ui.input_speed_slider.setTickPosition(QSlider.TicksLeft)
            self.ui.input_speed_slider.setTickInterval(10)
            self.ui.original_input_speed = self.ui.input_speed_slider.styleSheet()
            
            self.ui.input_speed_slider.valueChanged.connect(self.time_update)
            self.ui.input_speed_slider.valueChanged.connect(self.SpeedControl)
            
            # test        
            self.previous_speed = self.ui.input_speed_display.value()
            self.ui.input_speed_slider.show()
            
        # suggested speed
        if (self.ui.tb_suggested_speed_display.toPlainText()):
            suggested_speed = int(self.ui.tb_suggested_speed_display.toPlainText()) 
            self.ui.suggested_speed_display.display(suggested_speed)
            
        # suggested authority
        if (self.ui.tb_authority_display.toPlainText()):
            authority = int(self.ui.tb_authority_display.toPlainText()) 
            self.ui.authority_display.display(authority)
            
    
    
    
    # setting the manual and automatic modes
    def Automation(self):
        if(self.ui.manual_button.isChecked() == True):
            # setting current speed to the suggested (AUTO)
            self.ui.current_speed_display.display(suggested_speed)
            
            # removing the access of manual inputs
            self.ui.input_speed_slider.setStyleSheet("background-color: grey;")
            self.ui.input_speed_slider.setEnabled(False)
            
            self.ui.station_button.setStyleSheet("background-color: grey;")
            self.ui.station_button.setEnabled(False)
            
            self.ui.left_button.setStyleSheet("background-color: grey;")
            self.ui.left_button.setEnabled(False)
            
            self.ui.right_button.setStyleSheet("background-color: grey;")
            self.ui.right_button.setEnabled(False)
            
            self.ui.interior_button.setStyleSheet("background-color: grey;")
            self.ui.interior_button.setEnabled(False)
            
            self.ui.exterior_button.setStyleSheet("background-color: grey;")
            self.ui.exterior_button.setEnabled(False)
            
            self.ui.tunnel_display.setStyleSheet("background-color: grey;")
            self.ui.tunnel_display.setEnabled(False)
            
            self.ui.temp_slider.setStyleSheet("background-color: grey;")
            self.ui.temp_slider.setEnabled(False)
            
            self.ui.kp_slider.setStyleSheet("background-color: grey;")
            self.ui.kp_slider.setEnabled(False)
            
            self.ui.ki_slider.setStyleSheet("background-color: grey;")
            self.ui.ki_slider.setEnabled(False)
            
            self.ui.e_label_display.setStyleSheet("background-color: grey;")
            self.ui.e_label_display.setEnabled(False)
            self.ui.e_brake_button.setStyleSheet("background-color: grey;")
            self.ui.e_brake_button.setEnabled(False)
            
            self.ui.s_label_display.setStyleSheet("background-color: grey;")
            self.ui.s_label_display.setEnabled(False)
            self.ui.s_slider.setStyleSheet("background-color: grey;")
            self.ui.s_slider.setEnabled(False)
        else:
            # setting current speed back to manual
            #self.ui.current_speed_display.display(suggested_speed)
            
            # give the access back
            self.ui.input_speed_slider.setStyleSheet(self.ui.original_input_speed)
            self.ui.input_speed_slider.setEnabled(True)
            
            self.ui.station_button.setStyleSheet(self.ui.original_station)
            self.ui.station_button.setEnabled(True)
            
            self.ui.left_button.setStyleSheet(self.ui.original_left)
            self.ui.left_button.setEnabled(True)
            
            self.ui.right_button.setStyleSheet(self.ui.original_right)
            self.ui.right_button.setEnabled(True)
            
            self.ui.interior_button.setStyleSheet(self.ui.original_interior)
            self.ui.interior_button.setEnabled(True)
            
            self.ui.exterior_button.setStyleSheet(self.ui.original_exterior)
            self.ui.exterior_button.setEnabled(True)
            
            self.ui.tunnel_display.setStyleSheet(self.ui.original_tunnel)
            self.ui.tunnel_display.setEnabled(True)
            
            self.ui.temp_slider.setStyleSheet(self.ui.original_temp_slider)
            self.ui.temp_slider.setEnabled(True)
            
            self.ui.kp_slider.setStyleSheet(self.ui.original_kp)
            self.ui.kp_slider.setEnabled(True)
            
            self.ui.ki_slider.setStyleSheet(self.ui.original_ki)
            self.ui.ki_slider.setEnabled(True)
            
            self.ui.e_label_display.setStyleSheet(self.ui.original_e_label)
            self.ui.e_label_display.setEnabled(True)
            self.ui.e_brake_button.setStyleSheet(self.ui.original_e_button)
            self.ui.e_brake_button.setEnabled(True)
            
            self.ui.s_label_display.setStyleSheet(self.ui.original_s_label)
            self.ui.s_label_display.setStyleSheet("background-color: orange;")
            self.ui.s_label_display.setEnabled(True)
            self.ui.s_slider.setStyleSheet(self.ui.original_s_slider)
            self.ui.s_slider.setEnabled(True)
            
            
            
            
    
    # emergency brake state
    def EmergencyState(self):
        if (self.ui.e_label_display.text() == "Disengaged" or self.ui.tb_e_brake_button.isChecked() == True):
            self.ui.e_label_display.setText("Engaged")
            self.ui.e_label_display.setStyleSheet("background-color: red;")
            self.ui.tb_e_display.setStyleSheet("background-color: red;")
        else:
            self.ui.e_label_display.setText("Disengaged")
            self.ui.e_label_display.setStyleSheet("background-color: grey;")
            self.ui.tb_e_display.setStyleSheet("background-color: grey;")
            
            
    # service brake state
    def ServiceState(self):
        value = self.ui.s_slider.value()
        
        if(value != 0):
            self.ui.s_label_display.setText("       " + str(value) + " %")
            self.ui.s_label_display.setStyleSheet("background-color: orange;")
            self.ui.tb_s_display.setStyleSheet("background-color: orange;")
        else:
            self.ui.s_label_display.setStyleSheet("text-align: center;")
            self.ui.s_label_display.setText("Disengaged")
            self.ui.s_label_display.setStyleSheet("background-color: grey;")
            self.ui.tb_s_display.setStyleSheet("background-color: grey;")
    
    # input speed
    def SpeedControl(self):
        value = self.ui.input_speed_slider.value()
        
        test = self.model_values.get_current_speed()
        
        if(value != '0'):
            self.ui.input_speed_display.display(value)
        else:
            self.ui.input_speed_display.display(0)
        
       
        self.ui.current_speed_display.display(test)

    # current speed
    # ---- TODO: finish the slow incrementation
    def CurrentSpeedDelay(self):
        value = self.ui.input_speed_slider.value()
        speed = 0 
        
        for i in range(value):
            if(speed <= value):
                speed+=1
            else: 
                speed-=1
            
            self.ui.current_speed_display.display(speed)
    
        
    # controls the interior and exterior lights
    def InteriorLight(self):
        if(self.ui.interior_button.text() == "On"):
            self.ui.interior_button.setStyleSheet("background-color: grey;")
            self.ui.interior_button.setText("Off")
            self.ui.tb_interior_display.setText("Off")
        else:
            self.ui.interior_button.setStyleSheet("background-color: green;")
            self.ui.interior_button.setText("On")
            self.ui.tb_interior_display.setText("On")
    
    def ExteriorLight(self):    
        if(self.ui.exterior_button.text() == "On"):
            self.ui.exterior_button.setStyleSheet("background-color: grey;")
            self.ui.exterior_button.setText("Off")
            self.ui.tb_exterior_display.setText("Off")
        else:
            self.ui.exterior_button.setStyleSheet("background-color: green;")
            self.ui.exterior_button.setText("On")
            self.ui.tb_exterior_display.setText("On")
            
    # tunnel control
    def TunnelControl(self):
        if(self.ui.tunnel_display.isChecked() == True):
            self.ui.interior_button.setText("On")
            self.ui.tb_interior_display.setText("On")
            self.ui.interior_button.setStyleSheet("background-color: green;")
            
            self.ui.exterior_button.setText("On")
            self.ui.tb_exterior_display.setText("On")
            self.ui.exterior_button.setStyleSheet("background-color: green;")
        else:
            self.ui.exterior_button.setText("Off")
            self.ui.tb_exterior_display.setText("Off")
            self.ui.exterior_button.setStyleSheet("background-color: grey;")
        
    # door control for left and right
    def LeftDoor(self):
        if(self.ui.left_button.text() == "Open"):
            self.ui.left_button.setStyleSheet("background-color: grey;")
            self.ui.left_button.setText("Close")
            self.ui.tb_left_display.setText("Closed")
        else:
            self.ui.left_button.setStyleSheet("background-color: green;")
            self.ui.left_button.setText("Open")
            self.ui.tb_left_display.setText("Opened")
            
    def RightDoor(self):
        if(self.ui.right_button.text() == "Open"):
            self.ui.right_button.setStyleSheet("background-color: grey;")
            self.ui.right_button.setText("Close")
            self.ui.tb_right_display.setText("Closed")
        else:
            self.ui.right_button.setStyleSheet("background-color: green;")
            self.ui.right_button.setText("Open")
            self.ui.tb_right_display.setText("Opened")
    
    # temperature control    
    def TempControl(self):
        temp = self.ui.temp_slider.value()
        
            
        self.ui.set_temp_display.display(str(temp))
        #print (self.trainid)
        return 
        
        
    # station control 
    def StationControl(self):
        authority = self.ui.authority_display.value()
        
        for i in range(8000):
            authority = authority - 1
            self.ui.authority_display.display(authority)
            #print(authority)
            if(authority == 0):
                self.ui.authority_display.setStyleSheet("background-color: green;")
                self.ui.authority_display.display(authority)
                break
            
    def AnnounceStop(self):
        station = self.ui.station_display.text()
        
        self.ui.output_stop_display.setText(station)
        self.ui.tb_stop_display.setText(station)
            
    # power control
    def KpPower(self):
        kp = self.ui.kp_slider.value()
        
        if(kp != 0):
            self.ui.kp_display.display(kp)
        else:
            self.ui.kp_display.display(0)
    
    def KiPower(self):
        ki = self.ui.ki_slider.value()
        
        if(ki != 0):
            self.ui.ki_display.display(ki)
        else:
            self.ui.ki_display.display(0)
        
    # faults (Signal, Engine, Brake)
    def SignalFault(self):
        if(self.ui.tb_signal_display.isChecked() == True):
            self.ui.signal_display.setText("WARNING!")
            self.ui.signal_display.setStyleSheet("background-color: red;")
        else:
            self.ui.signal_display.setText("Good")
            self.ui.signal_display.setStyleSheet("background-color: green;")
            
    
    def EngineFault(self):
        if(self.ui.tb_engine_display.isChecked() == True):
            self.ui.engine_display.setText("WARNING!")
            self.ui.engine_display.setStyleSheet("background-color: red;")
            self.ui.used_power_display.display(0)
            self.ui.tb_power_display.display(0)
        else:
            self.ui.engine_display.setText("Good")
            self.ui.engine_display.setStyleSheet("background-color: green;")
            
    def BrakeFault(self):
        if(self.ui.tb_brake_display.isChecked() == True):
            self.ui.brake_display.setText("WARNING!")
            self.ui.brake_display.setStyleSheet("background-color: red;")
        else:
            self.ui.brake_display.setText("Good")
            self.ui.brake_display.setStyleSheet("background-color: green;")
            
    # clock
    def time_update(self):
        self.m_secs_passed += self.interval*self.simulation_speed
        self.ui.date_time_display.setDateTime(self.start_time.addMSecs(self.m_secs_passed))

        
        # temperature
        temp = self.ui.temp_slider.value()
        current_temp = self.ui.current_temp_display.value()
        
        if((temp > current_temp) and self.previous_temp == temp):
            current_temp+=1
            self.ui.current_temp_display.display(str(current_temp)) 
            self.ui.tb_temp_display.display(str(current_temp))
            
        elif((temp < current_temp) and self.previous_temp == temp):
            current_temp-=1
            self.ui.current_temp_display.display(str(current_temp)) 
            self.ui.tb_temp_display.display(str(current_temp))
            
        self.previous_temp = self.ui.temp_slider.value()
        
        # current speed
        speed = self.ui.input_speed_slider.value()
        current_speed = self.ui.current_speed_display.value()
        slow = self.ui.s_label_display.text()
        ebrake = self.ui.e_label_display.text()
        
            # service brake logic
        if(slow != "Disengaged"):
            slow = (self.ui.s_label_display.text())
            if(slow[7:8] < "10"):
                slow = float(slow[8])
            else:
                slow = float(slow[7:8])
            
            # emergency brake
        if(ebrake == "Disengaged"):
            if((speed > current_speed) and self.previous_speed == speed):
                
                    # service brake
                if(slow == "Disengaged"):
                    current_speed+=1
                    self.ui.current_speed_display.display(str(current_speed)) 
                    self.ui.tb_current_speed_display.display(str(current_speed))
                else:
                    current_speed-=slow
                    
                    if(current_speed <= 0):
                        current_speed = 0
                    
                    self.ui.current_speed_display.display(str(current_speed)) 
                    self.ui.tb_current_speed_display.display(str(current_speed))
                    
                
            elif((speed < current_speed) and self.previous_speed == speed):          
                if(slow == "Disengaged"):
                    current_speed-=1
                    self.ui.current_speed_display.display(str(current_speed)) 
                    self.ui.tb_current_speed_display.display(str(current_speed))
                else:
                    current_speed-=(slow/100)*10
                    
                    if(current_speed <= 0):
                        current_speed = 0
                    
                    self.ui.current_speed_display.display(str(current_speed)) 
                    self.ui.tb_current_speed_display.display(str(current_speed))
        else:
            current_speed-=5
            
            if(current_speed <= 0):
                current_speed = 0
                
            self.ui.current_speed_display.display(str(current_speed)) 
            self.ui.tb_current_speed_display.display(str(current_speed))
            
            
        self.previous_speed = self.ui.input_speed_display.value()
        
        # power 
        global e_k, u_k
        ki = self.ui.ki_slider.value()
        kp = self.ui.kp_slider.value()
        
        e_k_previous = e_k
        
        e_k = speed - current_speed
        
        u_k = u_k + self.interval/2 * (e_k + e_k_previous)
        
        power = kp*e_k + ki*u_k
            
        self.ui.used_power_display.display(power)
        self.ui.tb_power_display.display(power)

            
        
        return 
            
        
            
                
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main(BeaconDecoder)
    window.show()
    sys.exit(app.exec())