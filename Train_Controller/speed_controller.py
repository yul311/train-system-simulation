import copy
import numpy 

class SpeedController():
    #--------------------------------------------------------------------------
    # declare variables
    #--------------------------------------------------------------------------
    current_speed: float = 0
    commanded_speed: float = 0
    prev_commanded_speed: float = 0
    
    power: float = 0
    kp_value: float = 0
    prev_kp: float = 0
    ki_value: float = 0
    prev_ki: float = 0
    interval: float = 0
    e_k: float = 0
    e_k_previous: float = 0
    u_k: float = 0
    u_k_previous: float = 0
    temp_uk: float = 0
    temp_ek: float = 0
    
    fforce: float = 0
    gforce: float = 0
    
    #--------------------------------------------------------------------------
    # current speed
    #--------------------------------------------------------------------------
    def set_current_speed(self, x):
        self.current_speed = x
    
    #--------------------------------------------------------------------------
    # commanded speed
    #--------------------------------------------------------------------------
    def set_commanded_speed(self, s):
        self.commanded_speed = (s)
    
    #--------------------------------------------------------------------------
    # speed limit
    #--------------------------------------------------------------------------
    def set_speed_limit(self, l):
        self.speed_limit = l
        
        
    #--------------------------------------------------------------------------
    # kp and ki
    #--------------------------------------------------------------------------
    def set_kp_value(self, p):
        self.kp_value = p
    
    def set_ki_value(self, i):
        self.ki_value = i

    
    #--------------------------------------------------------------------------
    # time 
    #--------------------------------------------------------------------------
    def set_interval(self, t):
        self.interval = t
        
    def set_force(self, g, f):
        self.gforce = g
        self.fforce = f
    
    #--------------------------------------------------------------------------
    # power
    #--------------------------------------------------------------------------
    def calculate_power(self):
        # self.temp_ek = self.e_k
        # self.temp_uk = self.u_k
              
        # first iteration
        self.e_k_previous = (self.e_k)
        
        self.e_k = self.commanded_speed - self.current_speed

        
        self.u_k_previous = copy.deepcopy(self.u_k)
    
        if self.power < 120000:
            self.u_k = copy.deepcopy(self.u_k_previous) + (self.interval/2) * (self.e_k - self.e_k_previous)
        else:
            self.u_k = copy.deepcopy(self.u_k_previous)

        power1 = (self.kp_value*self.e_k) + (self.ki_value*self.u_k)

        
        # self.e_k_previous = self.e_k
    
    
        # power = power 1 + gforce*interval + fforce*interval
        
        # print("power 1: " + str(power1))
        
        # # # second iteration
        # self.e_k_previous2 = self.temp_ek
        
        # self.e_k2 = self.commanded_speed - self.current_speed
        

        self.e_k = self.commanded_speed - self.current_speed

        self.u_k = self.temp_uk + self.interval/2 * (self.e_k + self.e_k_previous)

        # self.u_k_previous2 = self.temp_uk
        
        # self.u_k2 = self.u_k_previous2 + self.interval/2 * (self.e_k2 - self.e_k_previous2)

        
        # power2 = self.kp_value*self.e_k2 + self.ki_value*self.u_k2
        
        # print("power 2: " + str(power2))
        
        # # third iteration
        # self.e_k_previous = self.temp_ek
        
        # self.e_k = self.commanded_speed - self.current_speed
        
        # self.u_k_previous = self.temp_uk
        
        # self.u_k = self.temp_uk + self.interval/2 * (self.e_k + self.e_k_previous)
        
        # power3 = self.kp_value*self.e_k + self.ki_value*self.u_k
        
        # # redundancy check for power calculation
        # if(power1 == power2 == power3):
        #     self.power = power1
        if(power1 <= 0):
            self.fforce = 0
            self.gforce = 0 
            

        self.power = power1 
        # print( "Power calculation " + str(self.power))
        
        #self.power = power1
        
        if(self.power >= 120000):
            self.power = 120000
            
        if(self.power < 0):
            self.power = 0
                
       # print("speed ctrl: power " + str(self.power))
            # return self.power
            
        #if((self.prev_commanded_speed != self.commanded_speed) or (self.prev_kp != self.kp_value) or (self.prev_ki != self.ki_value)):
            
        # self.prev_commanded_speed = self.commanded_speed
        
        # # store the previous values of Kp and Ki
        # self.prev_ki = self.ki_value
        # self.prev_kp = self.kp_value
        
        # print("*(*(*(*(*(*(*(*(*(*(*(*(*(*(*(*(*(*(*(*(*")
        # print("speed ctrl: ki " + str(self.ki_value))
        # print("speed ctrl: kp " + str(self.kp_value))  
        # print("speed ctrl: commanded speed " + str(self.commanded_speed))
        # print("speed ctrl: current speed " + str(self.current_speed))
        # print("speed ctrl: ek prev " + str(self.e_k_previous))
        # print("speed ctrl: ek " + str(self.e_k))
        # print("speed ctrl: uk " + str(self.u_k))
        # print("speed ctrl: uk prev " + str(self.u_k_previous)) 
        # print("speed ctrl: power " + str(self.power))
        # # print("speed ctrl: uk temp " + str(self.temp_uk))
        # print("speed ctrl: interval " + str(self.interval))
           
    def power_zero(self):
        self.power = 0
        # self.commanded_speed = 0


    def get_current_power(self):
        return self.power
