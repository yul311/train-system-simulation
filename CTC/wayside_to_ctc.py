import dataclasses

@dataclasses.dataclass(frozen=False)
class WaysideCTCAPI:
    
    def __init__(self, ctc: any):
        self.ctc = ctc
    
    def send_occupancies(self, node:int, block_id:int, occupancy:bool):
        #print("ws -> ctc: occupancy")
        self.ctc.set_occupancy(node, block_id, occupancy)
    
    def send_faults(self):
        pass
