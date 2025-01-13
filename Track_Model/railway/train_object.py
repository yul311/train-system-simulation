
from Track_Model.railway.build_train import construct_train

#Train object! CHOOO CHOOO 
class train(object):
    
    def __init__(self, train_id: int, track_instance: any):
        super(object, self).__init__()
        self.__train_id = train_id
        self.__line = None
        self.__train_authority = 0
        self.__last_block = 0
        self.__train_speed = 0
        self.__current_block = 0
        self.__train_on_station = True
        self.__direction = 0
        self.__distance_travelled = 0
        self.__passengers = 0
        self.__inyard = True
        self.__block_enter_time = None
        self.__block_last_cycle_time = None
        self.__train_length = 32.2
        self.beacon1 = None
        self.beacon2 = None
        self.direction0_list = None
        self.direction1_list = None
        self.__time_to_travel_block = None 
        self.__entered_switch_block = False
        self.__yard_delay = True
        self.__dwelling = False

        ## construct train objects ##
        self.model, self.controller, self.tr_to_tm = construct_train(track_model_instance=track_instance)

    #---------------------------------------------------------------
    # Set Functions 
    #---------------------------------------------------------------

    def set_dwelling(self, value:bool):
        '''
            parameters:
                value: boolean to self.__dwelling to for if train is dwelling
        '''
        self.__dwelling = value

    def get_dwelling(self):
        return self.__dwelling
    
    def set_yard_delay(self, value:bool):
        self.__yard_delay = value
        
    def get_yard_delay(self):
        return self.__yard_delay
    
    def set_entered_switch_block(self, value:bool):
        self.__entered_switch_block = value
    
    def get_entered_switch_block(self):
        return self.__entered_switch_block    
    
    def set_time_to_travel(self, distance:float):
        self.__time_to_travel_block =distance
        
    def get_time_to_travel(self):
        return self.__time_to_travel_block
    
    
    def set_line(self, line:str):
        self.__line = line

    def set_train_id(self, value:int):
        self.__train_id = value
        
    def get_line(self, line:str):
        return self.__line
    
    def set_block_last_cycle_time(self, time:int):
        self.__block_last_cycle_time = time
    
    def set_direction0_list(self, direction=[]):
        self.direction0_list = direction

    def set_direction1_list(self, direction=[]):
        self.direction1_list = direction

    def set_train_beacon1(self, beacon=[]):
        self.beacon1 = beacon

    def set_train_beacon2(self, beacon=[]):
        self.beacon2 = beacon

    def set_block_enter_time(self, time:int):
        self.__block_enter_time = time

    def set_change_in_yard(self, value:bool):
        self.__inyard = value
    
    def set_train_speed(self, speed:int):
        self.__train_speed = speed
        
    def set_train_in_station(self, value:bool):
        self.__train_on_station = value

    def set_train_direction(self, direction:int):
        self.__direction = direction
        
    def set_distance_travelled(self, distance:float):
        self.__distance_travelled = distance
        
    def set_train_on_station(self, bool:bool):
        self.__train_on_station = bool
        
    def set_train_position(self, block:int):
        self.__current_block = block
    
    def set_train_authority(self, authority:int):
        self.__train_authority = authority
        self.tr_to_tm.send_authority(self.__train_authority)

        
    def set_decrease_train_authority(self, decrease:float):
        self.train_authority = self.train_authority - decrease
    
    def set_passengers(self, num_passengers:int):
        self.__passengers = num_passengers
        self.tr_to_tm.send_ticket_sale(self.__passengers)
    
    def set_last_block(self, last_block:int):
        self.__last_block = last_block
    #---------------------------------------------------------------
    # Get Functions 
    #---------------------------------------------------------------
    def get_block_last_cycle_time(self):
        return self.__block_last_cycle_time
    
    def get_direction(self):
        return self.__direction
    
    def get_direction0_list(self):
        return self.direction0_list

    def get_direction1_list(self):
        return self.direction1_list

    def get_train_beacon1(self):
        return self.beacon1

    def get_train_beacon2(self):
        return self.beacon2


    def get_block_entry_time(self):
        return self.__block_enter_time
    
    def get_train_speed(self):
        return self.__train_speed
    
    def get_train_in_station(self):
        return self.__train_on_station

    def get_last_block(self):
        return self.__last_block

    def get_train_direction(self):
        return self.__direction
        
    def get_distance_travelled(self):
        return self.__distance_travelled

    def get_train_on_station(self):
        return self.__train_on_station
        
    def get_train_position(self):
        return self.__current_block
    
    def get_train_authority(self):
        return self.__train_authority
    
    def get_train_id(self):
        return self.__train_id
    
    def get_passengers(self):
        return self.__passengers
    
    def get_in_yard(self):
        return self.__inyard