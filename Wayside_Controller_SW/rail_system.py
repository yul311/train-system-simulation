

import pandas
import dataclasses
import os
import numpy as np

# wayside node placement
red_nodes = {
    1: "ABCDEFGHOPQRST",
    2: "HOPQRSTIJKLMN"
}
green_nodes = {
    3: "ABCDEFGXYZ",
    4: "HIJKLTUVW",
    5: "MNOPQRS"
}

all_nodes = {}
all_nodes.update(red_nodes)
all_nodes.update(green_nodes)

nodes = {
    1,
    2,
    3,  # add 151
    4,
    5,  # add 152
}

red_adjmat = np.loadtxt(os.path.join(os.getcwd(),"Other","red_adj.txt"))
green_adjmat = np.loadtxt(os.path.join(os.getcwd(),"Other","green_adj.txt"))

# block 0 is the yard
red_switches = {
    9: (10,0),
    15: (16,1),
    27: (28,77),
    32: (33,72),
    38: (39,71),
    43: (44,67),
    52: (53,56),
}
green_switches = {
    12: (13,1),
    29: (30,150),
    57: (58, 0),
    63: (62, 0),
    77: (76,101),
    85: (86,100),
}
    
red_signals = {
    0,
    1,
    7,
    9,
    10,
    15,
    16,
    21,
    25,
    27,
    28,
    32,
    33,
    35,
    38,
    39,
    43,
    44,
    48,
    52,
    53,
    60,
    66,
    67,
    71,
    72,
    77
}
green_signals = {
    0,
    1,
    2,
    9,
    12,
    13,
    16,
    22,
    29,
    30,
    31,
    39,
    48,
    57,
    58,
    62,
    63,
    65,
    73,
    76,
    77,
    85,#a
    86,
    88,
    96,
    100,
    101,
    105,
    114,
    123,
    132,
    141,
    150
}

red_crossings = {
    47
}
green_crossings = {
    19
}

# @brief    constructs block list
def construct_block_list(df: pandas.DataFrame, node: int) -> dict[int,"Block"]:
    """@brief constructs a block list given a dataframe (from archive) and wayside controller node id"""
    
    blocks = {}    
        
    if node==1:
        blocks[0] = Block(0,"red","YARD",75,False,False,50,50,False,None,Signal(1),None)
    elif node==4:
        blocks[0] = Block(0,"green","YARD",75,False,False,50,50,False,None,Signal(1),None)
        
    for index,row in df.iterrows():
        if all_nodes[node].find(str(row[1]))==-1: continue
        id = int(row[2])

        block = Block(
            id=id,
            line=row[0],
            section=row[1],
            len=row[3],
            occupied=False,
            maintenance=False,
            ctc_authority=row[3],
            ws_authority=row[3],
            use_ws_authority=False,
            switch=None,
            signal=None,
            crossing=None
        )
        if row[0]=="Red":
            if id in red_switches.keys():
                block.switch = Switch(
                    primary=red_switches[id][0],
                    secondary=red_switches[id][1],
                    state=1
                )
            if id in red_signals:
                block.signal = Signal(
                    state=1,
                )
            if id in red_crossings:
                block.crossing = Crossing(
                    state=1
                )
        else:
            if id in green_switches.keys():
                block.switch = Switch(
                    primary=green_switches[id][0],
                    secondary=green_switches[id][1],
                    state=1
                )
            if id in green_signals:
                block.signal = Signal(
                    state=1,
                )
            if id in green_crossings:
                block.crossing = Crossing(
                    state=1
                )

        blocks[id] = block
        
    return blocks
            
            
@dataclasses.dataclass(frozen=False,unsafe_hash=True)
class Block:
    """Responsible for storing all block related data for a single block"""
    # static
    id: int
    """CONST id number for block"""
    line: str
    """CONST indicates which rail line the block is a part of"""
    section: str
    """CONST indicates which section letter the block is a part of"""
    len: int
    """CONST stores the length of the block"""
    # dyn
    occupied: bool
    """stores whether the block is occupied"""
    maintenance: bool
    """stores whether the block is under maintenance"""
    ctc_authority: int
    """stores the authority assigned by CTC"""
    ws_authority: int
    """stores the authority assigned by wayside controller"""
    use_ws_authority: bool
    """stores whether to use wayside authority or ctc authority"""
    switch: "Switch"
    """stores the blocks switch. assigned to None if block has no switch"""
    signal: "Signal"
    """stores the blocks signal. assigned to None if block has no signal"""
    crossing: "Crossing"
    """stores the blocks crossing. assigned to None if block has no crossing"""

@dataclasses.dataclass(frozen=False)
class Switch:
    """Responsible for storing the connections and current state of a switch"""
    
    # static
    primary: int
    """CONST stores switch's primary (default) position"""
    secondary: int
    """CONST stores switch's secondary position"""
    # dyn
    state: int
    """stores the switch's current state (1 for primary, 2 for secondary)"""

@dataclasses.dataclass(frozen=False)
class Signal:
    """Responsible for storing the state of a traffic signal"""

    # dyn
    state: int
    """stores the signal's current state (1 for green, 2 for red)"""

@dataclasses.dataclass(frozen=False)
class Crossing:
    """Responsible for storing the state of a railroad crossing"""
    
    # dyn
    state: int # 1: open, 2: closed
    """stores the crossing's current state (1 for opened, 2 for closed)"""


    