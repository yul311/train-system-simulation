import dataclasses
#from Track_Model.Controller import greenLine #, redLine

@dataclasses.dataclass(frozen=False)
class TrainTrackAPI:
    
    def __init__(self, track_model_instance: any):
        self.track_model = track_model_instance
    
    def send_current_speed(self, train_id:int, speed: int):

        #print("train: "+ str(train_id) + " speed: " + str(speed))
        self.track_model.set_current_speed(train_id,speed)

    
    def send_leaving_passengers(self, train_id:int, passengers:int):
        '''
        Send the number of passengers leaving the train.
        Parameters:
            Note: Line does not matter. as trains are only associated w/ repsective rail lines
            - train_id(int): id of the train
            - passengers(int): number of passengers
        '''

        self.track_model.set_leaving_passengers(train_id, passengers)
