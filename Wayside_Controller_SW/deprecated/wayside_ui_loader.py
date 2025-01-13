import sys
from output import *
import numpy as np
import os
import pandas
from PySide6.QtCore import QTimer, QDateTime, QModelIndex

IMG_PATH = os.path.join(os.getcwd(),"Wayside_Controller_SW","img")

SWITCH_STATE1_PATH = os.path.join(IMG_PATH,"switch_state1.png")
SWITCH_STATE2_PATH = os.path.join(IMG_PATH,"switch_state2.png")
SIGNAL_GREEN_PATH = os.path.join(IMG_PATH,"greenlight.png")
SIGNAL_RED_PATH = os.path.join(IMG_PATH,"redlight.png")
CROSSING_OPEN_PATH = os.path.join(IMG_PATH,"rrc_open.png")
CROSSING_CLOSE_PATH = os.path.join(IMG_PATH,"rrc_close.png")
ICON_PATH = os.path.join(IMG_PATH,"AuroraLogo.jpg")
PAUSE_PATH = os.path.join(os.getcwd(),"Other","pause_button.jpg")

def construct_ui() -> "WaysideUI":
    
    # sample data
    switch_data = np.empty((3,4),dtype=np.dtype('U100'))
    for i in range(switch_data.shape[0]):
        switch_data[i,0] = f"{i+1}"
        switch_data[i,1] = "1"
        switch_data[i,2] = "152"
        switch_data[i,3] = f"{i+1} to 1"
      
    signal_data = np.empty((40,2),dtype=np.dtype('U100'))
    for i in range(signal_data.shape[0]):
        signal_data[i,0] = f"{i+1}"
        signal_data[i,1] = "Green"
    
    crossing_data = np.empty((1,2),dtype=np.dtype('U100'))
    for i in range(crossing_data.shape[0]):
        crossing_data[i,0] = f"{i+1}"
        crossing_data[i,1] = "Open"
    
    block_data = np.empty((40,4),dtype=np.dtype('U100'))
    for i in range(block_data.shape[0]):
        block_data[i,0] = f"{i+1}"
        block_data[i,1] = "A"
        block_data[i,2] = "Open"
        block_data[i,3] = "Unoccupied"
        
    ui = WaysideUI(switch_data,signal_data,crossing_data,block_data)
    return ui
    

