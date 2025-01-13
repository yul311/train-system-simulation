import pandas
import dataclasses
import os
import numpy as np
from datetime import datetime, timedelta
import math
from collections import defaultdict
from PySide6.QtCore import QDateTime
import pandas as pd


# wayside node placement
red_nodes = {
    1: "ABCDEFG",
    2: "HOPQRST",
    3: "IJKLMN"
}
green_nodes = {
    4: "ABCDE",
    5: "FGHIWXYZ",
    6: "JKLTUV",
    7: "MNOPQRS"
}
blue_nodes = {
    8: "ABC"
}

lines = ["Green", "Red"]

all_nodes = {}
all_nodes.update(red_nodes)
all_nodes.update(green_nodes)
all_nodes.update(blue_nodes)

nodes = {
    1,
    2,
    3,
    4,
    5,
    6,
    7
}

red_adjmat = np.loadtxt(os.path.join(os.getcwd(),"Other","red_adj.txt"))
green_adjmat = np.loadtxt(os.path.join(os.getcwd(),"Other","green_adj.txt"))

'''
@brief  track blocks
@attributes
block_number    block number
line            line
section         block section
length          length of block in meters
speed_limit     m/s
infrastructure  
authority       meters
suggested_speed m/s
'''

@dataclasses.dataclass(frozen=False,unsafe_hash=True)
class Block:
    # static
    id: int
    line: str
    section: str
    length:int
    speed_limit:float
    infrastructure:str
    station:str
    switch: "Switch"
    # dyn
    occupied: bool
    maintenance: bool
    authority:int
    suggested_speed:float

@dataclasses.dataclass(frozen=False)
class Switch:
    
    # static
    primary: int
    secondary: int

@dataclasses.dataclass(frozen=False,unsafe_hash=True)
class Train:
    # static
    id: int
    line: str
    destinations:list[str]
    departure_time: QDateTime
    # dyn
    destinations_in_route:list[int]
    arrival_times:list[QDateTime] #secs
    path:list
    position:int
    authority:int
    suggested_speed:int
    path_authority:list[int]
    path_speed:list
    path_time:list[QDateTime]
    dwelling:bool

# block 0 is the yard
red_switches = {
    9: (10,0),
    16: (15,1),
    27: (28,76),
    33: (32,72),
    38: (39,71),
    44: (43,67),
    52: (53,66),
}
green_switches = {
    13: (12,1),
    29: (30,150),
    57: (58, 0),
    62: (63, 0),
    77: (76,101),
    85: (86,100),
}

red_stations = {
    7 : "SHADYSIDE",
    16: "HERRON AVE",
    21: "SWISSVILLE",
    25: "PENN STATION",
    35: "STEEL PLAZA",
    45: "FIRST AVE",
    48: "STATION SQUARE",
    60: "SOUTH HILLES JUNCTION",
}

green_stations = {
    0: "YARD",
    2: "PIONEER",
    9: "EDGEBROOK",
    22: "WHITED",
    31: "SOUTH BANK",
    48: "INGLEWOOD",
    57: "OVERBROOK",
    65: "GLENBURY",
    73: "DORMONT",
    77: "MT LEBANON",
    88: "POPLAR",
    96: "CASTLE SHANNON",
    105: "DORMONT",
    114: "GLENBURY",
    123: "OVERBROOK",
    132: "INGLEWOOD",
    141: "CENTRAL"
}
green_yard_return_blocks = [57, 56, 55, 54, 53]
red_yard_return_blocks = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
lines = {
    "Red":"ABCDEFGHIJKLMNOPQRST",
    "Green":"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
}

path_restrictions = {
    "Red": {
        27: [76],
        33: [32],
        38: [71],
        44: [43],
        52: [66],
    },
    "Green":{}
}
dispatch_blocks = {
    "Red": [0, 9, 8, 10, 11, 12, 13],
    "Green": [0, 59, 60, 61, 62, 63, 64]
}

