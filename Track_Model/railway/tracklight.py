
#------------------------------------------------------------------
# Track Light Sub-class
#------------------------------------------------------------------
class track_Light(object): 
    #keep track of instances using class variables here
    def __init__(self, lightID:int):
        self.__lightID = lightID # Light ID
        self.__state = "Red" #state of light
        self.__enabled = True #by default lights are on

    #-------------------------------------------------------------------
    # Set Functions Below
    #-------------------------------------------------------------------
    def set_light_state(self, new_state):
        self.__state = new_state

    def change_light_state(self):
        if (self.__state == "Green"):
            self.__state = "Red"
        else:
            self.__state = "Green"
    
    #-------------------------------------------------------------------
    # Get Functions Below
    #-------------------------------------------------------------------
    def get_light_state(self):
        return self.__state
    
    def get_light_id(self):
        return self.__lightID
    
    def get_light_enabled(self):
        if(self.__state != "black"):
            self.__enabled = True
        else:
            self.__enabled = False
        return self.__enabled