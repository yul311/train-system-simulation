import numpy
from scipy.signal import TransferFunction, freqz
from typing import Optional
from PySide6.QtWidgets import (QApplication, QMainWindow, QSlider, QScrollArea, QPushButton, QLCDNumber, QTableWidgetItem, QMessageBox, QGraphicsView,
                               QGraphicsRectItem, QGraphicsScene, QHBoxLayout, QWidget, QLabel, QGraphicsItem, QVBoxLayout)
from PySide6.QtCore import QFile, Slot,QDate, QTime, QTimer, QDateTime, Qt, QEvent, QRectF
from PySide6.QtGui import QPalette, QColor, QIntValidator, QBrush, QPen, QPixmap
from PySide6.QtUiTools import QUiLoader

from Train_Controller.speed_controller import *
from Train_Controller.beacon_decoder import *
from Train_Controller.authority_logic import *

from Train_Controller.conversion import *

from Main.simulation_time import sim
from datetime import datetime

# testing stuff
from Train_Controller.rail_layout.database import *
from Train_Controller.rail_layout.legos import *

class TrainController():
    
    distance_brake: bool
    speed_brake: bool
    
    train_model_link: any 
    
    current_speed_main: float = 0
    command_speed_main: float = 0
    speed_limit_main: float = 0
    suggest_speed_main: float = 0

    service_brake: bool = False
    
    current_power_main: int = 0
    kp_main: float = 0
    ki_main: float = 0
    

    left_door_main: bool = False
    right_door_main: bool = False
    
    interior_light_main: bool = True
    exterior_light_main: bool = False

    temperature_main: int = 0
    current_temperature_main: int = 0
    
    brake_fault_main: bool = False
    engine_fault_main: bool = False
    signal_fault_main: bool = False
    
    polarity: bool = False
    old_polarity: bool = False

    current_authority: float = 0.0
    commanded_authority: float = 0.0
    
    manual: bool = False

    interval: int = 0
    new_time: int = 0
    old_time: int = 0
    
    simulation_speed: float = 0
    
    train_id: None
    train_line: None
    
    current_station: str = ""
    next_station: str = ""
    
    station_exit: bool = False
    block_grade: float = 0.0
    elevation: float = 0.0
    cumulative_elevation: float = 0.0
    underground: bool = False
    
    announcement: bool = False
    
    #--------------------------------------------------------------------------
    # constructor
    #--------------------------------------------------------------------------
    def __init__(self):
        self.distance_brake = False     # +Justin
        self.speed_brake = False        # +Justin
        
        self.localSpeedController = SpeedController()
        self.localBeaconDecoder = BeaconDecoder()
        self.localAuthorityLogicCtrl = AuthorityLogicCtrl()
        
        self.beacon1 = []
        self.beacon2 = []
        self.passenger_brake = False
        self.service_brake = False
        self.tc_instance = None # = tc
        
        self.trainid = None
        self.selected_train = None
        self.old_time = sim.get_curr_serial()
        self.current_authority = self.get_authority()
        self.interval = sim.get_sim_speed()*50/1000

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.time_update)
        # orginial is 100
        self.update_timer.setInterval(50)
        self.update_timer.start()  
        
        # ----
        # beacon stuff
        # ----
    
        self.localBeaconDecoder.build_green_rail_system()
        
    # linking the api 
    
    def link_train_model(self, api:any):
        self.train_model_link = api

    def delete_train(self):
        self.update_timer.stop()
        del self.update_timer
        del self.localAuthorityLogicCtrl
        del self.localBeaconDecoder
        del self.localSpeedController
        del self.train_model_link
        
    # ----------------------------------------------------------------
    # set communication with frontend 
    # ----------------------------------------------------------------
    def time_update(self):        
 
        self.interval = sim.get_sim_speed()*50/1000 
        
        self.automatic_control()
        self.to_model()

        
    def set_train_id(self, id: int):
        self.train_id = id
        
    def set_train_line(self, line: str):
        self.train_line = line
        self.localBeaconDecoder.set_train_line(self.train_line)
        
        
        if(self.train_line == "green"):
            self.localBeaconDecoder.build_green_rail_system()
        elif(self.train_line == "red"):
            # self.localBeaconDecoder.build_red_rail_system()
            pass

    # speed links
    def set_command_speed(self, command_speed):
        self.command_speed_main = mph_to_mps(command_speed)
        
    def get_command_speed(self):
        return mps_to_mph(self.command_speed_main)
    
    def set_current_speed(self, current_speed):
        self.current_speed_main = current_speed
        # mps
    
    def get_current_speed(self):
        return mps_to_mph(self.current_speed_main)
     
    def set_suggested_speed(self, suggested_speed):
        self.suggest_speed_main = mps_to_mph(suggested_speed)
    
    def get_suggested_speed(self):
        return (self.suggest_speed_main)
    
    # speed limit i would know that bc of the track layout
    def set_speed_limit(self, speed):
        self.speed_limit_main = speed
        
    def get_speed_limit(self):
        return kph_to_mph(self.speed_limit_main)

    # power links
    def set_kp(self, kp):
        self.kp_main = kp

    def set_ki(self, ki):
        self.ki_main = ki
        
    def get_kp(self):
        return self.kp_main
    
    def get_ki(self):
        return self.ki_main
        
    def get_current_power(self):
        return self.current_power_main

    # brake links
    def set_passenger_brake(self, brake):
        self.passenger_brake = brake

    def get_passenger_brake(self):
        return self.passenger_brake  
    
    def set_service_brake(self, service_brake):
        self.service_brake = service_brake
        
    def get_service_brake(self):
        return self.service_brake
                
    # door links
    def set_left_door(self, left):
        self.left_door_main = left

    def get_left_door(self):
        return self.left_door_main
    
    def set_right_door(self, right):
        self.right_door_main = right
        
    def get_right_door(self):
        return self.right_door_main
    
    # light links
    def set_interior_light(self, light):
        self.interior_light_main = light
        
    def get_interior_light(self):
        return self.interior_light_main
    
    def set_exterior_light(self, exterior):
        self.exterior_light_main = exterior
        
    def get_exterior_light(self):
        return self.exterior_light_main
    
    # temperature links
    def set_commanded_temperature(self, temperature):
        self.temperature_main = f_to_c(temperature)
    
    def get_commanded_temperature(self):
        return c_to_f(self.temperature_main)
        
    def set_current_temperature(self, temperature):
        self.current_temperature_main = temperature
        
        
    def get_current_temperature(self):
        return c_to_f(self.current_temperature_main)
    
    # faults links -- needs to be linked
    def set_failures(self, brake, engine, signal):
        self.set_brake_fault(brake)
        self.set_engine_fault(engine)
        self.set_signal_fault(signal)
    
    def set_signal_fault(self, fault):
        self.signal_fault_main = fault
    
    def get_signal_fault(self):
        return self.signal_fault_main
    
    def set_engine_fault(self, fault):
        self.engine_fault_main = fault
    
    def get_engine_fault(self):
        return self.engine_fault_main
    
    def set_brake_fault(self, fault):
        self.brake_fault_main = fault
    
    def get_brake_fault(self):
        return self.brake_fault_main
    
    # beacon stuff
    def set_polarity(self, polarity):
        self.polarity = polarity
        
        self.localBeaconDecoder.set_polarity(self.polarity)
        
        self.localBeaconDecoder.decoder()

    # authority
    def set_authority(self, authority):
        self.commanded_authority = authority
        #print("authority: ", authority)
    
    def get_authority(self):
        return m_to_ft(self.current_authority)
    
    
    # beacon stuff
    def set_beacon_package(self, beacon1, beacon2):
        self.localBeaconDecoder.set_encoded_data(beacon1, beacon2)
       

    # ---------------------------------
    # speed controller
    # ---------------------------------
    def speed_control(self):
        if(self.manual == False):
            self.localSpeedController.set_commanded_speed(self.suggest_speed_main)
        else:
            self.localSpeedController.set_commanded_speed(self.command_speed_main)
           
        self.localSpeedController.set_current_speed(self.current_speed_main)
        self.localSpeedController.set_kp_value(self.kp_main)
        self.localSpeedController.set_ki_value(self.ki_main)
        self.localSpeedController.set_interval(self.interval)
        
        
        self.localSpeedController.calculate_power()
        
        self.current_power_main = self.localSpeedController.get_current_power()
        
    # ---------------------------------
    # authority stuff
    # ---------------------------------
    def authority_control(self):
        
        # print("main : current speed " + str(self.current_speed_main))
        self.localAuthorityLogicCtrl.set_auto(self.manual)
        self.localAuthorityLogicCtrl.set_authority(self.commanded_authority)
        self.localAuthorityLogicCtrl.set_current_speed(self.current_speed_main)
        self.localAuthorityLogicCtrl.set_interval(self.interval)    
        self.localAuthorityLogicCtrl.set_polarity(self.polarity)
        self.localAuthorityLogicCtrl.traveled_distance()
        
        temp = self.localAuthorityLogicCtrl.get_brake_indicator()
        
        if temp:            # +Justin
            self.distance_brake = True      
            #self.set_service_brake(temp)
        else:
            self.distance_brake = False
        
        self.current_authority = self.localAuthorityLogicCtrl.get_new_authority()
        
        
    def beacon_control(self):
        self.localBeaconDecoder.set_polarity(self.polarity)
        try:
            self.speed_limit_main = self.localBeaconDecoder.get_speed_limit()
            self.current_station = self.localBeaconDecoder.get_current_station()
            self.next_station = self.localBeaconDecoder.get_next_station()
            self.block_grade = self.localBeaconDecoder.get_block_grade()
            
            if(self.get_current_speed() <= 0 and self.localBeaconDecoder.current_position != 0 and self.distance_brake == True):

                self.train_model_link.send_announcement("At station " + str(self.current_station))

                if(self.localBeaconDecoder.get_station_exit() == 2):
                    self.set_right_door(True)
                elif(self.localBeaconDecoder.get_station_exit() == 1):
                    self.set_left_door(True)
                elif(self.localBeaconDecoder.get_station_exit() == 0):
                    self.set_right_door(True)
                    self.set_left_door(True)
            elif(self.localAuthorityLogicCtrl.get_brake_indicator()):
                self.train_model_link.send_announcement("We are approaching station " + str(self.next_station))
            elif(self.localBeaconDecoder.get_current_station() == "Yard"):
                self.train_model_link.send_announcement("At station " + str(self.next_station))
            else:
                self.train_model_link.send_announcement("")
                self.set_right_door(False)
                self.set_left_door(False)
            
            
      
                    
        except AttributeError:
            pass
        
            
    def get_current_station(self):
        return self.current_station 
    
    def get_next_station(self):
        return self.next_station
    
                    
    def set_announcement(self, announcement):
        self.announcement = announcement
        
        
        
    # ---------------------------------
    # automatic stuff
    # ---------------------------------
    def set_automatic_mode(self, mode):
        self.manual = mode
        
    def get_automatic_mode(self):
        return self.manual
    
    def automatic_control(self):
        if(self.manual == False):
            self.set_command_speed(self.suggest_speed_main)
            self.set_kp(10000)
            self.set_ki(2000)
            self.set_commanded_temperature(72.0)
            self.set_interior_light(True)
            
            
            self.speed_control()
            self.beacon_control()
            self.authority_control()

            if(self.current_speed_main > self.command_speed_main):      # +Justin
                self.speed_brake = True
            elif(self.current_speed_main <= self.command_speed_main):
                self.speed_brake = False
                
            self.set_service_brake(self.distance_brake or self.speed_brake) # +Justin
                
            if(self.get_brake_fault() == False):
                if(self.get_engine_fault() == True or self.get_signal_fault() == True or self.passenger_brake == True or self.service_brake == True):
                    self.localSpeedController.power_zero() 
                    self.current_power_main = 0
                    self.command_speed_main = 0
                    
            if(self.localBeaconDecoder.get_underground() == True):
                self.set_interior_light(True)
                self.set_exterior_light(True)
            elif(self.localBeaconDecoder.get_underground() == False):
                self.set_exterior_light(False)
        
        elif(self.manual == True): 
            # self.set_interior_light(True)
            self.speed_control()
            self.beacon_control()
            self.authority_control()
            
            self.distance_brake = False     # +Justin
            self.speed_brake = False        # +Justin
            
            if(self.get_brake_fault() == False):
                if(self.get_engine_fault() == True or self.get_signal_fault() == True or self.passenger_brake == True or self.service_brake == True):
                    self.localSpeedController.power_zero() 
                    self.current_power_main = 0
                    self.command_speed_main = 0
                    
            # if(self.get_current_speed() != 0 and self.distance_brake == False):
            #     self.set_left_door(False)
            #     self.set_right_door(False)
            
        
            
        
            
    # ---------------------------------
    # to model data
    # ---------------------------------
    def to_model(self):
        try:
            self.train_model_link.send_motor_command(self.current_power_main, self.command_speed_main)

            self.train_model_link.send_service_brake_command(self.service_brake)
            
            self.train_model_link.send_emergency_brake_command(self.passenger_brake)
            
            self.train_model_link.send_doors(self.left_door_main, self.right_door_main)
            
            self.train_model_link.send_lights(self.interior_light_main, self.exterior_light_main)

            self.train_model_link.send_temperature_command(self.temperature_main)
            
            self.train_model_link.send_block_data(self.block_grade, False, self.speed_limit_main)
        
            
            
                
            if(self.announcement == True):
                self.train_model_link.send_announcement("At station " + str(self.current_station))
            
        except AttributeError:
            pass
    

   

   