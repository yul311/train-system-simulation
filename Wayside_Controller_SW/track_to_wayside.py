import dataclasses

# import wayside controller instances
from Wayside_Controller_SW.wayside_controller import wayside_nodes

@dataclasses.dataclass(frozen=False)
class TrackWaysideAPI:
    """API responsible for managing communications from Track Model to Wayside Controller"""
    selected_node:int
    """stores which wayside controller track model is sending information to"""
    
    def __init__(self):
        self.selected_node = 1

    def set_wayside_node(self, node: int):
        """changes which wayside controller to talk to"""
        self.selected_node = node

    def send_occupancies(self, line: str, block_id: int, occupied: bool):
        """sends an occupancy from track model -> wayside"""
        if(line == "green"):
            for id in [3,4,5]:
                if block_id in wayside_nodes[id].blocks.keys():
                    wayside_nodes[id].set_occupancy(block_id, occupied)
        elif(line == "red"):
            for id in [1,2]:
                if block_id in wayside_nodes[id].blocks.keys():
                    wayside_nodes[id].set_occupancy(block_id, occupied)
        else:
            raise Exception(f"'{line}' is not a valid line entry")