# @brief    constructs block list
# This is a new block list with up to date info
def construct_block_list_2(data_path: str) -> dict[int,"Block"]:
    block_df = pandas.read_excel(data_path, sheet_name=0)
    crossing_df = pandas.read_excel(data_path, "crossings")
    light_df = pandas.read_excel(data_path, "lights")
    switch_df = pandas.read_excel(data_path, "switches")
    station_df = pandas.read_excel(data_path, "stations")

    crossing_list = crossing_df['Crossing ID'].tolist()
    light_list = light_df['Light ID'].tolist()
    switch_dict = {}
    for index, row in switch_df.iterrows():
        switch = row.tolist()[2:]
        if switch[0] != switch[3]:
            switch[1] = switch[0]
            switch[0] = switch[3]
        switch_dict[row['SwitchID']] = switch
    
    station_dict = {}
    for index, row in station_df.iterrows():
        station_dict[row['StationID']] = row['Station Name']


    light_ids = light_df.loc[:, "Light ID"].values
    blocks = {}
    for index, row in block_df.iterrows():
        line = row['Line']
        id = row['Block Number']
        speed_limit = row['Speed Limit (Km/Hr)'] / 3.6
        length = row['Block Length (m)']
        station = row['Station List']
        section = str(row['Section']) if type(row['Section']) == str else ""
        is_underground = row['Underground']
        switch_id = row['Switch List']
        switch = None
        infrastructure = ""
        light = row['Light List']

        if switch_id in switch_dict:
            switch = Switch(
                primary=switch_dict[switch_id][1],
                secondary=switch_dict[switch_id][2]
            )
            infrastructure += f"Switch({id}-{switch.primary}, {id}-{switch.secondary}); "
        if station == station:  #checks if station != NaN
            station = station_df.loc[station, 'Station Name']
            if id != 0:
                infrastructure += "Station: "
            infrastructure += f"{station}; "
        else:
            station = None
        
        if is_underground == 1:
            infrastructure += "Underground; "
        
        if type(light) != float and light in light_list:
            infrastructure += "Signal; "

        if len(infrastructure) > 0:
            infrastructure = infrastructure[:len(infrastructure)-2]


        block = Block(
            id=id,
            line=line,
            section=section,
            speed_limit = speed_limit,
            infrastructure = infrastructure,
            station=station,
            occupied=False,
            maintenance=False,
            switch=switch,
            authority=0,
            suggested_speed=0,
            length=length
        )
        blocks[id] = block
    return blocks

def construct_block_list(df: pandas.DataFrame, line:str) -> dict[int,"Block"]:
    blocks = {}
    for index,row in df.iterrows():
        if lines[line].find(str(row.iloc[1])) == -1:
            continue
        id = int(row.iloc[2])
        speed_limit = float(int(row.iloc[5])) / 3.6
        

        block = Block(
            id=id,
            line=row.iloc[0],
            section=row.iloc[1],
            speed_limit = speed_limit,
            infrastructure = row.iloc[6],
            station=None,
            occupied=False,
            maintenance=False,
            switch=None,
            authority=0,
            suggested_speed=0,
            length=float(row.iloc[3])
        )
        if row.iloc[0]=="Red":
            if id in red_switches.keys():
                block.switch = Switch(
                    primary=red_switches[id][0],
                    secondary=red_switches[id][1],
                )
            if id in red_stations.keys():
                block.station = red_stations[id]
        else:
            if id in green_switches.keys():
                block.switch = Switch(
                    primary=green_switches[id][0],
                    secondary=green_switches[id][1],
                )
            if id in green_stations.keys():
                block.station = green_stations[id]
        blocks[id] = block
    return blocks

def construct_edge_graph(adj:list) -> dict[int, list[int]]:
    graph = {}
    for i, neighbors in enumerate(adj):
        graph[i] = [ii for ii, n in enumerate(neighbors) if n == 1]
    #print(graph)
    return graph