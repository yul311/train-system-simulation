import dataclasses
import numpy as np
import os

red_line_adj = np.loadtxt(os.path.join(os.getcwd(),"Other","red_adj.txt")).tolist()
green_line_adj = np.loadtxt(os.path.join(os.getcwd(),"Other","green_adj.txt")).tolist()

# primary role of this obj is to get train positions from changes in occupancy
# one instance for each node
@dataclasses.dataclass(frozen=False)
class OccupancyLogicController:
    
    blocks: set[int]
    entry_blocks: set[int]
    exit_blocks: set[int]
    adj: list[list[int]]
    train_paths: list[list[int]]
    trains_pos: list[int]       # each element is an index of path
    
    def get_adjacencies(self, block: int) -> list[int]:
        adj_list = []
        for i,v in enumerate(self.adj[block-1]):
            if not v: continue
            if i+1 in self.blocks:
                adj_list.append(i+1)
            else:
                adj_list.append(-(i+1))
        return adj_list
            
    def occupy(self, block: int) -> bool:
        if block not in blocks:     # this (theoretically) means a train exited the node zone
            for train,pos_index in enumerate(self.trains_pos):
                pos = self.train_paths[train][pos_index]
                if self.train_paths[train][pos_index+1]==block:
                    self.exit(train)
                    return True
            raise Exception(f"Control shouldnt reach here. block {block} may be invalid")
        for train,pos_index in enumerate(self.trains_pos):
            pos = self.train_paths[train][pos_index]
            if self.train_paths[train][pos_index+1]==block:
                self.trains_pos[train] += 1
                return False
        raise Exception(f"couldn't find any train whose next block is {block}")
            
    def enter(self, train_path: list[int]):
        for i,b in enumerate(train_path):
            if b in self.entry_blocks:
                if train_path[i+1] not in self.blocks:
                    continue
                self.train_paths.append(train_path)
                self.trains_pos.append(i)
                return
        raise Exception(f"couldn't find valid entry block")
    
    def exit(self, train_index: int):
        self.train_paths.pop(train_index)
        self.trains_pos.pop(train_index)
        
    def get_position(self, train_index) -> int:
        return self.train_paths[train_index][self.trains_pos[train_index]]
    
    def get_positions(self) -> list[int]:
        pos = []
        for i in range(len(self.train_paths)):
            pos.append(self.get_position(i))
        return pos
        
    
# ================================================================================================================================
# component testbench
# ================================================================================================================================
    
    
blocks = {b+1 for b in range(23,45)}   # wayside node 2
blocks.union(b+1 for b in range(66,76))
entries = {24,45}
exits = {24,45}

class OccupancyLogicControllerTB:
    
    def __init__(self):
        self.run_tests()
        
    def run_tests(self):
        import inspect
        for name,method in inspect.getmembers(self, inspect.ismethod):
            if name[:5]=="test_":
                try:
                    method()
                except AssertionError as failure:
                    print(f"\033[1;31mFailed {name}: \033[0m\n{failure}")
                except Exception as err:
                    print(f"\033[1;31mInternal error in {name}: \033[0m\n{err}")
                else:
                    print(f"\033[1;32mPassed {name}\033[0m")
                    
    # tests
    
    def test_1_train_entry_1(self):
        paths = [[b+1 for b in range(0,50)]]
        
        correct = [24]
        
        mod = OccupancyLogicController(blocks,entries,exits,red_line_adj,[],[])
        mod.enter(paths[0])
        response = mod.get_positions()
        
        assert response==correct, f"incorrect train positions: {response} (response) is not {correct} (correct)"
    
    def test_1_train_entry_2(self):
        paths = [[b+1 for b in range(50,0,-1)]]
        
        correct = [45]
        
        mod = OccupancyLogicController(blocks,entries,exits,red_line_adj,[],[])
        mod.enter(paths[0])
        response = mod.get_positions()
        
        assert response==correct, f"incorrect train positions: {response} (response) is not {correct} (correct)"
    
    def test_2_train_entry_1(self):
        paths = [[b+1 for b in range(0,50)],
                 [b+1 for b in range(50,0,-1)]]
        
        correct = [24,45]
        
        mod = OccupancyLogicController(blocks,entries,exits,red_line_adj,[],[])
        mod.enter(paths[0])
        mod.enter(paths[1])
        response = mod.get_positions()
        
        assert response==correct, f"incorrect train positions: {response} (response) is not {correct} (correct)"
    
    def test_2_train_entry_2(self):
        paths = [[b+1 for b in range(0,50)],
                 [b+1 for b in range(50,0,-1)]]
        
        correct = [45,24]
        
        mod = OccupancyLogicController(blocks,entries,exits,red_line_adj,[],[])
        mod.enter(paths[1])
        mod.enter(paths[0])
        response = mod.get_positions()
        
        assert response==correct, f"incorrect train positions: {response} (response) is not {correct} (correct)"
        
    def test_1_train_advance_by_1(self):
        paths = [[b+1 for b in range(0,50)]]
        
        correct = [25]
        
        mod = OccupancyLogicController(blocks,entries,exits,red_line_adj,[],[])
        mod.enter(paths[0])
        mod.occupy(25)
        response = mod.get_positions()
        
        assert response==correct, f"incorrect train positions: {response} (response) is not {correct} (correct)"
        
    def test_1_train_advance_by_1_failure(self):
        paths = [[b+1 for b in range(0,50)]]
        
        correct = "couldn't find any train whose next block is 26"
        response = ""
        try:
            mod = OccupancyLogicController(blocks,entries,exits,red_line_adj,[],[])
            mod.enter(paths[0])
            mod.occupy(26)                      # this should raise exception
            response = mod.get_positions()
        except Exception as err:
            response = str(err)
        
        assert response==correct, f"incorrect train positions: {response} (response) is not {correct} (correct)"
        
    def test_1_train_advance_by_many(self):
        paths = [[b+1 for b in range(0,50)]]
        
        correct = [40]
        
        mod = OccupancyLogicController(blocks,entries,exits,red_line_adj,[],[])
        mod.enter(paths[0])
        for block in range(25,41):
            mod.occupy(block)
        response = mod.get_positions()
        
        assert response==correct, f"incorrect train positions: {response} (response) is not {correct} (correct)"
        
    def test_1_train_enter_and_exit(self):
        paths = [[b+1 for b in range(0,50)]]
        
        correct = []
        
        mod = OccupancyLogicController(blocks,entries,exits,red_line_adj,[],[])
        mod.enter(paths[0])
        for block in range(25,47):
            mod.occupy(block)
        response = mod.get_positions()
        
        assert response==correct, f"incorrect train positions: {response} (response) is not {correct} (correct)"
    
if __name__=="__main__":
    OccupancyLogicControllerTB()