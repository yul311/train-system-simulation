import dataclasses

from CTC.ui.ctc_ui_loader import CTCUI
@dataclasses.dataclass(frozen=False)
class OfficeToUI:
    ui: CTCUI
    def __init__(self,ui):
        self.ui=ui
        
    def update_block_table(self, line:str, block_id:int):
        self.ui.update_block_table_row(line, block_id)

    def send_error(self, error:str):
        self.ui.set_error(error)

    def update_trains(self, train_id:int):
        print("CTC: update trains called")
        self.ui.update_scheduled_table(train_id)
        self.ui.update_dispatched_table(train_id)
        self.ui.update_train_info()
    
    def update_train_info(self):
        self.ui.update_train_info()

    def update_ticket_sales(self, tickets:int):
        self.ui.update_ticket_sales(tickets)