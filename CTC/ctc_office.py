from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import QDateTime, QDate, QTime, QTimer
from PySide6.QtWidgets import QApplication, QTableWidgetItem, QTableView, QAbstractItemView, QSizePolicy, QFileDialog
import sys
import os
import datetime
import openpyxl
import dataclasses
import pandas
import numpy as np
from collections import defaultdict

from Wayside_Controller_SW.ctc_to_wayside import CTCWaysideAPI
from Main.simulation_time import sim
#from CTC.ui.ctc_ui_loader import CTCUI
from CTC.ctc_objects import *

'''
TODO
Add new blocks
Get trains departing from a station
Get red line working
Send train to yard signal
Edit train route while train is enroute
'''

# wayside controller inputs
# blocks: list(dict[id:int, line:str, section:str, length:int (m), speed_limit:float (m/s), occupied:bool, maintenance:bool, switch:Switch, authority])
# layout: graph (adj matrix)
# 
# 
# TODO

# wayside controller outputs
# dispatch: dict(id:int, route:list(Block))
# maintenance: int
# switch: Block
# TODO

# Each module will have an API for each other moudle they talk to
# Each moudule will push data to API
# 


# faults
# power failure
# track circuit failure

DATA_PATH = os.path.join(os.getcwd(),"Other","data","Track Layout & Vehicle Data vF2.xlsx")
GREEN_DATA_PATH = os.path.join(os.getcwd(),"Track_Model","data","greenline.xlsx")
RED_DATA_PATH = os.path.join(os.getcwd(),"Track_Model","data","redline.xlsx")

