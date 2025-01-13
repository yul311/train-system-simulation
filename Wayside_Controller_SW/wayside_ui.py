
import sys
import traceback
import numpy as np
import os
import pandas
from PySide6.QtCore import QTimer, QDateTime, QModelIndex, QUrl, Qt
from PySide6.QtWidgets import QFileDialog
from PySide6.QtGui import QDesktopServices

# pyside6-uic Wayside_Controller_SW/ui/wayside_controller.ui -o Wayside_Controller_SW/ui/output.py

sys.path.append(os.getcwd())

from Wayside_Controller_SW.ui.output import *
from Wayside_Controller_SW.wayside_controller import wayside_nodes, WaysideController
from Main.simulation_time import sim

IMG_PATH = os.path.join(os.getcwd(),"Wayside_Controller_SW","img")

SWITCH_STATE1_PATH = os.path.join(IMG_PATH,"switch_state1.png")
SWITCH_STATE2_PATH = os.path.join(IMG_PATH,"switch_state2.png")
SIGNAL_GREEN_PATH = os.path.join(IMG_PATH,"greenlight.png")
SIGNAL_RED_PATH = os.path.join(IMG_PATH,"redlight.png")
CROSSING_OPEN_PATH = os.path.join(IMG_PATH,"rrc_open.png")
CROSSING_CLOSE_PATH = os.path.join(IMG_PATH,"rrc_close.png")

ICON_PATH = os.path.join(os.getcwd(),"Other","AuroraLogo.jpg")
PAUSE_PATH = os.path.join(os.getcwd(),"Other","pause_button.jpg")
PLAY_PATH = os.path.join(os.getcwd(),"Other","play_button.jpg")

#print(ICON_PATH)

def construct_ui() -> "WaysideUI":
    """@brief constructs Wayside Controller frontend"""
    
    # sample data
    switch_data = np.empty((1,4),dtype=np.dtype('U100'))
    switch_data[0,0] = "5"
    switch_data[0,1] = "6"
    switch_data[0,2] = "1"
    switch_data[0,3] = f"5 to 6"
      
    signal_data = np.empty((3,2),dtype=np.dtype('U100'))
    signal_data[0,0] = "5"
    signal_data[0,1] = "Green"
    signal_data[1,0] = "6"
    signal_data[1,1] = "Green"
    signal_data[2,0] = "11"
    signal_data[2,1] = "Green"
    
    crossing_data = np.empty((0,2),dtype=np.dtype('U100'))
    
    block_data = np.empty((15,4),dtype=np.dtype('U100'))
    for i in range(block_data.shape[0]):
        block_data[i,0] = f"{i+1}"
        block_data[i,1] = "A" if i<5 else "B" if i<10 else "C"
        block_data[i,2] = "Open"
        block_data[i,3] = "Unoccupied"
        
    ui = WaysideUI(switch_data,signal_data,crossing_data,block_data)
    ui.set_node(wayside_nodes[1])
    return ui

