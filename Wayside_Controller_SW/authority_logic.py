import dataclasses
import os,sys
import traceback
import warnings

try:
    from Wayside_Controller_SW.rail_system import Block
    from Wayside_Controller_SW.rail_system_controller import node_switches,node_signals
except:
    from rail_system import Block
    from rail_system_controller import node_switches,node_signals
    
green_adj_list = {
    0: (57,63),
    1: (13,151),
    2: (151,3),
    3: (2,4),
    4: (3,5),
    5: (4,6),
    6: (5,7),
    7: (6,8),
    8: (7,9),
    9: (8,10),
    10: (9,11),
    11: (10,12),
    12: (11,13),
    13: (12,14,1),
    14: (13,15),
    15: (14,16),
    16: (15,17),    
    17: (16,18),
    18: (17,19),
    19: (18,20),
    20: (19,21),
    21: (20,22),
    22: (21,23),
    23: (22,24),
    24: (23,25),
    25: (24,26),
    26: (25,27),
    27: (26,28),
    28: (27,29),
    29: (28,30,150),
    30: (29,31),
    31: (30,32),
    32: (31,33),
    33: (32,34),
    34: (33,35),
    35: (34,36),
    36: (35,37),
    37: (36,38),
    38: (37,39),
    39: (38,40),
    40: (39,41),
    41: (40,42),
    42: (41,43),
    43: (42,44),
    44: (43,45),
    45: (44,46),
    46: (45,47),
    47: (46,48),
    48: (47,49),
    49: (48,50),
    50: (49,51),
    51: (50,52),
    52: (51,53),
    53: (52,54),
    54: (53,55),
    55: (54,56),
    56: (55,57),
    57: (56,58,0),
    58: (57,59),
    59: (58,60),
    60: (59,61),
    61: (60,62),
    62: (61,63),
    63: (62,64,0),
    64: (63,65),
    65: (64,66),
    66: (65,67),
    67: (66,68),
    68: (67,69),
    69: (68,70),
    70: (69,71),
    71: (70,72),
    72: (71,73),
    73: (72,74),
    74: (73,75),
    75: (74,76),
    76: (75,77),
    77: (76,78,101),
    78: (77,79),
    79: (78,80),
    80: (79,81),
    81: (80,82),
    82: (81,83),
    83: (82,84),
    84: (83,85),
    85: (84,86,100),
    86: (85,87),
    87: (86,88),
    88: (87,89),
    89: (88,90),
    90: (89,91),
    91: (90,92),
    92: (91,93),
    93: (92,94),
    94: (93,95),
    95: (94,96),
    96: (95,97),
    97: (96,98),
    98: (97,99),
    99: (98,100),
    100: (85,99),
    101: (77,152),
    102: (152,103),
    103: (102,104),
    104: (103,105),
    105: (104,106),
    106: (105,107),
    107: (106,108),
    108: (107,109),
    109: (108,110),
    110: (109,111),
    111: (110,112),
    112: (111,113),
    113: (112,114),
    114: (113,115),
    115: (114,116),
    116: (115,117),
    117: (116,118),
    118: (117,119),
    119: (118,120),
    120: (119,121),
    121: (120,122),
    122: (121,123),
    123: (122,124),
    124: (123,125),
    125: (124,126),
    126: (125,127),
    127: (126,128),
    128: (127,129),
    129: (128,130),
    130: (129,131),
    131: (130,132),
    132: (131,133),
    133: (132,134),
    134: (133,135),
    135: (134,136),
    136: (135,137),
    137: (136,138),
    138: (137,139),
    139: (138,140),
    140: (139,141),
    141: (140,142),
    142: (141,143),
    143: (142,144),
    144: (143,145),
    145: (144,146),
    146: (145,147),
    147: (146,148),
    148: (147,149),
    149: (148,150),
    150: (149,29),
    151: (1,2),
    152: (101,102)
}
red_adj_list = {}

# switch 77->76