@dataclasses.dataclass(frozen=False)
class ctcOffice:
    #API Stuff
    wayside_link: CTCWaysideAPI
    """API to send information to Wayside Controller"""
    stations:dict[str,dict[str,int]]            # {line: {station name:block id}}
    """Dictionary containing stations, in the form dict[line, dict[station name, block id]]"""
    blocks : dict[str,dict[int,Block]]  
    """Dictionary containing blocks, in the form dict[line, dict[block id, Block]]"""
    dispatched_trains:dict[int,Train]
    """Dictionary containing dispatched trains, in the form dict[train id, Train]"""
    scheduled_trains:dict[int,Train]
    """Dictionary containing scheduled trains, in the form dict[train id, Train]"""
    manual_block_list:dict[str,list[str]]
    """Dictionary containing block numbers, to be displayed on UI, in the form dict[line, list["{block section}{block id}"]]"""
    manual_station_list:dict[str,list[str]]
    """Dictionary containing names of stations to be displayed on UI, in the form dict[line, list[station names]]"""
    station_names:dict[str,dict[str,list[int]]]
    """Dictionary of stations and block ids, in the form dict[line, dict[station, line[ids]]]"""

    edge_graph:dict
    dwell_time:int
    """Dwell time in seconds"""

    ticket_sales: dict[QDateTime,int]
    """Stores the time and amount for each ticket sale in the form dict[time, amount]"""
    train_number:int
    base_suggested_speed:dict[str,dict[int,int]]
    """Stores an aveaged suggested speed value for each block"""
    #update_timer:QTimer
    ui_link: any    #ctc to ui link
    current_time:datetime
    to_dispatch:list[int]
    yard_return:dict[str, bool]


    def __init__(self):
        self.train_number = 1
        self.dwell_time = 60
        self.scheduled_trains = {}
        self.dispatched_trains = {}
        self.ticket_sales = None
        #self.update_timer = QTimer()
        #self.update_timer 
        self.current_time = sim.get_curr_datetime()
        wayside_link = None
        self.block_data = None
        #self.ui.blue_line_block_objects = blue_line_block_objects
        self.m_secs_passed = 0
        self.interval = 100
        self.simulation_speed = 1
        self.tm_to_ctc = None
        self.ticket_sales = {}
        self.to_dispatch = []
        self.yard_return = {
            "Green": False,
            "Red": False
        }
        #self.base_suggested_speed = {"Green":{}, "Red":{}}
        self.setup_blocks()
        #self.setup_timer()

    def link_wayside(self, link:CTCWaysideAPI):
        self.wayside_link = link
    
    def link_ui(self, ui_link:any):
        self.ui_link = ui_link

    def setup_timer(self):
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.time_update)
        self.update_timer.setInterval(500)
        self.update_timer.setSingleShot(False)
        self.update_timer.start()
        return
    
    def time_update(self):
        if not sim.running:
            return
        
        self.current_time = sim.get_curr_datetime()
        for (id, train) in self.scheduled_trains.items():
            if id not in self.to_dispatch and train.departure_time.secsTo(self.current_time) > 0:
                self.to_dispatch.append(id)
        
        
        for i in range(len(self.to_dispatch)):
            id = self.to_dispatch[i]
            occupied = False
            for block_id in dispatch_blocks[self.scheduled_trains[id].line]:
                if self.blocks[self.scheduled_trains[id].line][block_id].occupied:
                    occupied = True
            if not occupied:
                self.dispatch_train(id)
                print(f"CTC: 1 {self.to_dispatch}")
                self.to_dispatch.pop(i)
                print(f"CTC: 2 {self.to_dispatch}")
                break
        
        for (id, train) in self.dispatched_trains.items():
            if train.position == len(train.path)-1 and not self.blocks[train.line][train.path[train.position]].occupied:
                self.dispatched_trains.pop(id)
        self.update_tickets()
        self.update_train_stations()
        self.update_yard_return_red()
        #print("CTC: time update called")
        #self.update_authority()
        #self.update_suggested_speed()
        #self.update_train_positions()
        return

    def setup_blocks(self):
        red = pd.read_excel(DATA_PATH, sheet_name=2)
        green = pd.read_excel(DATA_PATH, sheet_name=3)
        self.blocks = {
            "Red": construct_block_list(red, "Red"),
            "Green": construct_block_list(green, "Green")
        }

        #self.blocks["Red"].pop(77)
        #self.blocks["Red"].pop(78)
        self.blocks["Red"][0] = Block(
            id=0,
            line="Red",
            section="",
            speed_limit = 30/3.6,
            infrastructure = "Yard",
            station=None,
            occupied=False,
            maintenance=False,
            switch=None,
            authority=0,
            suggested_speed=0,
            length=50
        )
        self.blocks["Green"][0] = Block(
            id=0,
            line="Green",
            section="",
            speed_limit = 30/3.6,
            infrastructure = "Yard",
            station=None,
            occupied=False,
            maintenance=False,
            switch=None,
            authority=0,
            suggested_speed=0,
            length=50
        )
        self.manual_block_list = {}
        self.manual_station_list = {}
        self.station_names = {}
        self.block_names = {}
        for (line) in lines.keys():
            self.manual_block_list[line] = []
            self.manual_station_list[line] = []
        for (line, blocks) in self.blocks.items():
            self.block_names[line] = {}
            for (id, block) in blocks.items():
                self.manual_block_list[line] += [str(block.section + str(block.id))]
                self.block_names[line][str(block.section + str(block.id))] = id
                if block.station != None:
                    if block.station not in self.manual_station_list[line]:
                        self.manual_station_list[line] += [str(block.station)]
                        self.station_names[block.station] = [id]
                    else:
                        self.station_names[block.station] += [id]
        

        self.edge_graph = {
            "Red": construct_edge_graph(red_adjmat),
            "Green": construct_edge_graph(green_adjmat)
        }
        #print(self.edge_graph)
        self.base_suggested_speed = {
            "Green": self.setup_suggested_speed("Green"),
            "Red" : self.setup_suggested_speed("Red")
        }

        return
    
    def setup_suggested_speed(self, line:str) -> dict[int,int]:
        base_suggested_speed = {}
        for (id, block) in self.blocks[line].items():
            explored = [id]
            for i in range(1):
                new_explored = list(explored)
                #print(f"{line}: {id}: {explored}")
                for node in explored:
                    neighbors = self.edge_graph[line][node]
                    for neighbor in neighbors:
                        if neighbor not in new_explored:
                            new_explored.append(neighbor)
                explored = new_explored
            min_speed_limit = self.blocks[line][explored[0]].speed_limit
            for node in explored:
                if self.blocks[line][node].speed_limit < min_speed_limit:
                    min_speed_limit = self.blocks[line][node].speed_limit
            min_sugg_speed = min_speed_limit*0.8
            for node in explored:
                if node in base_suggested_speed:
                    if min_sugg_speed < base_suggested_speed[node]:
                        base_suggested_speed[node] = min_sugg_speed
                else:
                    base_suggested_speed[node] = min_sugg_speed
            
        return base_suggested_speed
    
    def set_path(self, line:str, back:int, start:int, end:int) -> list:
        adj:list
        routes:list[list]
        current:list[int]
        backs = [[back]]
        queue = [[start]]
        if line == "Red":
            if end == 0:
                path_restrictions[line][16] = [15]
            else:
                path_restrictions[line][16] = [1]
        while queue:
            path = queue.pop(0)
            node = path[len(path)-1]
            neighbors = self.edge_graph[line][node]
            back = backs.pop(0)

            for neighbor in neighbors:
                if node in path_restrictions[line].keys() and neighbor in path_restrictions[line][node]:
                    continue
                if neighbor not in back:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append(new_path)
                    new_back = [node]
                    #Makes sure the train will not go on around a switch and the train will not go backwards
                    if self.blocks[line][neighbor].switch != None:
                        if node == self.blocks[line][neighbor].switch.primary:
                            new_back.append(self.blocks[line][neighbor].switch.secondary)
                        elif node == self.blocks[line][neighbor].switch.secondary:
                            new_back.append(self.blocks[line][neighbor].switch.primary)
                    backs.append(new_back)
                    if neighbor == end:
                        return new_path
        return [0]

    def set_route(self, line:str, train:list) -> (list[int], list[int]):
        #current_train = self.ui.current_train
        route = [0]
        block_dest:list[int]
        destinations_in_route = [0]
        back = 0
        start = 0
        for i in range(len(train)):
            destination = train[i][0]
            if type(destination) == str:
                block_dest = self.station_names[destination]
            elif type(destination) == int:
                block_dest = [destination]
            else:
                self.ui_link.send_error(f"Wrong Destination type {type(destination)} for destination #{i}")
                print(f"Wrong Destination type {type(destination)} for destination #{i}")
                return
            routes:list[list[int]]
            routes = []
            path = []
            min = 200
            min_index = 0
            for dest in block_dest:
                path = self.set_path(line, back, start, dest)
                routes.append(path)
                if len(path) < min:
                    min = len(path)
                    min_index = len(routes)-1

            path = routes[min_index]
            route.extend(path[1:])
            destinations_in_route.extend([len(route)-1])

            start = route[-1]
            back = route[-2 if len(route) >= 2 else 0]
        
        last_path = self.set_path(line, route[-2], route[-1], 0)
        route.extend(last_path[1:])
        destinations_in_route.extend([len(route)-1])
        return route, destinations_in_route

    def make_train(self, line:str, train:list, departure_time:QDateTime) -> None:
        
        route, destinations_in_route = self.set_route(line, train)

        path_speed = []
        path_authority = []
        path_time = [departure_time]
        time_to_dest_1 = 0
        time = self.current_time
        qtime = QDateTime(QDate(time.year, time.month, time.day), QTime(time.hour, time.minute, time.second))
        for i in range(destinations_in_route[1]):
            time_to_dest_1 += self.blocks[line][route[i]].length / self.base_suggested_speed[line][route[i]]
        if departure_time.addSecs(math.ceil(time_to_dest_1)) > train[0][1]:
            if train[0][1].addSecs(math.floor(-1*time_to_dest_1 - self.dwell_time)).secsTo(qtime) < 0: # train[0][1] - time > current time
                departure_time = train[0][1].addSecs(-1*time_to_dest_1 - self.dwell_time)
            else:
                departure_time = QDateTime(self.current_time)
        for dest in range(len(destinations_in_route)-1):
            start = destinations_in_route[dest]
            end = destinations_in_route[dest+1]
            segmented_authority = [self.blocks[line][route[end]].length/2]
            segmented_speed = []
            iterations = 0
            for i in range(end, start, -1):
                #segmented_authority.insert(0, self.blocks[line][route[i]].length/2)
                if i != end:
                    segmented_authority.insert(0, self.blocks[line][route[i]].length+segmented_authority[0])
                #segmented_speed.insert(0, min(self.base_suggested_speed[line][route[i]], iterations*3))
                segmented_speed.insert(0, self.base_suggested_speed[line][route[i]])
                iterations += 1
            segmented_speed.append(0)
            path_authority.extend(segmented_authority)
            path_speed.extend(segmented_speed)
        
        
        for i in range(1, len(route)):
            path_time.append(path_time[i-1].addSecs(math.floor(self.blocks[line][route[i]].length/self.base_suggested_speed[line][route[i]])))
            if i-1 in destinations_in_route and i != 1:
                path_time[i] = path_time[i].addSecs(self.dwell_time)
        path_authority.insert(0, path_authority[0]+self.blocks[line][route[0]].length)
        #path_authority.append(self.blocks[line][route[i]].length/2)
        '''
        if line == "Red":
            path_authority[len(path_authority)-22] = self.blocks[line][route[len(route)-22]].length/2
            #path_authority[len(path_authority)-23] = 0
            for i in range(len(path_authority)-23, destinations_in_route[len(destinations_in_route)-2], -1):
                path_authority[i] = path_authority[i+1] + self.blocks[line][route[i]].length
                print(f"{i}: {path_authority[i]}")
        '''
        destinations = []
        for dest in train:
            destinations.append(dest[0])
        arrival_times = []
        for dest in range(len(destinations_in_route)):
            arrival_times.append(path_time[dest])
        
        new_train = Train(
            id=self.train_number,
            line=line,
            destinations=destinations,
            departure_time=departure_time,
            destinations_in_route=destinations_in_route,
            arrival_times=arrival_times,
            path=route,
            position=None,
            authority=None,
            suggested_speed=None,
            path_authority=path_authority,
            path_speed=path_speed,
            path_time=path_time,
            dwelling=False
        )
        self.scheduled_trains[self.train_number] = new_train
        self.ui_link.update_trains(self.train_number)
        self.train_number += 1
        print("-------------------------------------------------------")
        #print(f"Id: {new_train.id}")
        #print(f"Destinations: {new_train.destinations}")
        #print(f"Destinations in Route: {new_train.destinations_in_route}")
        print(new_train)
        return
    
    def dispatch_train(self, train_id:int):
        if self.scheduled_trains[train_id].line == "Red":
            self.wayside_link.set_wayside_node(1)
        else:
            self.wayside_link.set_wayside_node(4)
        self.dispatched_trains[train_id] = self.scheduled_trains.pop(train_id)
        self.dispatched_trains[train_id].position = 0
        self.dispatched_trains[train_id].authority = self.dispatched_trains[train_id].path_authority[0]
        self.dispatched_trains[train_id].suggested_speed = self.dispatched_trains[train_id].path_speed[0]
        self.wayside_link.dispatch_train(math.ceil(self.dispatched_trains[train_id].path_authority[0]), 
                                         math.floor(self.dispatched_trains[train_id].path_speed[0]))
        self.ui_link.update_trains(train_id)
        self.update_auth_speed()
        return

    def simulation_slider(self, speed):
        sim.set_sim_speed(speed)
        return
    
    def manual_switch_clicked(self, swtich_state:int, line:str, id:int):
        nodes = self.find_node(line, id)
        for node in nodes:
            self.wayside_link.set_wayside_node(node)
            self.wayside_link.send_maintenance_switch(id, swtich_state+1)
        return
    
    def send_wayside_maintenance(self, line:str, id:int, maintenance:bool):
        nodes = self.find_node(line, id)
        for node in nodes:
            self.wayside_link.set_wayside_node(node)
            self.wayside_link.send_maintenance_status(id,maintenance)
        self.blocks[line][id].maintenance = maintenance
        return
    
    #Train will depart if current time is = max(arrival time + dwell time, dwell time)
    # this ensures that if the train is late, it will always stay for the dwell time
    # if the train is early, the train waits until the passengers expect the train to leave
    def update_train_stations(self):
        "@brief: Function ensures that trains depart from stations on time"
        for (id, train) in self.dispatched_trains.items():
            if not train.dwelling and train.position in train.destinations_in_route[1:]:
                train.dwelling = True
                nodes = self.find_node(train.line, train.path[train.position])
                for node in nodes:
                    self.wayside_link.set_wayside_node(node)
                    self.wayside_link.dwell_time_actions(train.path[train.position])
                    
                print(f"CTC: Train in Station")
            if train.dwelling and train.position in train.destinations_in_route:
                train_dest_index = train.destinations_in_route.index(train.position)
                #print(f"CTC: {train.path_time[train.position]}---------------------")
                #print(f"CTC: {train.path_time[train.position].addSecs(self.dwell_time).secsTo(self.current_time)}")
                #print(f"CTC:  {train.destinations_in_route} {train_dest_index}")
                #print(f"CTC: {train.destinations_in_route} {train_dest_index} {train.arrival_times[train_dest_index].addSecs(self.dwell_time).secsTo(self.current_time)}")
                if train.path_time[train.position].addSecs(self.dwell_time).secsTo(self.current_time) >= 0 and train.arrival_times[train_dest_index].addSecs(self.dwell_time).secsTo(self.current_time) >= 0:
                    train.dwelling = False
                    train.path_authority[train.position] = train.path_authority[train.position+1] + self.blocks[train.line][train.path[train.position]].length
                    train.path_speed[train.position] = self.base_suggested_speed[train.line][train.path[train.position]]
                    nodes = self.find_node(train.line, train.path[train.position])
                    for node in nodes:
                        self.wayside_link.set_wayside_node(node)
                        self.wayside_link.depart_train(train.path[train.position])
                        
                    self.update_auth_speed()
        return
    
    def update_train_positions(self):
        for (id, train) in self.dispatched_trains.items():
            if self.blocks[train.line][train.path[train.position+1]].occupied and not self.blocks[train.line][train.path[train.position]].occupied:
                train.position += 1
                train.path_time[train.position] = QDateTime(self.current_time)
                self.update_time_path(id)
                self.update_auth_speed()
                self.update_yard_return_green()
                
                
        return
    
    def update_time_path(self, train_id:int):
        train = self.dispatched_trains[train_id]
        #train.path_time[train.position] = QDateTime(self.current_time)
        for i in range(train.position+1, len(train.path_time)):
            train.path_time[i] = train.path_time[i-1].addSecs(int(self.blocks[train.line][train.path[i-1]].length/self.base_suggested_speed[train.line][train.path[i-1]]))
            if i-1 in train.destinations_in_route and i != 1:
                train.path_time[i] = train.path_time[i].addSecs(self.dwell_time)
        #print([x.toString("yyyy/MM/dd hh:mm:ss") for x in train.path_time])
        return

    def update_auth_speed(self):
        """@brief: Sends suggested speed and suggested authority to wayside"""
        auth_speed = {
            "Green": self.compare_auth_speed("Green"),
            "Red": self.compare_auth_speed("Red")
        }
        '''
        for id,train in self.dispatched_trains.items():
            if train.position < len(train.path)-2:
                if self.blocks[train.line][train.path[train.position+2]].occupied or self.blocks[train.line][train.path[train.position+2]].maintenance:
                    print(f"CTC: 2 in front of {id}")
                    auth_speed[train.line]["Authority"][train.path[train.position+1]] = self.blocks[train.line][train.path[train.position+1]].length/2
                    auth_speed[train.line]["Authority"][train.path[train.position]] = self.blocks[train.line][train.path[train.position+1]].length/2 + self.blocks[train.line][train.path[train.position]].length
                if self.blocks[train.line][train.path[train.position+1]].occupied or self.blocks[train.line][train.path[train.position+1]].maintenance:
                    print(f"CTC: 1 in front of {id}")
                    auth_speed[train.line]["Authority"][train.path[train.position]] = self.blocks[train.line][train.path[train.position]].length/2
        '''
        for line in lines:
            for (id, block) in self.blocks[line].items():
                nodes = self.find_node(line, id)
                for node in nodes:
                    self.wayside_link.set_wayside_node(node)
                    self.wayside_link.send_authority(id, math.floor(auth_speed[line]["Authority"][id]))
                    self.wayside_link.send_suggested_speed(id, auth_speed[line]["Speed"][id])
                block.authority = auth_speed[line]["Authority"][id]
                block.suggested_speed = auth_speed[line]["Speed"][id]

        #print(auth_speed)
        return

    def compare_auth_speed(self, line:str): 
        """@brief Compares the expected time to arrival for every block for every train and sets the authority to the closest train
        @param line:str - which line of blocks
        @returns a dict containing the authority and suggested speed"""
        authority = {}
        speed = {}
        cur_time = QDateTime(self.current_time)
        for (id, block) in self.blocks[line].items():
            min_time:QDateTime = None
            min_auth = -1
            min_speed = -1
            for (train_id, train) in self.dispatched_trains.items():
                if train.path[train.position] == id:
                    min_auth = train.path_authority[train.position]
                    min_speed = train.path_speed[train.position]
                    min_time = cur_time
                    break
                index = -1
                if id in train.path[train.position:]:
                    index = train.path.index(id, train.position)
                    if min_time is None or train.path_time[index] < min_time:
                        min_time = train.path_time[index]
                        min_auth = train.path_authority[index]
                        min_speed = train.path_speed[index]
            time_string = "None"
            if min_auth >= 0:
                authority[id] = min_auth
                speed[id] = min_speed
                time_string = min_time.toString("yyyy/MM/dd hh:mm:ss")
            else:
                authority[id] = self.blocks[line][id].length
            speed[id] = self.base_suggested_speed[line][id]         # +Justin

            #print(f"{id}, {min_auth}, {time_string}")
        auth_speed = {
            "Authority": authority,
            "Speed": speed
        }
        return auth_speed
    
    def update_occupancy_authority(self, id:int) -> list[int]:
        train = self.dispatched_trains[id]
        next_train = len(train.path)-1
        for i in range(train.position+1, len(train.path)):
            if self.blocks[train.line][train.path[i]].occupied or self.blocks[train.line][train.path[i]].maintenance:
                auth = -1*self.blocks[train.line][train.path[i-1]].length/2
                for j in range(i-1, train.position-1, -1):
                    auth += self.blocks[train.line][train.path[j]].length
                    nodes = self.find_node(train.line, train.path[j])
                    for node in nodes:
                        self.wayside_link.set_wayside_node(node)
                        #self.wayside_link.send_authority(train.path[j], auth)
            if self.blocks[train.line][train.path[i]].switch is not None:
                for j in range(train.position, i):
                    nodes = self.find_node(train.line, train.path[j])
                    for node in nodes:
                        self.wayside_link.set_wayside_node(node)
                        #self.wayside_link.send_authority(train.path[j], train.path_authority[j])
                return
        
        return
    
        
    
    def update_yard_return_green(self):
        """@brief Sends yard return signal to Wayside Controller if requirements have been met"""
        #Green line
        for i in range(len(green_yard_return_blocks)):
            for id,train in self.dispatched_trains.items():
                if train.path[train.position] == green_yard_return_blocks[i]:
                    if self.find_next_dest(train) == len(train.destinations_in_route)-1:
                        node = 4
                        self.wayside_link.set_wayside_node(node)
                        self.wayside_link.set_yard_return_mode(node, True)
                        self.yard_return["Green"] = True
                        return
                    else:
                        node = 4
                        self.wayside_link.set_wayside_node(node)
                        self.wayside_link.set_yard_return_mode(node, False)
                        self.yard_return["Green"] = False
                        return
                
        node = 4
        self.wayside_link.set_wayside_node(node)
        self.wayside_link.set_yard_return_mode(node, False)
        self.yard_return["Green"] = False
        return
    
    def update_yard_return_red(self):
        if self.yard_return["Red"]:
            travelling_train = False
            for id in red_yard_return_blocks:
                if self.blocks["Red"][id].occupied:
                    return
        
        waiting_train:Train = None

        for id, train in self.dispatched_trains.items():
            if train.path[train.position] == 77 and self.find_next_dest(train) == len(train.destinations_in_route)-1:
                waiting_train = train
                break
        
        if waiting_train is None:
            node = 1
            self.wayside_link.set_wayside_node(node)
            self.wayside_link.set_yard_return_mode(node, False)
            self.yard_return["Red"] = False
            return
        
        #Check for trains/occupancies
        for id,train in self.dispatched_trains.items():
            if train.path[train.position] in red_yard_return_blocks:
                node = 1
                self.wayside_link.set_wayside_node(node)
                self.wayside_link.set_yard_return_mode(node, False)
                self.yard_return["Red"] = False
                return

        #Check for maintenance
        for block_id in red_yard_return_blocks:
            if self.blocks["Red"][block_id].maintenance:
                node = 1
                self.wayside_link.set_wayside_node(node)
                self.wayside_link.set_yard_return_mode(node, False)
                self.yard_return["Red"] = False
                return
        print("CTC: Going")
        train.path_authority[train.position] = train.path_authority[train.position+1] + self.blocks["Red"][train.path[train.position]].length
        node = 1
        self.wayside_link.set_wayside_node(node)
        self.wayside_link.set_yard_return_mode(node, True)
        self.yard_return["Red"] = True
        self.update_auth_speed()
        return
    
    
    def find_next_dest(self, train:Train) -> int:
        if train.position is None:
            return 0
        next_dest_index:int = 0
        i = 1
        for dest in train.destinations_in_route[1:]:
            if train.position < dest:
                next_dest_index = i
                return i
            i += 1
        return train.destinations_in_route[len(train.destinations_in_route)-1]
    
    def calc_ticket_rate(self):

        pass

    def update_tickets(self):

        for (time, tickets) in self.ticket_sales.items():
           if time.addSecs(300).secsTo(self.current_time) < 0: # if time + 300 < current_time
                #self.ticket_sales.pop(time)
                pass
        ticket_rate = 0
        for (time, tickets) in self.ticket_sales.items():
            ticket_rate += tickets
        ticket_rate = ticket_rate * 12
        self.ui_link.update_ticket_sales(ticket_rate)
        return
    
    def wayside_faults(self):
        print("Wayside sent a fault")

    def find_node(self, line:str, block_id:int) -> list[int]:
        node:int
        if line=="Green":
            if block_id in range(74,105) or block_id == 152:
                node = [5]
            elif block_id in range(33,74) or block_id in range(105,144) or block_id==0:
                node = [4]
            else:
                node = [3]
        if line=="Red":
            if block_id in range(24, 46) or block_id in  range(67, 78):
                node = [1, 2]
            elif block_id in range(0, 24):
                node = [1]
            else:
                node = [2]
        return node

    def set_ticket_sales(self, line:str, ticket:int):
        #Track model calls this to send a bundle of ticket sales
        if self.current_time not in self.ticket_sales:
           self.ticket_sales[QDateTime(self.current_time)] = ticket
        else:
           self.ticket_sales[QDateTime(self.current_time)] += ticket
        return

    def set_occupancy(self, node:int, block_id:int, occupancy:bool):
        line = "Red" if node in [1,2] else "Green"
        
        self.blocks[line][block_id].occupied = occupancy
        self.ui_link.update_block_table(line, block_id)
        #self.update_authority()
        #self.update_suggested_speed()
        #self.update_auth_speed()
        self.update_train_positions()
        for (id, train) in self.dispatched_trains.items():
            self.update_time_path(id)
            self.update_occupancy_authority(id)
        self.update_train_stations()
        self.ui_link.update_train_info()
        print("CTC: Set occupancy")
        return



def main():
    app = QApplication(sys.argv)
    #ui = CTCUI()

    #ui.show()
    app.exec()

if __name__ == '__main__':
    #Set up blocks for demo
    main()

ctc_office = ctcOffice()
