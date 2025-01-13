# train doors class
class TrainDoors:     

    def __init__(self, left: bool, right: bool):
        self.left_door = left
        self.right_door = right

    #mutators
    def set_left_door(self, left: bool):
        self.left_door = left

    def set_right_door(self, right: bool):
        self.right_door  = right

    #accessors
    def get_left_door_state(self):
        return self.left_door 

    def get_right_door_state(self):
        return self.right_door