import numpy

class AuthorityLogicCtrl:
    
    old_authority: float = 0
    new_authority: float = 0 
    authority: float = 0 
    travel_distance: float = 0 
    temp_authority: float = 0 
    
    target_stop_point: float = 0 
    
    current_speed: int = 0
   
    time: int = 0
    
    auto: bool = True
    
    interval: int = 0

    old_polarity: int = 0
    polarity: int = 0
    
    brake_indicator: bool = False
    

    def set_current_speed(self, speed):
        self.current_speed = speed
    
    def set_interval(self, interval):
        self.interval = interval
    
    def set_authority(self, authority):
        self.old_authority = self.authority
        self.authority = authority
        
    def set_auto(self, auto):
        self.auto = not(auto)
        
    def set_polarity(self, polarity):
        self.polarity = polarity
        
    def traveled_distance(self):
        
        # when entering a new block 
        # travel reset based on the block
        if(self.old_polarity != self.polarity):
            self.old_polarity = self.polarity
        if(self.old_authority != self.authority):
            self.travel_distance = 0
        
        # the stop(slow) point is based on how dast the train is moving 
        # as speed increases the slowing distance is increased
        self.target_stop_point = (.5*(self.current_speed * self.current_speed))/1.2
            
        # travel distance is based on how fast the train is going plus travel distance
        self.travel_distance += self.current_speed * self.interval 
        
        # new_authority is the how much distance the train has covered
        self.new_authority = self.authority - self.travel_distance
        
        if(self.target_stop_point >= self.new_authority ):
            self.brake_indicator = True
        else:
            self.brake_indicator = False
            
    # returns to get displayed to the driver
    def get_new_authority(self):
        return self.new_authority
    
    # for automatic to activate service brake
    def get_brake_indicator(self):
        return self.brake_indicator

# ---- from kyles
class AuthorityLogicCtrlTB:

    def __init__(self):
        self.run_tests()
        
    def run_tests(self):
        import inspect,traceback
        for name,method in inspect.getmembers(self, inspect.ismethod):
            if name[:5]=="test_":
                try:
                    method()
                except AssertionError as failure:
                    print(f"\033[1;31mFailed {name}: \033[0m\n{failure}")
                except Exception as err:
                    print(f"\033[1;31mInternal error in {name}: \033[0m\n{traceback.print_exc()}")
                else:
                    print(f"\033[1;32mPassed {name}\033[0m")

    def test_travelled_distance(self):

        mod = AuthorityLogicCtrl()
        mod.set_current_speed(15)
        mod.set_interval(1)
        mod.set_authority(10000)

#------- 
        
    

