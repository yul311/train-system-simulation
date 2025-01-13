from datetime import datetime, timedelta
import threading
import time
from PySide6.QtCore import  QTimer, QDateTime, QObject, QThread, QDate


# tick rate is how often the internal clock updates per second (default is 50 updates per second)


class SimulationTime(QObject):
    
    def __init__(self):
        QObject.__init__(self)
        self.__sim_speed_factor = 1.0
        self.simulation_elapsed = 0
        self.last_update_time = QDateTime.currentDateTime()
        self.__current_time = 0
        self.__running = True
    
    # @brief    start (or unpause) the simulation    
    def start(self): 
        self.__running = 1
    
    # @brief    stop (or pause) the simulation
    def cancel(self):
        self.__running = False

    def stop(self):
        self.__sim_speed_factor = 0
    
    def get_running(self):
        return self.__running
    
    @property
    def running(self):
        return self.__running
    
    def set_sim_speed(self, factor: int):
        self.__sim_speed_factor = factor
    
    def get_speed_factor(self):
        return self.__sim_speed_factor
    
    # @brief    updates the internal time
    def update_time(self):
        while self.__running:
            current_time = QDateTime.currentDateTime()
            elapsed = self.last_update_time.msecsTo(current_time)
            self.last_update_time = current_time
            # Increment the simulation time by the elapsed time times the speed factor
            self.simulation_elapsed += elapsed * self.__sim_speed_factor / 1000.0  # Convert to seconds
            # Format the simulation time
            simulated_time = QDateTime.fromMSecsSinceEpoch(int(self.simulation_elapsed * 1000))
            self.__current_time = simulated_time #simulated_time.toString('hh:mm:ss.z') #hh:mm:ss.zzz for milliseconds
            #print(self.__current_time)
            time.sleep(0.1) #update every 0.1 seconds
            
    # @brief    gets datetime obj of current simulation time
    def get_curr_datetime(self) -> datetime:
        return self.__current_time
    
    # @brief    gets serial datetime of current sim time
    def get_curr_serial(self) -> int:
        return int(self.__current_time)
    
    # @brief    gets formatted datetime string for current sim time
    def get_curr_string(self) -> str:
        #print(self.__current_time)    
        return str(self.__current_time)
    

    
    
# start sim
# TODO  all modules must be instantiated before calling sim.start()
sim2 = SimulationTime()

if __name__=="__main__":
    
    simulation_thread = threading.Thread(target=sim2.update_time)
    simulation_thread.start()
    
    def repeat():
        time.sleep(2)
        sim2.set_sim_speed(2.0)

        time.sleep(2)
        sim2.set_sim_speed(5.0)

        time.sleep(2)
        sim2.set_sim_speed(10.0)

        time.sleep(2)
        sim2.set_sim_speed(20.0)

        time.sleep(2)
        sim2.cancel()

    try:
            repeat()

    except KeyboardInterrupt as kbi:
        sim2.cancel()
        simulation_thread.join()
        exit()