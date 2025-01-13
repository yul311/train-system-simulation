
import dataclasses
from Train_Model.classes.Train_Model import TrainModel

@dataclasses.dataclass(frozen=False)
class TrackTrainModelAPI:

    def __init__(self, tm: TrainModel):
        self.tm = tm        
    
    def send_train_id(self, id:int):
        #print('track -> tm id')
        self.tm.set_train_id(id)

    def send_line(self, line:str):
        print('track_to_tm line: ' + str(line))
        self.tm.set_train_line(line)


    def send_authority(self, authority: int):
        #print('track -> tm auth: ' + str(authority))
        self.tm.set_authority(authority)
        #print("Track Model sending authority")

    def send_suggested_speed(self, suggested_speed: float):
        #print('track -> tm sg speed: ' + str(suggested_speed))
        self.tm.set_suggested_speed(suggested_speed)
        #print("Track Model sending suggested speed")

    def send_beacon_package(self, beacon1, beacon2):
        #print("track -> tm beacon")
        self.tm.set_coded_beacon(beacon1, beacon2)

    def send_ticket_sale(self, ticket_sale: int):
        self.tm.set_ticket_sales(ticket_sale)
        #print("track -> tm tickets")

    def send_polarity_change(self, changed: bool):
        self.tm.set_block_change(changed)
        #print("track -> tm polarity")
