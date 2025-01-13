import dataclasses
import inspect
import railway.rlines as rlines
from services.readdatabase import Database


@dataclasses.dataclass(frozen= False)
class testbench:
    
    green_line: rlines.rail_lines
    
    
    def __init__(self):
        green_line = rlines.rail_lines()
        self.run_tests()
        
    def run_tests(self):
        import inspect
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
        assert green_line.self.temp == 23
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
            assert green_line.get_blockID() == i  
        