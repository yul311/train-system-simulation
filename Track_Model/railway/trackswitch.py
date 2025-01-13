#------------------------------------------------------------------
# Track Switch Sub-class
#------------------------------------------------------------------
class track_Switch(object):
    #keep track of instances using class variables here

    def __init__(self, switch_ID:int, beaconb=[], beaconc=[]):
        # Initialize Variables
        self.__switchID             = switch_ID     # Switch ID
        self.__on_block             = None
        self.__cornerBlock          = None    # block switch is on
        self.__initial_connection   = None   # connection option 
        self.__alternate_connection = None   # connection option 2
        self.__connectedTO          = None # Switch will always be connected to block one initially!
        self.__beaconb              = beaconb
        self.__beaconc              = beaconc
        
    #-------------------------------------------------------------------
    # Set Functions Below
    #-------------------------------------------------------------------
    def set_beacons(self, beaconb, beaconc):
        self.__beaconb = beaconb
        self.__beaconc = beaconc

    def set_switch_connections(self, corner:int, endBlockOne:int, endBlockTwo:int, block_on:int):
        self.__cornerBlock = corner
        self.__initial_connection = endBlockOne
        self.__alternate_connection = endBlockTwo
        self.__connectedTO = self.__initial_connection
        self.__on_block = block_on

    def set_connected_to(self):
        if(self.__connectedTO == self.__initial_connection):
            self.__connectedTO = self.__alternate_connection
        else:
            self.__connectedTO = self.__initial_connection

    #-------------------------------------------------------------------
    # get Functions Below
    #-------------------------------------------------------------------
    def get_switch_id(self):
        return self.__switchID
    
    def get_connected_to(self):
        return self.__connectedTO
    
    def get_switch_on_block(self):
        return self.__on_block
    
    def get_switch_corner_block(self):
        return self.__cornerBlock
    
    def get_alternate_connection(self):
        return self.__alternate_connection
         
    def get_initial_connection(self):
        return self.__initial_connection
    
    def get_beaconb(self):
        if self.__beaconb != "NaN":
            return self.__beaconb
        else:
            return "N/A"
    
    def get_beaconc(self):
        if self.__beaconc != "NaN":
            return self.__beaconc
        else:
            return "N/A"