class WaysideUI(Ui_MainWindow,QMainWindow):
    """Frontend class for Wayside Controller UX"""
    
    wayside_node: WaysideController
    """stores which wayside controller is selected. changed by the yser"""
    
    selected_switch: int
    """stores which index is selected in the switch table. changed by the user"""
    selected_signal: int
    """stores which index is selected in the signal table. changed by the user"""
    selected_crossing: int
    """stores which index is selected in the crossing table. changed by the user"""
    selected_tb_block: int
    """stores which index is selected in the testbench block table. changed by the user"""
    selected_train: int
    """deprecated"""
    selected_line: str
    """deprecated"""
    selected_program: int
    """indicates which PLC program the user selected"""
    
    timer: QTimer
    """internal timer for polling the system clock"""
    
    def __init__(self,switch_data,signal_data,crossing_data,block_data):
        
        super().__init__()
        
        self.wayside_node = None
        
        self.selected_program = 1
        
        self.setupUi(self)
        self.connect_buttons()
        self.init_ui()
        self.load_table_data(switch_data,signal_data,crossing_data,block_data)
        
        self.set_selected_switch(0)
        self.set_selected_signal(0)
        self.set_selected_crossing(0)
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.__timeout__)
        self.timer.start(20)
        
        self.switch_toggle.setEnabled(False)
        self.signal_toggle.setEnabled(False)
        self.crossing_toggle.setEnabled(False)
        
    # @brief called on QTimer timeout; updates displayed time
    def __timeout__(self):
        """@brief polls the simulation clock updates displayed time. called when the QTimer expires"""
        
        time = sim.get_curr_string()
        self.update_clock(time)
        
    # @brief connects all interactions
    def connect_buttons(self):
        """@brief connects all buttons in the UI"""
        
        self.switch_table.clicked.connect(self.select_switch_action)
        self.signal_table.clicked.connect(self.select_signal_action)
        self.crossing_table.clicked.connect(self.select_crossing_action)
        self.node_select.currentIndexChanged.connect(self.select_node_action)
        self.horizontalSlider.valueChanged.connect(self.change_simspeed_action)
        self.pause_button.clicked.connect(self.pause_sim_action)
        self.switch_toggle.clicked.connect(self.toggle_switch_action)
        self.signal_toggle.clicked.connect(self.toggle_signal_action)
        self.crossing_toggle.clicked.connect(self.toggle_crossing_action)
        self.checkBox.stateChanged.connect(self.set_manual_mode_action)
        self.PLC_upload.clicked.connect(self.upload_plc_action)
        self.PLC_download.clicked.connect(self.view_plc_action)
        self.program_select_spinbox.valueChanged.connect(self.change_program_action)
        self.yard_return_box.stateChanged.connect(self.set_yard_return_action)
        
        self.tb_block_table.clicked.connect(self.select_tb_block_action)
        self.tb_occ.clicked.connect(self.set_occupancy_action)
        self.tb_dis.clicked.connect(self.set_maintenance_action)
        
    # @brief initializes UI elements not handled in designer output
    def init_ui(self):
        """@brief performs miscellaneous initializations for the UI"""
        
        icon = QIcon(ICON_PATH)
        self.setWindowIcon(icon)
        self.setWindowTitle("Wayside Controller")
            
        self.tabWidget.setCurrentIndex(0)
        
        self.header_layout.setAutoFillBackground(True)
        p = self.header_layout.palette()
        p.setColor(self.header_layout.backgroundRole(), QColor(242, 205, 109, 255))
        self.header_layout.setPalette(p)
        
        pm = QPixmap(ICON_PATH)
        if pm.isNull():
            pass
            #raise Exception(f"Icon image not found at\n{ICON_PATH}")
        self.label.setPixmap(pm)
        self.pause_button.setIcon(QPixmap(ICON_PATH))
        
        # node combobox
        for node in range(1,6):
            if node in [1,2]:
                line = "red line"
            else:
                line = "green line"
            self.node_select.addItem(f"Wayside Node {node} ({line})")
            
        self.PLC_label.setText("node_1.plc")
        
    # @brief loads all tables; called upon initializing and selecting a node
    def load_tables(self):
        """@brief loads table values from selected wayside controller node"""
        
        # 1: 1-32,72-77
        # 2: 28-77,78
        # 1&2: 28-32,72-77,78
        node_1_omit = {32,33,34,35,36,37,38,39,40,41,42,43,44,45,67,68,69,70,71}
        node_2_omit = {24,25,26,27}
        
        switch_data = np.empty((0,4),dtype=np.dtype('U100'))
        signal_data = np.empty((0,2),dtype=np.dtype('U100'))
        crossing_data = np.empty((0,2),dtype=np.dtype('U100'))
        block_data = np.empty((0,4),dtype=np.dtype('U100'))
        
        for id,block in self.wayside_node.blocks.items():
            
            if self.wayside_node.node_id==1 and id in node_1_omit:
                continue
            elif self.wayside_node.node_id==2 and id in node_2_omit:
                continue
            
            block_row = [f"{id}",f"{block.section}","Under Maintenance" if block.maintenance else "Open","Occupied" if block.occupied else "Unoccupied"]
            block_data = np.vstack((block_data,block_row))
            
            if block.switch:
                if id in {12,15,32,43}:
                    curr = f"{block.switch.primary} to {id}" if block.switch.state==1 else f"{block.switch.primary} to {block.switch.secondary}"
                else:
                    curr = f"{id} to {block.switch.primary}" if block.switch.state==1 else f"{id} to {block.switch.secondary}"
                switch_row = [f"{block.id}",f"{block.switch.primary}",f"{block.switch.secondary}",curr]
                switch_data = np.vstack((switch_data,switch_row))
                
            if block.signal:
                signal_row = [f"{id}", "Green" if block.signal.state==1 else "Red"]
                signal_data = np.vstack((signal_data,signal_row))
                
            if block.crossing:
                crossing_row = [f"{id}","Open" if block.crossing.state==1 else "Closed"]
                crossing_data = np.vstack((crossing_data,crossing_row))
        
        self.load_table_data(switch_data,signal_data,crossing_data,block_data)
        self.set_selected_switch(0)
        self.set_selected_signal(0)
        self.set_selected_crossing(0)
        self.set_selected_block_tb(0)
    
    # @brief called by load_tables to insert data into QTableWidgets
    def load_table_data(self, switch_data: np.ndarray, signal_data: np.ndarray, crossing_data: np.ndarray, block_data: np.ndarray):
        """@brief loads passed-in data to UI tables"""
        
        if block_data.shape[1] != 4:
            raise Exception("\033[0;31mIncorrect number of cols for block tables.\033[0m")
        if switch_data.shape[1] != 4:
            raise Exception("\033[0;31m Incorrect number of cols for switch table.\033[0m")
        if signal_data.shape[1] != 2:
            raise Exception("\033[0;31m Incorrect number of cols for signal table.\033[0m")
        if crossing_data.shape[1] != 2:
            raise Exception("\033[0;31m Incorrect number of cols for crossing table.\033[0m")
        
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
        self.tb_block_table.setColumnCount(8)
        for row in range(block_data.shape[0]):
            
            if block_data[row,0] in switch_data[:,0]:
                sw_entry = switch_data[switch_data[:,0]==block_data[row,0],3][0]
            else:
                sw_entry = ""
                
            if block_data[row,0] in signal_data[:,0]:
                sg_entry = signal_data[signal_data[:,0]==block_data[row,0],1][0]
            else:
                sg_entry = ""
                
            if block_data[row,0] in crossing_data[:,0]:
                cr_entry = crossing_data[crossing_data[:,0]==block_data[row,0],1][0]
            else:
                cr_entry = ""
                
            if self.wayside_node.blocks[int(block_data[row,0])].use_ws_authority:
                auth_entry = f"{int(self.wayside_node.blocks[int(block_data[row,0])].ws_authority*3.28)} ft (Wayside)"
            else:
                auth_entry = f"{int(self.wayside_node.blocks[int(block_data[row,0])].ctc_authority*3.28)} ft (CTC)"
                
            self.tb_block_table.setItem(row, 0, QTableWidgetItem(block_data[row, 0]))
            self.tb_block_table.setItem(row, 1, QTableWidgetItem(block_data[row, 1]))
            self.tb_block_table.setItem(row, 2, QTableWidgetItem(block_data[row, 2]))
            self.tb_block_table.setItem(row, 3, QTableWidgetItem(block_data[row, 3]))
            self.tb_block_table.setItem(row, 4, QTableWidgetItem(sw_entry))
            self.tb_block_table.setItem(row, 5, QTableWidgetItem(sg_entry))
            self.tb_block_table.setItem(row, 6, QTableWidgetItem(cr_entry))
            self.tb_block_table.setItem(row, 7, QTableWidgetItem(auth_entry))
                
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
        
    # @brief called when user selects a different node
    def set_node(self, node: WaysideController):
        """@brief changes which wayside controller node is selected"""
                
        self.wayside_node = node
        
        self.yard_return_box.setEnabled(self.wayside_node.node_id in {1,4})
        self.yard_return_box.setChecked(self.wayside_node.controller.yard_return_mode)
        
        if self.selected_program in self.wayside_node.controller.plc_paths.keys():
            path = self.wayside_node.controller.plc_paths[self.selected_program]
            program = path[path.rfind("\\")+1:]
            self.PLC_label.setText(program)
        else:
            self.PLC_label.setText("No program loaded")
        self.load_tables()
    
    # @brief sets displayed switch state in switch control tab
    def set_displayed_switch_state(self,state: int):
        """@brief changes the switch graphic shown on the display"""
        
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid switch state")
        
        owner = int(self.switch_table.item(self.selected_switch,0).text())
        primary = int(self.switch_table.item(self.selected_switch,1).text())
        secondary = int(self.switch_table.item(self.selected_switch,2).text())     
        
        if owner==12:
            owner=13
            primary=12
        if owner==15:
            owner=16
            primary=15
        if owner==32:
            owner=33
            primary=32
        if owner==43:
            owner=44
            primary=43
        
        secstr = f"Block {secondary}"
        if secondary==0:
            secstr = "Yard"
        
        self.switch_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Switch in block {owner}</span></p></body></html>")
        self.owner_block_label.setText(f"<html><head/><body><p align=\"center\">Block {owner}</p></body></html>")
        self.state1_block_label.setText(f"<html><head/><body><p align=\"center\">Block {primary}</p></body></html>")
        self.state2_block_label.setText(f"<html><head/><body><p align=\"center\">{secstr}</p></body></html>")
        self.switch_graphic.setPixmap(QPixmap(SWITCH_STATE1_PATH if state==1 else SWITCH_STATE2_PATH))

    # @brief changes state of currently displayed signal in signal control tab
    def set_displayed_signal_state(self,state: int):
        """@brief changes the signal graphic shown on the display"""
        
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid signal state")

        if self.signal_table.rowCount()==0:
            self.signal_label.setText("")
            self.signal_graphic.setPixmap(QPixmap("none"))
            return
        
        new_table_entry = "Green" if state==1 else "Red"
        block_id = self.signal_table.item(self.selected_signal,0).text()
        
        self.signal_table.setItem(self.selected_signal,1,QTableWidgetItem(new_table_entry))
        self.signal_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Signal in block {block_id}</span></p></body></html>")
        self.signal_graphic.setPixmap(QPixmap(SIGNAL_GREEN_PATH if state==1 else SIGNAL_RED_PATH))
    
    # @brief changes state of currently displayed crossing in crossing control tab
    def set_displayed_crossing_state(self, state: int):
        """@brief changes the crossing graphic shown on the display"""
        
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid crossing state")

        if self.crossing_table.rowCount()==0:
            self.crossing_label.setText("")
            self.crossing_graphic.setPixmap(QPixmap("none"))
            return
        
        new_table_entry = "Open" if state==1 else "Closed"
        block_id = self.crossing_table.item(self.selected_crossing,0).text()
        
        self.crossing_table.setItem(self.selected_crossing,1,QTableWidgetItem(new_table_entry))
        self.crossing_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Crossing in block {self.selected_crossing+1}</span></p></body></html>")
        self.crossing_graphic.setPixmap(QPixmap(CROSSING_OPEN_PATH if state==1 else CROSSING_CLOSE_PATH))
        
    # @brief changes the switch shown in the switch control tab
    def set_selected_switch(self, index: int):
        """@brief changes the selected switch. updates the switch graphic"""
        
        self.selected_switch = index
        currstr = self.switch_table.item(index,3).text()
        if int(currstr[currstr.rfind(" "):])==int(self.switch_table.item(index,1).text()):
            state=1
        else:
            state=2
        self.set_displayed_switch_state(state)
        
    # @brief changes the signal shown in the signal control tab
    def set_selected_signal(self, index: int):
        """@brief changes the selected signal. updates the signal graphic"""
        
        self.selected_signal = index
        if self.signal_table.rowCount()==0:
            self.set_displayed_signal_state(1)
            return
        state = 1 if self.signal_table.item(index,1).text()=="Green" else 2
        self.set_displayed_signal_state(state)
        
    # @brief changes the crossing shown in the crossing control tab
    def set_selected_crossing(self, index: int):
        """@brief changes the selected crossing. updates the crossing graphic"""
        
        self.selected_crossing = index
        if self.crossing_table.rowCount()==0:
            self.set_displayed_crossing_state(1)
            return
        state = 1 if self.crossing_table.item(index,1).text()=="Open" else 2
        self.set_displayed_crossing_state(state)
        
    # @brief changes the block selected in the testbench
    def set_selected_block_tb(self, index: int):
        """@brief changes the selected block on the testbench table."""
        
        self.selected_tb_block = index
        b = self.tb_block_table.item(index, 0).text()
        s = self.tb_block_table.item(index, 1).text()
        self.tb_block_label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Section {s}, Block {b}</span></p></body></html>")
        self.tb_occ.setChecked(self.tb_block_table.item(index, 3).text()=="Occupied")
        self.tb_dis.setChecked(self.tb_block_table.item(index, 2).text()!="Open")
        
    # @brief changes the state of a switch on the switch table, tb table, and displayed switch (if applicable)
    def set_switch_table_state(self, block_id: int, state: int):
        """@brief changes the value of a switch on the table. updates graphic if switch is selected"""
        
        index = -1
        for i in range(self.switch_table.rowCount()):
            if int(self.switch_table.item(i,0).text())==block_id:
                index=i
                break
        tindex = -1
        for i in range(self.tb_block_table.rowCount()):
            if int(self.tb_block_table.item(i,0).text())==block_id:
                tindex=i
                break
        if index==-1 or tindex==-1:
            return
        owner = int(self.switch_table.item(index,0).text())
        primary = int(self.switch_table.item(index,1).text())
        secondary = int(self.switch_table.item(index,2).text())    
        if owner in {12,15,32,43}:
            new_table_entry = f"{primary} to {owner}" if state==1 else f"{primary} to {secondary}"
        else:
            new_table_entry = f"{owner} to {primary}" if state==1 else f"{owner} to {secondary}"
        self.switch_table.setItem(index,3,QTableWidgetItem(new_table_entry))
        self.tb_block_table.setItem(tindex,4,QTableWidgetItem(new_table_entry))
        if index==self.selected_switch:
            self.set_displayed_switch_state(state)
            
    # @brief changes the state of a signal on the signal table, tb table, and displayed signal (if applicable)
    def set_signal_table_state(self, block_id: int, state: int):
        """@brief changes the value of a signal on the table. updates graphic if signal is selected"""
        
        index = -1
        for i in range(self.signal_table.rowCount()):
            if int(self.signal_table.item(i,0).text())==block_id:
                index=i
                break
        tindex = -1
        for i in range(self.tb_block_table.rowCount()):
            if int(self.tb_block_table.item(i,0).text())==block_id:
                tindex=i
                break
        if index==-1 or tindex==-1:
            return
        new_table_entry = "Green" if state==1 else "Red"
        self.signal_table.setItem(index,1,QTableWidgetItem(new_table_entry))
        self.tb_block_table.setItem(tindex,5,QTableWidgetItem(new_table_entry))
        if index==self.selected_signal:
            self.set_displayed_signal_state(state)
            
    # @brief changes the state of a crossing on the crossing table, tb table, and displayed crossing (if applicable)
    def set_crossing_table_state(self, block_id: int, state: int):
        """@brief changes the value of a crossing on the table. updates graphic if crossing is selected"""
        
        index = -1
        for i in range(self.crossing_table.rowCount()):
            if int(self.crossing_table.item(i,0).text())==block_id:
                index=i
                break
        tindex = -1
        for i in range(self.tb_block_table.rowCount()):
            if int(self.tb_block_table.item(i,0).text())==block_id:
                tindex=i
                break
        if index==-1 or tindex==-1:
            return
        new_table_entry = "Open" if state==1 else "Closed"
        self.crossing_table.setItem(index,1,QTableWidgetItem(new_table_entry))
        self.tb_block_table.setItem(tindex,6,QTableWidgetItem(new_table_entry))
        if index==self.selected_crossing:
            self.set_displayed_crossing_state(state)
            
    # @brief changes the occupancy on all applicable tables
    def set_occupancy(self, block_id: int, occupied: bool):
        """@brief changes occupancy value of a block on all applicable tables"""
        
        index = -1
        for i in range(self.block_table_1.rowCount()):
            if int(self.block_table_1.item(i,0).text())==block_id:
                index=i
                break
        if index==-1:
            return #raise Exception(f"Block {block_id} not found")
        new_table_entry = "Occupied" if occupied else "Unoccupied"
        self.block_table_1.setItem(index,3,QTableWidgetItem(new_table_entry))
        self.block_table_2.setItem(index,3,QTableWidgetItem(new_table_entry))
        self.block_table_3.setItem(index,3,QTableWidgetItem(new_table_entry))
        self.tb_block_table.setItem(index,3,QTableWidgetItem(new_table_entry))
        
    def set_maintenance(self, block_id: int, maintenance: bool):
        """@brief changes maintenance state of a block on all applicable tables"""
        
        index = -1
        for i in range(self.block_table_1.rowCount()):
            if int(self.block_table_1.item(i,0).text())==block_id:
                index=i
                break
        if index==-1:
            return #raise Exception(f"Block {block_id} not found")
        new_table_entry = "Maintenance" if maintenance else "Open"
        self.block_table_1.setItem(index,2,QTableWidgetItem(new_table_entry))
        self.block_table_2.setItem(index,2,QTableWidgetItem(new_table_entry))
        self.block_table_3.setItem(index,2,QTableWidgetItem(new_table_entry))
        self.tb_block_table.setItem(index,2,QTableWidgetItem(new_table_entry))     
        
    def set_authority(self, block_id: int, authority: int):
        """@brief changes authority value of a block on testbench table"""
        
        index = -1
        for i in range(self.block_table_1.rowCount()):
            if int(self.block_table_1.item(i,0).text())==block_id:
                index=i
                break
        if index==-1:
            return
        if self.wayside_node.blocks[block_id].use_ws_authority:
            a = int(self.wayside_node.blocks[block_id].ws_authority*3.28)
            if a>1e6:
                new_table_entry = "inf (Wayside)"
            else:
                new_table_entry = f"{a} ft (Wayside)"
        else:
            a = int(self.wayside_node.blocks[block_id].ctc_authority*3.28)
            if a>1e6:
                new_table_entry = "inf (CTC)"
            else:
                new_table_entry = f"{a} ft (CTC)"
        self.tb_block_table.setItem(index,7,QTableWidgetItem(new_table_entry))
            
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
        self.set_node(wayside_nodes[index+1])
        
    def update_clock(self, time: str):
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Simulation time\n"f"{time}", None))
        
    def select_tb_block_action(self, index: any):
        self.set_selected_block_tb(index.row())
        
    def change_simspeed_action(self,value):
        sim.set_sim_speed(value)
        
    def pause_sim_action(self):
        if sim.running:
            sim.stop()
            self.pause_button.setIcon(QPixmap(PLAY_PATH))
        else:
            sim.start()
            self.pause_button.setIcon(QPixmap(PAUSE_PATH))
            
    def set_manual_mode_action(self,state):
        self.switch_toggle.setEnabled(bool(state))
        self.signal_toggle.setEnabled(bool(state))
        self.crossing_toggle.setEnabled(bool(state))
        self.wayside_node.set_manual_mode(bool(state))
        
    def upload_plc_action(self):
        path,_ = QFileDialog.getOpenFileName(self, 'Load PLC File', os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC"))
        print(path)
        if path[-4:]==".plc".lower():
            try:    
                self.wayside_node.load_plc_program(path,self.selected_program)
            except:
                print("\033[1;31mFailed to load PLC file\033[0m")
                traceback.print_exc()
            else:
                self.update_program_label(path)
        else:
            raise FileExistsError("Incorrect file extension")
        
    def set_yard_return_action(self, state):
        self.wayside_node.set_yard_return(bool(state))
        
    def update_program_label(self,path):
        delim_idx = path.rfind("\\")
        if delim_idx==-1: delim_idx = path.rfind("/")
        program = path[delim_idx+1:]            
        self.PLC_label.setText(program)
        
    def change_program_action(self,value:int):
        self.selected_program = value
        self.update_program_label(self.wayside_node.controller.plc_paths[value])

    """
    def upload_plc_action(self):
        path,_ = QFileDialog.getOpenFileName(self, 'Upload File', os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC"), "*.plc")
        if path[-4:]!=".plc":
            raise FileExistsError("Incorrect file type")
        print(path)
        self.wayside_node.load_plc_program(path)
    """
    def view_plc_action(self):
        if self.wayside_node.has_plc_program():
            QDesktopServices.openUrl(QUrl.fromLocalFile(self.wayside_node.controller.plc_paths[self.selected_program]))
            
    def toggle_switch_action(self):
        block_id = int(self.switch_table.item(self.selected_switch,0).text())
        current_state = self.wayside_node.blocks[block_id].switch.state
        new_state = 1 if current_state==2 else 2
        self.wayside_node.set_switch(block_id,new_state)
        self.set_switch_table_state(block_id,new_state)
        
    def toggle_signal_action(self):
        block_id = int(self.signal_table.item(self.selected_signal,0).text())
        current_state = self.wayside_node.blocks[block_id].signal.state
        new_state = 1 if current_state==2 else 2
        self.wayside_node.set_signal(block_id,new_state)
        self.set_signal_table_state(block_id,new_state)
        
    def toggle_crossing_action(self):
        block_id = int(self.crossing_table.item(self.selected_crossing,0).text())
        current_state = self.wayside_node.blocks[block_id].crossing.state
        new_state = 1 if current_state==2 else 2
        self.wayside_node.set_crossing(block_id,new_state)
        self.set_crossing_table_state(block_id,new_state)

    # testbench ##
        
    def set_occupancy_action(self,state):
        self.wayside_node.set_occupancy(int(self.tb_block_table.item(self.selected_tb_block,0).text()),bool(state))
        
    def set_maintenance_action(self,state):
        self.wayside_node.set_maintenance(int(self.tb_block_table.item(self.selected_tb_block,0).text()),bool(state))
        
if __name__=="__main__":
    try:
        app = QApplication(sys.argv)
        form = construct_ui()
        form.show()
        app.exec()
    finally:

        sim.cancel()