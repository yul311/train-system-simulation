import dataclasses

from rail_system import *
from train import Train
from rail_system_controller import RailSystemController

DATA_PATH = os.path.join(os.getcwd(),"Other","data","Track Layout & Vehicle Data vF2.xlsx")


@dataclasses.dataclass(frozen=False)
class WaysideController:
    
    node_id: int
    line: str
    blocks: dict[int:Block]
    entries: set[int]
    exits: set[int]
    
    trains: dict[int:Train]
    
    controller: RailSystemController
    
    def __init__(self, node_id: int, blocks: dict[int:Block], entries: set[int], exits: set[int]):
        
        self.node_id = node_id
        if node_id in [1,2,3]:
            self.line = "Red"
        else:
            self.line = "Green"
        self.blocks = blocks
        self.entries = entries
        self.exits = exits
        self.controller = RailSystemController(blocks,entries,exits)
        
        self.trains = {}
        
    # @brief    adds a train to the node region
    def add_train(self, id: int, path: list[int], pos: int):
        
        if path[pos] not in self.entries:
            raise ValueError(f"Train with id {id} is not at valid entry point\ntrain {id} is currently at {path[pos]} and must be at one of {self.entries}")
        self.trains[id] = Train(id,path,pos)
        self.controller.add_train(self.trains[id])
        
    # @brief    removes a train from the node region
    def remove_train(self, id: int):
        
        if id in self.trains.keys():
            raise ValueError(f"Train with id {id} not found in wayside node {self.node_id}")
        elif self.trains[id].path[self.trains[id].pos] not in self.exits:
            raise ValueError(f"Train with id {id} is not at a valid exit point\ntrain {id} is currently at {self.trains[id].path[self.trains[id].pos]} and must be at one of {self.exits}")
        self.trains.pop(id)
        
    # @brief    set internally stored train position by path index
    def set_train_pos(self, id: int, pos: int):
        
        if id in self.trains.keys():
            raise ValueError(f"Train with id {id} not found in wayside node {self.node_id}")
        self.trains[id].pos = pos
        
    # @brief    sets internally stored switch state
    def set_switch(self, block_id: int, state: int):
        
        if not self.blocks[block_id].switch:
            raise ValueError(f"Block {block_id} doesn't have a switch")
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid switch state")
        self.blocks[block_id].switch.state = state
    
    # @brief    sets internally stored signal state
    def set_signal(self, block_id: int, state: int):
        
        if not self.blocks[block_id].signal:
            raise ValueError(f"Block {block_id} doesn't have a signal")
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid signal state")
        self.blocks[block_id].signal.state_1 = state
        self.blocks[block_id].signal.state_2 = state
    
    # @brief    sets internally stored crossing state
    def set_crossing(self, block_id: int, state: int):
        
        if not self.blocks[block_id].crossing:
            raise ValueError(f"Block {block_id} doesn't have a crossing")
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid crossing state")
        self.blocks[block_id].crossing.state = state
        
    # @brief    sets ONE internally stored occupancy
    def set_occupancy(self, block_id: int, occupied: bool):
        
        if block_id not in self.blocks.keys():
            raise ValueError(f"Block {block_id} is not in wayside node {self.node_id}")
        self.blocks[block_id].occupied = occupied      
    
    # @brief    sets internally stored maintenance state
    def set_maintenance(self, block_id: int, under_maintenance: bool):
        
        if block_id not in self.blocks.keys():
            raise ValueError(f"Block {block_id} is not in wayside node {self.node_id}")
        self.blocks[self.node_id][block_id].maintenance = under_maintenance
        
        
red_data = pandas.read_excel(DATA_PATH, sheet_name=2)
green_data = pandas.read_excel(DATA_PATH, sheet_name=3)
blue_data = pandas.read_excel(DATA_PATH, sheet_name=1)
wayside_nodes = {
    1: WaysideController(1,construct_block_list(red_data,1), {9,23}, {9,23}),
    2: WaysideController(2,construct_block_list(red_data,2), {24,45}, {24,45}),
    3: WaysideController(3,construct_block_list(red_data,3), {46}, {46}),
    4: WaysideController(4,construct_block_list(green_data,4), {20}, {20}),
    5: WaysideController(5,construct_block_list(green_data,5), {21,57}, {21,122}),
    6: WaysideController(6,construct_block_list(green_data,6), {58,63,105}, {73,121}),
    7: WaysideController(7,construct_block_list(green_data,7), {74}, {104}),
}

if __name__=="__main__":
    
    wayside_nodes[1].add_train(1, [23,22,21,20,19,18,17,16,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], 0)
    print(wayside_nodes[1].controller.trains)