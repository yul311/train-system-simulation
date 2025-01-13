import sys,os
sys.path.append(os.getcwd())
import threading
import traceback

from sys import getsizeof
import json

## local imports ##
from Main.launcher_ui import LauncherUI, QApplication
app = QApplication(sys.argv)
from Main.simulation_time import sim
from Main.init_system import construct_frontends,link_apis

#from memory_profiler import profile
import gc

## MAIN FOR FULL APPLICATION ##
def main():
        
    try:

        ctc_ui,wayside_ui,track_model_ui,train_model_ui,train_controller_ui = construct_frontends()

        link_apis()

        launcher = LauncherUI(ctc_ui,wayside_ui,track_model_ui,train_model_ui,train_controller_ui)

        launcher.show()
        app.exec()
    except:
        print(f"\033[1;31mException caught in main thread\033[0m")
        print(f"{traceback.print_exc()}")
    else:
        print(f"\033[1;32mProcess terminated successfully.\033[0m")
    finally:
        sim.cancel()
        #sim2.cancel()
        sys.exit()
            
if __name__=="__main__": main()