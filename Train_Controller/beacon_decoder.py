import numpy
import copy
from Train_Controller.rail_layout.database import *
from Train_Controller.rail_layout.legos import *

class BeaconDecoder(object):
    
    #--------------------------------------------------------------------------
    # declar variables
    #--------------------------------------------------------------------------
    def __init__(self):
        
        self.speed_limit: int = 0
        self.block_grade: float = 0
        
        self.gblock_station = {0: "Yard", 2: "Pioneer", 9: "Edgebrook", 16: "Brittania", 22: "Whited", 31: "South Bank", 39: "Central", 48: "Inglewood", 57: "Overbrook", 
                        65: "Glenbury", 73: "Dormont", 77: "Mt Lebanon", 88: "Poplar", 96: "Castle Channon", 105: "Dorment", 114: "Glenbury", 123: "Overbrook", 
                        132: "Inglewood", 141: "Central",}
                        
        self.gstation_list = {0: "Yard", 1: "Pioneer", 2: "Edgebrook", 3: "Brittania", 4: "Whited", 5: "South Bank", 6: "Central", 7: "Inglewood", 8: "Overbrook", 
                        9: "Glenbury", 10: "Dormont", 11: "Mt Lebanon", 12: "Poplar", 13: "Castle Channon",}
        
        self.rblock_station = {0: "Yard", 7: "Shadyside", 16: "Herron Ave", 21: "Swissville", 25: "Penn Station", 35: "Steel Pizza", 
                        48: "First Ave", 60: "Station Square", }
        
        self.rstation_list = {0: "Yard", 1: "Shadyside", 2: "Herron Ave", 3: "Swissville", 4: "Penn Station", 5: "Steel Pizza", 
                        6: "First Ave", 7: "Station Square", }
        
        self.station_exit_side: bool = False 
        self.underground_flag: bool = False 
        self.elevation: float = 0 
        self.cumulative_elevation: float = 0.0


        self.direction: int = 0
        self.train_id: int = 0
        self.train_line: str = ""
        self.beacon1 = []
        self.beacon2 = []

        self.greenLine = []
        self.redLine = []
        
        self.current_position: int = 0

        self.block_position0 = []
        self.block_position1 = []
        
        self.current_station: str = ""
        self.next_station: str = ""
        
        self.old_polarity: bool = 0
        self.polarity: bool = 0
        
        
    def set_train_line(self, train_line):
        self.train_line = train_line
        

    def build_green_rail_system(self):
        #Build track blocks
        for i in range(len(Database.green_line["blockNumbers"])):
            self.greenLine.append((lego_blocks(Database.green_line["blockNumbers"][i],
                                    Database.green_line["Length"][i], Database.green_line["Elevation"][i],
                                    Database.green_line["cumulativeElevation"][i],
                                    Database.green_line["Grade"][i], Database.green_line["maxSpeed"][i], Database.green_line["Underground"][i])))
        
    def build_red_rail_system(self):
        #Build track blocks
        for i in range(len(Database.red_line["blockNumbers"])):
            self.redLine.append((lego_blocks(Database.red_line["blockNumbers"][i],
                                    Database.red_line["Length"][i], Database.red_line["Elevation"][i],
                                    Database.red_line["cumulativeElevation"][i],
                                    Database.red_line["Grade"][i], Database.red_line["maxSpeed"][i], Database.red_line["Underground"][i])))
    
    #--------------------------------------------------------------------------
    # decoding the beacon
    #--------------------------------------------------------------------------

    def set_encoded_data(self, beacon_1, beacon_2):
            
        try:
            if(beacon_1 != None or beacon_2 == None):
                
                self.beacon1 = copy.deepcopy(beacon_1[0])
                self.beacon2 = copy.deepcopy(beacon_1[1])
                
                if(self.direction == 0):
                    # if(isinstance(self.beacon1, list)):
                        # if( (isinstance(self.beacon1[0], str))):
                    if(self.beacon1[0] == "Dir 1"):
                        self.direction = 1
                    else:
                        self.direction = 0
                else:
                    # if(isinstance(self.beacon2, list)):
                        # if( (isinstance(self.beacon2[0], str))):
                            # if(isinstance(self.beacon2[0], str)):
                    if(self.beacon2[0] == "Dir 0"):
                        self.direction = 0
                    else:
                        self.direction = 1
                        
        
                if(self.direction == 0):
                    if(self.beacon1 != None):
                        try:self.set_block_position0(self.beacon1[3]) 
                        except: pass
                
                if(self.direction == 1):
                    if(self.beacon2 != None):
                        try:self.set_block_position1(self.beacon2[3])
                        except:pass
                        
                # if the current position is in the dict of the blocks
                # get the current position station and compare to the to the list of station
                # set the current station to that name
                # set the doors
                if(self.train_line == "green" and self.direction == 0):
                    if(self.current_position in self.gblock_station):
                        self.set_current_station(self.gstation_list[self.beacon1[0]])
                        self.set_station_exit(self.beacon1[2])
                    # set the next station        
                    if(self.beacon1[1] in self.gstation_list):
                        self.set_next_station(self.gstation_list[self.beacon1[1]])
                        
                if(self.train_line == "green" and self.direction == 1):      
                    if(self.current_position in self.gblock_station):
                        self.set_current_station(self.gstation_list[self.beacon2[0]])
                        self.set_station_exit(self.beacon2[2])
                    
                    # set the next station        
                    if(self.beacon2[1] in self.gstation_list):
                        self.set_next_station(self.gstation_list[self.beacon2[1]])
                        
                        
                if(self.train_line == "red" and self.direction == 0):
                    if(self.current_position in self.rblock_station):
                        self.set_current_station(self.rstation_list[self.beacon1[0]])
                        #self.set_station_exit(self.beacon1[2])
                    # set the next station        
                    if(self.beacon1[1] in self.rstation_list):
                        self.set_next_station(self.rstation_list[self.beacon1[1]])
                        
                if(self.train_line == "red" and self.direction == 1):  
                    if(self.current_position in self.rblock_station):
                        self.set_current_station(self.rblock_station[self.current_position])
                        #self.set_station_exit(self.beacon2[2])
                                
                    if(self.beacon2[1] in self.rstation_list):
                        self.set_next_station(self.rstation_list[self.beacon2[1]])
        except:pass
                
            

            
                    
        try:            
            if(self.block_position0[0] != 0):
                self.decoder()
            elif(self.block_position0[0] == 0):
                
                if(self.train_line == "red"):
                    self.set_speed_limit(self.redLine[self.block_position0[0]].get_block_speed_max())
                
                if(self.train_line == "green"):
                    self.set_speed_limit(self.greenLine[self.block_position0[0]].get_block_speed_max())
                
        except TypeError:
            pass
        except:
            pass
         
    def decoder(self):
        
        #print("direction " + str(self.direction))
        try:
            if(self.direction == 0):
                if(len(self.block_position0) != 0):
                    if(self.current_position == self.block_position0[0]):
                        
                        self.block_position0.pop(0)
                        self.current_position = self.block_position0[0]
                        
                        if(self.train_line == "green"):
                            self.set_speed_limit(self.greenLine[self.current_position].get_block_speed_max())
                            self.set_underground(self.greenLine[self.current_position].get_underground())
                            self.set_block_grade(self.greenLine[self.current_position].get_gradient())
                            self.set_elevation(self.greenLine[self.current_position].get_elevation())
                            self.set_cumulative_elevation(self.greenLine[self.current_position].get_cum_elevation())

                        
                        if(self.train_line == "red"):
                            self.set_speed_limit(self.redLine[self.current_position].get_block_speed_max())
                            self.set_underground(self.redLine[self.current_position].get_underground())
                            self.set_block_grade(self.redLine[self.current_position].get_gradient())
                            self.set_elevation(self.redLine[self.current_position].get_elevation())
                            self.set_cumulative_elevation(self.redLine[self.current_position].get_cum_elevation())
                        
                        
                                
                        
                
        except IndexError:
            pass
        try:
            if(self.direction == 1):
                if(len(self.block_position1) != 0):
                    if(self.current_position == self.block_position1[0]):
                        
                        self.block_position1.pop(0)
                        self.current_position = self.block_position1[0]
                        
                        if(self.train_line == "green"):
                            self.set_speed_limit(self.greenLine[self.current_position].get_block_speed_max())
                            self.set_underground(self.greenLine[self.current_position].get_underground())
                            self.set_block_grade(self.greenLine[self.current_position].get_gradient())
                            self.set_elevation(self.greenLine[self.current_position].get_elevation())
                            self.set_cumulative_elevation(self.greenLine[self.current_position].get_cum_elevation())

                        
                        if(self.train_line == "red"):
                            self.set_speed_limit(self.redLine[self.current_position].get_block_speed_max())
                            self.set_underground(self.redLine[self.current_position].get_underground())
                            self.set_block_grade(self.redLine[self.current_position].get_gradient())
                            self.set_elevation(self.redLine[self.current_position].get_elevation())
                            self.set_cumulative_elevation(self.redLine[self.current_position].get_cum_elevation())

                           
              
                        
        except IndexError:
            pass
        
                           
              
        
    #--------------------------------------------------------------------------
    # speed limit
    #--------------------------------------------------------------------------
    def set_speed_limit(self, s):
        self.speed_limit = s
    
    def get_speed_limit(self):
        return self.speed_limit
    
    def set_current_position(self, block):
        self.current_position = block
    
    def get_current_position(self):
        return self.current_position
    
    #--------------------------------------------------------------------------
    # block grade
    #--------------------------------------------------------------------------
    def set_block_grade(self, grade):
        self.block_grade = grade
    
    def get_block_grade(self):
        return self.block_grade
    
    
    #--------------------------------------------------------------------------
    # station exit status
    #--------------------------------------------------------------------------
    def set_station_exit(self, exit):
        self.station_exit_side = exit
    
    def get_station_exit(self):
        return self.station_exit_side
        
    
    #--------------------------------------------------------------------------
    # underground status
    #--------------------------------------------------------------------------
    def set_underground(self, u):
        self.underground_flag = u
    
    def get_underground(self):
        return self.underground_flag
    
    
    #--------------------------------------------------------------------------
    # elevation
    #--------------------------------------------------------------------------
    def set_elevation(self, ele):
        self.elevation = ele
    
    def get_elevation(self):
        return self.elevation
    
    #--------------------------------------------------------------------------
    # cumulative elevation
    #--------------------------------------------------------------------------
    def set_cumulative_elevation(self, cum ):
        self.cumulative_elevation = cum
    
    def get_cumulative_elevation(self):
        return self.cumulative_elevation 
    
    
    # ----------------------------------------------------------------
    # set the direction block of the train 
    # ----------------------------------------------------------------
    def set_block_position0(self, direction = []):
        self.block_position0 = direction
    
    def set_block_position1(self, direction = []):
        self.block_position1 = direction
    
    
    def set_current_station(self, current_station):
        self.current_station = current_station
        
    def set_next_station(self, next_station):
        self.next_station = next_station
    
    def get_current_station(self):
        return self.current_station 
    
    def get_next_station(self):
        return self.next_station
    
    def set_polarity(self, polarity):
        self.polarity = polarity
        
        # print("polarity: ", self.polarity)
    