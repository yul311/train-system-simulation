# train failure class
class TrainFailures:     

    def __init__(self, engine: bool, brake: bool, signal: bool):
        self.engine_failure = engine
        self.brake_failure = brake
        self.signal_pickup_failure = signal

    #mutators
    def set_engine_failure(self):
        self.engine_failure = True

    def set_brake_failure(self):
        self.brake_failure = True

    def set_signal_pickup_failure(self):
        self.signal_pickup_failure  = True

    def reset_faults(self):
        self.engine_failure = False
        self.brake_failure = False
        self.signal_pickup_failure = False

    #accessors
    def get_engine_failure_state(self):
        return self.engine_failure 

    def get_brake_failure_state(self):
        return self.brake_failure
    
    def get_signal_pickup_failure_state(self):
        return self.signal_pickup_failure 