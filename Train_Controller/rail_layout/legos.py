#------------------------------------------------------------------
# Track Block Super-class
#------------------------------------------------------------------
class lego_blocks(object):

    def __init__(self, blockID:int, blockLength:int, elevation:float,
                 cu_elev:float, gradlevel:float, maxSpeed:int, underground:int):       
        #initialize all class variables
        self.__block_id    = blockID            # ID of block
        # self.__section     = section             # Section A, B ,C etc
        self.__blockLength = blockLength         # length of block
        self.__elevation   = elevation           # Elevation
        self.__gradlevel   = gradlevel           # gradient Level
        self.__maxSpeed    = maxSpeed            # max speed
        self.__cumulative_elevation = cu_elev   # Cumulative elevation
        self.__underground = underground        # is underground?

    #-------------------------------------------------------------------
    # Get Functions Below
    #-------------------------------------------------------------------
    def get_block_id(self):
        return self.__block_id
    
    # def get_section_id(self):
    #     return self.__section
    
    def get_block_length(self):
        return self.__blockLength
    
    def get_elevation(self):
        return self.__elevation

    def get_cum_elevation(self):
        return self.__cumulative_elevation

    def get_gradient(self):
        return self.__gradlevel

    def get_underground(self):
        return self.__underground
    
    def get_block_speed_max(self):
        return self.__maxSpeed