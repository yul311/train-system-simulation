# ================================================================================================================================
# component testbench
# ================================================================================================================================
import traceback
from Train_Model.classes.Train_Model import TrainModel

class TrainModelTB:
    
    def __init__(self):
        print("Start Test")
        self.run_tests()
        print("End Test")
        
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

    def test_train_model_set_authority(self):

        mod = TrainModel()

        correct = 100

        mod.set_authority(100)
        response = mod.authority

        assert correct==response, f"{correct} (correct authority) is not {response} (response authority)"

    def test_train_model_set_suggested_speed(self):

        mod = TrainModel()

        correct = 18.5

        mod.set_suggested_speed(18.5)
        response = mod.suggested_speed

        assert correct==response, f"{correct} (correct suggested speed) is not {response} (response suggested speed)"

    def test_train_model_set_ticket_sales(self):
        
        mod = TrainModel()

        correct = 40

        mod.set_ticket_sales(40)
        response = mod.num_passenger

        assert correct==response, f"{correct} (correct ticket sales) is not {response} (response ticket sales)"

    def test_train_model_set_block_change(self):
        
        mod = TrainModel()

        correct = 2

        mod.set_block_change(True)
        mod.set_block_change(True)
        response = mod.num_block_change

        assert correct==response, f"{correct} (correct number of block change) is not {response} (response number of block change)"

    def test_train_model_set_train_id(self):
        
        mod = TrainModel()

        correct = 4

        mod.set_train_id(4)
        response = mod.train_id

        assert correct==response, f"{correct} (correct train id) is not {response} (response train id)"

    def test_train_model_set_train_line(self):
        
        mod = TrainModel()

        correct = "Green"

        mod.set_train_line("Green")
        response = mod.train_line

        assert correct==response, f"{correct} (correct train line) is not {response} (response train line)"

    def test_train_model_set_commanded_speed(self):

        mod = TrainModel()

        correct = 18.5

        mod.set_commanded_speed(18.5)
        response = mod.commanded_speed

        assert correct==response, f"{correct} (correct commanded speed) is not {response} (response commanded speed)"

    def test_train_model_set_power_command(self):

        mod = TrainModel()

        correct = 120000

        mod.set_power_command(120000)
        response = mod.power_command

        assert correct==response, f"{correct} (correct power command) is not {response} (response power command)"

    def test_train_model_set_annoucement(self):

        mod = TrainModel()

        correct = "Station Pitty"

        mod.set_announcement("Station Pitty")
        response = mod.announcements

        assert correct == response, f"{correct} (correct announcements) is not {response} (response announcement)"

    def test_train_model_set_light(self):
        
        mod = TrainModel()

        correct_int = True
        correct_ext = True

        mod.set_light_commands(True, True)
        response_int = mod.lights.get_internal_lights_state()
        response_ext = mod.lights.get_external_lights_state()

        assert correct_int == response_int, f"{correct_int} (correct internal) is not {response_int} (response internal)"
        assert correct_ext == response_ext, f"{correct_ext} (correct external) is not {response_ext} (response external)"

    def test_train_model_set_door(self):
        
        mod = TrainModel()

        correct_left = True
        correct_right = True

        mod.set_door_commands(True, True)
        response_left = mod.doors.get_left_door_state()
        response_right = mod.doors.get_right_door_state()

        assert correct_left == response_left, f"{correct_left} (correct left) is not {response_left} (response left)"
        assert correct_right == response_right, f"{correct_right} (correct right) is not {response_right} (response right)"

    def test_train_model_set_emergency(self):

        mod = TrainModel()

        correct = True

        mod.set_emergency_command(True)
        response = mod.brakes.get_emergency_brake_state()

        assert correct==response, f"{correct} (correct e-brake) is not {response} (response e-brake)"

    def test_train_model_set_service(self):

        mod = TrainModel()

        correct = True

        mod.set_service_command(True)
        response = mod.brakes.get_service_brake_state()

        assert correct==response, f"{correct} (correct service brake) is not {response} (response service brake)"

    def test_train_model_set_temperature(self):

        mod = TrainModel()

        correct = 35

        mod.set_temperature_command(35)
        response = mod.temperature_command

        assert correct==response, f"{correct} (correct temperature command) is not {response} (response temperature command)"

    def test_train_model_set_block_data(self):

        mod = TrainModel()

        correctbg = 0.5
        correctunder = True
        correctlimit = 15

        mod.set_block_data(0.5, True, 15)
        responsebg = mod.block_Grade
        responseunder = mod.tunnel_underground
        responselimit = mod.speed_limit

        assert correctbg == responsebg, f"{correctbg} (correct block grade) is not {responsebg} (response block grade)"
        assert correctunder == responseunder, f"{correctunder} (correct under/tunnel) is not {responseunder} (response under/tunnel)"
        assert correctlimit == responselimit, f"{correctlimit} (correct limit) is not {responselimit} (response limit)"

    def test_train_model_force(self):

        mod = TrainModel()

        correct = 119395.73173253353

        mod.set_block_data(0.05, False, 40)
        mod.calc_total_mass()
        mod.set_power_command(120000)
        mod.calc_force()
        response = mod.force

        assert correct==response, f"{correct} (correct force) is not {response} (response force)"
    
    def test_train_model_accel(self):

        mod = TrainModel()

        correct = 0.5

        mod.set_block_data(0.05, False, 40)
        mod.calc_total_mass()
        mod.set_power_command(120000)
        mod.calc_force()
        mod.calc_acceleration()
        response = mod.acceleration

        assert correct==response, f"{correct} (correct acc) is not {response} (response acc)"

    def test_train_model_total_mass(self):

        mod = TrainModel()

        correct = 44306.69

        mod.set_ticket_sales(40)
        mod.calc_total_mass()
        response = mod.total_mass

        assert correct==response, f"{correct} (correct mass) is not {response} (response mass)"

    def test_train_model_current_temp(self):

        mod = TrainModel()

        correct = 30

        mod.set_temperature_command(35)
        mod.calc_current_temp
        response = mod.current_temperature

        assert correct==response, f"{correct} (correct) is not {response} (response)"