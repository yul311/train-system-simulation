
import dataclasses,os,pandas,traceback
import statistics
import warnings

try:
    from plc_interpreter import PLCInterpreter
    from rail_system import Block, construct_block_list
except:
    from Wayside_Controller_SW.plc_interpreter import PLCInterpreter
    from Wayside_Controller_SW.rail_system import Block
    
DATA_PATH = os.path.join(os.getcwd(),"Other","data","Track Layout & Vehicle Data vF2.xlsx")

node_switches = {
    1: {9,15,27},
    2: {32,38,43,52},
    3: {12,29},
    4: {57,63},
    5: {77,85}
}
node_signals = {
    1: {0,1,7,9,10,15,16,21,25,27,28,77},
    2: {32,33,35,38,39,43,44,48,52,53,60,66,67,71,72},
    3: {1,2,9,12,13,16,22,29,30,31,150},
    4: {0,39,48,57,58,62,63,65,73,105,114,123,132,141},
    5: {76,77,85,86,88,96,100,101}
}
node_crossings = {
    1: {},
    2: {47},
    3: {19},
    4: {},
    5: {}
}

@dataclasses.dataclass(frozen=False)
class RailSystemController:
    """Responsible for encapsulating all PLC functionality"""
    
    plc_paths: dict[int:os.PathLike]
    """path to PLC program file"""
    plc_interpreters: dict[int:PLCInterpreter]
    """internally stored instance of PLCInterpreter"""
    node: int
    """indicates which wayside controller this object is a part of"""
    yard_return_mode: bool
    """mode for wayside controller. if true and node is either 1 or 4"""
    
    def __init__(self,node):
        self.node = node
        self.plc_paths = {}
        self.plc_interpreters = {1:PLCInterpreter(node),2:PLCInterpreter(node),3:PLCInterpreter(node)}
        self.yard_return_mode = False

    def load_program(self, path: os.PathLike, program_number: int = None) -> None:
        """@brief loads PLC code from provided file path"""
        if not program_number:
            self.plc_paths[1] = path
            self.plc_paths[2] = path
            self.plc_paths[3] = path
            for p in range(1,4):
                with open(self.plc_paths[p]) as program:
                    fstr = program.read()
                    self.plc_interpreters[p].tokenize(fstr)
        else:
            self.plc_paths[program_number] = path
            with open(self.plc_paths[program_number]) as program:
                fstr = program.read()
                self.plc_interpreters[program_number].tokenize(fstr)
            

    def set_yard_return_mode(self, mode: bool):
        """sets yard_return_mode attribute"""

        if self.node in {1,4}:
            self.yard_return_mode = mode
        else:
            self.yard_return_mode = False
            warnings.warn("Wayside controller ")
        
    def run(self, blocks: dict[int:Block]) -> (dict[int:int],dict[int:int],dict[int:int]):
        """@brief runs the PLC program
        @returns new states for all switches, signals, and crossings controller by this wayside controller"""
        switch_states = {}
        occupancies = {}
        
        for block in blocks.values():
            if block.switch:
                switch_states[block.id] = block.switch.state
            occupancies[block.id] = block.occupied
            
        # NOTE this prevents overlapping node errors
        if self.node==1:
            switch_states.pop(32)
            switch_states.pop(38)
            switch_states.pop(43)
        elif self.node==2:
            switch_states.pop(27)
            
        switch_trials = {}
        signal_trials = {}
        crossing_trials = {}
        
        for trial,plc_interpreter in self.plc_interpreters.items():
            
            plc_interpreter.set_inputs(switch_states,occupancies)
            
            switches_iter = {}
            signals_iter = {}
            crossings_iter = {}
            
            for switch in switch_states.keys():
                if self.node==4 and switch==57 and self.yard_return_mode:
                    switches_iter[switch] = 2
                elif self.node==1 and switch==9 and self.yard_return_mode:
                    switches_iter[switch] = 2
                elif self.node==1 and switch==15 and self.yard_return_mode:
                    switches_iter[switch] = 2
                else:
                    switches_iter[switch] = plc_interpreter.get_switch(switch)
                    
            plc_interpreter.set_inputs(switches_iter,occupancies)   # add new switches before calculating signals
            
            for signal in node_signals[self.node]:
                signals_iter[signal] = plc_interpreter.get_signal(signal)
                
            for crossing in node_crossings[self.node]:
                crossings_iter[crossing] = plc_interpreter.get_crossing(crossing)
                
            switch_trials[trial] = switches_iter
            signal_trials[trial] = signals_iter
            crossing_trials[trial] = crossings_iter
            
        switches = {}
        signals = {}
        crossings = {}
        
        for switch in switch_trials[1].keys():
            rslt_array = [switch_trials[t][switch] for t in range(1,4)]
            switches[switch] = statistics.mode(rslt_array)
            
        for signal in signal_trials[1].keys():
            rslt_array = [signal_trials[t][signal] for t in range(1,4)]
            signals[signal] = statistics.mode(rslt_array)
            
        for crossing in crossing_trials[1].keys():
            rslt_array = [crossing_trials[t][crossing] for t in range(1,4)]
            crossings[crossing] = statistics.mode(rslt_array)
            
        return switches,signals,crossings

    
