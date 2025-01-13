import dataclasses

# TODO work out purely boolean implementation
# mut switch logic class controls one switch
# each instance only handles 1 or 2 trains
@dataclasses.dataclass(frozen=False)
class SwitchLogicController:
    
    switch: tuple[int]                # switch tuple is (owner, primary, secondary)
    train_paths: list[list[int]]        # full train path
    
    @property
    def owner(self):
        return self.switch[0]
    
    @property
    def primary(self):
        return self.switch[1]
    
    @property
    def secondary(self):
        return self.switch[2]
    
    # proximity of train to switch's OWNER block
    def proximity(self, train_index: int, train_position: int) -> int:
        prox=0
        for b in self.train_paths[train_index][train_position:]:
            if b==self.owner:
                return prox
            prox += 1
        raise ValueError(f"train at index {train_index} does not cross this switch after position {train_position}")
    
    # switch state for train
    def next_state(self, train_index: int, train_position: int) -> int:
        for i,b in enumerate(self.train_paths[train_index][train_position:]):
            i+=train_position
            if b==self.owner:
                if self.train_paths[train_index][i-1] == self.primary or self.train_paths[train_index][i+1] == self.primary:
                    return 1
                elif self.train_paths[train_index][i-1] == self.secondary or self.train_paths[train_index][i+1] == self.secondary:
                    return 2
                else:
                    raise ValueError("Invalid Path")
        raise ValueError(f"train at index {train_index} does not cross this switch after position {train_position}")
               
    # train indices in order of proximity to switch's OWNER block
    def sorted_proximities(self, position_indices: list[int]) -> list[int]:
        proximities = []
        for train_index,train_position in enumerate(position_indices):
            p = self.proximity(train_index,train_position)
            if p==-1: continue
            proximities.append(p)
        return [i for i,p in sorted(enumerate(proximities), key = lambda entry: entry[1])]
            
    # stochastic queue for switch states
    def state_queue(self, position_indices: list[int]) -> list[int]:
        train_order = self.sorted_proximities(position_indices)
        if len(train_order)==2:
            if self.train_side(train_order[0],position_indices[0])!=0 and self.train_side(train_order[1],position_indices[1])==0:
                train_order.reverse()
        return [self.next_state(train,position_indices[train]) for train in train_order]
            
    # which side of the switch a train is approaching from
    #   0 -> owner side
    #   1 -> primary side
    #   2 -> secondary side
    def train_side(self, train_index: int, train_position: int) -> int:
        for b in self.train_paths[train_index][train_position:]:
            if b==self.owner:
                return 0
            elif b==self.primary:
                return 1
            elif b==self.secondary:
                return 2
        raise ValueError(f"train at index {train_index} does not cross this switch after position {train_position}")
        
    
# ================================================================================================================================
# component testbench
# ================================================================================================================================

