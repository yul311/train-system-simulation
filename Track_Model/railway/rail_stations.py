#------------------------------------------------------------------
# Station Sub-class
#------------------------------------------------------------------
class station(object):
    #keep track of instances using class variables here
    
    def __init__(self, id:int, name:str, is_underground:bool = 0, ticketsales:int = 5, 
                 station_side:int = 0, beacon1 = [], beacon2 = []):
        # initialize
        self.__station_id       = id                #station ID
        self.__name             = name              #station name
        self.__underground      = is_underground    #is station underground
        self.__ticketSales      = ticketsales       #ticket sales
        self.__station_side     = station_side      #Which side do civies exit on
        self.__beacon1          = beacon1
        self.__beacon2          = beacon2
        self.__dwelling         = False
        self.__leaving          = 0
        self.__boarding         = 0

    #--------------------------asd-------------------------------------
    # Set Functions Below
    #------------------------------------------------------------------

    def set_leaving_passengers(self, value:int):
        self.__leaving = value

    def set_boarding_passengers(self, value:int):
        self.__boarding = value
        
    def set_beacons(self, beacon1, beacon2):
        self.__beacon1 = beacon1
        self.__beacon2 = beacon2

    def set_ticket_sales(self, new_sales):
        self.__ticketSales = new_sales
    
    #station side 0 = both sides, 1 Left, 2
    def set_station_side(self, side):
        self.__station_side = side

    def set_dwelling(self, value:bool):
        self.__dwelling = value
    #-------------------------------------------------------------------
    # Get Functions Below
    #-------------------------------------------------------------------
    def get_dwelling(self):
        return self.__dwelling

    def get_station_id(self):
        return self.__station_id
    
    def get_station_name(self):
        return self.__name
    
    def get_station_side(self):
        return self.__station_side
    
    def get_station_ticket_sales(self):
        return self.__ticketSales

    def get_is_station_underground(self):
        return self.__underground
    
    def clear_ticket_sales(self):
        self.__ticketSales = 0

    def get_beacon1(self):
        return self.__beacon1
    
    def get_beacon2(self):
        return self.__beacon2
    
    def get_boarding_passengers(self):
        return self.__boarding

    def get_leaving_passengers(self):
        return self.__leaving