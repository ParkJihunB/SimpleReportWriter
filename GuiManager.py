import sys 
from PyQt5.QtWidgets import *

class GuiManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 300)

        btn1 = QPushButton("Button1")
        btn2 = QPushButton("Button2")

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

app = QApplication(sys.argv)
win = GuiManager()
win.show()
app.exec_()