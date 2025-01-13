
import dataclasses,os,inspect
import re

## keyword tokens ##
OCC_COUNT = "occ"
SW_COUNT = "sw"
SG_COUTN = "sg"
CR_COUNT = "cr"

IF_OCCUPIED = "if-occupied"
ELIF_OCCUPIED = "elif-occupied"
# followed by:
#   - b[num]     
#   - b[num],b[num] (NO SPACES)
#   - s[char]
#   - s[char],s[char] (NO SPACES)
IF_SWITCH = "if-switch"
ELSE = "else"
END = "end"

@dataclasses.dataclass(frozen=False)
class PLCInterpreter:
    """Responsible for tokenizing, interpreting, and executing PLC code"""

    switch_states_input: dict[int:bool]
    """Switch states passed as inputs to PLC code"""
    occupancies_input: dict[int:bool]
    """Occupancies passed as inputs to PLC code"""
    tokens: list[str]
    """Tokenized PLC program"""
    oc_count: int
    """Number of blocks addressed in loaded PLC program"""
    sw_count: int
    """Number of switches addressed in loaded PLC program"""
    sg_count: int
    """Number of signals addressed in loaded PLC program"""
    cr_count: int
    """Number of crossings addressed in loaded PLC program"""

    def __init__(self,node:int):

        self.node = node
        self.switch_states_input = None
        self.occupancies_input = None
        self.tokens = []

    # @brief reads the PLC file (as a string) into tokens
    def tokenize(self, code: str):
        """@brief tokenizes input string and stores tokens internally. overwrites internal tokens if they already exist
        @param code - PLC code file read as a string"""

        self.tokens.clear()

        self.switch_states_input = None
        self.occupancies_input = None
        
        for line in code.split("\n"):
            if ";" in line: 
                continue
            for token in line.split(" "):
                token = re.sub(r"\s+", "", token)
                if token:
                    self.tokens.append(token)

        self.oc_count = int(self.tokens[self.tokens.index("occ")+1])
        self.sw_count = int(self.tokens[self.tokens.index("sw")+1])
        self.sg_count = int(self.tokens[self.tokens.index("sg")+1])
        self.cr_count = int(self.tokens[self.tokens.index("cr")+1])

    # @brief updates the PLC program's inputs
    def set_inputs(self, switch_states: dict[int:int], occupancies: dict[int:bool]):
        """@brief sets input values for switch states and occupancies
        @throws ValueError if params are not the correct length"""

        if len(switch_states)!=self.sw_count:
            raise ValueError(f"Incorrect number of switch state inputs for wayside node {self.node}\nexpected {self.sw_count}, got {len(switch_states)}")
        elif len(occupancies)!=self.oc_count:
            raise ValueError(f"Incorrect number of occupancy inputs for wayside node {self.node}\nexpected {self.oc_count}, got {len(occupancies)}")
        switch_states_bool = {}
        for k,v in switch_states.items():
            switch_states_bool[k] = v!=1
        self.switch_states_input = switch_states_bool
        self.occupancies_input = occupancies

    # @brief evaluates the condition of an 'if-occupied' statement
    def eval_if_occupied(self, condition_token: str) -> bool:
        """@brief evaluates the condition of an 'if-occupied' or 'elif-occupied' statement in the PLC code
        @param condition_token - token that immediately follows the 'if-occupied' or 'elif-occupied' token
        @returns whether the condition evaluates to true or false"""

        for elem in condition_token.split(","):
            if elem[0]=="b":
                id = int(elem[1:])
                if self.occupancies_input[id]:
                    return True
            elif elem[0]=="s":
                print("section")
            else:
                print("bad element")
        return False

    # @brief parses an 'if-occupied' statement
    def parse_if_occupied(self, assignee_token_index: int) -> bool:
        """@brief parses and evaluates an 'if-occupied' section of the loaded PLC code
        @param assignee_token_index - index of the PLC variable to which to get a new value
        @returns the new value for the assignee variable"""

        start = assignee_token_index+2
        if IF_OCCUPIED not in self.tokens[assignee_token_index:assignee_token_index+3]:
            return bool(int(self.tokens[start]))
        end = self.tokens.index(END,start)
        these_tokens = self.tokens[start:end]
        for index,token in enumerate(these_tokens):
            if token==IF_OCCUPIED or token==ELIF_OCCUPIED:
                if self.eval_if_occupied(these_tokens[index+1]):
                    return bool(int(these_tokens[index+2]))
            elif token==ELSE:
                return bool(int(these_tokens[index+1]))

    # @brief evaluates the condition of an 'if-switch' statement
    def eval_if_switch(self, condition_token: str) -> bool:
        """@brief evaluates the condition of an 'if-switch' or 'elif-switch' statement in the PLC code
        @param condition_token - token that immediately follows the 'if-switch' or 'elif-switch' token
        @returns whether the condition evaluates to true or false"""

        for elem in condition_token.split(","):
            if elem[0:2]=="sw":
                id = int(elem[2:])
                if self.switch_states_input[id]:
                    return True
            else:
                print("bad element")
        return False

    # @brief parses an 'if-switch' statement
    def parse_if_switch(self, assignee_token_index: int) -> bool:
        """@brief parses and evaluates an 'if-switch' section of the loaded PLC code
        @param assignee_token_index - index of the PLC variable to which to get a new value
        @returns the new value for the assignee variable"""

        start = assignee_token_index+2
        if IF_SWITCH not in self.tokens[assignee_token_index:assignee_token_index+3]:
            return bool(int(self.tokens[start]))
        end = self.tokens.index(END,start)
        these_tokens = self.tokens[start:end]
        for index,token in enumerate(these_tokens):
            if token==IF_SWITCH:
                if self.eval_if_switch(these_tokens[index+1]):
                    return bool(int(these_tokens[index+2]))
            elif token==ELSE:
                return bool(int(these_tokens[index+1]))

    # @brief gets the state of the switch on a block
    def get_switch(self, block_id: int) -> int:
        """@brief gets the new state of a switch based on input values
        @param block_id - location of the switch to get
        @returns the new state of the switch
        @throws ValueError if either PLC input attribute is None"""

        if not self.switch_states_input or not self.occupancies_input:
            raise ValueError("Must provide inputs to PLC before running")
        sw_index = self.tokens.index(f"sw{str(block_id)}")
        state = self.parse_if_occupied(sw_index)
        return 2 if state else 1
        
    # @brief gets the state of the signal on a block
    def get_signal(self, block_id: int):
        """@brief gets the new state of a signal based on input values
        @param block_id - location of the signal to get
        @returns the new state of the signal
        @throws ValueError if either PLC input attribute is None"""

        if not self.switch_states_input or not self.occupancies_input:
            raise ValueError("Must provide inputs to PLC before running")
        sg_index = self.tokens.index(f"sg{str(block_id)}")
        if self.tokens[sg_index+2]==IF_OCCUPIED:
            state = self.parse_if_occupied(sg_index)
        elif self.tokens[sg_index+2]==IF_SWITCH:
            state = self.parse_if_switch(sg_index)
        else:
            if self.tokens[sg_index+2]=="0":
                state = False
            elif self.tokens[sg_index+2]=="1":
                state = True
            else:
                print(f"bad token {self.tokens[sg_index+2]}")
        return 2 if state else 1
        
    # @brief gets the state of the crossing on a block
    def get_crossing(self, block_id: int):
        """@brief gets the new state of a crossing based on input values
        @param block_id - location of the crossing to get
        @returns the new state of the crossing
        @throws ValueError if either PLC input attribute is None"""

        if not self.switch_states_input or not self.occupancies_input:
            raise ValueError("Must provide inputs to PLC before running")
        cr_index = self.tokens.index(f"cr{str(block_id)}")
        state = self.parse_if_occupied(cr_index)
        return 2 if state else 1    

