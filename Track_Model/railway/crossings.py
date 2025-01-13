#------------------------------------------------------------------
# Crossings Sub-class
#------------------------------------------------------------------

class rail_Crossings(object):
    #keep track of instances using class variables here
    
    def __init__(self, initialID:int):
        super(object, self).__init__()
        self.__crossingID       = initialID #set crossingID
        self.__state            = False #set crossing state to be open. Open = False | Closed = True

    #-------------------------------------------------------------------
    # Set Functions Below
    #-------------------------------------------------------------------
    def set_crossing_state(self, state:bool):
        self.__state = state
    
    def change_crossing_state(self):
        if(self.__state == False):
            self.__state = True
        else:
            self.__state = False
    #-------------------------------------------------------------------
    # Get Functions Below
    #-------------------------------------------------------------------
    def get_crossing_id(self):
        return self.__crossingID
    
    def get_crossing_state(self):
        return self.__state