class WaysideUI(QMainWindow,Ui_MainWindow):
    
    displayed_switch_state: int     # 1: primary, 2: secondary
    displayed_signal_state: int     # 1: green, 2: red
    displayed_crossing_state: int   # 1: open, 2: closed
    
    selected_switch: int
    selected_signal: int
    selected_crossing: int
    selected_tb_block: int
    
    timer_1s: QTimer
    
    def __init__(self,switch_data,signal_data,crossing_data,block_data):
        super().__init__()
        
        self.setupUi(self)
        self.connect_buttons()
        self.init_ui()
        self.init_tables(switch_data,signal_data,crossing_data,block_data)
        
        self.set_selected_switch(0)
        self.set_selected_signal(0)
        self.set_selected_crossing(0)
        
    def connect_buttons(self):
        self.switch_table.clicked.connect(self.select_switch_action)
        self.signal_table.clicked.connect(self.select_signal_action)
        self.crossing_table.clicked.connect(self.select_crossing_action)
        self.node_select.currentIndexChanged.connect(self.select_node_action)
        
        self.tb_block_table.clicked.connect(self.select_tb_block_action)
        
    def init_ui(self):
        icon = QIcon(ICON_PATH)
        self.setWindowIcon(icon)
            
        self.tabWidget.setCurrentIndex(0)
        
        self.header_layout.setAutoFillBackground(True)
        p = self.header_layout.palette()
        p.setColor(self.header_layout.backgroundRole(), QColor(242, 205, 109, 255))
        self.header_layout.setPalette(p)
        
        self.label.setPixmap(QPixmap(ICON_PATH))
        self.pause_button.setIcon(QPixmap(PAUSE_PATH))
        
        # iteration 3 use case preset
        # dispatch train from yard to dormont (section T)
        self.tb_train_path.setText("0,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,85,84,83,82,81,80,79,78,77,101,102,103,104,105")
        # TODO another path for dormont station in section L
        self.tb_train_table.setWordWrap(True)
    
    def init_tables(self, 
                    switch_data: np.ndarray, 
                    signal_data: np.ndarray,
                    crossing_data: np.ndarray,
                    block_data: np.ndarray):
        
        if block_data.shape[1] != 4:
            raise Exception("\033[0;31mIncorrect number of rows for block tables.\033[0m")
        if switch_data.shape[1] != 4:
            raise Exception("\033[0;31m Incorrect number of rows for switch table.\033[0m")
        if signal_data.shape[1] != 2:
            raise Exception("\033[0;31m Incorrect number of rows for signal table.\033[0m")
        if crossing_data.shape[1] != 2:
            raise Exception("\033[0;31m Incorrect number of rows for signal table.\033[0m")
        
        self.selected_switch = 0
        self.selected_signal = 0
        self.selected_crossing = 0
        
        # block data
        for table in [self.block_table_1,self.block_table_2,self.block_table_3]:
            table.setRowCount(block_data.shape[0])
            table.setColumnCount(block_data.shape[1])
            for r,c in np.ndindex(block_data.shape):
                table.setItem(r, c, QTableWidgetItem(block_data[r, c]))
        
        # testbench block data
        self.tb_block_table.setRowCount(block_data.shape[0])
        self.tb_block_table.setColumnCount(7)
        for row in range(block_data.shape[0]):
            
            if block_data[row,0] in switch_data[:,0]:
                sw_entry = switch_data[switch_data[:,0]==block_data[row,0],3][0]
            else:
                sw_entry = "N/A"
                
            if block_data[row,0] in signal_data[:,0]:
                sg_entry = signal_data[signal_data[:,0]==block_data[row,0],1][0]
            else:
                sg_entry = "N/A"
                
            if block_data[row,0] in crossing_data[:,0]:
                cr_entry = crossing_data[crossing_data[:,0]==block_data[row,0],1][0]
            else:
                cr_entry = "N/A"
                
            self.tb_block_table.setItem(row, 0, QTableWidgetItem(block_data[row, 0]))
            self.tb_block_table.setItem(row, 1, QTableWidgetItem(block_data[row, 1]))
            self.tb_block_table.setItem(row, 2, QTableWidgetItem(block_data[row, 2]))
            self.tb_block_table.setItem(row, 3, QTableWidgetItem(block_data[row, 3]))
            self.tb_block_table.setItem(row, 4, QTableWidgetItem(sw_entry))
            self.tb_block_table.setItem(row, 5, QTableWidgetItem(sg_entry))
            self.tb_block_table.setItem(row, 6, QTableWidgetItem(cr_entry))
                
        # switch data
        self.switch_table.setRowCount(switch_data.shape[0])
        self.switch_table.setColumnCount(switch_data.shape[1])
        for r,c in np.ndindex(switch_data.shape):
            self.switch_table.setItem(r, c, QTableWidgetItem(switch_data[r, c]))
        #self.switch_table.setCurrentIndex(0)
            
        # signal data
        self.signal_table.setRowCount(signal_data.shape[0])
        self.signal_table.setColumnCount(signal_data.shape[1])
        for r,c in np.ndindex(signal_data.shape):
            self.signal_table.setItem(r, c, QTableWidgetItem(signal_data[r, c]))
        #self.signal_table.setCurrentIndex(0)
            
        # crossing data
        self.crossing_table.setRowCount(crossing_data.shape[0])
        self.crossing_table.setColumnCount(crossing_data.shape[1])
        for r,c in np.ndindex(crossing_data.shape):
            self.crossing_table.setItem(r, c, QTableWidgetItem(crossing_data[r, c]))
        #self.crossing_table.setCurrentIndex(0)
            
        # comboboxes
        for node in range(1,8):
            if node in [1,2,3]:
                line = "red line"
            else:
                line = "green line"
            self.node_select.addItem(f"Wayside Node {node} ({line})")
    
    # @brief    sets displayed switch state in switch control tab
    def set_displayed_switch_state(self,state: int):
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid switch state")
        self.displayed_switch_state = state
        
        owner = int(self.switch_table.item(self.selected_switch,0).text())
        primary = int(self.switch_table.item(self.selected_switch,1).text())
        secondary = int(self.switch_table.item(self.selected_switch,2).text())     
        
        new_table_entry = f"{owner} to {primary}" if state==1 else f"{owner} to {secondary}"
        
        self.switch_table.setItem(self.selected_switch,3,QTableWidgetItem(new_table_entry))
        self.switch_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Switch in block {owner}</span></p></body></html>")
        self.owner_block_label.setText(f"<html><head/><body><p align=\"center\">Block {owner}</p></body></html>")
        self.state1_block_label.setText(f"<html><head/><body><p align=\"center\">Block {primary}</p></body></html>")
        self.state2_block_label.setText(f"<html><head/><body><p align=\"center\">Block {secondary}</p></body></html>")
        self.switch_graphic.setPixmap(QPixmap(SWITCH_STATE1_PATH if state==1 else SWITCH_STATE2_PATH))

    def set_displayed_signal_state(self,state: int):
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid signal state")
        self.displayed_signal_state = state

        if self.signal_table.rowCount()==0:
            self.signal_label.setText("")
            self.signal_graphic.setPixmap(QPixmap("none"))
            return
        
        new_table_entry = "Green" if state==1 else "Red"
        block_id = self.signal_table.item(self.selected_signal,0).text()
        
        self.signal_table.setItem(self.selected_signal,1,QTableWidgetItem(new_table_entry))
        self.signal_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Signal in block {block_id}</span></p></body></html>")
        self.signal_graphic.setPixmap(QPixmap(SIGNAL_GREEN_PATH if state==1 else SIGNAL_RED_PATH))
    
    def set_displayed_crossing_state(self, state: int):
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid crossing state")
        self.displayed_crossing_state = state

        if self.crossing_table.rowCount()==0:
            self.crossing_label.setText("")
            self.crossing_graphic.setPixmap(QPixmap("none"))
            return
        
        new_table_entry = "Open" if state==1 else "Closed"
        block_id = self.crossing_table.item(self.selected_crossing,0).text()
        
        self.crossing_table.setItem(self.selected_crossing,1,QTableWidgetItem(new_table_entry))
        self.crossing_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Crossing in block {self.selected_crossing+1}</span></p></body></html>")
        self.crossing_graphic.setPixmap(QPixmap(CROSSING_OPEN_PATH if state==1 else CROSSING_CLOSE_PATH))
        
    def set_selected_switch(self, index: int):
        self.selected_switch = index
        currstr = self.switch_table.item(index,3).text()
        if int(currstr[currstr.rfind(" "):])==int(self.switch_table.item(index,1).text()):
            state=1
        else:
            state=2
        self.set_displayed_switch_state(state)
        
    def set_selected_signal(self, index: int):
        self.selected_signal = index
        if self.signal_table.rowCount()==0:
            self.set_displayed_signal_state(1)
            return
        state = 1 if self.signal_table.item(index,1).text()=="Green" else 2
        self.set_displayed_signal_state(state)
        
    def set_selected_crossing(self, index: int):
        self.selected_crossing = index
        if self.crossing_table.rowCount()==0:
            self.set_displayed_crossing_state(1)
            return
        state = 1 if self.crossing_table.item(index,1).text()=="Open" else 2
        self.set_displayed_crossing_state(state)
        
    def set_selected_block_tb(self, index: int):
        self.selected_tb_block = index
        b = self.tb_block_table.item(index, 0).text()
        s = self.tb_block_table.item(index, 1).text()
        self.tb_block_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Section {s}, Block {b}</span></p></body></html>")
        self.tb_occ.setChecked(self.tb_block_table.item(index, 3).text()=="Occupied")
        self.tb_dis.setChecked(self.tb_block_table.item(index, 2).text()!="Open")
        
    # actions
    def select_switch_action(self, tw_index: int or any):
        if isinstance(tw_index, int):
            self.set_selected_switch(tw_index)
        else:
            self.set_selected_switch(tw_index.row())
    def select_signal_action(self, tw_index: int or any):
        if isinstance(tw_index, int):
            self.set_selected_signal(tw_index)
        else:
            self.set_selected_signal(tw_index.row())
    def select_crossing_action(self, tw_index: int or any):
        if isinstance(tw_index, int):
            self.set_selected_crossing(tw_index)
        else:
            self.set_selected_crossing(tw_index.row())
    def select_node_action(self, index):
        pass
        #print(f"node {index+1}")
    def update_clock(self, time: str):
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Simulation time\n"f"{time}", None))
        
    def select_tb_block_action(self, index: any):
        self.set_selected_block_tb(index.row())
    
        
if __name__=="__main__":
    
    app = QApplication(sys.argv)
    form = construct_ui()
    form.show()
    sys.exit(app.exec())