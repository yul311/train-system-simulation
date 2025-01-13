
import dataclasses
from CTC.ctc_office import *

@dataclasses.dataclass(frozen = False)
class TrackCTCAPI:

    def __init__(self, ctc: any):
        self.ctc = ctc

    def send_ticket_sales(self, line:str ,ticket_sales:int):
        #NOTE: TO CTC
        #line:str is for telling ctc which line the tickets are to be added for
        #set ticket sales function needs modified to this purpose
        self.ctc.set_ticket_sales(line,ticket_sales)

        #print("tr -> ctc: tickets")