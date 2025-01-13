from Track_Model.railway.trackblock import track_Block
from Track_Model.railway.train_object import train
from Main.simulation_time import sim
#sim = sim2
import copy
from Track_Model.services.readdatabase import Database

import random

#------------------------------------------------------------------
# Rail Line Class
#------------------------------------------------------------------
class rail_lines(track_Block):
    def __init__(self, line_name:str):
        self.__line_name = line_name
        #Variables
        self.block_list = []  #list of all block objects
        self.trains = {}      #Dictionary of all train objects
        self.setup_trains()
        self.__num_blocks = 0
        self.__temperature = 23
        self.__throughput = 0
        self.__heaters = False      #start temperature is 75 degrees >35
        self.train_counter = 1
        self.ctc_link = None
        self.wayside_link = None
        self.__total_passengers = 0


    def setup_trains(self):
        '''
            Setup the train lists for the other UIs to pull from
        '''
        #ignore blue line
        if self.__line_name == "green":
            for i in range(1,150):
                self.trains[i] = "Yard"
        
        if self.__line_name == "red":
            for i in range(1,70):
                self.trains[i] = "Yard"

    def build_rail_blocks(self, blockID:int, section:str, blockLength:int, elevation:int, cumul_elev:int,
                   gradlevel:int, maxSpeed:int, occupancy:int, authority:int, polarity:int, underground:int):
        '''
            Build the rail blocks into block_list
            
            Parameters:
                blockID: ID of the current block
                Section: Section of line this block is on
                elevation: Elevation of the current block
                cumulative elevation: The cumulative elevation up till this block
                gradient level: gradient level of the block
                max speed: max speed allowed on the block
                occupancy: Is block occupied (False)
                authority: can be added to pre-set authority to block, but atm is not used
                polarity: Polarity of each track block
                underground: whether the block is underground or not
        '''
        
        self.block_list.append(track_Block(blockID, section, blockLength, elevation,cumul_elev, 
                                           gradlevel, maxSpeed, occupancy, polarity, underground))
        self.__num_blocks += 1

    def set_links(self, ctc_link, wayside_link):
        self.ctc_link = ctc_link
        self.wayside_link = wayside_link



    #------------------------------------------------------------------
    # Set Operations
    #------------------------------------------------------------------
    def set_throughput(self, throughput:int):
        self.__throughput = throughput
    
    def set_temperature(self, newtemp:int):
        self.__temperature = newtemp
        if (self.__temperature <= 1.7):
            self.__heaters = True
        else:
            self.__heaters = False

    #------------------------------------------------------------------
    # Get Operations
    #------------------------------------------------------------------
    def get_line(self):
        return self.__line_name
    
    def get_temperature(self):
        return self.__temperature

    def get_heater_state(self):
        if self.__heaters == True:
            return "ON"
        else:
            return "OFF"
        
    def dwell_time_actions(self, blockid:int):
        '''
            Parameters:
                blockid: station block train is dwelling on

            Set dwelling to True for
                - station: to display boarding, exiting passengers
                - train(graphically): To change colors on line for if the train is supposed to be there
        '''
        if(self.block_list != None and self.block_list[blockid].stations != None):
            #----
            #Integration
            #-----
            #get the train ID for the train on the block
            train_id = None
            self.block_list[blockid].set_dwelling(True)
            
            if len(list(self.trains)) >= 1:
                for key,value in self.trains.items():
                    #print("key: " + str(key) + " value: " + str(value))
                    if value != "Yard":
                        if self.trains[key].get_train_position() == int(blockid):
                            train_id = key
                            self.trains[train_id].set_dwelling(True)
                            self.boarding_passenger_calculation(blockid)
                            self.trains[train_id].tr_to_tm.send_ticket_sale(int(self.block_list[blockid].get_boarding_passengers()))
                            
                     
            self.__total_passengers = self.__total_passengers + int(self.block_list[blockid].get_boarding_passengers())       
            #send the ticketsales to the CTC
            self.ctc_link.send_ticket_sales(self.__line_name, int(self.block_list[blockid].get_station_ticket_sales()))
            # update throughput for my module
            self.__throughput = self.__throughput + int(self.block_list[blockid].get_boarding_passengers())
            
            #----------------
            #UPDATE THIS 12-8-23
            #--------------
            # update to perfrom random variable check and push a random number of passengers to
            # to the train separate of ticket sales
            # decrease ticket sales


    def depart_train(self, block_id:int):
        '''
            Set dwelling to false for
                - station: to display boarding, exiting passengers
                - train(graphically): To change colors on line for if the train is supposed to be there
            Parameters:
                block_id: Station Block to set depart train from
        '''
        self.block_list[block_id].set_dwelling(False)

        if len(list(self.trains)) >= 1:
            for key,value in self.trains.items():
                #print("key: " + str(key) + " value: " + str(value))
                if value != "Yard":
                    if self.trains[key].get_train_position() == int(block_id):
                        self.trains[key].set_dwelling(False)
                        

        #update total passengers in system
        self.__total_passengers = self.__total_passengers - self.block_list[block_id].get_leaving_passengers()

        #reset values for boarding and departing back to 0
        self.block_list[block_id].set_boarding_passengers(0)
        self.block_list[block_id].set_leaving_passengers(0)


    def get_throughput(self):
        return self.__throughput


    def set_leaving_passengers(self, train_id:int, passengers:int):
        #passengers leaving train
        position = self.trains[train_id].get_train_position()
        self.block_list[position].set_leaving_passengers(passengers)

    def increase_ticket_sales(self):
        for i in range(len(self.block_list)):
            if self.block_list[i].stations != None:
                a = self.block_list[i].get_station_ticket_sales()
                if a <= 5:
                    self.block_list[i].set_ticket_sales(6)
                else:
                    self.block_list[i].set_ticket_sales(a+1)

    def boarding_passenger_calculation(self,block_id:int):
        '''
        Retrieve ticket sales, select a random number of them. Send the selection to train.
        Decrease the stations ticket sales
        '''
        station_tickets = self.block_list[block_id].get_station_ticket_sales()
        boarding_passengers = random.randint(0,station_tickets)
        self.block_list[block_id].set_ticket_sales(int(station_tickets - boarding_passengers))
        self.block_list[block_id].set_boarding_passengers(boarding_passengers)

    def set_total_passengers(self, value:int):
        self.__total_passengers = value
    
    def get_total_passengers(self):
        return self.__total_passengers


    #------------------------------------------------------------------
    # Train Operations
    #------------------------------------------------------------------

    def get_current_time(self):
        return (sim.get_sim_speed()*50/1000)
    
    def add_train(self):
        #increment train counter
        #create train object
        #set the block enter time that the train started on the yard
        #set the yard's occupancy to 1
        #set the train's speed to the block's max speed
        while self.trains[self.train_counter] != "Yard":
            self.train_counter +=1
            if self.trains[self.train_counter] == "Yard":
                break
            
        #print("train id: " +str(self.train_counter))
        self.trains[self.train_counter] = train(self.train_counter,self)
        #print("train item: " +str(self.trains[self.train_counter]))
        self.trains[self.train_counter].set_block_enter_time(self.get_current_time())
        #change occupancy of block 0 "yard"
        self.change_occupancy(0)
        #update train values for track model
        self.trains[self.train_counter].set_block_last_cycle_time(self.get_current_time())
        self.trains[self.train_counter].set_line(self.__line_name)
        self.trains[self.train_counter].set_train_id(self.train_counter)
        self.trains[self.train_counter].set_time_to_travel(self.block_list[0].get_time_to_travel())
        self.trains[self.train_counter].set_entered_switch_block(True)
        # set the train speed to block suggested speed
        #--------
        # Integration
        #--------
        # send train authority to train
        # self.trains[self.train_counter].tr_to_tm.send_polarity_change(bool(self.block_list[0].get_polarity()))
        # send authority from block, received by CTC -> Wayside to Train
        self.trains[self.train_counter].tr_to_tm.send_authority(self.block_list[0].get_authority())
        # send yard beacon to train
        self.trains[self.train_counter].tr_to_tm.send_beacon_package(self.block_list[0].get_station_beacon1(),self.block_list[0].get_station_beacon2())
        # send train line
        self.trains[self.train_counter].tr_to_tm.send_line(self.__line_name)
        # send train id
        self.trains[self.train_counter].tr_to_tm.send_train_id(self.train_counter)
        # send train suggested speed
        self.trains[self.train_counter].tr_to_tm.send_suggested_speed(self.block_list[0].get_suggested_speed())

    def get_polarity(self, block_id:int):
        self.block_list[block_id].get_polarity()
    
    def get_authority(self, block_id:int):
        return self.block_list[block_id].get_authority()

    def set_block_enter_time(self, train_id:int):
        self.trains[train_id].set_block_enter_time(self.get_current_time())

    def set_train_position(self, train_id:int, block:int):
        self.trains[train_id].set_train_position(block)

    def delete_train(self,train_id:int):
        #delete the train object, model, controller, and all sub-class objects of each.
        position = self.trains[train_id].get_train_position()
        self.block_list[position].set_occupancy(False)
        self.trains[train_id].model.delete_train()
        self.trains[train_id].controller.delete_train()
        del self.trains[train_id].model
        del self.trains[train_id].controller
        del self.trains[train_id].tr_to_tm
        self.trains[train_id] = "Yard"
        #print("Train Returned to Yard" + str(self.trains))
        if self.__line_name == "blue":
            if self.train_counter == 14:
                self.train_counter = 0
        elif self.__line_name == "green":
            if self.train_counter == 150:
                self.train_counter = 0
        else:
            #if number of trains matches length of redline set to 0 here
            pass
    
    def get_train_speed(self, train_id:int):
        return self.trains[train_id].get_train_speed()

    def update_trains(self):
        # if there is a train that exists
        # get it's current position, get the time it entered the block,
        # get current time and find the difference
        # Get the trains speed
        # check the algorithm to see if the train has travelled the block length
        # use the algorithm to find the time till the end of the block
        # if the time till end of block == 0, set the train to the next block
        # update train's last block position so the ability to reset track_block
        # colors to default colors exists for that block
        if len(list(self.trains)) >= 1:
            for key,value in self.trains.items():
                #print("key: " + str(key) + " value: " + str(value))
                if value != "Yard":
                    #If train position is 57 and it goes to the yard. Delete the train
                    train_current_pos = self.trains[key].get_train_position()
                    last_block = self.trains[key].get_last_block()
                    if train_current_pos == 0 and last_block == 57:
                        position = self.trains[key].get_train_position()
                        self.block_list[position].set_occupancy(False)
                        self.delete_train(key)
                        return

                    #get trains position
                    train_position = self.trains[key].get_train_position()
                    self.block_list[train_position].set_occupancy(True)
                    #----
                    #
                    # GET TRAIN SPEED FROM TRAIN HERE
                    #
                    #---------
                    # send current suggested speed to train
                    self.trains[key].tr_to_tm.send_suggested_speed(self.block_list[train_position].get_suggested_speed())

                    # get current train speed
                    train_speed = copy.deepcopy(self.trains[key].get_train_speed())
                    #print("Track Model Train cycle speed: " + str(train_speed))
                    #check block authority every update and set it to the trains authority
                    block_authority = copy.deepcopy(self.block_list[train_position].get_authority())
                    self.trains[key].tr_to_tm.send_authority(block_authority)
                    self.trains[key].set_train_authority(block_authority)

                    #train authority is separate
                    #train_authority = self.trains[key].get_train_authority()
                    #get latest times
                    current_time = self.get_current_time()
                    last_time = copy.deepcopy(self.trains[key].get_block_last_cycle_time())
                    self.trains[key].set_block_last_cycle_time(current_time)

                    #if(train_authority <= 0):
                    #    train_authority = 0

                    if(train_speed >= 0): #modified 12/15/23 "and train_authority > 0"

                        #print(current_time)
                        #print(last_time)
                        #delta_time = current_time - last_time
                        #delta_time = delta_time/1000
                        delta_time = self.get_current_time()
                        #print(delta_time)

                        #get train speed of block
                        train_speed = copy.deepcopy(self.trains[key].get_train_speed())
                        distance_travelled = copy.deepcopy(self.trains[key].get_distance_travelled())
                        #set the distance travelled to speed * change in time
                        self.trains[key].set_distance_travelled(distance_travelled + (train_speed * delta_time))

                        #print("--------------------------------------")
                        #print("train speed: " + str(train_speed))
                        #print("delta_time: " + str(delta_time))
                        #get the value we just set
                        distance_travelled = copy.deepcopy(self.trains[key].get_distance_travelled())

                        #get the block length
                        block_length = self.block_list[train_position].get_block_length()
                        #get the time it takes to travel the block
                        #time_to_travel = copy.deepcopy(self.trains[key].get_time_to_travel())
                        # reset block entry tim
                        try:
                            if ((block_length-distance_travelled) <= 0):
                                self.update_train_block(key)
                            else:
                                #print("Total distance travelled: "+ str(block_length - distance_travelled))
                                pass
                            #time = block_length - (speed * time) / train speed | = time travelled
                            #time = (float(block_length) - float(distance_travelled))/float(train_speed)
                            #subtract the time it takes to travel the block remaining by absolute value of time
                            #time_to_travel = time_to_travel - abs(time)
                            #time_to_travel = time_to_travel - abs(time)
                            #print(f"ttt = {time_to_travel}, spd = {train_speed}")
                            #print("time: " + str(time))
                            #print("time to travel: " + str(time_to_travel))
                            #if time_to_travel <= 0:
                            #    self.update_train_block(key)                        
                            #else:
                            #    self.trains[key].set_time_to_travel(time_to_travel)
                        #in case there is a division error
                        except ZeroDivisionError:
                            pass
                            #print("ZeroDivisionError")
                            #self.update_train_block(key)
                        #print(time)

                else:
                    return

    def update_train_block(self, train_id:int):
        #perform checks on the blocks to check if the train is on a block with a switch.
        #if the train is, then it increments to the next block the switch connects to.
        #else increment block, or decrement block by 1. based on train direction.
        #print("-----------------------------------------------------------------")
        #print("entered new block")
        #get block enter time, and set the last cycle time
        
        #print("IN UPDATE TRAIN BLOCK FUNCTION")
        #print("--------------------------------")
        bypass = False
        
        self.trains[train_id].set_block_enter_time(self.get_current_time())
        self.trains[train_id].set_block_last_cycle_time(self.get_current_time())
        
        #get the train current position
        train_current_pos = self.trains[train_id].get_train_position()
        train_direction = self.trains[train_id].get_direction()
        self.trains[train_id].set_distance_travelled(0)
        self.trains[train_id].set_time_to_travel(self.block_list[train_current_pos].get_time_to_travel())
        # self.trains[train_id].tr_to_tm.send_polarity_change(bool(self.block_list[train_current_pos].get_polarity()))
        #if the train is moved onto a block with a station set the train on station flag
        if(self.block_list[train_current_pos].stations != None):
            self.trains[train_id].set_train_in_station(True)
            #self.ticket_sales(train_current_pos, train_id)
        else:
            self.trains[train_id].set_train_in_station(False)

        #print("old train position: " +str(train_current_pos)) 
        #print("train direction: " + str(train_direction))

        #check if train is currently on a switch block
        switch_exists = self.train_check_for_switch(train_id)
            
        if(self.block_list[train_current_pos].stations != None):
            #pull the beacons and place the beacon into the train
            beacon1 = copy.deepcopy(self.block_list[train_current_pos].get_station_beacon1())
            beacon2 = copy.deepcopy(self.block_list[train_current_pos].get_station_beacon2())
            # separate the beacon data into parts if needed
            
            self.trains[train_id].set_train_beacon1(beacon1)
            self.trains[train_id].set_train_beacon2(beacon2)
            #self.trains[train_id].tr_to_tm.send_beacon_package(beacon1,beacon2)


            #Split beacon 1 that has the information into directions
            beacon = beacon1
            beacon1 = beacon[0]
            beacon2 = beacon[1]

            #print("station beacon1: " + str(beacon1))
            #print("station beacon2: " + str(beacon2))
            #if beacon1 == ""
            #Based on text in beacon, change train direction

            if(beacon1 != None and beacon2 != None):
                if(train_direction == 0):
                    if(isinstance(beacon1[0], str)):

                        if(beacon1[0] == "Dir 1"):
                            #print("Changing direction to 1")
                            self.trains[train_id].set_train_direction(1)
                        else:
                            #print("Changing direction to 0")
                            self.trains[train_id].set_train_direction(0)
                else:
                    if(isinstance(beacon2[0], str)):
                        if (beacon2[0] == "Dir 0"):
                            #print("Changing direction to 0")
                            self.trains[train_id].set_train_direction(0)
                        else:
                            #print("Changing direction to 1")
                            self.trains[train_id].set_train_direction(1)                


            # Get the new direction
            train_direction = self.trains[train_id].get_direction()
            #set the beacon position lists pulled from the beacon
            if(train_direction == 0):
                if(beacon1 != None):
                    #print("new beacon1: " + str(beacon1[4]))
                    self.trains[train_id].set_direction0_list(beacon1[3])
                    #print("new dir0 list: "+ str(self.trains[train_id].get_direction0_list()))
                    
            if(train_direction == 1):
                if(beacon2 != None):
                    #print("new beacon2: " +str(beacon2[4]))
                    self.trains[train_id].set_direction1_list(beacon2[3])
                    #print("new dir1 list: "+ str(self.trains[train_id].get_direction1_list()))
        elif (switch_exists == "switch_leg_b" or switch_exists == "switch_leg_c"):
            bypass = True
            
            if switch_exists == "switch_leg_b":
                switch_on = self.block_list[train_current_pos].get_block_switch_on()
                beacon = copy.deepcopy(self.block_list[switch_on].get_switch_beaconb())
                self.trains[train_id].tr_to_tm.send_beacon_package(beacon,None)
                #print("Beacon inside leg B: " + str(beacon))
                beacon1 = beacon[0]
                beacon2 = beacon[1]
                #print( "Beacon1 inside leg B: " + str(beacon1))
                #print( "Beacon2 inside leg B: " + str(beacon2))
                self.trains[train_id].set_train_beacon1(beacon1)
                self.trains[train_id].set_train_beacon2(beacon2)
                
                if beacon1[0] != "Error":
                    self.trains[train_id].set_direction0_list(beacon1[3])
                if beacon2[0] != "Error":
                    self.trains[train_id].set_direction1_list(beacon2[3])

            if switch_exists == "switch_leg_c":
                switch_on = self.block_list[train_current_pos].get_block_switch_on()
                beacon = copy.deepcopy(self.block_list[switch_on].get_switch_beaconc())
                self.trains[train_id].tr_to_tm.send_beacon_package(beacon, None)
                #print("Beacon inside leg C: " + str(beacon))
                beacon1 = beacon[0]
                beacon2 = beacon[1]
                #print( "Beacon1 inside leg C: " + str(beacon1))
                #print( "Beacon2 inside leg C: " + str(beacon2))
                self.trains[train_id].set_train_beacon1(beacon1)
                self.trains[train_id].set_train_beacon2(beacon2)
                
                if beacon1[0] != "Error":
                    self.trains[train_id].set_direction0_list(beacon1[3])
                else:
                    self.trains[train_id].set_direction0_list(None)
                    
                if beacon2[0] != "Error":
                    self.trains[train_id].set_direction1_list(beacon2[3])
                else:
                    self.trains[train_id].set_direction1_list(None)

        '''
        #if train is on a switch block and last block is also a block with a switch
        if switch_exists == "switch_corner_block" or switch_exists == "switch_leg_b" or switch_exists == "switch_leg_c":
            last_block = self.trains[train_id].get_last_block()
            switch_on_last = self.block_list[last_block].get_block_switch_on()
            if switch_on_last != None:
                corner = self.block_list[switch_on_last].get_switch_corner()
                leg_b = self.block_list[switch_on_last].get_switch_leg_b()
                leg_c = self.block_list[switch_on_last].get_switch_leg_c()
                if self.trains[train_id].get
                #print("block: "+ str(train_current_pos) + " Leg_b: " + str(leg_b) + " Leg_c: " + str(leg_c)  + " Corner: " + str(corner))
                # Can't remember why this is here.......... oof
        '''        

        #Get block movement data
        train_dir0_list = self.trains[train_id].get_direction0_list()
        train_dir1_list = self.trains[train_id].get_direction1_list()
        #print("Train Direction: " + str(self.trains[train_id].get_direction()))
        #print("train dir0 list: " + str(train_dir0_list))
        #print("train dir1 list: " + str(train_dir1_list))
        #et current train positions
        train_current_pos = self.trains[train_id].get_train_position()
            
        #update train position using the array in the beacons
        if (train_direction == 0):
            #if train position is the same as the first variable delete it
            #set the next value in the array as the current position of the train
            if(train_current_pos == train_dir0_list[0]):
                #print("Inside Train Direction 0")
                self.trains[train_id].set_last_block(train_dir0_list[0])
                old_pos = train_current_pos
                train_dir0_list.pop(0)
                if len(train_dir0_list) == 0:
                    self.move_train_to_switch_connection(train_id, switch_exists)
                    self.set_occupancy(old_pos, False)
                    #return    
                else:
                    train_current_pos = train_dir0_list[0]
                    self.trains[train_id].set_train_position(train_current_pos)
                    self.set_occupancy(train_current_pos, True)
                    self.set_occupancy(old_pos, False)
                
        if train_direction == 1:
            #print("Inside Train Direction 1")
            if(train_current_pos == train_dir1_list[0]):
                self.trains[train_id].set_last_block(train_dir1_list[0])
                old_pos = train_current_pos
                train_dir1_list.pop(0)
                if len(train_dir1_list) == 0:
                    self.move_train_to_switch_connection(train_id, switch_exists)
                    self.set_occupancy(old_pos, False)
                    #return
                else:
                    train_current_pos = train_dir1_list[0]
                    self.trains[train_id].set_train_position(train_current_pos)
                    self.set_occupancy(train_current_pos, True)
                    self.set_occupancy(old_pos, False)
        
        #check if train was moved to a switch block, if it was send beacon data
        if bypass == True:
            switch_exists = self.train_check_for_switch(train_id)
            if switch_exists == "switch_leg_b" or switch_exists == "switch_leg_c":
                if switch_exists == "switch_leg_b":
                    #if switch exists, get switch block
                    #use switch block to get beacon b
                    switch_on = self.block_list[train_current_pos].get_block_switch_on()

                    beacon = self.block_list[switch_on].get_switch_beaconb()
                    self.trains[train_id].tr_to_tm.send_beacon_package(beacon,None)
                    beacon1 = beacon[0]
                    beacon2 = beacon[1]
                    self.trains[train_id].set_train_beacon1(beacon1)
                    self.trains[train_id].set_train_beacon2(beacon2)
                    
                if switch_exists == "switch_leg_c":
                    #if switch exists, get switch block
                    #use switch block to get beacon b
                    switch_on = self.block_list[train_current_pos].get_block_switch_on()
                    self.trains[train_id].tr_to_tm.send_beacon_package(beacon,None)
                    beacon = self.block_list[switch_on].get_switch_beaconc()
                    beacon1 = beacon[0]
                    beacon2 = beacon[1]
                    self.trains[train_id].set_train_beacon1(beacon1)
                    self.trains[train_id].set_train_beacon2(beacon2)
                    
        
        #print("New train position: " +str(train_current_pos))
        #Send polarity of new block to train
                    
        self.trains[train_id].tr_to_tm.send_polarity_change(bool(self.block_list[train_current_pos].get_polarity()))
        if self.block_list[self.trains[train_id].get_train_position()].stations != None:
            try: self.trains[train_id].tr_to_tm.send_beacon_package(beacon, None)
            except:pass


    def train_check_for_switch(self, train_id:int):
        #get train position
        #print("in Train Check for switch function")
        train_position = self.trains[train_id].get_train_position()
        #get switch components
        corner = self.block_list[train_position].get_switch_corner()
        leg_b = self.block_list[train_position].get_switch_leg_b()
        leg_c = self.block_list[train_position].get_switch_leg_c()

        #check if the train is on a switch component
        if (corner != None or leg_b != None or leg_c != None):
            #if train is on a corner block return corner block
            if (corner != None and train_position == corner):
                return "switch_corner_block"
            elif(leg_b != None and train_position == leg_b):
                #Return that the train is on leg B
                return "switch_leg_b"
            elif(leg_c != None and train_position == leg_c):
                return "switch_leg_c"
            else:
                return "no switch component"
        else:
            #if there is no switch component pass
            return "no switch component"

    def move_train_to_switch_connection(self, train_id:int, component:str):
        # check the connected status of the switch
        # move the train to the connected block
        # if the train is on a switch component block, push tfhe new beacon data to the train

        #get train position and set occupancy to false
        train_position = self.trains[train_id].get_train_position()
        self.block_list[train_position].set_occupancy(False)
        self.trains[train_id].set_last_block(train_position)
        
        #get switch components
        corner = self.block_list[train_position].get_switch_corner()
        leg_b = self.block_list[train_position].get_switch_leg_b()
        leg_c = self.block_list[train_position].get_switch_leg_c()

        #if train is on a corner block, move train to the connected block
        if (component == "switch_corner_block"):
            #get block switch is on
            switch_block = self.block_list[train_position].get_block_switch_on()
            #use switch block to get connection
            connected_block = self.block_list[switch_block].get_connected_to()
            #move the train to the connection block and send new polarity
            new_train_position = connected_block
            self.trains[train_id].set_train_position(new_train_position)
            self.trains[train_id].tr_to_tm.send_polarity_change(bool(self.block_list[new_train_position].get_polarity()))
            #if the train moved to leg_B push that beacon to train
            beaconb = self.block_list[switch_block].get_switch_beaconb()
            #if train moved to leg_C push that beacon to the train
            beaconc = self.block_list[switch_block].get_switch_beaconc()

            if new_train_position == leg_b:
                #print("Train on leg B from corner block")
                #send train beacons to train
                self.trains[train_id].set_train_beacon1(beaconb[0])
                self.trains[train_id].set_train_beacon2(beaconb[1])
                self.trains[train_id].tr_to_tm.send_beacon_package(beaconb, None)
                self.block_list[new_train_position].set_occupancy(True)
                #set train direction list
                self.trains[train_id].set_direction0_list(beaconb[0])
                self.trains[train_id].set_direction1_list(beaconb[1])
                dir0_list_temp = self.trains[train_id].get_direction0_list()
                dir1_list_temp = self.trains[train_id].get_direction1_list()
                if self.trains[train_id].get_train_position() == dir0_list_temp[0]:
                    dir0_list_temp.pop(0)
                    self.trains[train_id].set_direction0_list(dir0_list_temp)
                
                if self.trains[train_id].get_train_position() == dir1_list_temp[0]:
                    dir1_list_temp.pop(0)
                    self.trains[train_id].set_direction0_list(dir1_list_temp) 
                
            elif new_train_position == leg_c:
                #print("Train on leg C from corner block")
                #send beacons to train
                self.trains[train_id].set_train_beacon1(beaconc[0])
                self.trains[train_id].set_train_beacon2(beaconc[1])
                self.trains[train_id].tr_to_tm.send_beacon_package(beaconc, None)
                self.block_list[new_train_position].set_occupancy(True)
                #set train direction list
                self.trains[train_id].set_direction0_list(beaconc[0])
                self.trains[train_id].set_direction1_list(beaconc[1])
            else:
                pass
            
        elif(component == "switch_leg_b"):
            #print("Train train on leg B")
            #if train is on legb, if it the switch is connected to leg b, move train to this block
            #else train is destroyed
            #get block switch is on and it's connection
            switch_block = self.block_list[train_position].get_block_switch_on()
            connected_block = self.block_list[switch_block].get_connected_to()
            #move the train to the corner block
            self.block_list[train_position].set_occupancy(False)
            if connected_block == leg_b:
                self.trains[train_id].set_last_block(train_position)
                new_train_position = corner
                self.block_list[new_train_position].set_occupancy(True)
                #Send polarity of new block to train
                self.trains[train_id].tr_to_tm.send_polarity_change(bool(self.block_list[new_train_position].get_polarity()))
                #print("Train on corner block")
            else:
                #self.delete_train(train_id)
                raise Exception("Train de-railed, no switch connection to switch leg B")

        elif(component == "switch_leg_c"):
            #print("Train on leg C")
            #if train is on a leg c block get beacon associated with leg C
            #get block switch is on
            switch_block = self.block_list[train_position].get_block_switch_on()
            #use switch block to get connection
            connected_block = self.block_list[switch_block].get_connected_to()
            #print("connected block: " + str(connected_block))
            #print("corner block: " + str(corner))
            #set block occupancy to false
            self.block_list[train_position].set_occupancy(False)
            if connected_block == leg_c:
                self.trains[train_id].set_last_block(train_position)
                #move the train to the connection block
                new_train_position = corner
                self.block_list[new_train_position].set_occupancy(True)
                #Send polarity of new block to train
                self.trains[train_id].tr_to_tm.send_polarity_change(bool(self.block_list[new_train_position].get_polarity()))
                #print("Train on corner block")
            else:
                #self.delete_train(train_id)
                raise Exception("Train de-railed, no switch connection to switch leg c")

        dir0_list = self.trains[train_id].get_direction0_list()
        dir1_list = self.trains[train_id].get_direction1_list()
        train_direction = self.trains[train_id].get_direction()
        train_position = self.trains[train_id].get_train_position()
        if (train_direction == 0):
            if(train_position == dir0_list[0]):
                dir0_list.pop(0)
                train_position = dir0_list[0]
                self.trains[train_id].set_train_position(train_position)
        else:
            if(train_position == dir1_list[0]):
                dir1_list.pop(0)
                train_position = dir0_list[0]
                self.trains[train_id].set_train_position(train_position)

        self.set_occupancy(train_position, True)



    #-----------------------------------------------------------------
    # Train Set Operations
    #------------------------------------------------------------------
    
    def set_current_speed(self, train_id:int, speed:float):
        #print("train: "+ str(train_id) + " speed: " + str(speed))
        #print("authority" + str(self.trains[train_id].get_train_authority()))
        try:
            self.trains[train_id].set_train_speed(speed)
        except KeyError:
            pass

    def set_train_direction(self, train_id:int, direction:int):
        self.trains[train_id].set_train_direction(direction)

    def set_train_dist_travelled(self, train_id:int, distance:float):
        self.trains[train_id].set_distance_travelled(distance)
    
    def set_train_authority(self, train_id:int, authority:int):
        self.trains[train_id].set_train_authority(authority)
        
    def set_train_on_station(self, train_id:int, bool:bool):
        self.trains[train_id].sefdt_train_on_station(bool)
    
    def set_train_position(self, train_id:int, block:int):
        self.trains[train_id].set_train_position(block)
    
    def set_passengers(self, train_id:int, num_passengers:int):
        self.trains[train_id].set_passengers(num_passengers)
    
    #------------------------------------------------------------------
    # Train Get Operations
    #------------------------------------------------------------------
    def get_occupancy(self, block_id:int):
        return self.block_list[block_id].get_occupancy()

    def change_occupancy(self, block_id:int):
        self.block_list[block_id].change_occupancy()
        self.wayside_link.send_occupancies(self.__line_name, block_id, self.block_list[block_id].get_occupancy())

    def set_occupancy(self, block_id:int, boolean:bool):
        self.block_list[block_id].set_occupancy(boolean)
        self.wayside_link.send_occupancies(self.__line_name, block_id, boolean)

    def get_block_entry_time(self, train_id:int):
        return self.track_lights[train_id].get_block_entry_time()

    def get_train_direction(self, train_id:int):
        return self.trains[train_id].get_train_direction()
    
    def get_distance_travelled(self, train_id:int):
        return self.trains[train_id].get_distance_travelled()
    
    def get_train_on_station(self, train_id:int):
        return self.trains[train_id].get_train_on_station()
    
    def get_train_position(self, train_id:int):
        return self.trains[train_id].get_train_position()
    
    def get_train_authority(self, train_id:int):
        return self.trains[train_id].get_train_authority()
    
    def get_train_id(self, train_id:int):
        return self.trains[train_id].get_train_id()
    
    def get_train_line(self):
        return self.__line_name
    
    def get_passengers(self, train_id:int):
        return self.trains[train_id].get_passengers()
