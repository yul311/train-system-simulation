
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)

        self.setFixedSize(QSize(400, 300))

        self.setCentralWidget(button)
    def the_button_was_clicked(self):
        print("The button wsa pressed")


app = QApplication([])

app.setStyle('Windows')
window = MainWindow()

window.show()

app.exec()