import dataclasses

#import train model class
from Train_Model.classes.Train_Model import TrainModel

class ControllerTrainModelAPI:

    def __init__(self, tm: TrainModel):
        self.tm = tm

    def send_motor_command(self, power_command: float, commanded_speed: float):
        self.tm.set_commanded_speed(commanded_speed)
        self.tm.set_power_command(power_command)
        #print("tc -> tm sending motor control")

    def send_announcement(self, announcement: str):
        self.tm.set_announcement(announcement)
        #print("tc -> tm sending announcements")

    def send_doors(self, left: bool, right: bool):
        self.tm.set_door_commands(left, right)
        #print("tc -> tm sending door commands (left, right)")
 
    def send_lights(self, internal: bool, external: bool):
        self.tm.set_light_commands(internal, external)
        #print("tc -> tm sending light commands (internal, external)")

    def send_emergency_brake_command(self, emergency: bool):
        self.tm.set_emergency_command(emergency)
        #print("tc -> tm sending e-brakes command")

    def send_service_brake_command(self, service: bool):
        self.tm.set_service_command(service)
        #print("tc -> tm sending service brakes command")

    def send_block_data(self, block_grade: float, tunnel_under: bool, speed_limit: float):
        self.tm.set_block_data(block_grade, tunnel_under, speed_limit)
        #print("tc -> tm sending tunnel or underground status")

    def send_temperature_command(self, temperature_command: int):
        self.tm.set_temperature_command(temperature_command)
        #print("tc -> tm sending temperature command")
        