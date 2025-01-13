

import dataclasses
import sys
import traceback
import warnings
from statistics import mode


try:
    from Wayside_Controller_SW.rail_system import *
    from Wayside_Controller_SW.train import Train
    from Wayside_Controller_SW.rail_system_controller import RailSystemController
    from Wayside_Controller_SW.authority_logic import AuthorityLogicController
except Exception as e:
    print(e)
    from rail_system import *
    from train import Train
    from rail_system_controller import RailSystemController
    from authority_logic import AuthorityLogicController

DATA_PATH = os.path.join(os.getcwd(),"Other","data","Track Layout & Vehicle Data vF2.xlsx")


@dataclasses.dataclass(frozen=False)
class WaysideController:
    """Top Level backend class for wayside controller. Responsible for all vital and non-vital functions"""
    
    ui_link: any
    """mutable reference to instance of wayside controller API for frontend"""

    ctc_link: any
    """mutable reference to instance of WaysideCTCAPI"""
    track_link: any
    """mutable reference to instance of WaysideTrackAPI"""
    
    node_id: int
    """identification number indicated which wayside controller this object is"""
    line: str
    """string identifying which rail line this wayside controller is placed on"""
    blocks: dict[int:Block]
    """dictionary containing all block related information for this wayside controller.\n
    also used to indicate which blocks are under this wayside controller's jurisdiction"""
    entries: set[int]
    """deprecated"""
    exits: set[int]
    """deprecated"""
    
    trains: dict[int:Train]
    """stores all train related information (deprecated?)"""
    train_id: int
    """deprecated?"""
    
    controller: RailSystemController
    """owned instance of RailSystemController for PLC"""
    authority_controller: AuthorityLogicController
    """owned isntance of AuthorityLogicController"""
    manual_mode: bool
    """whether the controller is in manual mode"""
    
    def __init__(self, node_id: int, blocks: dict[int:Block], entries: set[int], exits: set[int]):
        
        self.ui_link = None

        self.ctc_link = None
        self.track_link = None
        
        self.node_id = node_id
        if node_id in [1,2]:
            self.line = "Red"
        else:
            self.line = "Green"
        self.blocks = blocks
        
        self.entries = entries
        self.exits = exits
        
        self.manual_mode = False
        
        self.controller = RailSystemController(self.node_id)
        self.authority_controller = AuthorityLogicController(self.node_id, blocks)
        
        self.trains = {}
        self.train_id = 1

    ## link apis ##
    # @brief links Wayside-to-CTC API
    def link_ctc(self, ctc_api: any):
        """@brief assigns the ctc_link attribute"""
        
        self.ctc_link = ctc_api

    # @brief links Wayside-to-Track API
    def link_track(self, track_api: any):
        """@brief assigns the track_link attribute"""
        
        self.track_link = track_api
        
    # @brief links Wayside-to-WaysideUI API
    def link_ui(self,ui_link: any):
        """@brief assigns the ui_link attribute"""
        
        self.ui_link = ui_link
        
    ## fns ##
    # @brief sets/unsets manual mode
    def set_manual_mode(self,man:bool):
        """@brief sets whether this wayside controller is in manual mode"""
        
        self.manual_mode = man
        if not man: self.run_plc_program()

    # @brief    dispatches a train
    def dispatch_train(self, auth: int, speed: int):
        """@brief adds a new train to the internal dict and sends dispatch signal to track model"""
        
        self.add_train(self.train_id, auth, speed)
        self.train_id += 1
        if self.track_link:
            self.track_link.send_dispatch_signal(self.node_id, auth,speed)
        else:
            warnings.warn("Track model not linked!")
        
    # @brief    adds a train to the node region
    def add_train(self, id: int, auth: int, speed: int):
        """@brief adds train to internal dict"""
        
        self.trains[id] = Train(id,auth,speed)
        
    # @brief    removes a train from the node region
    def remove_train(self, id: int):
        """@brief removes train from internal dict"""
        
        if id in self.trains.keys():
            raise ValueError(f"Train with id {id} not found in wayside node {self.node_id}")
        self.trains.pop(id)
        self.train_id -= 1
                
    # @brief    sets internally stored switch state
    def set_switch(self, block_id: int, state: int):
        """@brief sets the internally stored state of switch. also sends the new state\n
        to track model and to the UI. reruns authority logic with new switch values"""
        
        if not self.blocks[block_id].switch:
            raise ValueError(f"Block {block_id} doesn't have a switch")
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid switch state")
        self.blocks[block_id].switch.state = state
        if self.ui_link:
            self.ui_link.send_switch(self.line.lower(), block_id, state)
        if self.track_link:
            connected_block_id = self.blocks[block_id].switch.primary if state==1 else self.blocks[block_id].switch.secondary
            # FIXME
            if block_id==12: connected_block_id = 12 if state==1 else 1
            if block_id==15: connected_block_id = 15 if state==1 else 1
            self.track_link.send_switch_command(self.node_id,block_id,connected_block_id)
        else:
            warnings.warn("Track model not linked!")
        
        self.authority_controller.update_switch_authorities()
        self.send_new_authorities()
    
    # @brief    sets internally stored signal state
    def set_signal(self, block_id: int, state: int):
        """@brief sets the internally stored state of signal. also sends the new state\n
        to track model and to the UI. reruns authority logic with new signal values ONLY\n
        in manual mode"""
        
        if not self.blocks[block_id].signal:
            raise ValueError(f"Block {block_id} doesn't have a signal")
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid signal state")
        self.blocks[block_id].signal.state = state
        red_or_green = "green" if state==1 else "red"
        if self.ui_link:
            self.ui_link.send_signal(self.line.lower(), block_id, state)
        if self.track_link:
            self.track_link.send_signal_command(self.node_id,block_id,"Green" if state==1 else "Red")
        else:
            warnings.warn("Track model not linked!")
        
        if self.manual_mode:
            self.authority_controller.update_signal_authorities()
            self.send_new_authorities()
    
    # @brief    sets internally stored crossing state
    def set_crossing(self, block_id: int, state: int):
        """@brief sets the internally stored state of crossing. also sends the new state\n
        to track model and to the UI."""
        
        if not self.blocks[block_id].crossing:
            raise ValueError(f"Block {block_id} doesn't have a crossing")
        if state not in [1,2]:
            raise ValueError(f"'{state}' is not a valid crossing state")
        self.blocks[block_id].crossing.state = state
        open_or_closed = "open" if state==1 else "closed"
        if self.ui_link:
            self.ui_link.send_crossing(self.line.lower(), block_id, state)
        if self.track_link:
            self.track_link.send_crossing_command(self.node_id,block_id,state==1)
        else:
            warnings.warn("Track model not linked!")
        
    # @brief    sets ONE internally stored occupancy
    def set_occupancy(self, block_id: int, occupied: bool):
        """@brief sets the internally stored occupancy of a block. also sends the new occupancy\n
        to the CTC office and to the UI. reruns PLC program ONLY when NOT in manual mode. \n
        TODO reruns authority logic with new occupancies"""
        
        if block_id not in self.blocks.keys():
            raise ValueError(f"Block {block_id} is not in wayside node {self.node_id}")
        self.blocks[block_id].occupied = occupied     
        occ_or_unocc = "occupied" if occupied else "unoccupied" 
        if self.ui_link:
            self.ui_link.send_occupancy(self.line.lower(), block_id, occupied)
        if self.ctc_link:
            self.ctc_link.send_occupancies(self.node_id, block_id, occupied)
        else:
            warnings.warn("CTC office not linked!")
            
        if not self.manual_mode:
            self.run_plc_program()
    
    # @brief    sets internally stored maintenance state 
    def set_maintenance(self, block_id: int, under_maintenance: bool):
        """@brief sets whether a block is under maintenance. called by CTC Office"""
        
        if block_id not in self.blocks.keys():
            raise ValueError(f"Block {block_id} is not in wayside node {self.node_id}")
        self.blocks[block_id].maintenance = under_maintenance
        if self.ui_link:
            self.ui_link.send_maintenance(self.line.lower(), block_id, under_maintenance)
        
    # @brief sets the ctc authority of a block (to be passed to a train)
    def set_ctc_authority(self, block_id: int, auth: int):
        """@brief sets the authority of a block assigned by CTC. calls authority logic\n
        to recalculate which authority to use"""
        
        if self.node_id==3 and block_id==152: return
        self.blocks[block_id].ctc_authority = auth
        self.authority_controller.set_ctc_authority(block_id, auth)
        self.authority_controller.load_authority_to_block(block_id)
        self.send_authority(block_id)
        
    # @brief sends authority to track model
    def send_authority(self, block_id: int):
        """@brief sends the internally stored authority value for a block\n
        to the track model"""
        
        if self.blocks[block_id].use_ws_authority:
            auth = self.blocks[block_id].ws_authority  
        else:
            auth = self.blocks[block_id].ctc_authority
            
        if self.ui_link:
            self.ui_link.send_authority(self.line.lower(),block_id,auth)
            
        if self.track_link:
            self.track_link.send_authority(self.node_id,block_id,auth)
        else:
            warnings.warn("Track model not linked!")      
        
    # FIXME send, not set
    # @brief sets the suggested speed of a block (to be passed to a train)
    def set_suggested_speed(self, block_id: int, speed: int):
        """@brief sends suggested speed of block to track model"""
        
        if self.track_link:
            self.track_link.send_suggested_speed(self.node_id,block_id,speed)
        else:
            warnings.warn("Track model not linked!")
    
    # @brief loads a PLC program
    def load_plc_program(self, path: os.PathLike, program_number: int = None):
        """@brief loads a PLC program into the rail system controller.
        also immediately reruns the new PLC program"""
        
        self.controller.load_program(path,program_number)
        self.run_plc_program()
                    
    # @brief runs the PLC program using internally stored occupancies and switch states
    def run_plc_program(self):      
        """@brief runs the PLC program stored in the rail system controller. assigns the
        new switch, signal, and crossing state using their corresponding setters: this function
        also sends new states to track model"""
            
        if self.manual_mode:
            warnings.warn(f"Node {self.node_id} cannot run PLC because it is currently in manual mode")
        elif self.has_plc_program():
            switches,signals,crossings = self.controller.run(self.blocks)
            
            for block in self.blocks.values():
                if block.switch and block.id in switches.keys():
                    self.set_switch(block.id, switches[block.id])
                if block.signal and block.id in signals.keys():
                    self.set_signal(block.id, signals[block.id])
                if block.crossing and block.id in crossings.keys():
                    self.set_crossing(block.id, crossings[block.id])
        else:
            warnings.warn(f"Node {self.node_id} currently has no PLC program loaded")
            
    def set_yard_return(self,state: bool):
        """@brief sets the wayside controller to yard return mode if the wayside controller is connected to the yard"""
        
        if self.node_id not in {1,4}:
            warnings.warn(f"Wayside Controller {self.node_id} does not have a yard return mode")
        else:
            self.controller.set_yard_return_mode(state)
            self.run_plc_program()
            
    # @brief computes new authorities and sends deltas to track model
    def send_new_authorities(self):
        """@brief loads authority controller values to blocks dict. then, sends each changed
        authority value to track model. ignores unchanged authority values"""
        
        authority_deltas = self.authority_controller.load_authorities_to_blocks()
        for block_id in authority_deltas:
            self.send_authority(block_id)
        
    # @brief returns whether the controller has a PLC program loaded
    def has_plc_program(self) -> bool:
        """@brief gets whether the rail system controller has a PLC program loaded"""
        
        return bool(self.controller.plc_paths[1])
    
    def send_dwell_time(self,block_id:int):
        """@brief sends dwell time to a block in track model"""
        
        if self.track_link:
            self.track_link.dwell_time_actions(self.node_id,block_id)
        else:
            warnings.warn("Track model not linked!")

    def send_departure_signal(self,block_id:int):
        """@brief sends departure signal to block in track model"""
        
        if self.track_link:
            self.track_link.depart_train(self.node_id,block_id)
        else:
            warnings.warn("Track model not linked!")    
        
