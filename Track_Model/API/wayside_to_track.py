import dataclasses
import warnings

from Track_Model.Controller import greenLine, redLine

switch_correction_map = {
    77:76,
}

@dataclasses.dataclass(frozen=True)
class WaysideTrackAPI:

    def build_train(self, node_id: int):
        #print("ws -> track: build train")
        #wayside 1 & 2 redline
        #wayside 3, 4 , 5 greenline #iteration2 green
        if(node_id == 1 or node_id==2):
            #warnings.warn("red line not implemented")
            redLine.add_train()
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            greenLine.add_train()
        else: 
            raise ValueError(f"Invalid wayside controller {node_id}")

    def send_switch_command(self, node_id:int, block_id:int, connected_to:int):
        #print("ws -> track: send sw")
        if(node_id == 1 or node_id==2):
            if block_id in switch_correction_map.keys():
                block_id = switch_correction_map[block_id]
            if redLine.block_list[block_id].get_connected_to()!=connected_to:
                redLine.block_list[block_id].set_connected_to()
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            if block_id in switch_correction_map.keys():
                block_id = switch_correction_map[block_id]
            if greenLine.block_list[block_id].get_connected_to()!=connected_to:
                greenLine.block_list[block_id].set_connected_to()
        else: 
            raise ValueError(f"Invalid wayside controller {node_id}")

    def send_signal_command(self, node_id:int, block_id:int, state:str):
        #print("ws -> track: send sig")
        if(node_id == 1 or node_id==2):
            redLine.block_list[block_id].set_light_state(state)
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            if block_id==3: return      # FIXME
            #print("block id: " + str(block_id) + " Light state: " + str(state))
            greenLine.block_list[block_id].set_light_state(state)
            #pass
        else: 
            raise ValueError(f"Invalid wayside controller {node_id}")

    def send_crossing_command(self, node_id:int, block_id:int, state:bool):
        #print("ws -> track: send crossing")
        if(node_id == 1 or node_id==2):
            #warnings.warn("red line not implemented")
            redLine.block_list[block_id].set_crossing_state(not(state))
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            greenLine.block_list[block_id].set_crossing_state(not(state))
            #pass
        else: 
            raise ValueError(f"Invalid wayside controller {node_id}")

    def send_authority(self, node_id:int, block_id:int, authority:int):
        #print("ws -> track: send auth")
        if(node_id == 1 or node_id==2):
            #warnings.warn("red line not implemented")
            redLine.block_list[block_id].set_authority(authority)
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            greenLine.block_list[block_id].set_authority(authority)
            #pass
        else: 
            raise ValueError(f"Invalid wayside controller {node_id}")

    def send_suggested_speed(self, node_id:int, block_id:int, speed:int):
        #print("ws -> track: send sgspeed")
        if(node_id == 1 or node_id==2):
            #warnings.warn("red line not implemented")
            redLine.block_list[block_id].set_suggested_speed(speed)
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            greenLine.block_list[block_id].set_suggested_speed(speed)
            #pass
        else: 
            pass

    def send_dispatch_signal(self, node_id: int, authority: int, suggested_speed: int):
        #print("ws -> track: dispatch")
        self.send_authority(node_id, 0, authority)
        self.build_train(node_id)
        return
    
    def get_switch_state(self, node_id:int, block_id:int):
        if(node_id == 1 or node_id==2):
            #warnings.warn("red line not implemented")
            redLine.block_list[block_id].get_connected_to()
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            greenLine.block_list[block_id].get_connected_to()
            #pass
        else: 
            pass

    def get_crossing_state(self, node_id:int, block_id:int):
        if(node_id == 1 or node_id==2):
            #warnings.warn("red line not implemented")
            redLine.block_list[block_id].get_crossing_state()
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            greenLine.block_list[block_id].get_crossing_state()
            #pass
        else: 
            pass
        
    # CTC lets Track Model know the train is in Dwell time at X station block
    # During dwell time, passengers get on the train, ticket sales and passengers
    # get sent to the train and CTC from Track Model
    def dwell_time_actions(self, node_id: int, block_id: int):
        if(node_id == 1 or node_id==2):
            #warnings.warn("red line not implemented")
            redLine.dwell_time_actions(block_id)
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            greenLine.dwell_time_actions(block_id)
        else: 
            pass

    def depart_train(self, node_id:int, block_id: int):
        if(node_id == 1 or node_id==2):
            #warnings.warn("red line not implemented")
            redLine.depart_train(block_id)
        elif (node_id == 3 or node_id == 4 or node_id == 5):
            greenLine.depart_train(block_id)
        else: 
            pass