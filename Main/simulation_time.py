
from datetime import datetime, timedelta
from threading import Timer
import time

import gc


class SimulationTime(object):
    
    __sim_speed_factor: int
    __tick_rate: int
    
    __time_increment: timedelta
    __start: datetime
    __curr_datetime: datetime
    
    __timer: Timer
    
    __running: bool
    
    def __init__(self, start: datetime = None):
        self.__start = start if start else datetime.now()
        self.__curr_datetime = self.__start
        self.__tick_rate = 20
        self.set_sim_speed(1)
        
        self.__timer = Timer(interval=1/self.__tick_rate,function=self.__update)
        self.__running = False
        
        self.__timer.start()
        
        print("\033[1;33mSimulation Constructed\033[0m")
    
    # @brief    start (or unpause) the simulation    
    def start(self): 
        print("\033[1;33mSimulation Running\033[0m")
        self.__running = 1
    
    # @brief    stops clock (called on exit)
    def cancel(self):
        print("\033[1;33mSimulation Cancelled\033[0m")
        self.__timer.cancel()
        gc.collect()
        del self

    # @brief    pause the simulation
    def stop(self):
        print("\033[1;33mSimulation Paused\033[0m")
        self.__running = False
    
    @property
    def running(self):
        return self.__running
    
    def set_sim_speed(self, factor: int):
        self.__sim_speed_factor = factor      # TODO figure out why this isnt exactly one second
        
        mseconds: float = 1000 * self.__sim_speed_factor / self.__tick_rate
        self.__time_increment = timedelta(milliseconds=mseconds)
    
    def get_sim_speed(self):
        if (self.__running == False):
            return 0
        else:
            return self.__sim_speed_factor 

    # @brief    updates the internal time
    def __update(self):
        self.__timer = Timer(interval=1/self.__tick_rate,function=self.__update)
        self.__timer.start()
        if self.__running:
            self.__curr_datetime += self.__time_increment
            #time.sleep(0.1) #update every 0.1 seconds
        #gc.collect()
            
    # @brief    gets datetime obj of current simulation time
    def get_curr_datetime(self):
        return self.__curr_datetime
    
    # @brief    gets serial datetime of current sim time
    def get_curr_serial(self) -> int:
        return int(self.__curr_datetime.timestamp()*1000)
    
    # @brief    gets formatted datetime string for current sim time
    def get_curr_string(self) -> str:
        return self.__curr_datetime.strftime("%m/%d/%Y, %H:%M:%S")

    # @brief    gets time delta in serial
    def get_delta_serial(self) -> int:
        raise Exception("do not use me")
        return self.__time_increment.microseconds//1000
        
# start sim
# TODO  all modules must be instantiated before calling sim.start()
sim = SimulationTime()

if __name__=="__main__":

    def display_time():
        sim.get_curr_datetime()
        print(f"{sim.get_curr_string()}")
    def repeat():
        display_time()
        timer = Timer(interval=1,function=repeat)
        timer.start()
        
    timer = Timer(interval=1,function=repeat)
    timer.start()
    
    sim.start()
    
    def repeat():
        time.sleep(2)
        sim.set_sim_speed(2.0)

        time.sleep(2)
        sim.set_sim_speed(5.0)

        time.sleep(2)
        sim.set_sim_speed(10.0)

        time.sleep(2)
        sim.set_sim_speed(20.0)

        time.sleep(2)
        sim.cancel()

    try:
        repeat()

    except KeyboardInterrupt as kbi:
        sim.cancel()
