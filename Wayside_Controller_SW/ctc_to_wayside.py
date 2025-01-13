import dataclasses

from Wayside_Controller_SW.wayside_controller import wayside_nodes

@dataclasses.dataclass(frozen=False)
class CTCWaysideAPI:
    """API responsible for sending CTC values into wayside controller. called by CTC Office backend"""
    selected_node: int
    """current selected wayside controller:\n
    indicates which wayside controller CTC is talking to"""
    
    def __init__(self):
        self.selected_node = 1

    def set_wayside_node(self, node: int):
        """@brief changes which wayside controller to send information to"""
        self.selected_node = node

    def dispatch_train(self, authority: int, speed: int):
        """@brief sends dispatch train signal from CTC -> wayside"""
        #print("ctc -> ws: dispatch")
        wayside_nodes[self.selected_node].dispatch_train(authority,speed)

    def send_authority(self, block_id: int, authority: int):
        """@brief sends new authority value for block from CTC -> wayside"""
        #print("ctc -> ws: auth")
        wayside_nodes[self.selected_node].set_ctc_authority(block_id,authority)

    def send_suggested_speed(self, block_id: int, speed: int):
        """@brief sends new suggested speed value for block from CTC -> wayside"""
        #print("ctc -> ws: suggspeed")
        wayside_nodes[self.selected_node].set_suggested_speed(block_id,speed)

    def send_maintenance_status(self, block_id: int, maintenance: bool):
        """@brief sends maintenance status for block from CTC -> wayside"""
        #print("ctc -> ws: maintenance")
        wayside_nodes[self.selected_node].set_maintenance(block_id, maintenance)

    def send_maintenance_switch(self, block_id: int, switch_state: int):
        """@brief sends request to change switch under maintenance for block from CTC -> wayside"""
        #print("ctc -> ws: sw control")
        # TODO convert correct switch states
        wayside_nodes[self.selected_node].set_switch(block_id,switch_state)

    #send command train should be in dwell time now to track model
    def dwell_time_actions(self, block_id: int):
        """@brief sends dwell time to block from CTC -> wayside"""
        
        wayside_nodes[self.selected_node].send_dwell_time(block_id)

    #send command train to end dwell time actions
    def depart_train(self, block_id: int):
        """@brief triggers a train to depart (passthrough) CTC -> Wayside"""
        wayside_nodes[self.selected_node].send_departure_signal(block_id)
        
    def set_yard_return_mode(self, node_id: int, mode: bool):
        """@brief sets wayside controller to yard return mode CTC -> Wayside"""
        wayside_nodes[node_id].set_yard_return(mode)