# ================================================================================================================================
# component testbench
# ================================================================================================================================
green_data = pandas.read_excel(DATA_PATH, sheet_name=3)

code_path_3 = os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_3.plc")
code_path_4 = os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_4.plc")

class RailSystemControllerTB:
    
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
                    print(f"\033[1;31mInternal error in {name}: \033[0m\n{traceback.print_exc()}")
                else:
                    print(f"\033[1;32mPassed {name}\033[0m")
    
    def test_n4_dispatch(self):
        
        mod = RailSystemController(4)
        mod.load_program(code_path_4)
        
        blocks = construct_block_list(green_data,4)
        blocks[0] = Block(0,"green","$",False,False,100,None,None,None)
        
        blocks[0].occupied = True
        
        switches, signals, crossings = mod.run(blocks)
        
        correct_switches = {57: 2, 63: 2}
        correct_signals = {0: 1, 65: 1, 132: 1, 39: 1, 73: 1, 105: 1, 141: 1, 48: 1, 114: 1, 57: 1, 123: 1, 62: 2}
        correct_crossings = {}
            
        assert switches==correct_switches, f"for switches,\ncorrect:\t{correct_switches}\nresponse:\t{switches}"
        assert signals==correct_signals, f"for signals,\ncorrect:\t{correct_signals}\nresponse:\t{signals}"
        assert crossings==correct_crossings, f"for crossings,\ncorrect:\t{correct_crossings}\nresponse:\t{crossings}"
    
    def test_n4_dispatch_obstructed(self):
        
        # FIXME signals on b0 & b62 dont change
        
        mod = RailSystemController(4)
        mod.load_program(code_path_4)
        
        blocks = construct_block_list(green_data,4)
        blocks[0] = Block(0,"green","$",False,False,100,None,None,None)
        
        blocks[0].occupied = True
        blocks[60].occupied = True
        
        switches, signals, crossings = mod.run(blocks)
        
        correct_switches = {57: 2, 63: 1}
        correct_signals = {0: 2, 65: 1, 132: 1, 39: 1, 73: 1, 105: 1, 141: 1, 48: 1, 114: 1, 57: 1, 123: 1, 62: 1}
        correct_crossings = {}
            
        assert switches==correct_switches, f"for switches,\ncorrect:\t{correct_switches}\nresponse:\t{switches}"
        assert signals==correct_signals, f"for signals,\ncorrect:\t{correct_signals}\nresponse:\t{signals}"
        assert crossings==correct_crossings, f"for crossings,\ncorrect:\t{correct_crossings}\nresponse:\t{crossings}"
    
    def test_n3_DEF_occupied(self):
        
        mod = RailSystemController(3)
        mod.load_program(code_path_3)
        
        blocks = construct_block_list(green_data,3)
        
        blocks[24].occupied = True
        
        switches, signals, crossings = mod.run(blocks)
        
        correct_switches = {13: 1, 29: 1}
        correct_signals = {16: 1, 1: 2, 2: 1, 22: 1, 150: 1, 9: 1, 31: 1}
        correct_crossings = {}
            
        assert switches==correct_switches, f"for switches,\ncorrect:\t{correct_switches}\nresponse:\t{switches}"
        assert signals==correct_signals, f"for signals,\ncorrect:\t{correct_signals}\nresponse:\t{signals}"
        assert crossings==correct_crossings, f"for crossings,\ncorrect:\t{correct_crossings}\nresponse:\t{crossings}"
        
if __name__=="__main__":
    
    RailSystemControllerTB()