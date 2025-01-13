import sys
from output import *
import numpy as np
import os
import pandas




if __name__=="__main__":
    
    app = QApplication(sys.argv)
    form = Ui_MainWindow()
    form.show()
    sys.exit(app.exec())