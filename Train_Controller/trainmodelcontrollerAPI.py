import dataclasses
from Train_Controller.train_controller import *

# model to me 

@dataclasses.dataclass(frozen = True)
class TrainControllerAPI:
    train_controller: TrainController

    # get the current speed from the model
    def send_current_speed(self, speed):
        #print("tm -> tc: send curr speed")

        self.train_controller.set_current_speed(speed)
        # print("tm -> tc: current speed " + str(speed))

    # get the authority from the track circuit 
    def send_authority(self, authority):

        #print("tm -> tc: send auth")

        self.train_controller.set_authority(authority)


    # get the suggested speed from the track circuit 
    def send_suggested_speed(self, speed):
        #print("tm -> tc: send sugg speed")

        self.train_controller.set_suggested_speed(speed)
        
        #print("tm -> tc: suggest speed " + str(speed))
    
    # get the bool for the failures 
    def send_failures(self, brake, engine, signal):
        #print("tm -> tc: send fault")
        self.train_controller.set_failures(brake, engine, signal)
        
    def send_current_temperature(self, temp):
        self.train_controller.set_current_temperature(temp)
        
    def send_passenger_emergency_brake(self, brake):
        self.train_controller.set_passenger_brake(brake)

    def send_train_id(self, id: int):
        #print("tm -> tc: send train id")
        self.train_controller.set_train_id(id)

    def send_train_line(self, tr_line: str):
        #print("tm -> tc: send train line speed")
        self.train_controller.set_train_line(tr_line)

    # get the block ids of the rails
    def send_beacon_package(self, beacon1, beacon2):
        self.train_controller.set_beacon_package(beacon1, beacon2)
        # print("tm to tc beacon 1 " + str(beacon1) + " " + str(beacon2)
        
        
    def send_polarity(self, polarity):
        self.train_controller.set_polarity(polarity)