# switch_id: ({primary position authorities},{secondary position authorities})
green_switch_authorities = {
    12: ({1:0, 151:50, 2:150, 3:250},{}),
    29: ({150:0, 149:35, 148:219},{}),
    57: ({},{}),
    63: ({0:0},{62:0, 61:50, 60:100, 59:150, 58:200}),
    77: ({},{76:0, 75:100, 74:200}),
    85: ({100:0, 99:75, 98:150, 97:225},{})
}
green_signal_authorities = {
    0: {0:0},
    1: {},#{1:0, 151:50, 2:150, 3:250},
    2: {2:0, 3:100, 4:200},
    9: {9:0, 10:100, 11:200},
    12: {12:0, 13:150, 14:300},
    13: {13:0, 1:50, 151:100, 2:200, 14:150, 15:300},
    16: {16:0, 15:150, 14:300, 17:150, 18:300},
    22: {22:0, 21:300, 23:300},
    29: {29:0, 28:50, 27:100, 26:200, 150:35, 149:75, 148:259},
    30: {30:0, 29:50, 28:100, 27:150, 26:250},
    31: {31:0, 30:50, 29:100, 28:150, 27:200},
    39: {39:0, 38:50, 37:100, 36:150, 35:200},
    48: {48:0, 47:50, 46:100, 45:150, 44:200},
    57: {57:0, 56:50, 55:100, 54:150, 53:200},
    58: {58:0, 57:50, 56:100, 55:150, 54:200},
    62: {62:0, 61:50, 60:100, 59:150, 58:200},
    63: {63:0, 62:50, 61:100, 60:150, 59:200},
    65: {65:0, 64:100, 63:200},
    73: {73:0, 72:100, 71:200},
    76: {},#{76:0, 75:100, 74:200},
    77: {77:0, 76:100, 75:200, 78:300},
    85: {85:0, 84:300, 100:75, 99:150, 98:225},
    86: {86:0, 85:300},
    88: {88:0, 87:87, 86:187, 85:487},
    96: {96:0, 95:75, 94:150, 93:225},
    100: {},#{100:0, 99:75, 98:150, 97:225},
    101: {101:0, 77:300},
    105: {105:0, 104:75, 103:175, 102:275},
    114: {114:0, 113:100, 112:200},
    123: {123:0, 122:50, 121:100, 120:150, 119:190, 118:240},
    132: {132:0, 131:50, 130:100, 129:150, 128:200},
    141: {141:0, 140:50, 139:100, 138:150, 137:200},
    150: {},#{150:0, 149:40, 148:224},
}
red_switch_authorities = {
    9: ({0:0},{10:0, 11:75, 12:150, 13:220}),
    15: ({1:0, 2:50, 3:100, 4:150, 5:200},{}),
    27: ({77:0, 76:25, 75:50, 74:100, 73:150, 72:200},{}),
    32: ({},{32:0, 31:50, 30:100, 29:150, 28:200}),
    38: ({71:0, 70:50, 69:100, 68:150, 67:200},{}),
    43: ({},{43:0, 42:50, 41:100, 40:150, 39:200}),
    52: ({66:0, 78:75, 65:113, 64:150, 63:225},{})
}
red_signal_authorities = {
    0: {0:0},
    1: {},#{1:0, 2:50, 3:100, 4:150, 5:200},
    7: {7:0, 6:50, 5:100, 4:150, 3:200, 8:75, 9:150, 10:225, 0:200},
    9: {9:0, 8:75, 7:150, 6:200, 10:75, 11:150, 12:225},
    10: {10:0, 9:75, 8:150, 7:225, 11:75, 12:150, 13:220},
    15: {},
    16: {16:0, 1:50, 2:100, 3:150, 4:200, 17:200},
    21: {21:0, 20:200, 22:100, 23:100},
    25: {25:0, 24:50, 23:150, 22:250, 26:50, 27:100, 77:125, 76:150, 75:200},
    27: {},
    28: {},
    32: {},
    33: {},
    35: {35:0, 34:50, 33:100, 32:150, 31:200},
    38: {},
    39: {},
    43: {},
    44: {},
    48: {48:0, 47:75, 46:150, 45:225, 49:50, 50:100, 51:150, 52:190},
    52: {},
    53: {},
    60: {60:0, 59:75, 58:150, 57:225, 61:75, 62:150, 63:225},
    66: {},
    67: {},
    71: {},
    72: {},
    77: {},
}

# TODO
#   authority types:
#       vital:
#           switch authority (static)
#           signal authority (static)
#           train authority (dyn)
#       nonvital:
#           ctc authority (dyn)
#   precedence:
#       vital > nonvital

@dataclasses.dataclass(frozen=False)
class Authority:
    
    ctc: int
    """authority value from CTC office"""
    switch: int
    """wayside authority value determined purely by switch states"""
    signal: int
    """wayside authority value determined purely by signal states. only applied on certain signals"""
    train: int
    """wayside authority value determined purely from occupancies. NOTE ctc might have to do this part..."""
    
    use_ws: bool
    """whether to use wayside or ctc authority"""
    