red_data = pandas.read_excel(DATA_PATH, sheet_name=2)
green_data = pandas.read_excel(DATA_PATH, sheet_name=3)

if len(sys.argv) > 1:
    hw = sys.argv[1]=="hw"
else:
    hw = False

if hw:
    from Wayside_HW.wayside_software_wrapper import WaysideSoftwareWrapper as WaysideControllerHardware
    wayside_nodes = {
        1: WaysideController(1,construct_block_list(red_data,1), {}, {}),
        2: WaysideController(2,construct_block_list(red_data,2), {}, {}),
        3: WaysideControllerHardware(3,construct_block_list(green_data,3), {}, {}),
        4: WaysideController(4,construct_block_list(green_data,4), {}, {}),
        5: WaysideController(5,construct_block_list(green_data,5), {}, {}),
    } 
else:
    wayside_nodes = {
        1: WaysideController(1,construct_block_list(red_data,1), {}, {}),
        2: WaysideController(2,construct_block_list(red_data,2), {}, {}),
        3: WaysideController(3,construct_block_list(green_data,3), {}, {}),
        4: WaysideController(4,construct_block_list(green_data,4), {}, {}),
        5: WaysideController(5,construct_block_list(green_data,5), {}, {}),
    }

    
# ================================================================================================================================
# component testbench
# ================================================================================================================================


class WaysideControllerTB:
    
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
                    
    def test_use_case_ctc_dispatch(self):
        wayside_nodes[4].dispatch_train(75, 15)
        
        assert wayside_nodes[4].blocks[0].authority==75, "incorrect block stored authority"
        assert wayside_nodes[4].trains[1].authority==75, "incorrect train stored authority"
        assert wayside_nodes[4].trains[1].suggested_speed==15, "incorrect train stored suggspeed"
        
    def test_use_case_tmdl_sends_occupancy(self):
        test_block = 22
        
        wayside_nodes[3].set_occupancy(test_block,True)
        
        assert wayside_nodes[3].blocks[test_block].occupied, "incorrect occupancy"
        assert wayside_nodes[3].blocks[test_block].signal.state==2, "incorrect signal state"


if __name__=="__main__": WaysideControllerTB()