class SwitchLogicControllerTB:
    
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
    
    # blue line cases
    def test_1_train_state_queue(self):
        switch = (5,6,11)
        paths = [[1,2,3,4,5,6,7,8,9,10]]
        pos = [0]
        correct = [1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_parallel_trains_owner_1(self):
        switch = (5,6,11)
        paths = [[1,2,3,4,5,6,7,8,9,10],
                 [1,2,3,4,5,11,12,13,14,15]]
        pos = [3,0]
        correct = [1,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_parallel_trains_owner_2(self):
        switch = (5,6,11)
        paths = [[1,2,3,4,5,6,7,8,9,10],
                 [1,2,3,4,5,11,12,13,14,15]]
        pos = [0,3]
        correct = [2,1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_parallel_trains_primary_1(self):
        switch = (5,6,11)
        paths = [[10,9,8,7,6,5,4,3,2,1],
                 [10,9,8,7,6,5,4,3,2,1]]
        pos = [3,0]
        correct = [1,1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_parallel_trains_primary_2(self):
        switch = (5,6,11)
        paths = [[10,9,8,7,6,5,4,3,2,1],
                 [10,9,8,7,6,5,4,3,2,1]]
        pos = [3,0]
        correct = [1,1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_parallel_trains_secondary_1(self):
        switch = (5,6,11)
        paths = [[15,14,13,12,11,5,4,3,2,1],
                 [1,2,3,4,5,11,12,13,14,15]]
        pos = [3,0]
        correct = [2,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_parallel_trains_secondary_2(self):
        switch = (5,6,11)
        paths = [[15,14,13,12,11,5,4,3,2,1],
                 [1,2,3,4,5,11,12,13,14,15]]
        pos = [0,3]
        correct = [2,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_2_trains_state_queue_primary(self):
        switch = (5,6,11)
        paths = [[1,2,3,4,5,11,12,13,14,15],
                 [10,9,8,7,6,5,4,3,2,1]]
        pos = [0,0]
        correct = [2,1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_2_trains_state_queue_primary_inverted(self):
        switch = (5,6,11)
        paths = [[1,2,3,4,5,11,12,13,14,15],
                 [10,9,8,7,6,5,4,3,2,1]]
        pos = [0,3]
        correct = [2,1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_2_trains_state_queue_secondary(self):
        switch = (5,6,11)
        paths = [[1,2,3,4,5,6,7,8,9,10],
                 [15,14,13,12,11,5,4,3,2,1]]
        pos = [0,0]
        correct = [1,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_2_trains_state_queue_secondary_inverted(self):
        switch = (5,6,11)
        paths = [[1,2,3,4,5,6,7,8,9,10],
                 [15,14,13,12,11,5,4,3,2,1]]
        pos = [0,3]
        correct = [1,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_2_trains_primary_secondary_1(self):
        switch = (5,6,11)
        paths = [[10,9,8,7,6,5,4,3,2,1],
                 [15,14,13,12,11,5,4,3,2,1]]
        pos = [4,3]
        correct = [1,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_2_trains_primary_secondary_2(self):
        switch = (5,6,11)
        paths = [[10,9,8,7,6,5,4,3,2,1],
                 [15,14,13,12,11,5,4,3,2,1]]
        pos = [3,4]
        correct = [2,1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    def test_2_trains_primary_secondary_3(self):
        switch = (5,6,11)
        paths = [[10,9,8,7,6,5,4,3,2,1],
                 [15,14,13,12,11,5,4,3,2,1]]
        pos = [0,0]
        correct = [1,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
        
    # loop cases (redline sections JKLMN)
    
    def test_1_train_loop_first_pass_cw(self):
        switch = (52,53,66)
        paths = [[49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,52,51,50,49]]
        pos = [0]
        correct = [1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
    
    def test_1_train_loop_second_pass_cw(self):
        switch = (52,53,66)
        paths = [[49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,52,51,50,49]]
        pos = [4]
        correct = [2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
    
    def test_1_train_loop_first_pass_ccw(self):
        switch = (52,53,66)
        paths = [[49,50,51,52,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49]]
        pos = [0]
        correct = [2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
    
    def test_1_train_loop_second_pass_ccw(self):
        switch = (52,53,66)
        paths = [[49,50,51,52,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49]]
        pos = [4]
        correct = [1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
    
    def test_2_train_loop_first_pass_cw(self):
        switch = (52,53,66)
        paths = [[49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,52,51,50,49],
                 [49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,52,51,50,49]]
        pos = [0,2]
        correct = [1,1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
    
    def test_2_train_loop_second_pass_cw(self):
        switch = (52,53,66)
        paths = [[49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,52,51,50,49],
                 [49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,52,51,50,49]]
        pos = [2,4]
        correct = [1,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
    
    def test_2_train_loop_first_pass_cw(self):
        switch = (52,53,66)
        paths = [[49,50,51,52,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49],
                 [49,50,51,52,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49]]
        pos = [0,2]
        correct = [2,2]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        assert response==correct, f"incorrect state queue: {response} (response) is not {correct} (correct)"
    
    def test_2_train_loop_second_pass_cw(self):
        switch = (52,53,66)
        paths = [[49,50,51,52,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49],
                 [49,50,51,52,66,65,64,63,62,61,60,59,58,57,56,55,54,53,52,51,50,49]]
        pos = [2,4]
        correct = [2,1]
        
        mod = SwitchLogicController(switch,paths)
        response = mod.state_queue(pos)
        
        
if __name__=="__main__": SwitchLogicControllerTB()