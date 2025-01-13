import dataclasses

from Wayside_Controller_SW.wayside_ui import WaysideUI

@dataclasses.dataclass(frozen=False)
class ControllerToUI:
    """API responsible for sending information from backend to frontend. called by wayside backend"""

    ui: WaysideUI
    """wayside ui:\n
    mutable reference to wayside controller ui"""
    def __init__(self,ui):
        self.ui=ui
        
    def send_switch(self, line: str, block: int, state: int):
        """@brief sends a switch state from wayside backend to wayside frontend"""
        if self.ui.wayside_node.node_id in [1,2] and line=="red":
            self.ui.set_switch_table_state(block,state)
        elif self.ui.wayside_node.node_id in [3,4,5] and line=="green":
            self.ui.set_switch_table_state(block,state)
        
    def send_signal(self, line: str, block: int, state: int):
        """@brief sends a signal state to wayside frontend"""
        if self.ui.wayside_node.node_id in [1,2] and line=="red":
            self.ui.set_signal_table_state(block,state)
        elif self.ui.wayside_node.node_id in [3,4,5] and line=="green":
            self.ui.set_signal_table_state(block,state)
        
    def send_crossing(self, line: str, block: int, state: int):
        """@brief sends a crossing state to wayside frontend"""
        if self.ui.wayside_node.node_id in [1,2] and line=="red":
            self.ui.set_crossing_table_state(block,state)
        elif self.ui.wayside_node.node_id in [3,4,5] and line=="green":
            self.ui.set_crossing_table_state(block,state)
        
    def send_occupancy(self, line: str, block: int, occupied: bool):
        """@brief sends an occupancy update to wayside frontend"""
        if self.ui.wayside_node.node_id in [1,2] and line=="red":
            self.ui.set_occupancy(block,occupied)
        elif self.ui.wayside_node.node_id in [3,4,5] and line=="green":
            self.ui.set_occupancy(block,occupied)
            
    def send_maintenance(self, line: str, block: int, maintenance: bool):
        """@brief sends a maintenance state to wayside frontend"""
        if self.ui.wayside_node.node_id in [1,2] and line=="red":
            self.ui.set_maintenance(block,maintenance)
        elif self.ui.wayside_node.node_id in [3,4,5] and line=="green":
            self.ui.set_maintenance(block,maintenance)
            
    def send_authority(self, line: str, block: int, authority: int):
        """@brief sends an authority to wayside frontend"""
        if self.ui.wayside_node.node_id in [1,2] and line=="red":
            self.ui.set_authority(block,authority)
        elif self.ui.wayside_node.node_id in [3,4,5] and line=="green":
            self.ui.set_authority(block,authority)
        