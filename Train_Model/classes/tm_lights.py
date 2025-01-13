# train light class
class TrainLights:     

    def __init__(self, internal: bool, external: bool):
        self.internal_light = internal
        self.external_light = external

    #mutators
    def set_internal_lights(self, internal: bool):
        self.internal_light = internal

    def set_external_lights(self, external: bool):
        self.external_light  = external

    #accessors
    def get_internal_lights_state(self):
        return self.internal_light
    
    def get_external_lights_state(self):
        return self.external_light