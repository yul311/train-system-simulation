import os,sys
from ctc_objects import *


edge_graph = {
    "Red": construct_edge_graph(red_adjmat),
    "Green": construct_edge_graph(green_adjmat)
}
DATA_PATH = os.path.join(os.getcwd(),"Other","data","Track Layout & Vehicle Data vF2.xlsx")

GREEN_DATA_PATH = os.path.join(os.getcwd(),"Track_Model","data","greenline.xlsx")
#print(GREEN_DATA_PATH)
b = {
    #"Green": construct_block_list_2(GREEN_DATA_PATH)
}
#print(b)
#print((b["Green"][0].section))



red_data = pandas.read_excel(DATA_PATH, sheet_name=2)
green_data = pandas.read_excel(DATA_PATH, sheet_name=3)
blocks = {
    "Red": construct_block_list(red_data, "Red"),
    "Green": construct_block_list(green_data, "Green")
}
blocks["Red"][0] = Block(
    id=0,
    line="Red",
    section="",
    speed_limit = 30/3.6,
    infrastructure = "Yard",
    station=None,
    occupied=False,
    maintenance=False,
    switch=None,
    authority=0,
    suggested_speed=0,
    length=50
)
'''
for id, block in blocks["Green"].items():
    other = vars(b['Green'][id])
    this = vars(block)
    #print(other)
    #print(this)
    for (var,val) in this.items():
        #print(f"{var}, {val}")
        if val != other[var]:
            print(f"{id}: {var}: {val} - {other[var]}")
'''
#print(edge_graph["Green"])
#for (key, item) in edge_graph["Green"].items():
#    print(key)

path_restrictions = {
    "Red": {
        27: [76],
        33: [32],
        38: [71],
        44: [43],
        52: [66],
    }
    
}

def set_path(line:str, back:int, start:int, end:int) -> list:
    adj:list
    routes:list[list]
    current:list[int]
    backs = [[back]]
    queue = [[start]]
    if end == 0:
        path_restrictions[line][16] = [15]
    else:
        path_restrictions[line][16] = [1]
    while queue:
        #print(f"{queue}")
        path = queue.pop(0)
        node = path[len(path)-1]
        neighbors = edge_graph[line][node]
        back = backs.pop(0)
        print(f"{node} : Path:{path} \n Back:{back}")
        print(f"{node}: {neighbors}")
        for neighbor in neighbors:
            if node in path_restrictions[line].keys() and neighbor in path_restrictions[line][node]:
                continue
            
            if neighbor not in back:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                new_back = [node]
                #Makes sure the train will not go on around a switch and the train will not go backwards
                if blocks[line][neighbor].switch != None:
                    if node == blocks[line][neighbor].switch.primary:
                        new_back.append(blocks[line][neighbor].switch.secondary)
                    elif node == blocks[line][neighbor].switch.secondary:
                        new_back.append(blocks[line][neighbor].switch.primary)
                backs.append(new_back)
                if neighbor == end:
                    return new_path
    return [0]

def restrict_path(self, line, neighbor, node:int, back):

    return


#Testing
# 1 Testing Yard to 8 blocks in front of yard
# testing a straight line
#print(set_path("Green", 0, 0, 70))
# 2 Testing Yard to Dormont
# Straight line
#print(set_path("Green", 0, 0, 73))
# 3 Testing Dormont to other side of Dormont
# testing the switch logic
#print(set_path("Green", 72, 73, 105))
# 4 testing Dormont to Pioneer
#print(set_path("Green", 72, 73, 2))

#testing red line
#print(set_path("Red", 0, 0, 10))

#test path restriction
print(set_path("Red", 46, 45, 35))

#test all path restrictions
print(set_path("Red", 0, 0, 10))
print(set_path("Red", 9, 8, 0))
#print(blocks["Red"][27])