@dataclasses.dataclass(frozen=False)
class AuthorityLogicController:
    """responsible for determining wayside authority values. must also VITALLY determine which authority value to use"""
    
    node: int
    """CONST wayside node id:\n
    indicates which wayside controller this object is a part of"""
    blocks: dict[int:Block]
    """block dict reference:\n
    mutable reference to wayside controller blocks dict"""
    authorities: dict[int:Authority]
    """internal authority dict:\n
    stores authorities for CTC, switches, signals, and occupancies, for"""
    adj_list: dict[int:(int,int)]
    """CONST adjacency list:\n
    track block adjacency list for red line or green line"""
    switches: dict[int:(int,int)]
    """CONST switch positions dict:\n
    dict of all switch placements on this wayside controller and their connections"""
    signals: set[int]
    """CONST signal positions set:\n
    set of all signal placements on this wayside controller"""
    
    def __init__(self, node: int, blocks: dict[int:Block]):
        
        self.node=node
        self.blocks=blocks
        if node in {1,2}:
            self.adj_list = red_adj_list
        else:
            self.adj_list = green_adj_list
        self.switches = node_switches[node]
        self.signals = node_signals[node]
        
        self.authorities = {}
        for block in blocks.values():
            self.authorities[block.id] = Authority(
                ctc=block.ctc_authority,
                switch=sys.maxsize,
                signal=sys.maxsize,
                train=sys.maxsize,
                use_ws=False
            )
            
    def set_ctc_authority(self, block_id: int, authority: int):
        """@brief sets internally stored value for CTC authority. called when CTC sends a new authority"""
        
        self.authorities[block_id].ctc = authority
        
    # NOTE this is vital
    def choose_authority(self, block_id: int):
        """@brief chooses which authority to use for a block and sets the corresponding boolean in the internal authority dict"""
        
        ws_auth = min(self.authorities[block_id].switch,self.authorities[block_id].signal,self.authorities[block_id].train)
        if ws_auth<self.authorities[block_id].ctc:
            self.authorities[block_id].use_ws = True
        else:
            self.authorities[block_id].use_ws = False
    
    def load_authorities_to_blocks(self) -> set[int]:
        """@brief decides which authority value to assign to each block and performs the assignment
        @returns a set of blocks whose authority values have changed"""
        
        deltas = set()
        for block in self.blocks.values():
            self.choose_authority(block.id)
            new_ws_authority = min(self.authorities[block.id].switch,self.authorities[block.id].signal,self.authorities[block.id].train)
            new_use_ws_authority = self.authorities[block.id].use_ws
            if new_ws_authority!=block.ws_authority:
                block.ws_authority = new_ws_authority
                deltas.add(block.id)
            if new_use_ws_authority!=block.use_ws_authority:
                block.use_ws_authority = new_use_ws_authority
                deltas.add(block.id)
        return deltas
    
    def load_authority_to_block(self, block_id: int):
        """@brief loads internally stored authority value to block in blocks dict. also\n
        chooses which authority to use"""
        
        self.choose_authority(block_id)
        self.blocks[block_id].ws_authority = min(self.authorities[block_id].switch,self.authorities[block_id].signal,self.authorities[block_id].train)
        self.blocks[block_id].use_ws_authority = self.authorities[block_id].use_ws
            
    def update_switch_authorities(self):
        """@brief updates authorities based on all switch states in node region"""
        
        if self.node in {1,2}:
            self.load_switch_authorities(red_switch_authorities)
        else:
            self.load_switch_authorities(green_switch_authorities)
            
    def update_signal_authorities(self):
        """@brief updates authorities based on all signal states in node region"""
        
        if self.node in {1,2}:
            self.load_signal_authorities(red_signal_authorities)
        else:
            self.load_signal_authorities(green_signal_authorities)
            
    def load_switch_authorities(self, switch_authority_dict: dict[int:(dict[int:int],dict[int:int])]):
        """@brief calculates authorities based in block switch state and puts them in internal authority storage"""
        
        for switch in self.switches:
            primary_authorities,secondary_authorities = switch_authority_dict[switch]
            if self.blocks[switch].switch.state==1:
                for block,authority in primary_authorities.items():
                    self.authorities[block].switch = authority
                for block,authority in secondary_authorities.items():
                    self.authorities[block].switch = self.authorities[block].ctc
            else:
                for block,authority in primary_authorities.items():
                    self.authorities[block].switch = self.authorities[block].ctc
                for block,authority in secondary_authorities.items():
                    self.authorities[block].switch = authority
            
    def load_signal_authorities(self, signal_authority_dict: dict[int:dict[int:int]]):
        """@brief calculates authorities based in block switch state and puts them in internal authority storage"""
                    
        for signal in self.signals:
            redlight_authorities = signal_authority_dict[signal]
            if self.blocks[signal].signal.state==1:
                for block in redlight_authorities.keys():
                    if block not in self.authorities.keys():
                        continue
                    self.authorities[block].signal = self.authorities[block].ctc
            else:
                for block,authority in redlight_authorities.items():
                    if block not in self.authorities.keys():
                        continue
                    self.authorities[block].signal = authority

    # NOTE may be unnecessary  
    def load_all_occupancy_authorities(self):
        """@brief loads authorities to internal authority dict for each occupied track block"""
        pass

    def load_occupancy_authorities(self, block_id: int, occupied: bool):
        """@brief loads authorities to internal authority dict for the specified block id and occupancy"""
        pass
        
    def get_clearance_region(self, block_id: int, track_direction: int) -> dict[int:Block]:
        """@brief assumes block_id param is occupied and returns surrounding blocks for which authority must be changed (including og block_id)"""
        pass