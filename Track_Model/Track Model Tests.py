import dataclasses
import inspect
import traceback
import Track_Model.railway.rlines as rlines
from Track_Model.services.readdatabase import Database
import inspect

@dataclasses.dataclass(frozen= False)
class testbench:


    def __init__(self):
        print("initialize")
        self.run_tests()
        exit()
        
    def run_tests(self):
        print("run Tests")
        for name,method in inspect.getmembers(self, inspect.ismethod):
            if name[:5]=="test_":
                try:
                    method()
                except AssertionError as failure:
                    print(f"\033[1;31mFailed {name}: \033[0m\n{failure}")
                except Exception as err:
                    print(f"\033[1;31mInternal error in {name}: \033[0m\n{traceback.print_exc()}")
                else:
                    print(f"\033[1;32mPassed {name}\033[0m")
                    
    def test_build_rail(self):
        green_line = rlines.rail_lines("green")
        assert green_line.__line_name == "green"
        assert green_line.__num_blocks == 0
        assert green_line.__temperature == 23
        assert green_line.__heaters == False
        assert green_line.train_counter == 0
        
    def test_add_block(self):
        #Build track blocks
        green_line = rlines.rail_lines("green")
        for i in range(len(Database.greendatabase["blockNumbers"])):
            green_line.build_rail_blocks(Database.greendatabase["blockNumbers"][i],Database.greendatabase["Sections"][i],
                                    Database.greendatabase["Length"][i], Database.greendatabase["Elevation"][i],
                                    Database.greendatabase["cumulativeElevation"][i],
                                    Database.greendatabase["Grade"][i], Database.greendatabase["maxSpeed"][i]*.277778,
                                        False, False, Database.greendatabase["polarity"][i])
        
        for i in range(len(green_line.block_list)):
            assert green_line.get_blockID() == Database.greendatabase["blockNumbers"][i]
            assert green_line.get_blockSection() == Database.greendatabase["Sections"][i]
            assert green_line.get_blockLength() == Database.greendatabase["Length"][i]
            assert green_line.get_cumulative_elevation() == Database.greendatabase["cumulativeElevation"][i]
            assert green_line.get_blockGrade() == Database.greendatabase["Grade"][i]
            assert green_line.get_max_speed() == Database.greendatabase["maxSpeed"][i]*.277778
            assert green_line.get_polarity() == Database.greendatabase["polarity"][i]
            
    def test_add_block(self):
        #Build track blocks
        green_line = rlines.rail_lines("green")
        for i in range(len(Database.greendatabase["blockNumbers"])):
            green_line.build_rail_blocks(Database.greendatabase["blockNumbers"][i],Database.greendatabase["Sections"][i],
                                    Database.greendatabase["Length"][i], Database.greendatabase["Elevation"][i],
                                    Database.greendatabase["cumulativeElevation"][i],
                                    Database.greendatabase["Grade"][i], Database.greendatabase["maxSpeed"][i]*.277778,
                                        False, False, Database.greendatabase["polarity"][i])
        
        green_line.add_train()
        assert green_line.train_counter == 1
        assert green_line.trains[1].get_trainID() == 1
        assert green_line.trains[1].get_trainLine() == "green"
        assert green_line.trains[1].get_trainBlock() == 0
        assert green_line.trains[1].get_trainSpeed() == 0
        assert green_line.trains[1].get_trainAuthority() == 0
        assert green_line.trains[1].get_trainPassengers() == 0
        assert green_line.trains[1].get_position() == 0
        assert green_line.trains[1].get_trainDirection() == 0