#create the train controler
from Train_Controller.train_ctrl_ui import TrainCtrlUi 
from Train_Controller.traincontrolleruiAPI import TrainCtrlAPI 

from Train_Model.Train_Model_ui_loader import TrainModelUI

from Track_Model.railway.build_train import construct_train

from PySide6.QtWidgets import QApplication

from Main.simulation_time import sim 

app = QApplication([])

tm,tc,_ = construct_train(None)

ui = TrainCtrlUi(tc)
tcapi = TrainCtrlAPI(ui)

pop = TrainModelUI(tm)


sim.start()
pop.show()
ui.show()


app.exec()
