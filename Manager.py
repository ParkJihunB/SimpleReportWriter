from JsonManager import JsonManager
from Writer import Writer
from Project import Project
from Content import Content
from Act import Act

#gui 와 Writer 프로그램을 이어주는 메인 프로그램
class Manager:
    dataM: JsonManager
    writer: Writer
    selected_project = ""
    
    def __init__(self) -> None:
        self.dataM = JsonManager()
        self.writer = Writer()
        self.selected_project = self.dataM.GetSelectedProejct()
        if not(self.selected_project in self.dataM.GetProject()):
            self.cb_SelectProject(list(self.dataM.GetProject().keys())[0])

        self.project = Project(self.dataM.GetProject())
        self.content = Content(self.dataM.GetContentPrefix(),self.dataM.GetContent(),None)
        self.act = Act(None, self.dataM.GetAct(),self.dataM.GetActSuffix())

    def btn_Write(self):
        print(self.project.GetRandomData())
        print(self.content.GetRandomData())
        print(self.act.GetRandomData())

    def cb_SelectProject(self, selected:str):
        self.selected_project = selected
        self.dataM.SaveSelectedProject(selected)

    def GetProjectList(self) -> list:
        return self.dataM.data[self.dataM.PROJECT]
    
    def GetSubProjectList(self, selected_project="")->list:
        return self.dataM.data[self.dataM.PROJECT][selected_project]

m = Manager()
m.btn_Write()