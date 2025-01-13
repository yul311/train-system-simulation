import sys, os, dataclasses
from PySide6.QtWidgets import (QApplication, QMainWindow,  QLCDNumber, QTableWidgetItem, QMessageBox, QGraphicsView, QStyleOptionGraphicsItem,
                               QGraphicsRectItem, QGraphicsScene, QHBoxLayout, QWidget, QGraphicsItem, QVBoxLayout)
from PySide6.QtCore import QFile, Slot,QDate, QTime, QTimer, QDateTime, Qt, QEvent, QRectF, QLine, QPoint, QPointF
from PySide6.QtGui import QPalette, QColor, QIntValidator, QBrush, QPen, QPainter, QCursor, QIcon, QPixmap

sys.path.append(os.getcwd())

## import sim clock ##
from Main.simulation_time import sim
## import qt output file for launcher ##
from Main.launcher_ui_output import Ui_menu

## import module UI types ##
from CTC.ui.ctc_ui_loader import CTCUI
from Wayside_Controller_SW.wayside_ui import WaysideUI
from Track_Model.Controller import track_model_ui as TrackModelUI
from Train_Model.Train_Model_ui_loader import TrainModelUI
from Train_Controller.train_ctrl_ui import TrainCtrlUi as TrainControllerUI
import threading

## paths ##
ICON_PATH = os.path.join(os.getcwd(),"Other","AuroraLogo.jpg")

class LauncherUI(QMainWindow,Ui_menu):

    ctc_ui: CTCUI
    wayside_ui: WaysideUI
    track_model_ui: TrackModelUI
    train_model_ui: TrainModelUI
    train_controller_ui: TrainControllerUI
    
    def __init__(self, 
                 ctc_ui: CTCUI, 
                 ws_ui: WaysideUI, 
                 tm_ui: TrackModelUI, 
                 tr_ui: TrainModelUI, 
                 tc_ui: TrainControllerUI):
        
        super(LauncherUI, self).__init__()

        self.setFixedSize(281,320)

        self.ctc_ui = ctc_ui
        self.wayside_ui = ws_ui
        self.track_model_ui = tm_ui
        self.train_model_ui = tr_ui
        self.train_controller_ui = tc_ui
        
        self.setupUi(self)
        self.load_colors()
        
        self.connect_buttons()

        self.ctc_button.setEnabled(False)
        self.wayside_button.setEnabled(False)
        self.track_model_button.setEnabled(False)
        self.train_model_button.setEnabled(False)
        self.train_controller_button.setEnabled(False)


    def load_colors(self):
        icon = QIcon(ICON_PATH)
        self.setWindowIcon(icon)
        
        self.yellow.setAutoFillBackground(True)
        p = self.yellow.palette()
        p.setColor(self.yellow.backgroundRole(), QColor(242, 205, 109, 255))
        self.yellow.setPalette(p)
        
        self.image.setPixmap(QPixmap(ICON_PATH))
        
    def connect_buttons(self):
        
        self.ctc_button.clicked.connect(self.launch_ctc_action)
        self.wayside_button.clicked.connect(self.launch_wayside_action)
        self.track_model_button.clicked.connect(self.launch_track_action)
        self.train_model_button.clicked.connect(self.launch_train_model_action)
        self.train_controller_button.clicked.connect(self.launch_tcontroller_action)

        self.commandLinkButton.clicked.connect(self.start_system_action)


    def launch_ctc_action(self):
        print("\033[1mLaunching CTC UI...\033[0m")
        self.ctc_ui.show()

    def launch_wayside_action(self):
        
        print("\033[1mLaunching Wayside UI...\033[0m")
        self.wayside_ui.show()

    def launch_track_action(self):
        print("\033[1mLaunching Track Model UI...\033[0m")
        self.track_model_ui.setFixedSize(1262,920)
        self.track_model_ui.show()

    def launch_train_model_action(self):
        
        print("\033[1mLaunching Train Model UI...\033[0m")
        self.train_model_ui.show()

    def launch_tcontroller_action(self):
        self.train_controller_ui.setFixedSize(748,741)
        print("\033[1mLaunching Train Controller UI...\033[0m")
        self.train_controller_ui.show()

    def start_system_action(self):
        self.ctc_button.setEnabled(True)
        self.wayside_button.setEnabled(True)
        self.track_model_button.setEnabled(True)
        self.train_model_button.setEnabled(True)
        self.train_controller_button.setEnabled(True)
        
        sim.start()
        #sim2.update_time
        #simulation_thread = threading.Thread(target=sim2.update_time)
        #simulation_thread.start()

if __name__ == "__main__":
    
    raise Exception("DONT RUN THIS ONE")
    app = QApplication(sys.argv)
    window = LauncherUI()
    window.show()
    sys.exit(app.exec())