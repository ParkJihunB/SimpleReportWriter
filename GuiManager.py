import sys 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Manager import Manager

class GuiManager(QWidget):
    manager: Manager
    def __init__(self):
        super().__init__()
        self.manager = Manager()

        self.cb_project = self.CreateCombo(self.manager.GetProjectList(),None)
        self.cb_project.setCurrentText(self.manager.selected_project)
        
        current_sub_project = self.manager.GetSubProjectList(self.cb_project.currentText())
        self.tb_sub_proejct_view = self.CreateTextBrowser(current_sub_project)
        #서브 프로젝트랑 함께 업데이트 하는 함수랑 연결되는데 서브 프로젝트 ui 만들기도 전에 함수 연결할 수가 없음
        self.cb_project.currentIndexChanged.connect(self.cb_Project) 

        project_vbox = QVBoxLayout()
        project_vbox.addWidget(self.cb_project)
        project_vbox.addWidget(self.tb_sub_proejct_view)

        self.tb_result = self.CreateTextBrowser([""])
        self.btn_write = self.CreatePushBtn("Write",self.btn_Write)
        self.btn_clear = self.CreatePushBtn("Clear",self.tb_result.clear)

        result_func_hbox = QHBoxLayout()
        result_func_hbox.addWidget(self.btn_write)
        result_func_hbox.addWidget(self.btn_clear)

        result_vbox = QVBoxLayout()
        result_vbox.addWidget(self.tb_result)
        result_vbox.addLayout(result_func_hbox)

        layout = QHBoxLayout()
        layout.addLayout(project_vbox,stretch=2)
        layout.addLayout(result_vbox,stretch=3)
        self.setLayout(layout)

    #매니저와 연결되는 함수들
    def btn_Write(self): 
        self.tb_result.append(self.manager.btn_Write())
        self.tb_result.append(self.manager.btn_Write())
        self.tb_result.append(self.manager.btn_Write())

    def cb_Project(self): 
        self.manager.cb_SelectProject(self.cb_project.currentText())
        self.sub_project_update(self.manager.GetSubProjectList(self.cb_project.currentText()))
    
    def dl_project_open(self):
        self.dl_project.setWindowModality(Qt.WindowModality.ApplicationModal)
        self.le_proejct.setText(self.manager.selected_project)
        self.dl_project.show()

    #그 외 gui 함수
    def sub_project_update(self,sub_project_list:list):
        self.tb_sub_proejct_view.clear()
        for item in sub_project_list: self.tb_sub_proejct_view.append(item)

    #gui 전용 helper function
    def CreatePushBtn(self, name, func):
        btn = QPushButton(name,self)
        btn.clicked.connect(func)
        return btn
    
    def CreateCombo(self, items:list, func):
        combo = QComboBox(self)
        for item in items: combo.addItem(item)
        if func is not None: combo.currentIndexChanged.connect(func)
        return combo
    
    def CreateTextBrowser(self, contents:list):
        tb = QTextBrowser()
        for item in contents: tb.append(item)
        return tb
    
app = QApplication(sys.argv)
win = GuiManager()
win.show()
app.exec_()