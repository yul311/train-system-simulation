# train brakes class
class TrainBrakes:     

    def __init__(self, emergency: bool, service: bool):
        self.emergency_brake = emergency
        self.service_brake = service

    #mutators
    def set_emergency_brake(self, emerg: bool):
        self.emergency_brake = emerg

    def set_service_brake(self, service: bool):
       # print("setting service brake")
        self.service_brake = service

    #accessors
    def get_emergency_brake_state(self):
        return self.emergency_brake 

    def get_service_brake_state(self):
        return self.service_brake
    
    def disable_brakes(self):
        self.emergency_brake = False
        self.service_brake = False