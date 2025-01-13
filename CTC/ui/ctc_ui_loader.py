from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QDateTime, QDate, QTime, QTimer
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QTableView, QAbstractItemView, QSizePolicy, QFileDialog
import sys
import os
import CTC.ui.ctc_ui as ui
from CTC.ctc_office import ctc_office as ctc, ctcOffice
from CTC.ctc_objects import *
import datetime
import openpyxl
import dataclasses
import pandas
import inspect
from Main.simulation_time import sim


ICON_PATH = os.path.join(os.getcwd(),"Other","AuroraLogo.jpg")
PAUSE_PATH = os.path.join(os.getcwd(),"Other","pause_button.jpg")
PLAY_PATH = os.path.join(os.getcwd(),"Other","play_button.jpg")


red_line_blocks = [str(b) for b in range(0,77)]
green_line_blocks = [str(b) for b in range(0,151)]
blue_line_blocks = [str(b) for b in range(1,16)]


@dataclasses.dataclass(frozen=False)
class CTCUI(QtWidgets.QMainWindow):
    is_manual_mode:bool
    current_train:list[str,datetime.datetime]
    train_number:int
    selected_block:int
    start_time = QDateTime()
    simulation_speed:int
    interval:int
    backend:ctcOffice
    update_timer:QTimer
    selected_train:int
    clicked:bool
    

    tb_selected_train:Train
    tb_selected_block:int
    

    def __init__(self, parent=None):
        super(CTCUI, self).__init__()
        self.ui =  ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.backend = ctc
        
        icon = QtGui.QIcon(ICON_PATH)
        self.setWindowIcon(icon)
        self.setWindowTitle("CTC Office")

        #declarations
        self.is_manual_mode = False
        self.current_train = []
        self.train_number = 1
        self.selected_block = None
        self.start_time = QDateTime()
        self.clicked = False
        
        self.simulation_speed = 1
        self.interval = 50
        self.manual_block_list = {"red": red_line_blocks, "green": green_line_blocks, "blue": blue_line_blocks}
        
        self.selected_train = -1
        self.selected_block = -1

        #self.tb_selected_train:Train
        #self.tb_selected_block = 0

        #timer
        #self.start_time = QDateTime.currentDateTime()
        update_timer = QTimer(self)
        update_timer.timeout.connect(self.time_update)
        update_timer.setInterval(self.interval)
        update_timer.setSingleShot(False)
        update_timer.start()

        self.setup()

        #Testbench
        self.setup_tb_tab()
        #self.ui.tb_train_table.cellClicked.connect(self.tb_train_table_clicked)
        #self.ui.tb_block_table.cellClicked.connect(self.tb_block_table_clicked)
        #self.ui.tb_block_status_input.currentTextChanged.connect(self.tb_status_input_clicked)


        return
    
    def setup(self):
        self.setup_header()
        self.setup_dispatch()
        self.setup_train()
        self.setup_block()
        self.ui.Automatic_Layout.setFixedWidth(self.ui.Manual_Layout.width())
    
        #self.setup_button_connections()
        #self.setup_manual_lists()
        return

    def setup_header(self):
        """@brief set up ui elements and button connection for header"""
        self.ui.header_layout.setAutoFillBackground(True)
        p = self.ui.header_layout.palette()
        p.setColor(self.ui.header_layout.backgroundRole(), QtGui.QColor(242, 205, 109, 255))
        self.ui.header_layout.setPalette(p)
        self.ui.header_icon.setPixmap(QtGui.QPixmap(ICON_PATH))
        time = datetime.datetime(2020,1,1,1,1,1,1)        #self.backend.current_time
        current_time = QDateTime(QDate(time.year, time.month, time.day), QTime(time.hour, time.minute, time.second))
        self.ui.header_time_display.setText(str(current_time.toString("MM/dd/yyyy hh:mm:ss")))
        self.ui.simulation_slider.sliderMoved.connect(self.simulation_slider)
        self.ui.header_pause_button.clicked.connect(self.play_pause_clicked)
        return
    
    def setup_dispatch(self):
        """@brief set up ui elements and button connection for dispatch section"""
        # manual mode setup
        self.ui.Manual_Layout.setDisabled(True)
        self.ui.Manual_Layout.hide()
        self.ui.send_automatic_button.toggled.connect(self.ui.Automatic_Layout.setVisible)
        self.ui.send_manual_button.toggled.connect(self.ui.Manual_Layout.setVisible)
        #self.ui.send_manual_button.toggled.connect(self.ui.manual_block_layout.setVisible)
        self.ui.send_automatic_button.toggled.connect(self.ui.Automatic_Layout.setEnabled)
        self.ui.send_manual_button.toggled.connect(self.ui.Manual_Layout.setEnabled)
        self.ui.send_manual_button.toggled.connect(self.ui.manual_block_layout.setEnabled)

        self.ui.manual_train_time_input.setDateTime(self.backend.current_time)

        automatic_policy = self.ui.Automatic_Layout.sizePolicy()
        automatic_policy.setHorizontalPolicy(QtWidgets.QSizePolicy.Policy.Fixed)
        self.ui.Automatic_Layout.setSizePolicy(automatic_policy)
        self.ui.Automatic_Layout.setFixedWidth(self.ui.Manual_Layout.width())

        #manual mode setup
        manual_dispatch_header = self.ui.manual_route_table.horizontalHeader()
        manual_dispatch_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)
        manual_dispatch_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.manual_route_table.setHorizontalHeader(manual_dispatch_header)
        table_policy = self.ui.manual_route_table.sizePolicy()
        table_policy.setRetainSizeWhenHidden(True)
        self.ui.manual_route_table.setSizePolicy(table_policy)
        self.reset_current_train()

        
        self.ui.Automatic_Layout.setFixedWidth(self.ui.Manual_Layout.width())

        #automatic mode buttons
        self.ui.automatic_upload_button.clicked.connect(self.automatic_upload)

        #manual mode buttons
        self.ui.manual_train_line_input.currentTextChanged.connect(self.change_available_stations)  # Logic for changing the stations based on the line
        self.ui.manual_train_station_input.activated.connect(self.reset_block_input)
        self.ui.manual_train_block_input.activated.connect(self.reset_station_input)
        self.ui.manual_train_destination_button.released.connect(self.add_destination)   # Logic for the Add destination button
        self.ui.manual_train_dispatch_button.clicked.connect(self.dispatch_button_clicked)
        self.ui.manual_reset_button.clicked.connect(self.reset_current_train)
        
        
        return
    
    def setup_train(self):
        """@brief set up ui elements and button connection for train display"""
        scheduled_header = self.ui.train_schedule_table.horizontalHeader()
        scheduled_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)
        scheduled_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Fixed)
        scheduled_header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.train_schedule_table.setHorizontalHeader(scheduled_header)

        dispatched_header = self.ui.train_dispatch_table.horizontalHeader()
        dispatched_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)
        dispatched_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Fixed)
        dispatched_header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.train_dispatch_table.setHorizontalHeader(dispatched_header)

        route_header = self.ui.train_route_table.horizontalHeader()
        route_header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Stretch)
        route_header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.ui.train_route_table.setHorizontalHeader(route_header)

        self.ui.train_schedule_table.cellClicked.connect(self.scheduled_table_clicked)
        self.ui.train_dispatch_table.cellClicked.connect(self.dispatched_table_clicked)

        return
    
    def setup_block(self):
        """@brief set up ui elements and button connections for block section"""
        self.ui.manual_block_switch_input.show()
        self.ui.manual_block_switch_input.setEnabled(False)
        self.ui.manual_block_open_button.show()
        self.ui.manual_block_open_button.setEnabled(False)
        self.ui.manual_block_close_button.setVisible(False)
        self.ui.manual_block_layout.setVisible(True)

        block_table = self.ui.manual_block_table
        header = block_table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableview = QTableView()
        self.tableview.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)

        # Block maintanence
        block_table = self.ui.manual_block_table
        
        block_table.cellClicked.connect(self.manual_block_table_click)
        self.ui.manual_block_close_button.clicked.connect(self.manual_block_close_clicked)
        self.ui.manual_block_open_button.clicked.connect(self.manual_block_open_clicked)
        self.ui.manual_block_switch_input.currentIndexChanged.connect(self.manual_switch_clicked)
        self.ui.block_line_input.currentTextChanged.connect(self.change_block_line)
        # Setup blocks in table
        self.change_block_line("Green Line")

        return
    
    def time_update(self):
        self.ui.header_time_display.setText(sim.get_curr_string())
        self.backend.time_update()

        #print(self.backend.scheduled_trains.keys())
        #print(self.backend.dispatched_trains.keys())
        return
    
    def simulation_slider(self, value):
        self.backend.simulation_slider(value)
        return
    
    def play_pause_clicked(self):
        print(f"Pause/Play pressed with Sim: {sim.running}")
        if sim.running:
            sim.stop()
            self.ui.header_pause_button.setText("Play")
            #self.ui.header_pause_button.setIcon(QtGui.QPixmap(PLAY_PATH))
            #self.ui.header_pause_button.setIcon(QtGui.QPixmap(PLAY_PATH))
            print("In sim.running")
        else:
            sim.start()
            #self.ui.header_pause_button.setIcon(QtGui.QPixmap(PAUSE_PATH))
            self.ui.header_pause_button.setText("Pause")
            print("In not sim.running")
        return
    
    def automatic_upload(self):
        if self.clicked:
            self.clicked = False
            return
        else:
            self.clicked = True
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setNameFilter("Excel(*.xlsx)")
        dialog.setViewMode(QFileDialog.ViewMode.Detail)
        dialog.setDirectory(os.getcwd())
        fileName = []
        if dialog.exec():
            fileName = dialog.selectedFiles()
        #schedule = openpyxl.load_workbook(fileName[0])
        #sheet = schedule.get_sheet_by_name("Sheet1")
        schedule = pd.read_excel(fileName[0], sheet_name=0)
        time = []
        stations = []
        train:list
        line:str
        departure_time:QDateTime


        for row, series in schedule.iterrows():
            print(f"{row}: {series}")
            if row == 0:
                line = series.loc["Line"]
                if len(series) >= 2:
                    departure_time = QDateTime(series.loc["Departure Time"])
                    if departure_time.secsTo(self.backend.current_time) > 0:
                        departure_time = QDateTime(self.backend.current_time)
                else:
                    departure_time = QDateTime(self.backend.current_time)
            elif row == 2:
                stations.append(str(series.iloc[0]))
                time.append(QDateTime((departure_time.addSecs(series.iloc[1]*60))))
            elif row > 2:
                time.append(QDateTime((time[len(time)-1].addSecs(series.iloc[1]*60))))
                stations.append(str(series.iloc[0]))


        #print(f"{[value for value in rows]}")
        #print(f"{[value for value in cols]}")
        '''
        for row in rows:
            #print(f"{row},{row[0].value}, {row[1].value}")
            val0 = row[0].value
            val1 = row[1].value
            if type(row[0]) != str:
                continue
            if row[0].value in ["Line", "Station"]:
                continue
            elif row[0].value in ["Red", "Green"]:
                line = row[0].value
                if len(row) > 1:
                    departure_time = QDateTime(row[1].value)
                else:
                    departure_time = self.backend.current_time
            else:
                stations.append(row[0].value)
                time.append(departure_time.addSecs(row[1].value*60))
        '''
        print(line)
        print(time)
        print(stations)
        train = []
        for i in range(len(time)):
            train.append([stations[i], time[i]])
        print(train)

        self.backend.make_train(line, train, departure_time)

        return
    #Defines logic for when the a line is selected in manual mode, changes the lists for 
    def change_available_stations(self):    #move
        line = self.ui.manual_train_line_input.currentText()
        if line == "Green Line":
            self.ui.manual_train_station_input.clear()
            self.ui.manual_train_station_input.addItems(self.backend.manual_station_list["Green"])
            self.ui.manual_train_block_input.clear()
            self.ui.manual_train_block_input.addItems(self.backend.manual_block_list["Green"])
        elif line == "Red Line":
            self.ui.manual_train_station_input.clear()
            self.ui.manual_train_station_input.addItems(self.backend.manual_station_list["Red"])
            self.ui.manual_train_block_input.clear()
            self.ui.manual_train_block_input.addItems(self.backend.manual_block_list["Red"])
        else:
            print("Choose valid line")
            self.set_error("Choose valid line")
        self.reset_current_train()
        return
    
    def reset_current_train(self):
        self.ui.manual_route_table.setRowCount(0)
        self.current_train = []
        self.reset_block_input()
        self.reset_station_input()
        return
    
    def reset_block_input(self):
        self.ui.manual_train_block_input.setCurrentIndex(-1)
        self.ui.manual_train_block_input.setCurrentText("Select Block")

    def reset_station_input(self):
        self.ui.manual_train_station_input.setCurrentIndex(-1)
        self.ui.manual_train_station_input.setCurrentText("Select Station")

    def add_destination(self):
        print("Add destinations called")
        if self.clicked:
            self.clicked = False
            #return
        else:
            self.clicked = True
        line = self.ui.manual_train_line_input.currentText()
        line = "Green" if self.ui.manual_train_line_input.currentText()=="Green Line" else "Red"
        station = self.ui.manual_train_station_input.currentIndex()
        block = self.ui.manual_train_block_input.currentIndex()
        #id = block+1
        id:int = None
        time = self.ui.manual_train_time_input.dateTime()
        
        destination:str
        if station == -1 and block != -1:       #block selected
            id = self.backend.block_names[line][self.backend.manual_block_list[line][block]]
            destination = str(self.backend.blocks[line][id].section + str(self.backend.blocks[line][id].id))
            self.current_train.append([id, time])
        elif station != -1 and block == -1:     #station selected
            destination = self.ui.manual_train_station_input.currentText()
            self.current_train.append([destination, time])
        else:
            self.set_error("Neither Station nor Block is Selected")
            print("Neither Station nor Block is selected")
            print(f"{station}, {block}")
            return

        row_length = self.ui.manual_route_table.rowCount()
        self.ui.manual_route_table.insertRow(row_length)
        self.ui.manual_route_table.setItem(row_length, 0, QTableWidgetItem(destination))
        self.ui.manual_route_table.setItem(row_length, 1, QTableWidgetItem(time.toString("hh:mm MM/dd/yyyy")))
        print(self.current_train)
        return
    
    def dispatch_button_clicked(self):
        print("dispatch_button clicked")
        if self.clicked:
            self.clicked = False
            #return
        else:
            self.clicked = True
        if len(self.current_train) == 0:
            self.set_error("Train must have more than 0 destinations")
            print("Train must have more than 0 destinations")
            return

        train = self.current_train
        departure_time = train[0][1]
        line = "Green" if self.ui.manual_train_line_input.currentText()=="Green Line" else "Red"
        self.backend.make_train(line, train, departure_time)

        self.reset_current_train()
        return
    
    def scheduled_table_clicked(self, row:int, column:int):
        self.selected_train = int(self.ui.train_schedule_table.item(row, 1).text())
        self.update_train_info()
        return
    
    def dispatched_table_clicked(self, row:int, column:int):
        self.selected_train = int(self.ui.train_dispatch_table.item(row, 1).text())
        self.update_train_info()
        print(f"CTC: {int(self.ui.train_dispatch_table.item(row, 1).text())}")
        return

    def update_scheduled_table(self, train_id:int):
        table = self.ui.train_schedule_table
        ids = []
        for row in range(table.rowCount()):
            it = table.item(row, 1)
            id = int(it.text()) if it is not None else -1
            ids.append(id)
        if train_id in self.backend.scheduled_trains.keys():
            if train_id in ids:
                index = ids.index(train_id)
                table.setItem(rowCount, 0, QTableWidgetItem(self.backend.scheduled_trains[train_id].line))
                table.setItem(rowCount, 1, QTableWidgetItem(str(train_id)))
                table.setItem(rowCount, 2, QTableWidgetItem(self.backend.scheduled_trains[train_id].departure_time.toString("hh:mm MM/dd/yyyy")))
            else:
                rowCount = table.rowCount()
                table.insertRow(rowCount)
                table.setItem(rowCount, 0, QTableWidgetItem(self.backend.scheduled_trains[train_id].line))
                table.setItem(rowCount, 1, QTableWidgetItem(str(train_id)))
                table.setItem(rowCount, 2, QTableWidgetItem(self.backend.scheduled_trains[train_id].departure_time.toString("hh:mm MM/dd/yyyy")))
        elif train_id in ids and train_id not in self.backend.scheduled_trains.keys():
            index = ids.index(train_id)
            table.removeRow(index)
        return
    
    def update_dispatched_table(self, train_id:int):
        table = self.ui.train_dispatch_table
        ids = []
        for row in range(table.rowCount()):
            it = table.item(row, 1)
            id = int(it.text()) if it is not None else -1
            ids.append(id)
        if train_id in self.backend.dispatched_trains.keys():
            if train_id in ids:
                index = ids.index(train_id)
                table.setItem(rowCount, 0, QTableWidgetItem(self.backend.dispatched_trains[train_id].line))
                table.setItem(rowCount, 1, QTableWidgetItem(str(train_id)))
                table.setItem(rowCount, 2, QTableWidgetItem(self.backend.dispatched_trains[train_id].departure_time.toString("hh:mm MM/dd/yyyy")))
            else:
                rowCount = table.rowCount()
                table.insertRow(rowCount)
                table.setItem(rowCount, 0, QTableWidgetItem(self.backend.dispatched_trains[train_id].line))
                table.setItem(rowCount, 1, QTableWidgetItem(str(train_id)))
                table.setItem(rowCount, 2, QTableWidgetItem(self.backend.dispatched_trains[train_id].departure_time.toString("hh:mm MM/dd/yyyy")))
        elif train_id in ids and train_id not in self.backend.dispatched_trains.keys():
            index = ids.index(train_id)
            table.removeRow(index)
        return
    
    def update_train_info(self):
        train:Train
        print(f"{self.selected_train}-----------")
        if self.selected_train in self.backend.scheduled_trains.keys():
            train = self.backend.scheduled_trains[self.selected_train]
            print(f"Selected train in scheduled")
        elif self.selected_train in self.backend.dispatched_trains.keys():
            train = self.backend.dispatched_trains[self.selected_train]
            print(f"Selected train is dispatched")
        else:
            self.ui.train_id_display.setText("No Train Selected")
            self.ui.train_line_display.setText("No Train Selected")
            self.ui.train_position_display.setText("No Train Selected")
            self.ui.train_destination_display.setText("No Train Selected")
            self.ui.tb_authority_value.setText("No Train Selected")
            self.ui.tb_speed_value.setText("No Train Selected")
            self.ui.train_route_table.setRowCount(0)
            print(f"Selected train not found")
            return
        
        self.ui.train_id_display.setText(str(train.id))
        self.ui.train_line_display.setText(train.line)
        position:str
        if train.position is None:
            position = "None"
        else:
            position = f"{self.backend.blocks[train.line][train.path[train.position]].section}{self.backend.blocks[train.line][train.path[train.position]].id}"
        self.ui.train_position_display.setText(position)

        next_dest_index:int
        next_dest_index = self.backend.find_next_dest(train)
        print(f"Next Destination Index: {next_dest_index}")
        next_dest:str
        if next_dest_index is None:
            next_dest = "No Destination Found"
        else:
            if next_dest_index == len(train.destinations_in_route) - 1:
                next_dest = "Yard"
            else:
                next_dest = train.destinations[next_dest_index - 1]
        self.ui.train_destination_display.setText(self.destination_to_string(train.line, next_dest))
        
        self.ui.train_route_table.setRowCount(0)
        for i in range(len(train.destinations_in_route)):
            self.ui.train_route_table.insertRow(i)
            destination = train.destinations[i-1] if i >= 1 and i < len(train.destinations_in_route)-1 else 0 
            self.ui.train_route_table.setItem(i, 0, QTableWidgetItem(self.destination_to_string(train.line, destination)))
            self.ui.train_route_table.setItem(i, 1, QTableWidgetItem(train.path_time[train.destinations_in_route[i]].toString("MM/dd/yyyy hh:mm:ss")))
        
        return

    def update_ticket_sales(self, ticket_rate:int):
        self.ui.block_throughput_display.setText(str(ticket_rate) + " /hr")
        return

    def manual_block_table_click(self, row, column):
        policy = self.ui.manual_block_open_button.sizePolicy()
        policy.setRetainSizeWhenHidden(False)
        self.ui.manual_block_open_button.setSizePolicy(policy)
        self.selected_block = row
        line:str
        if self.ui.block_line_input.currentText() == "Green Line":
            line = "Green"
        else:
            line = "Red"
        block = self.backend.blocks[line][row]
        self.update_maintenance_buttons()
        
        if block.switch != None:
            self.ui.manual_block_switch_input.setEnabled(True)
            switches = [str(block.section + str(block.id)) + " to " + str(self.backend.manual_block_list[line][block.switch.primary]), 
                        str(block.section + str(block.id)) + " to " + str(self.backend.manual_block_list[line][block.switch.secondary])]
            self.ui.manual_block_switch_input.clear()
            self.ui.manual_block_switch_input.addItems(switches)
            self.ui.manual_block_switch_input.setCurrentIndex(-1)
            self.ui.manual_block_switch_input.setCurrentText("Select Switch State")
        else:
            self.ui.manual_block_switch_input.setEnabled(False)
        return
    
    def update_maintenance_buttons(self):
        line = "Green" if self.ui.block_line_input.currentText() == "Green Line" else "Red"
        block = self.backend.blocks[line][self.selected_block]
        if block.maintenance:
            self.ui.manual_block_close_button.hide()
            self.ui.manual_block_close_button.setEnabled(False)
            self.ui.manual_block_open_button.show()
            self.ui.manual_block_open_button.setEnabled(True)
        elif not block.maintenance:
            self.ui.manual_block_close_button.show()
            self.ui.manual_block_close_button.setEnabled(True)
            self.ui.manual_block_open_button.hide()
            self.ui.manual_block_open_button.setEnabled(False)
        else:
            self.ui.manual_block_close_button.show()
            self.ui.manual_block_close_button.setEnabled(False)
            self.ui.manual_block_open_button.hide()

    def change_block_line(self, line:str):
        
        if line=="Green Line":
            line = "Green"
        elif line=="Red Line":
            line = "Red"
        else:
            self.set_error("Block Line not available")
            print("Block Line not available")
        
        block_table = self.ui.manual_block_table
        block_table.setRowCount(0)

        for id in range(len(self.backend.blocks[line].items())):
            block = self.backend.blocks[line][id]
            block_table.insertRow(id)
            block_table.setItem(id, 0, QTableWidgetItem(str(block.section + str(block.id))))
            status:str
            if block.maintenance:
                status = "Maintenance"
            elif block.occupied:
                status = "Occupied"
            else:
                status = "Unoccupied"
            block_table.setItem(id, 1, QTableWidgetItem(status))
            infrastructure = block.infrastructure if type(block.infrastructure) == str else ""
            block_table.setItem(id, 2, QTableWidgetItem(infrastructure))
            

        self.selected_block = None
        #self.ui.manual_block_layout.hide()
        return
    
    def update_block_table_row(self, line:str, id:int):
        displayed_line = "Green" if self.ui.block_line_input.currentText()=="Green Line" else "Red"
        if displayed_line != line:
            return
        block_table = self.ui.manual_block_table
        block = self.backend.blocks[line][id]
        block_table.setItem(id, 0, QTableWidgetItem(str(block.section + str(block.id))))
        status:str
        if block.maintenance:
            status = "Maintenance"
        elif block.occupied:
            status = "Occupied"
        else:
            status = "Unoccupied"
        block_table.setItem(id, 1, QTableWidgetItem(status))
        infrastructure = block.infrastructure if type(block.infrastructure) == str else ""
        block_table.setItem(id, 2, QTableWidgetItem(infrastructure))
        return

    def manual_block_close_clicked(self):
        line = "Green" if self.ui.block_line_input.currentText()=="Green Line" else "Red"
        if self.backend.blocks[line][self.selected_block].occupied:
            self.set_error(f"Cannot put an occupied block into maintenace")  # Add a fault pop up
            print(f"Cannot put an occupied block into maintenace")  # Add a fault pop up
        else:
            self.backend.blocks[line][self.selected_block].maintenance = True
            self.update_block_table_row(line, self.selected_block)
            self.backend.send_wayside_maintenance(line, self.selected_block, True)
            self.update_maintenance_buttons()
        return
    
    def manual_block_open_clicked(self):
        line = "Green" if self.ui.block_line_input.currentText()=="Green Line" else "Red"
        self.backend.blocks[line][self.selected_block].maintenance = False
        self.update_block_table_row(line, self.selected_block)
        self.backend.send_wayside_maintenance(line, self.selected_block, False)
        self.update_maintenance_buttons()
        return
    
    def manual_switch_clicked(self, switch_state:int):
        line = "Green" if self.ui.block_line_input.currentText()=="Green Line" else "Red"
        self.backend.manual_switch_clicked(switch_state, line, self.selected_block)
        return
    
    def destination_to_string(self, line:str, destination) -> str:
        dest:str
        if type(destination) == int:
            if destination == 0:
                dest = "Yard"
            else:
                dest = self.backend.blocks[line][destination].section + str(self.backend.blocks[line][destination].id)
        else:
            dest = destination

        return dest
    
    def setup_tb_tab(self):

        #self.ui.tb_train_input.setCurrentIndex(-1)
        #self.ui.tb_train_input.setCurrentText("Search Trains")
        
        #self.ui.tb_block_input.setCurrentIndex(-1)
        #self.ui.tb_block_input.setCurrentText("Search Blocks")

        #self.update_tb_tab()
        self.ui.tb_position_input.clicked.connect(self.send_ticket)
        return

    def set_error(self, error:str):
        self.ui.manual_error_label.setText(error)
        self.ui.automatic_error_label.setText(error)
        return

    def tb_block_occupancy(self):
        line = "Green" if self.ui.block_line_input.currentText()=="Green Line" else "Red"
        node = self.backend.find_node(line, self.selected_block)
        self.backend.set_occupancy(node, self.selected_block, not self.backend.blocks[line][self.selected_block].occupied)
        return

    def tb_update_train_info(self):
        
        self.ui.tb_authority_value.setText(str(f"{self.backend}"))
        return

    def get_ctc_backend(self):
        return self.backend

    def send_ticket(self):
        self.backend.set_ticket_sales("Green", 100)


def main():
    app = QApplication(sys.argv)
    ui = CTCUI()

    ui.show()
    app.exec()

if __name__ == '__main__':
    #Set up blocks for demo
    main()