# ================================================================================================================================
# component testbench
# ================================================================================================================================

if __name__ == "__main__":

    with open(os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_3.plc")) as file:
        code_3 = file.read()
    with open(os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_4.plc")) as file:
        code_4 = file.read()
    with open(os.path.join(os.getcwd(),"Wayside_Controller_SW","PLC","node_5.plc")) as file:
        code_5 = file.read()
        
    class PLCInterpreterTB:
        
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

        def test_tokenize_5(self):
            mod = PLCInterpreter()
            mod.tokenize(code_5)
            
            correct = ['occ', '31', 'sw', '2', 'sg', '7', 'cr', '0']
            response = mod.tokens
            
            assert response==correct, f"correct:\t{correct}\nresponse:\t{response}"

        def test_tokenize_4(self):
            mod = PLCInterpreter()
            mod.tokenize(code_4)
            
            test_indices = {10,11}
            correct = ['if-occupied','b58,b59,b60,b61,b62']
            response = [mod.tokens[i] for i in test_indices]
            
            assert response==correct, f"correct:\t{correct}\nresponse:\t{response}"

        def test_tokenize_3(self):
            mod = PLCInterpreter()
            mod.tokenize(code_3)
            
            test_indices = {10,11}
            correct = ['if-occupied','b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25,b26,b27,b28,b29']
            response = [mod.tokens[i] for i in test_indices]
            
            assert response==correct, f"correct:\t{correct}\nresponse:\t{response}"

    PLCInterpreterTB()
