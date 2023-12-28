import sys 
from PyQt5.QtWidgets import *
from Manager import Manager

class GuiManager(QWidget):
    Manager: Manager
    def __init__(self):
        super().__init__()
        self.Manager = Manager()

        btn1 = self.CreatePushBtn("Write",self.btn_Write)
        btn2 = QPushButton("Button2")

        layout = QVBoxLayout()
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)

    def btn_Write(self):
        print("Write button")

    #gui 전용 helper function
    def CreatePushBtn(self, name, func):
        btn = QPushButton(name,self)
        btn.clicked.connect(func)
        return btn

app = QApplication(sys.argv)
win = GuiManager()
win.show()
app.exec_()