from typing import Optional
import sys
import os
import math

# for the main to work
import Train_Controller.GUI.train_ctrl_ui as ui
#import Train_Controller.train_controller as TrainController

from Track_Model.Controller import greenLine as track_model

import time
import numpy as np 
from scipy.signal import TransferFunction, freqz
from typing import Optional
from PySide6.QtWidgets import (QApplication, QMainWindow, QSlider, QScrollArea, QPushButton, QLCDNumber, QTableWidgetItem, QMessageBox, QGraphicsView,
                               QGraphicsRectItem, QGraphicsScene, QHBoxLayout, QWidget, QLabel, QGraphicsItem, QVBoxLayout)
from PySide6.QtCore import QFile, Slot,QDate, QTime, QTimer, QDateTime, Qt, QEvent, QRectF
from PySide6.QtGui import QPalette, QColor, QIntValidator, QBrush, QPen, QPixmap, QIcon
from PySide6.QtUiTools import QUiLoader

from Train_Controller.train_controller import TrainController
from Main.simulation_time import sim
from datetime import datetime

from Track_Model.Controller import greenLine, redLine

ICON_PATH = os.path.join(os.getcwd(),"Other","AuroraLogo.jpg")


class TrainCtrlUi(QMainWindow):
    
    #--------------------------------------------------------------------------
    # Declare variables
    #--------------------------------------------------------------------------
    speed_limit: int = 0
    suggested_speed: int = 0
    current_speed: int = 0
    command_speed: int = 0
    
    power: int = 0
    kp_value: int = 0
    ki_value: int = 0 
    
    passenger_brake: bool = False
    service_brake: bool = False
    
    right_door: bool = False
    left_door: bool = False
    
    exterior_light: bool = False
    interior_light: bool = False
    
    temperature: int = 0
    current_temperature: int = 0
    

    automatic: bool = False
    
    ## neeed to sort out
    authority: int = 0
    current_station: str = ""
    next_station: str = ""
    tunnel: bool = False
    
    signal_fault: bool = False
    engine_fault: bool = False
    brake_fault: bool = False
    
    tc_instance: TrainController
    
    time: datetime
    

    #need to select green line or red line trains
    #greenline.trains for green max 152
    #blueline.trains for blue max 15
    #redline.trains for red max XXX
    #greenline.get_line() name 'green'
    #blueline.get_line() name 'blue'
    #blueline.get_line() name'red'
    
    # alex
    # track send id to ctrl
    
    #--------------------------------------------------------------------------
    # constructor
    #--------------------------------------------------------------------------

    def __init__(self):

        super().__init__()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.tc_instance = None # = tc
        self.time = datetime.now()
        self.trainid = None
        self.selected_train = None
        self.interval = 50

        self.setWindowTitle("Train Controller")
        icon = QIcon(ICON_PATH)
        self.setWindowIcon(icon)
        
        validator = QIntValidator()
        self.ui.train_id.setValidator(validator)
        
        self.start_time = QDateTime.currentDateTime()
        update_timer = QTimer(self)
        update_timer.timeout.connect(self.display_data)
        update_timer.setInterval(self.interval)
        update_timer.setSingleShot(False)
        update_timer.start()       


        self.set_up()
        self.display_data()
        self.Automation()
        self.connection_button()
        

    #--------------------------------------------------------------------------
    # Function Controls
    #--------------------------------------------------------------------------
    
    def set_up(self):
    # set logo and header        
        self.ui.logo_txt.setPixmap(QPixmap(os.path.join(os.getcwd(), "Train_Controller/images/AuroraLogo.jpg")))
        self.ui.header_txt.setPixmap(QPixmap(os.path.join(os.getcwd(), "Train_Controller/images/yellow.png")))
    
    #--------------------------------------------------------------------------
    # Train ID
    #--------------------------------------------------------------------------
