#------------------------------------------------------------------
# Track Block Super-class
#------------------------------------------------------------------
from Track_Model.railway.crossings import rail_Crossings
from Track_Model.railway.rail_stations import station
from Track_Model.railway.trackswitch import track_Switch
from Track_Model.railway.tracklight import track_Light

class track_Block(object):

    def __init__(self, blockID:int, section:str, blockLength:int, elevation:float,
                 cu_elev:float, gradlevel:float, maxSpeed:int, occupancy:bool, polarity:int,underground:int):       
        #initialize all class variables
        self.stations     =  None               #class objects go into these variables
        self.track_switches = None
        self.rail_crossings = None
        self.track_lights =  None 
        self.__polarity  = polarity
        self.__blockID    = blockID             # ID of block
        self.__section    = section             # Section A, B ,C etc
        self.__blockLength= blockLength         # length of block
        self.__elevation  = elevation           # Elevation
        self.__gradlevel  = gradlevel           # gradient Level
        self.__maxSpeed   = maxSpeed            # max speed
        self.__suggested_speed = 0
        self.__occupancy  = occupancy           # occupancy of block
        self.__authority  = 0                   # authority distance given to this block
        self.__cumulative_elevation = cu_elev   #Cumulative elevation
        self.__failureBR = False                #Broken Rail
        self.__failureTC = False                #Track Circuit
        self.__failurePW = False                #Power Failure
        self.__time_to_travel = 0               #Time it takes to travel block based on block max speed
        self.__underground = underground
        self.__switch_leg_b = None
        self.__switch_leg_c = None
        self.__switch_corner = None
        self.__block_switch_on = None

    def set_failure(self, failureBR:bool = False, failureTC:bool = False, failurePW:bool = False):
        #initialize my failure states for each rail block initially as none
        self.__failureBR = failureBR            #Broken Rail
        self.__failureTC = failureTC           #Track Circuit
        self.__failurePW = failurePW # False = no power failure. True = power failure
    
    #-------------------------------------------------------------------
    # Make Station objects Functions Below
    #-------------------------------------------------------------------
    def set_suggested_speed(self, speed:int):
        self.__suggested_speed = speed

    def build_station(self, id:int, name:str, is_underground:bool, ticketsales:int, side:int = 0, beacon1 = [], beacon2=[]):
        self.stations = station(id, name, is_underground, ticketsales, side, beacon1, beacon2)
        
    def build_light(self, lightID:int):
        self.track_lights = track_Light(lightID)
        
    def build_switch(self, switch_ID:int, beaconb = [], beaconc = []):
        self.track_switches = track_Switch(switch_ID, beaconb, beaconc)
    
    def set_switch_connections(self, startBlock:int, endBlockOne:int, endBlockTwo:int, block_on:int):
        self.track_switches.set_switch_connections(startBlock, endBlockOne, endBlockTwo, block_on)

    def build_crossing(self, initialID:int):
        self.rail_crossings = rail_Crossings(initialID)
    #-------------------------------------------------------------------
    # Set Functions Below
    #-------------------------------------------------------------------
    def set_station_beacon(self, beacon):
        if(self.stations != None):
            self.stations.set_beacon(beacon)
        else: 
            raise Exception("No Station Exists")
        
    def set_switch_beacon(self, beacon):
        if(self.track_switches != None):
            self.track_switches.set_beacon(beacon)
        else: 
            raise Exception("No Switch Exists")
        
    def change_occupancy(self):
        if(self.__occupancy == False):
            self.__occupancy = True
        else:
            self.__occupancy = False

    def change_authority(self, dist:int):
        self.__authority = dist

    def set_occupancy(self, isoccupied:bool):
        self.__occupancy = isoccupied

    def set_authority(self, new_authority:int):
        self.__authority = new_authority

    def set_failureBR(self, failureBR:bool):
        self.__failureBR = failureBR

    def set_failurePW(self, failurePW:bool):
        self.__failurePW = failurePW

    def set_failureTC(self, failureTC:bool):
        self.__failureTC = failureTC

    def set_block_length(self, new_length:int):
        self.__blockLength = new_length
    
    def set_time_to_travel(self, time:float):
        self.__time_to_travel = time

    #-------------------------------------------------------------------
    # Get Functions Below
    #-------------------------------------------------------------------
    def get_suggested_speed(self):
        return self.__suggested_speed
    
    def get_time_to_travel(self):
        return self.__time_to_travel
    
    def get_station_beacon1(self):
        if(self.stations != None):
            return self.stations.get_beacon1()
        else: 
            raise Exception("No Station Exists")
        
    def get_station_beacon2(self):
        if(self.stations != None):
            return self.stations.get_beacon2()
        else: 
            raise Exception("No Station Exists")
        
    def get_underground(self):
        return self.__underground

    def get_blockID(self):
        return self.__blockID
    
    def get_sectionID(self):
        return self.__section
    
    def get_block_length(self):
        return self.__blockLength
    
    def get_elevation(self):
        return self.__elevation

    def get_cumulative_elevation(self):
        return self.__cumulative_elevation

    def get_gradLevel(self):
        return self.__gradlevel

    def get_max_speed(self):
        return self.__maxSpeed
    
    def get_occupancy(self):
        return self.__occupancy
    
    def get_authority(self):
        return self.__authority

    def get_failure_exists(self):
        if (self.__failureBR == True or self.__failureTC == True or self.__failurePW == True):
            return True
        else:
            return False
        
    def get_failureBR(self):
        if(self.__failureBR == False):
            return "Normal Operation"
        else:
            return "Broken Rail Fault!"

    def get_failureTC(self):
        if(self.__failureTC == False):
            return "Normal Operation"
        else:
            return "Track Circuit Failure!"
    
    def get_failurePW(self):
        if(self.__failurePW == False):
            return "Normal Operation"
        else:
            return "Power Failure!"
        
    def get_polarity(self):
        return self.__polarity

    #-------------------------------------------------------------------
    # Set/GET Staton functions Below
    #-------------------------------------------------------------------
    

    def set_leaving_passengers(self, value:int):
        if(self.stations != None):
            self.stations.set_leaving_passengers(value)
        else: 
            raise Exception("No Station Exists")

    def set_boarding_passengers(self, value:int):
        if(self.stations != None):
            self.stations.set_boarding_passengers(value)
        else: 
            raise Exception("No Station Exists")
        
    def get_leaving_passengers(self):
        if(self.stations != None):
            return self.stations.get_leaving_passengers()
        else: 
            raise Exception("No Station Exists")
    
    def get_boarding_passengers(self):
        if(self.stations != None):
            return self.stations.get_boarding_passengers()
        else: 
            raise Exception("No Station Exists")
        
    def set_dwelling(self, value:bool):
        if(self.stations != None):
            self.stations.set_dwelling(value)
        else: 
            raise Exception("No Station Exists")

    def get_dwelling(self):
        if(self.stations != None):
            return self.stations.get_dwelling()
        else: 
            return
            raise Exception("No Station Exists")
    
    def set_ticket_sales(self, num_tickets:str):
        if(self.stations != None):
            self.stations.set_ticket_sales(num_tickets)
        else: 
            raise Exception("No Station Exists")
        
    def get_station_ticket_sales(self):
        if(self.stations != None):
            self.stations.get_station_ticket_sales()
        else: 
            raise Exception("No Station Exists")

    def clear_ticket_sales(self):
        if(self.stations != None):
            self.stations.clear_ticket_sales()
        else: 
            raise Exception("No Station Exists")
        
    def get_station_id(self):
        if (self.stations != None):
            return self.stations.get_station_id()
        else: 
            raise Exception("No Station Exists")
        
    def get_station_name(self):
        if(self.stations != None):
            return self.stations.get_station_name()
        else: 
            raise Exception("No Station Exists")
        
    def get_station_side(self):
        if (self.stations != None):
            if(self.stations.get_station_side() == 0):
                return "Both"
            elif(self.stations.get_station_side() == 1):
                return "Left"
            else:
                return "Right"
        else: 
            raise Exception("No Station Exists")
        
    def get_station_ticket_sales(self):
        if(self.stations != None):
            return self.stations.get_station_ticket_sales()
        else: 
            raise Exception("No Station Exists")
        
    def get_is_station_underground(self):
        if(self.stations != None): 
            return self.stations.get_is_station_underground()
        else: 
            raise Exception("No Station Exists")
        
    #-------------------------------------------------------------------
    # Set/Get Light functions Below
    #-------------------------------------------------------------------
    def set_light_state(self, new_state:str):
        if(self.track_lights != None):
            if (self.__failurePW == False):
                self.track_lights.set_light_state(new_state)
        else: 
            raise Exception("No Signal Exists")

    def change_light_state(self):
        if(self.track_lights != None):
            if (self.__failurePW == False):
                self.track_lights.change_light_state()
        else: 
            raise Exception("No Signal Exists")
       
    def get_light_state(self):
        if(self.track_lights != None):
            return self.track_lights.get_light_state()
        else: 
            raise Exception("No Signal Exists")
        
    def get_light_id(self):
        if(self.track_lights != None):
            return self.track_lights.get_light_id()
        else: 
            raise Exception("No Signal Exists")
        
    def get_light_enabled(self):
        if(self.track_lights != None):
            return self.track_lights.get_light_enabled()
        else: 
            raise Exception("No Signal Exists")
    #-------------------------------------------------------------------
    # Set/Get Crossings functions Below
    #-------------------------------------------------------------------  
    def set_crossing_state(self, new_state:str):
        if (self.__failurePW == False):
            self.rail_crossings.set_crossing_state(new_state)
        else: 
            raise Exception("No Crossing Exists")

    def change_crossing_state(self):
        if (self.__failurePW == False):
            self.rail_crossings.change_crossing_state()
        else: 
            raise Exception("No Crossing Exists")

    def get_crossing_state(self):
        if(self.rail_crossings != None):
            return self.rail_crossings.get_crossing_state()
        else: 
            raise Exception("No Rail Crossing Exists")
    
    def get_crossing_id(self):
        if(self.rail_crossings != None):
            return self.rail_crossings.get_crossing_id()
        else: 
            raise Exception("No Rail Crossing Exists")
    #-------------------------------------------------------------------
    # Set/Get Switch functions Below
    #-------------------------------------------------------------------
    def set_connected_to(self):
        if(self.track_switches != None):
            if (self.__failurePW == False):
                return self.track_switches.set_connected_to()
            else: 
                raise Exception("No Switch Exists")
            
    def get_switch_id(self):
        if(self.track_switches != None):
            return self.track_switches.get_switch_id()
        else: 
            raise Exception("No Switch Exists")
    
    def get_initial_connection(self):
        if(self.track_switches != None):
            return self.track_switches.get_initial_connection()
        else: 
            raise Exception("No Switch Exists")

    def get_connected_to(self):
        if(self.track_switches != None):
            return self.track_switches.get_connected_to()
        else: 
            raise Exception("No Switch Exists")

    def get_switch_on_block(self):
        if(self.track_switches != None):
            return self.track_switches.get_switch_on_block()
        else: 
            raise Exception("No Switch Exists")
        
    def get_switch_corner_block(self):
        if(self.track_switches != None):
            return self.track_switches.get_switch_corner_block()
        else: 
            raise Exception("No Switch Exists")
        
    def get_alternate_connection(self):
        if(self.track_switches != None):
            return self.track_switches.get_alternate_connection()
        else: 
            raise Exception("No Switch Exists")
        
    #-------------------------------------------------------------------
    # Set/Get Switch beacon functions Below
    #-------------------------------------------------------------------
    def get_station_beacon1(self):
        if(self.stations != None):
            return self.stations.get_beacon1()
        else: 
            raise Exception("No Station Exists")
    
    def get_station_beacon2(self):
        if(self.stations != None):
            return self.stations.get_beacon2()
        else: 
            raise Exception("No Switch Exists")
    
    def get_switch_beaconb(self):
        if( self.track_switches != None):
            return self.track_switches.get_beaconb()
        else: 
            raise Exception("No switch beacon b Exists")
    
    def get_switch_beaconc(self):
        if(self.track_switches != None):
            return self.track_switches.get_beaconc()
        else: 
            raise Exception("No switch beacon C Exists")
        
    def set_switch_leg_b(self, leg):
        self.__switch_leg_b = leg

    def get_switch_leg_b(self):
        return self.__switch_leg_b

    def set_switch_leg_c(self, leg):
        self.__switch_leg_c = leg

    def get_switch_leg_c(self):
        return self.__switch_leg_c
    
    def set_switch_corner(self, corner):
        self.__switch_corner = corner
        
    def get_switch_corner(self):
        return self.__switch_corner
    
    def get_block_switch_on(self):
        return self.__block_switch_on
    
    def set_block_switch_on(self, switch_on):
        self.__block_switch_on = switch_on