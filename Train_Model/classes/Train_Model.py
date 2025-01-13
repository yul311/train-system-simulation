import math
import random
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
from datetime import datetime
from Main.simulation_time import sim
from Track_Model.API.train_to_track import TrainTrackAPI
from Train_Controller.trainmodelcontrollerAPI import TrainControllerAPI
from Train_Model.classes.tm_brakes import TrainBrakes
from Train_Model.classes.tm_lights import TrainLights
from Train_Model.classes.tm_doors import TrainDoors
from Train_Model.classes.tm_failures import TrainFailures


# train class
class TrainModel: 
    
    # Declaring constants (Train Base Mass in kg)
    TRAINBASEMASS: float = 40946.69 #kg
    acceleration_limit: float = 0.5 #m/s^2
    e_brake_decele: float = -2.73 
    service_brake_decele: float = -1.2 
    max_speed: float = 19.4444 #m/s

    #variables that will only be passed
    authority: int = 0.00 #m
    suggested_speed: float = 0.00 #m/s

    #Declaring variables
    train_id: int
    train_line: str
    announcements: str = " "
    power_command: float = 0.0 #watts
    current_speed: float = 0.00 #m/s
    commanded_speed: float = 0.00 
    speed_limit: float = 43.00
    acceleration: float = 0.00
    a_n: float = 0.00
    force: float = 0.00
    gforce: float = 0.00
    frforce: float = 0.00
    block_Grade: float = 0.00
    tunnel_underground: bool = False
    block_change: bool = False
    num_block_change: int = 0
    num_crew: int = 2
    num_passenger: int = 0
    total_mass: float = 40946.69 #kg
    current_temperature: float = 30 #celsius
    temperature_command: float = 30 #celsius
    
    track_link: TrainTrackAPI
    ctrl_link: TrainControllerAPI

    #time variables
    timer: QTimer
    temptimer: QTimer
    interval: int = 0
    temp_time: int = 0
    temp_delta: float = 0

    def __init__(self):
        self.lights = TrainLights(False, False)
        self.doors = TrainDoors(False, False)
        self.brakes = TrainBrakes(False, False)
        self.failures = TrainFailures(False, False, False)
        
        self.train_id = None
        self.train_line = None
        self.track_link = None
        self.ctrl_link = None
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_update)
        self.timer.start(50)
        
        self.temptimer = QTimer()
        self.temptimer.timeout.connect(self.calc_current_temp)
        self.temptimer.start(1000)
    
    #link api 
    def link_track_model(self, track_api: TrainTrackAPI):
        self.track_link = track_api
    
    def link_train_control(self, ctrl_api: TrainControllerAPI):
        self.ctrl_link = ctrl_api
        
    def delete_train(self):
        self.timer.stop()
        del self.timer
        del self.lights
        del self.doors
        del self.brakes
        del self.failures
        del self.track_link
        del self.ctrl_link

    def time_update(self):
        #functions to be updated with the timer refreshing
        self.interval = sim.get_sim_speed()*50/1000
        self.calc_force()
        self.calc_acceleration()
        self.calc_current_speed()
        self.calc_total_mass()

    # Calculation Functions
        
    def calc_force(self):
        #F_g = mgsin(theta)
        #blockgrade = sin(theta)
        theta = math.atan(self.block_Grade/100)
        self.gforce = self.total_mass*9.8*math.sin(theta)

        #friction
        frictcoeff = 0.001
        #if train is on slope, normal force = mgcos(theta)
        if(self.block_Grade > 0.00):
            normalforce = self.total_mass*9.8*math.cos(theta)
        else:
            normalforce = self.total_mass*9.8
        
        self.frforce = frictcoeff*normalforce

        #if engine/signal pickup/brake failure or doors are open
        if(self.failures.get_engine_failure_state() == True or self.failures.get_signal_pickup_failure_state() == True or self.failures.get_brake_failure_state() == True or self.doors.get_left_door_state() == True or self.doors.get_right_door_state() == True):
            self.power_command = 0
        
        try:
            if(self.brakes.get_emergency_brake_state() == False):
                if(self.brakes.get_service_brake_state() == False):
                    #if emergency and service brake not on
                    self.force = (self.power_command/self.current_speed) - self.gforce - self.frforce
                else:
                    #if service brake on
                    self.power_command = 0
                    self.force = (self.power_command/self.current_speed) - self.gforce - self.frforce + self.service_brake_decele*self.total_mass
            else: 
                #emergency brake on
                self.power_command = 0
                self.force = (self.power_command/self.current_speed) - self.gforce - self.frforce + self.e_brake_decele*self.total_mass
        #if current speed is zero
        except ZeroDivisionError:
                if(self.brakes.get_emergency_brake_state() == False):
                    if(self.brakes.get_service_brake_state() == False):
                        #if emergency and service brake not on
                        self.force = self.power_command - self.gforce 
                    else:
                        #if service brake on
                        self.power_command = 0
                        self.force = self.power_command - self.gforce + self.service_brake_decele*self.total_mass
                else: 
                    #emergency brake on
                        self.power_command = 0
                        self.force = self.power_command - self.gforce + self.e_brake_decele*self.total_mass

    def calc_acceleration(self):
        #a = f/m
        self.acceleration = self.force/self.total_mass

        #if acceleration is greater than the limit, set it to the limit
        if(self.acceleration>self.acceleration_limit):
            self.acceleration = self.acceleration_limit

        #if acceleration is less than 2.73, set it to the limit
        elif(self.acceleration<self.e_brake_decele):
            self.acceleration = self.e_brake_decele

    def calc_current_speed(self):
        a_n_previous = self.a_n
        self.a_n = self.acceleration
        self.current_speed = self.current_speed + self.interval/2*(self.a_n + a_n_previous)
        if(self.current_speed < 0):
            self.current_speed = 0
        self.track_link.send_current_speed(self.train_id, self.current_speed)
        self.ctrl_link.send_current_speed(self.current_speed)
        
    def calc_total_mass(self):
        #make average weight like 80 kg and just multiply by number of passengers (including crew)
        self.total_mass = (self.num_passenger+self.num_crew)*80 + self.TRAINBASEMASS

    def calc_current_temp(self):
        self.temp_time = self.temp_time + 1
        if(self.temp_time < 5):
            self.current_temperature = self.temp_delta + self.current_temperature
        elif(self.temp_time >= 5):
             self.current_temperature = self.temperature_command
        self.ctrl_link.send_current_temperature(self.current_temperature)

    #---------------------------------------------------------------
    # Functions to get information from Track Model
    #---------------------------------------------------------------
    def set_authority(self, auth: float):
        if(auth >= 0 and self.failures.get_signal_pickup_failure_state() == False):
            self.authority = auth
            self.ctrl_link.send_authority(self.authority)
        elif(self.current_speed > 0 and auth == 0):
            raise Exception(f"Authority can't be '{auth}' when current speed isn't zero")
        elif(auth < 0):
            raise Exception(f"Authority can't be negative '{auth}'")
        else:
            raise Exception("Signal Pickup fault is currently active")
        
    def set_suggested_speed(self, speed: float):
        #if commanded speed is nonnegative and less than/equal to max speed
        if(speed >= 0 and speed <= self.max_speed and self.failures.get_signal_pickup_failure_state() == False):
            self.suggested_speed = speed
            self.ctrl_link.send_suggested_speed(self.suggested_speed)
        elif(speed > self.max_speed):
            raise Exception(f"'{speed} is over the max speed of the train")
        elif(self.failures.get_signal_pickup_failure_state() == True):
            raise Exception("Signal Pickup fault is currently active")
        else:
            raise Exception(f"Train Model Suggested Speed Error:{speed} is negative") 
        
    def set_coded_beacon(self, beacon1, beacon2):
        if(self.failures.get_signal_pickup_failure_state() == False):
            self.ctrl_link.send_beacon_package(beacon1, beacon2)
        else: 
            raise Exception("Signal Pickup fault is currently active")

    def set_ticket_sales(self, ticketsale: int):
        if(self.failures.get_signal_pickup_failure_state() == False):
            if(ticketsale >= 0):
               self.num_passenger += ticketsale
            else:
                raise Exception(f"'{ticketsale}' is not a valid ticket sale entry")
        else:
            raise Exception("Signal Pickup fault is currently active")

    def set_block_change(self, block_c: bool):
        if(self.failures.get_signal_pickup_failure_state() == False):  
            # block_old = self.block_change
            # self.block_change = block_c
            # if(block_c == True and block_old == False):
            #    self.num_block_change += 1
            self.ctrl_link.send_polarity(block_c)
        else:
            raise Exception("Signal Pickup fault is currently active")

    def set_train_id(self, id: int):
        #print("train model ID set")
        self.train_id = id
        self.ctrl_link.send_train_id(id)

    def set_train_line(self, tr_line: str):
        #print("train Line set MODEL")
        self.train_line = tr_line
        self.ctrl_link.send_train_line(tr_line)

    #---------------------------------------------------------------
    # Functions to get information from Train Controller
    #---------------------------------------------------------------
    def set_commanded_speed(self, commanded_speed: float):
        #if commanded speed is nonnegative and less than/equal to max speed
        if(commanded_speed >= 0 and commanded_speed <= self.max_speed):
            self.commanded_speed = commanded_speed
        elif(commanded_speed > self.max_speed):
            raise Exception(f"'{commanded_speed} is over the max speed of the train")
        else:
            raise Exception(f"Train Model Commanded Speed Error:{commanded_speed} is negative")            

    def set_power_command(self, power_com: float):
        if(power_com <= 120000):
            self.power_command = power_com
        else:
            raise Exception(f"'{power_com}' is over the max motor power of the train")

    def set_announcement(self, annonce: str):
        self.announcements = annonce

    def set_light_commands(self, int: bool, ext: bool):
        self.lights.set_internal_lights(int)
        self.lights.set_external_lights(ext)

    def set_door_commands(self, left: bool, right: bool):
        #passenger get off code
        left_old = self.doors.get_left_door_state()
        right_old = self.doors.get_right_door_state()
        if((left == True and left_old == False) or (right == True and right_old == False)):
            passengeroff = random.randint(0, self.num_passenger)
            self.track_link.send_leaving_passengers(self.train_id,passengeroff)
            self.num_passenger = self.num_passenger - passengeroff

        self.doors.set_left_door(left)
        self.doors.set_right_door(right)

    def set_emergency_command(self, emergency: bool):
        if(self.failures.get_brake_failure_state() == False):
            self.brakes.set_emergency_brake(emergency)
        else:
            raise Exception("Train brake failure is raised")

    def set_service_command(self, service: bool):
        if(self.failures.get_brake_failure_state() == False):
            self.brakes.set_service_brake(service)
        else:
            raise Exception("Train brake failure is raised")

    def set_temperature_command(self, temp_com: float):
        self.temperature_command = temp_com
        self.temp_time = 0
        self.temp_delta = (self.temperature_command - self.current_temperature)/float(5)

    def set_block_data(self, block_g: float, tun_under: bool, limit: float):
        self.block_Grade = block_g
        self.tunnel_underground = tun_under
        self.speed_limit = limit