#        self.ui.blue_button.clicked.connect(self.update_blue)
        self.ui.green_button.clicked.connect(self.update_green)
        self.ui.red_button.clicked.connect(self.update_red)
           
    # commanded speed set up 
        self.ui.input_speed_slider.setMinimum(0)
        self.ui.input_speed_slider.setMaximum(100)
        self.ui.input_speed_slider.setRange(0, 43.495)
        self.ui.input_speed_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.input_speed_slider.setTickInterval(10)
        self.ui.original_input_speed = self.ui.input_speed_slider.styleSheet()
        self.ui.input_speed_display.setText(f'{0.0:.2f}')
        self.ui.input_speed_slider.setValue(0)
        self.ui.input_speed_slider.show()
        
    # brake set up
        # emergency brake
        self.ui.e_label_display.setText("Disengaged")
        self.ui.e_label_display.setStyleSheet("background-color: grey;")
        self.ui.e_brake_button.setStyleSheet("background-color: red;")
        
        # service brake  
        self.ui.s_label_display.setStyleSheet("background-color: grey;")
        self.ui.s_brake_button.setStyleSheet("background-color: orange;")
        self.ui.original_s_brake = self.ui.s_brake_button.styleSheet()
        self.ui.original_s_label = self.ui.s_label_display.styleSheet()
        
    # authority set up 
        self.ui.authority_display.setText(str(self.authority))
        self.ui.original_station = self.ui.station_button.styleSheet()
        
        self.ui.output_stop_display.setText(self.current_station)
        self.ui.output_stop_display.setStyleSheet("text-align: center;")
        
    # lights set up
        # interior lights
        self.ui.interior_button.setStyleSheet("background-color: grey;")
        self.ui.interior_button.setText("Off")
        self.ui.original_interior = self.ui.interior_button.styleSheet()
        
        # exterior lights
        self.ui.exterior_button.setStyleSheet("background-color: grey;")
        self.ui.exterior_button.setText("Off")
        self.ui.original_exterior = self.ui.exterior_button.styleSheet()
        
    # door set up
        # left door
        self.ui.left_button.setStyleSheet("background-color: grey;")
        self.ui.left_button.setText("Close")
        self.ui.original_left = self.ui.left_button.styleSheet()
        
        # right door
        self.ui.right_button.setStyleSheet("background-color: grey;")
        self.ui.right_button.setText("Close")
        self.ui.original_right = self.ui.right_button.styleSheet()
        
    # temperature set up
        self.ui.temp_slider.setMinimum(0)
        self.ui.temp_slider.setMaximum(100)
        self.ui.temp_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.temp_slider.setTickInterval(10)
        self.ui.original_temp_slider = self.ui.temp_slider.styleSheet()
        self.ui.temp_slider.setValue(0)
        self.ui.temp_slider.show()
    
    # fault set up
        self.ui.signal_txt.setStyleSheet("background-color: green;")
        
        self.ui.engine_txt.setStyleSheet("background-color: green;")
        
        self.ui.brake_fail_txt.setStyleSheet("background-color: green;")
        
    # power set up
        self.ui.original_kp = self.ui.kp_slider.styleSheet()
        self.ui.original_ki = self.ui.ki_slider.styleSheet()
        
        self.ui.kp_display.setText(f'{(0.0):.2f}')
        self.ui.ki_display.setText(f'{(0.0):.2f}') 
        
        self.ui.kp_slider.setMinimum(0)
        self.ui.kp_slider.setMaximum(100000)
        self.ui.kp_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.kp_slider.setTickInterval(1)
        self.ui.kp_slider.setValue(0)
        self.ui.kp_slider.show()
        
        self.ui.ki_slider.setMinimum(0)
        self.ui.ki_slider.setMaximum(100000)
        self.ui.ki_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.ki_slider.setTickInterval(1)
        self.ui.ki_slider.setValue(0)
        self.ui.ki_slider.show()
        
    # time 
        self.ui.date_time_display.setText(sim.get_curr_string())
        self.ui.time_slider.setMinimum(1)
        self.ui.time_slider.setMaximum(10)
        self.ui.time_slider.setTickPosition(QSlider.TicksLeft)
        self.ui.time_slider.setTickInterval(10)
        self.ui.time_slider.setValue(0)
        self.ui.time_slider.show()
    
    # testbench
        # self.ui.tb_e_display.setStyleSheet("background-color: grey;")
        # self.ui.tb_s_display.setStyleSheet("background-color: grey;")
        
    def sim_time(self):
        sim.set_sim_speed(self.ui.time_slider.value())
        
    def sim_pause(self):
        if sim.running:
            sim.stop()
        else:
            sim.start()


    #--------------------------------------------------------------------------
    # Trains
    #--------------------------------------------------------------------------
    def update_blue(self):
        #  if (self.ui.train_id.text() != ""):
        #     self.trainid = int(self.ui.train_id.text())
        #     try:
        #         self.selected_train = blueLine.trains[self.trainid].controller
        #         print(self.trainid)
        #     except KeyError:
        #         print("Train being selected does not exist")
        pass
    
    def update_red(self):
        if(self.ui.train_id.text() != ""):
            self.trainid = int(self.ui.train_id.text())
            try:
                self.selected_train = redLine.trains[self.trainid].controller
                #print(self.trainid)
            except KeyError:
                print("Train being selected does not exist")
            #print(self.trainid)
    
    def update_green(self):
        if(self.ui.train_id.text() != ""):
            self.trainid = int(self.ui.train_id.text())
            try:
                self.selected_train = greenLine.trains[self.trainid].controller
                #print(self.trainid)
            except KeyError:
                print("Train being selected does not exist")
            #print(self.trainid)

    def testing_green(self):
        try:
            self.selected_train = greenLine.trains[self.trainid].controller
            
            
            #print(self.trainid)
        except KeyError:
            print("Train being selected does not exist")
        #print(self.trainid)
            
            
    #----------------------------------------------------------------
    # setter and getter functions
    #----------------------------------------------------------------

    # ---------------------------
    # speed value
    # ---------------------------
    
    def get_current_speed(self):
        try:
            self.current_speed = self.selected_train.get_current_speed()
        except KeyError:
            print("Key Error get current speed")
        except AttributeError:
            pass
        
        return self.current_speed
    
    def set_command_speed(self):
        self.command_speed = self.ui.input_speed_slider.value()
        self.selected_train.set_command_speed(self.command_speed)
        
    def get_speed_limit(self):
        try:
            self.speed_limit = self.selected_train.get_speed_limit()
        except KeyError:
            print("Key Error get speed limit")
        except AttributeError:
            pass
        
        return self.speed_limit
        
    def get_suggested_speed(self):
        try:
            self.suggested_speed = self.selected_train.get_suggested_speed()
        except KeyError:
            print("Key Error get suggested speed")
        except AttributeError:
            pass
        
        return self.suggested_speed
    # ---------------------------
    # power control
    # ---------------------------
    def set_kp_value(self):
        self.kp_value = self.ui.kp_slider.value()
        self.selected_train.set_kp(self.kp_value)
        
    def set_ki_value(self):
        self.ki_value = self.ui.ki_slider.value()
        self.selected_train.set_ki(self.ki_value)
    
    def get_current_power(self):
        try:
            self.power = self.selected_train.get_current_power()
           # print("ui: works and power: " + str(self.power))
        except KeyError:
            print("Key Error get_current_power_main")
        except AttributeError:
            pass
        return self.power
        
    
    # ----------------------------
    # break logic
    # ----------------------------

    def emergency_brake_state(self):
        try:
            temp_state = self.selected_train.get_passenger_brake()

            if temp_state:
                temp_state = False
                self.selected_train.set_passenger_brake(temp_state)
            else:
                temp_state = True
                self.selected_train.set_passenger_brake(temp_state)
        except KeyError:
            print("Key error passenger brake")
        except AttributeError:
            pass

    def display_emergency_brake_state(self):
        try:
            self.passenger_brake = self.selected_train.get_passenger_brake()
        except KeyError:
            print("Key error passenger brake")
        except AttributeError:
            #print("ignore this")
            pass
        if (self.passenger_brake):
            self.ui.e_label_display.setText("Engaged")
            self.ui.e_label_display.setStyleSheet("background-color: red;")
            # self.ui.tb_e_display.setStyleSheet("background-color: red;")
        else:
            self.ui.e_label_display.setText("Disengaged")
            self.ui.e_label_display.setStyleSheet("background-color: grey;")
            # self.ui.tb_e_display.setStyleSheet("background-color: grey;")
    
    def service_brake_state(self):
        try:
            temp_state = self.selected_train.get_service_brake()
            if temp_state:
                temp_state = False
                self.selected_train.set_service_brake(temp_state)
            else:
                temp_state = True
                self.selected_train.set_service_brake(temp_state)
        except KeyError:
            print("Key error service brake")
        except AttributeError:
            pass
        


    def display_service_brake_state(self):
        try:
            self.service_brake = self.selected_train.get_service_brake()
        except KeyError:
            print("Key error service brake")
        except AttributeError:
            #print("ignore this")
            pass
    
        if(self.service_brake == True):
            self.ui.s_label_display.setText("Engaged")
            self.ui.s_label_display.setStyleSheet("background-color: orange;")
            # self.ui.tb_s_display.setStyleSheet("background-color: orange;")
        else:
            self.ui.s_label_display.setStyleSheet("text-align: center;")
            self.ui.s_label_display.setText("Disengaged")
            self.ui.s_label_display.setStyleSheet("background-color: grey;")
            # self.ui.tb_s_display.setStyleSheet("background-color: grey;")


    # ---------------------------
    # door control
    # ---------------------------
    def is_left_door(self):
        try:
            temp_state = self.selected_train.get_left_door()

            if temp_state:
                temp_state = False
            else:
                if(self.selected_train.get_current_speed() == 0):
                    temp_state = True
                else:
                    temp_state = False
                
            self.selected_train.set_left_door(temp_state)
                
        except KeyError:
            print("Key error left door")
        except AttributeError:
            pass
    
    def left_door_control(self):
        try:
            self.left_door = self.selected_train.get_left_door()
        except KeyError:
            print("Key error left door")
        except AttributeError:
            #print("ignore this")
            pass
        
        if(self.left_door == False):
            self.ui.left_button.setStyleSheet("background-color: grey;")
            self.ui.left_button.setText("Close")
            # self.ui.tb_left_display.setText("Closed")
        else:
            self.ui.left_button.setStyleSheet("background-color: green;")
            self.ui.left_button.setText("Open")
            # self.ui.tb_left_display.setText("Opened")
        


    def is_right_door(self):
        try:
            temp_state = self.selected_train.get_right_door()

            if temp_state:
                temp_state = False
            else:
                if(self.selected_train.get_current_speed() == 0):
                    temp_state = True
                else:
                    temp_state = False
                
                
                
            self.selected_train.set_right_door(temp_state)
               
        except KeyError:
            print("Key error right door")
        except AttributeError:
            pass
    
    def right_door_control(self):
        try:
            self.right_door = self.selected_train.get_right_door()
        except KeyError:
            print("Key error right door")
        except AttributeError:
            #print("ignore this")
            pass
        

        if(self.right_door == False):
            self.ui.right_button.setStyleSheet("background-color: grey;")
            self.ui.right_button.setText("Close")
            # self.ui.tb_right_display.setText("Closed")
            
        else:
            
            self.ui.right_button.setStyleSheet("background-color: green;")
            self.ui.right_button.setText("Open")
            # self.ui.tb_right_display.setText("Opened")

    # ----------------------------
    # light control
    # ----------------------------
    def is_interior_light(self):
        try:
            temp_state = self.selected_train.get_interior_light()

            if temp_state:
                temp_state = False
                self.selected_train.set_interior_light(temp_state)
            else:
                temp_state = True
                self.selected_train.set_interior_light(temp_state)
        except KeyError:
            print("Key error interior light")
        except AttributeError:
            pass
    
    def interior_light_control(self):
        try:
            self.interior_light = self.selected_train.get_interior_light()
        except KeyError:
            print("Key error interior light")
        except AttributeError:
            #print("ignore this")
            pass
        

        if(self.interior_light == False):
            self.ui.interior_button.setStyleSheet("background-color: grey;")
            self.ui.interior_button.setText("Off")
            # self.ui.tb_interior_display.setText("Off")
        else:
            self.ui.interior_button.setStyleSheet("background-color: green;")
            self.ui.interior_button.setText("On")
            # self.ui.tb_interior_display.setText("On")
            
    def is_exterior_light(self):
        try:
            temp_state = self.selected_train.get_exterior_light()

            if temp_state:
                temp_state = False
                self.selected_train.set_exterior_light(temp_state)
            else:
                temp_state = True
                self.selected_train.set_exterior_light(temp_state)
        except KeyError:
            print("Key error exterior light")
        except AttributeError:
            pass
    
    def exterior_light_control(self):
        try:
            self.exterior_light = self.selected_train.get_exterior_light()
        except KeyError:
            print("Key error exterior light")
        except AttributeError:
            #print("ignore this")
            pass
        

        if(self.exterior_light == False):
            self.ui.exterior_button.setStyleSheet("background-color: grey;")
            self.ui.exterior_button.setText("Off")
            # self.ui.tb_exterior_display.setText("Off")
        else:
            self.ui.exterior_button.setStyleSheet("background-color: green;")
            self.ui.exterior_button.setText("On")
            # self.ui.tb_exterior_display.setText("On")
    
    # ----------------------------
    # temperature control
    # ----------------------------
    def set_commanded_temperature(self):
        self.temperature = self.ui.temp_slider.value()
        self.selected_train.set_commanded_temperature(self.temperature)   
        
    def current_temperature_control(self):
        try:
            self.current_temperature = self.selected_train.get_current_temperature()
        except KeyError:
            print("Key error current temperature")
        except AttributeError:
            #print("ignore this")
            pass
        
    # ----------------------------
    # authority control
    # ----------------------------
    def get_authority(self):
        try:
            self.authority = self.selected_train.get_authority()
            
            # print("ui : authority " + str(self.authority))
        except KeyError:
            print("Key error authority")
        except AttributeError:
           # print("shoueofnso")
            pass
        
        return self.authority
        
    # ----------------------------
    # fault control
    # ----------------------------
    def signal_fault_control(self):
        try:
            self.signal_fault = self.selected_train.get_signal_fault()

            if(self.signal_fault == True):
                self.ui.signal_txt.setStyleSheet("background-color: red;")
            else:
                self.ui.signal_txt.setStyleSheet("background-color: green;")
        except KeyError:
            print("Key error signal fault")
        except AttributeError:
            pass
        
    def engine_fault_control(self):
        try:
            self.engine_fault = self.selected_train.get_engine_fault()

            if(self.engine_fault == True):
                self.ui.engine_txt.setStyleSheet("background-color: red;")
            else:
                self.ui.engine_txt.setStyleSheet("background-color: green;")
        except KeyError:
            print("Key error engine fault")
        except AttributeError:
            pass
        
    def brake_fault_control(self):
        try:
            self.brake_fault = self.selected_train.get_brake_fault()

            if(self.brake_fault == True):
                self.ui.signal_txt.setStyleSheet("background-color: red;")
            else:
                self.ui.signal_txt.setStyleSheet("background-color: green;")
        except KeyError:
            print("Key error signal fault")
        except AttributeError:
            pass

    # ----------------------------
    # station name
    # ----------------------------
    def get_current_station(self):
        try:
            self.current_station = self.selected_train.get_current_station()
        except KeyError:
            pass
        except AttributeError:
            pass
        
        return self.current_station
    
    def get_next_station(self):
        try:
            self.next_station = self.selected_train.get_next_station()
        except KeyError:
            pass
        except AttributeError:
            pass
        
        return self.next_station
    
    
    def announce_stop(self):
        try: 
            self.selected_train.set_announcement(True)
        except KeyError:
            pass
        except AttributeError:
            pass
    
    # ----------------------------
    # connection buttons
    # ----------------------------
    def connection_button(self):
        # automation button
        self.ui.manual_button.clicked.connect(self.is_automatic_mode)
        
        # testbench button
       # self.ui.tb_load_data_display.clicked.connect(self.testbench_mode)
        
        # command speed
        self.ui.input_speed_slider.valueChanged.connect(self.set_command_speed)
        self.ui.input_speed_slider.valueChanged.connect(self.display_data)
        
        # station name
        self.ui.station_button.clicked.connect(self.display_data)
        
        # emergency brake
        self.ui.e_brake_button.clicked.connect(self.emergency_brake_state)
        
        # service brake  
        self.ui.s_brake_button.clicked.connect(self.service_brake_state)
        
        # lights detection
        self.ui.interior_button.clicked.connect(self.is_interior_light)
        self.ui.exterior_button.clicked.connect(self.is_exterior_light)
        
        # door detection
        self.ui.left_button.clicked.connect(self.is_left_door)
        self.ui.right_button.clicked.connect(self.is_right_door)
        
        # temperature sensor
        self.ui.temp_slider.valueChanged.connect(self.set_commanded_temperature)
        self.ui.temp_slider.valueChanged.connect(self.display_data)
        
        # power detection
        self.ui.kp_slider.valueChanged.connect(self.set_kp_value)
        self.ui.ki_slider.valueChanged.connect(self.set_ki_value)
        self.ui.kp_slider.valueChanged.connect(self.display_data)
        self.ui.ki_slider.valueChanged.connect(self.display_data)
        
        # time update slider
        self.ui.time_slider.valueChanged.connect(self.sim_time)
        self.ui.pause_button.clicked.connect(self.sim_pause)
        
        self.ui.station_button.clicked.connect(self.announce_stop)
        
        
        
    # ----------------------------
    # display the data
    # ----------------------------
    def display_data(self):
        # time
        self.ui.date_time_display.setText(sim.get_curr_string())
        self.ui.suggested_speed_display.setText(f'{(self.get_suggested_speed()):.2f}')
        
        # speed stuff
        if(self.automatic == False): 
            try:
                temp_state = self.selected_train.get_service_brake()
                if(temp_state == False):       
                    self.ui.input_speed_display.setText(f'{(self.get_suggested_speed()):.2f}')
                else:
                    self.ui.input_speed_display.setText(f'{0.0:.2f}')
            except KeyError:
                print("displaying command speed is not supported")
            except AttributeError:
            # print("shoueofnso")
                pass
                
        else:
            self.ui.input_speed_display.setText(f'{(self.command_speed):.2f}')
        
        self.ui.speed_limit_display.setText(f'{(self.get_speed_limit()):.2f}')
        
        self.ui.current_speed_display.setText(f'{(self.get_current_speed()):.2f}')
             
        
        # power things 
        self.ui.kp_display.setText(f'{(self.kp_value):.2f}')
        self.ui.ki_display.setText(f'{(self.ki_value):.2f}') 
        self.ui.used_power_display.setText(f'{(self.get_current_power()):.2f}')
       

        # temperatures
        self.ui.set_temp_display.setText(f'{(self.temperature):.2f}')
        self.ui.current_temp_display.setText(f'{(self.current_temperature):.2f}')
        
        # brakes
        self.display_emergency_brake_state()
        self.display_service_brake_state()

        # doors
        self.left_door_control()
        self.right_door_control()
        
        # light 
        self.interior_light_control()
        self.exterior_light_control()
        
        # automation
        self.Automation()
        
        # temperature
        self.current_temperature_control()
        
        # authority
        self.ui.authority_display.setText(f"{(self.get_authority()):.2f}")
        
        # faults
        self.signal_fault_control()
        self.engine_fault_control()
        self.brake_fault_control()
        
        
        self.ui.station_display.setText(str(self.get_current_station()))
        self.ui.output_stop_display.setText(str(self.get_next_station()))
    # ----------------------------
    # automatic stuff
    # ----------------------------
        
    def is_automatic_mode(self):
        try:
            temp_state = self.selected_train.get_automatic_mode()

            #print("ui: temp auto " + str(temp_state))
            
            if temp_state:
                temp_state = False
                self.selected_train.set_automatic_mode(temp_state)
            else:
                temp_state = True
                self.selected_train.set_automatic_mode(temp_state)
        except KeyError:
            print("Key error auto")
        except AttributeError:
            #print("Attribute error auto")
            pass
        
    # setting the manual and automatic modes
    def Automation(self):
        try:
            self.automatic = self.selected_train.get_automatic_mode()
        except KeyError:
            print("Key error auto")
        except AttributeError:
            pass
        
        if(self.automatic == False):
            try:
                self.command_speed = self.selected_train.get_command_speed()
                self.kp_value = self.selected_train.get_kp()
                self.ki_value = self.selected_train.get_ki()
                self.temperature = self.selected_train.get_commanded_temperature()
                self.power = self.get_current_power()
                self.speed_limit = self.selected_train.get_speed_limit()
                # self.service_brake = self.service_brake_state()
            # key, value
            #for key, value in railline.trains.items():
            # if value == "Yard"
            #   delete the dropdown item
            # if value != yard add the item and set the trian
            # id to the dropdown item 
            
            except KeyError:
                print("Key error auto")
            except AttributeError:
                pass
            
            #print("ui: command speed " + str(self.command_speed))
            
            self.ui.input_speed_slider.setStyleSheet("background-color: grey;")
            self.ui.input_speed_slider.setEnabled(False)
            self.ui.input_speed_slider.setValue(self.command_speed)
                        
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
            
            self.ui.temp_slider.setStyleSheet("background-color: grey;")
            self.ui.temp_slider.setEnabled(False)
            self.ui.temp_slider.setValue(self.temperature)
            
            self.ui.kp_slider.setStyleSheet("background-color: grey;")
            self.ui.kp_slider.setEnabled(False)
            self.ui.kp_slider.setValue(self.kp_value)
            
            self.ui.ki_slider.setStyleSheet("background-color: grey;")
            self.ui.ki_slider.setEnabled(False)
            self.ui.ki_slider.setValue(self.ki_value)
            
            # self.ui.s_label_display.setStyleSheet("background-color: grey;")
            # self.ui.s_label_display.setEnabled(False)
            
            self.ui.s_brake_button.setStyleSheet("background-color: grey;")
            self.ui.s_brake_button.setEnabled(False)
            
        else:
            # setting current speed back to manual
            #self.ui.current_speed_display.display(suggested_speed)
            self.get_speed_limit()
            
            # give the access back
            self.ui.input_speed_slider.setStyleSheet(self.ui.original_input_speed)

            if(self.get_speed_limit() != 0):
                self.ui.input_speed_slider.setMaximum(self.get_speed_limit())
                
            self.ui.input_speed_slider.setEnabled(True)
            
            self.ui.station_button.setStyleSheet(self.ui.original_station)
            self.ui.station_button.setEnabled(True)
            
            self.ui.left_button.setStyleSheet(self.ui.original_left)
            self.left_door_control()
            self.ui.left_button.setEnabled(True)
            
            self.ui.right_button.setStyleSheet(self.ui.original_right)
            self.right_door_control()
            self.ui.right_button.setEnabled(True)
            
            self.ui.interior_button.setStyleSheet(self.ui.original_interior)
            self.interior_light_control()
            self.ui.interior_button.setEnabled(True)
            
            self.ui.exterior_button.setStyleSheet(self.ui.original_exterior)
            self.exterior_light_control()
            self.ui.exterior_button.setEnabled(True)
            
            self.ui.temp_slider.setStyleSheet(self.ui.original_temp_slider)
            self.ui.temp_slider.setEnabled(True)
            
            self.ui.kp_slider.setStyleSheet(self.ui.original_kp)
            self.ui.kp_slider.setEnabled(True)
            
            self.ui.ki_slider.setStyleSheet(self.ui.original_ki)
            self.ui.ki_slider.setEnabled(True)
            
            self.ui.s_brake_button.setStyleSheet(self.ui.original_s_brake)
            self.ui.s_brake_button.setEnabled(True)
            
        
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrainCtrlUi()
    window.show() 
    sys.exit(app.exec())