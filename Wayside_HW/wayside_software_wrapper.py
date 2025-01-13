import paho.mqtt.client as mqtt
import json
import os
import sys
import time
import threading
import queue
sys.path.append(os.getcwd())

mqtt_connected = threading.Event()

from Wayside_Controller_SW .wayside_controller import WaysideController

class Block:
    id: int
    section: str
    occupied: bool
    maintenance: bool
    switch: "Switch"
    signal: "Signal"
    crossing: "Crossing"
    
class Signal:
    state_1: int
    state_2: int
    
class Switch:
    state: int
    
class Crossing:
    state: int

class WaysideSoftwareWrapper(WaysideController):
    node_id: int
    line: str
    blocks: dict[int:Block]
    switches: dict[int:bool]
    signals: dict[int:bool]
    crossing: dict[int:bool]
    occupancy: dict[int:bool]


    def __init__(self, node_id: int, blocks: dict[int:Block], entries: set[int], exits: set[int]):
        super().__init__(node_id, blocks, entries, exits)
        self.mqtt_broker = "172.20.10.2"
        #self.mqtt_broker = "10.0.0.209"
        self.mqtt_port = 1883
        self.client = mqtt.Client("pooman", True, None, mqtt.MQTTv31)
        self.client.connect(self.mqtt_broker, self.mqtt_port, 3600)
        
        self.client.on_connect = self.on_connect
        
        mqtt_thread = threading.Thread(target=self.mqtt_loop)
        mqtt_thread.start()

        mqtt_connected.wait()
        
        #self.client.loop_start()
        
        #self.client.on_disconnect = self.on_disconnect
        self.client.on_message = self.on_message
        self.occupancy = {1:False,151:False,2:False,3:False,4:False,5:False,6:False,7:False,8:False,9:False,10:False,11:False,12:False,13:False,14:False,15:False,16:False,17:False,18:False,19:False,20:False,21:False,22:False,23:False,24:False,25:False,26:False,27:False,28:False,29:False,30:False,31:False,32:False,144:False,145:False,146:False,147:False,148:False,149:False,150:False}
        self.last_block_data = {}
        self.switches = {}
        self.crossing = {}
        self.signals = {}
        if not getattr(self, 'plc_published', False):
            self.publish_plc()
            self.plc_published = True
        self.publish_occupancies(self.occupancy)
    
    def on_connect(self, client, userdata, flags, rc):
            if rc==0:
                print("Connection OK Returned code=", rc)
                mqtt_connected.set()
                client.subscribe("wayside/switches")
                client.subscribe("wayside/crossing")
                client.subscribe("wayside/signals")
                client.subscribe("wayside/keepalive")
            else:
                print("Connection Error Returned code=", rc)
    def on_message(self, client, userdata, msg):
        payload = json.loads(msg.payload)
        if msg.topic == "wayside/switches":
            self.update_switch(payload)
        elif msg.topic == "wayside/crossing":
            self.update_crossing(payload)
        elif msg.topic == "wayside/signals":
            self.update_signal(payload)
        elif msg.topic == "wayside/keepalive":
            pass
    
    def on_disconnect(self, client, userdata, rc):
        print(f"Disconnected with result code {rc}")
    def mqtt_loop(self):
        while True:
            self.client.loop()
    
    def update_switch(self, payload):
        #this calls track model
        print("Received Switch States:", payload)
        for block_id, state in payload.items():
        # Convert block_id to int if needed
            block_id = int(block_id)
            self.switches[block_id] = state
        # Update switches in your track model
            print("Updating switch - Block ID:", block_id, "State:", state)
            state_val = 2 if state else 1
            self.set_switch(block_id, state_val)
        
    def update_crossing(self, payload): #this calls track model
        print("Received Crossing State: ", payload)
        for block_id, state in payload.items():
            block_id = int(block_id)
            self.crossing[block_id] = state
            state_val = 2 if state else 1
            self.set_crossing(block_id, state_val)
        
    def update_signal(self, payload): #this calls track model
        for block_id, state in payload.items():
            block_id = int(block_id)
            self.signals[block_id] = state
            state_value = 2 if state else 1
            self.set_signal(block_id, state_value)
        
        
        
        
    def set_occupancy(self, block_id: int, occupied: bool): #track calls this
        self.occupancy[block_id] = occupied
        self.publish_occupancies(self.occupancy)
        if self.ui_link:
            self.ui_link.send_occupancy(self.line.lower(), block_id, occupied)
        if self.ui_link:
            pass
        
        
    def set_maintenance(self, block_id: int, under_maintenance): #ctc calls this
        self.blocks[block_id].maintenance = under_maintenance
   
    
   # def set_authority():
        
    def publish_plc(self):
        with open(os.path.join(os.getcwd(), "Wayside_Controller_SW", "PLC", "node_3.plc"), "r") as file:
            plc_code = file.read()
            self.client.publish(f"wayside/plc", plc_code)
        print("Published PLC")
        
    
    
    # @brief loads a PLC program override
    def load_plc_program(self, path: os.PathLike, program_number: int = None):
        """@brief loads a PLC program into the rail system controller.
        also immediately reruns the new PLC program"""
        
        self.publish_plc(path)

    def publish_occupancies(self, occupancy):
        block_data = {block_id: occupied for block_id, occupied in occupancy.items()}
        block_json_data = json.dumps(block_data)
        
        with open("blockOccs.json", "w") as json_file:
            json.dump(block_json_data, json_file)
            
        if hasattr(self, 'last_block_data'):
            for block_id, occupied in block_data.items():
                last_occupied = self.last_block_data.get(block_id, False)

                if last_occupied and not occupied:
                    print(f"Skipping publishing for {block_id}...")
                    break  # Skip publishing for this function call

                elif block_id==144:
                    self.client.publish("wayside/blocks", block_json_data)

            else:  # This block will execute if the loop completes without a break
                print("Publishing data now...")
                self.client.publish("wayside/blocks", block_json_data)

        # Update last_block_data at the end
        self.last_block_data = block_data

        
    def publish_switches(self, blocks):
        switch_data = json.dumps(blocks)
        self.client.publish(f"wayside/switches", switch_data)

    def publish_signals(self, data):
        self.client.publish(f"wayside/signals", data)
    
    def close(self):
        self.client.disconnect()

node_id = 3
blocks = {}  # Fill in your block data here
entries = set()  # Fill in your entries data here
exits = set()  # Fill in your exits data here
#mqtt_broker = "10.0.0.209"
#mqtt_port = 1883  # Adjust the port as needed
#wrapper = WaysideSoftwareWrapper(node_id, blocks, entries, exits)
#wrapper.publish_plc()

# Start the MQTT client thread



#block_id = 7  # Replace with the desired block ID
#occupied = False  # Replace with the desired occupancy state
#wrapper.set_occupancy(7, False)
#wrapper.set_occupancy(1, True)
#wrapper.set_occupancy(4, False)
#wrapper.set_occupancy(3, True)
#print("Occupancy Dictionary:")
#print(wrapper.occupancy)
    
    # Print the occupancy dictionary