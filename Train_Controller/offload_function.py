### 
# ------------------------------
# test bench
# ------------------------------
def testbench_mode(self):
    # emergency brake
    
    self.ui.tb_e_brake_button.clicked.connect(self.emergency_brake_state)
    
    
    # faults
    self.ui.tb_signal_display.clicked.connect(self.fault_detection)
    self.ui.tb_engine_display.clicked.connect(self.fault_detection)
    self.ui.tb_brake_display.clicked.connect(self.fault_detection)
    
    # temperature 
    self.ui.tb_temp_display.display(self.temperature)
    
    # power display
    self.ui.tb_power_display.display(self.power)
    
    if (self.ui.tb_speed_limit_display.toPlainText()):
        speed_limit = int(self.ui.tb_speed_limit_display.toPlainText()) 
        self.set_speed_limit_ui(speed_limit)
        
    
    # suggested speed
    if (self.ui.tb_suggested_speed_display.toPlainText()):
        suggested_speed = int(self.ui.tb_suggested_speed_display.toPlainText()) 
        self.set_suggested_speed_ui(suggested_speed)
        
    self.ui.tb_temp_display.display(self.temperature)
    
    

# load the test values
def load_data(self):

    if (self.ui.tb_speed_limit_display.toPlainText()):
        speed_limit = int(self.ui.tb_speed_limit_display.toPlainText()) 
        self.set_speed_limit(speed_limit)
        
    
    # suggested speed
    if (self.ui.tb_suggested_speed_display.toPlainText()):
        suggested_speed = int(self.ui.tb_suggested_speed_display.toPlainText()) 
        self.set_suggested_speed(suggested_speed)
    
        
        
    self.display_data()
    
    # ---------------------------
    # station control
    # ---------------------------
    
    ## TODO: this need to be done once the physics are working
    def set_authority_ui(self, value):
        self.authority = value
        
    def set_station_name_ui(self, value):
        self.station_name = value
        
    def set_tunnel_ui(self, value):
        self.tunnel = value
        
   
        
    
################################################################
    

    
   # ---------------------------------
    # to model data
    # ---------------------------------
    def to_model(self):
        self.train_model_link.send_service_brake_command(self.service_brake_main)
        self.train_model_link.send_emergency_brake_command(self.passenger_brake)
        
    # ---------------------------------
    # motor controller
    # ---------------------------------
    def motor_control(self):
        self.train_model_link.send_motor_command(self.current_power_main, float(self.command_speed_main))

    # ---------------------------------
    # door controller
    # ---------------------------------
    def door_control(self):
        self.train_model_link.send_doors(self.left_door_main, self.right_door_main)
        
    # ---------------------------------
    # light controller
    # ---------------------------------
    def light_control(self):
        self.train_model_link.send_lights(self.interior_light_main, self.exterior_light_main)

    # ---------------------------------
    # temperature controller
    # ---------------------------------
    def temperature_control(self):
        self.train_model_link.send_temperature_command(self.temperature_main)
    

    