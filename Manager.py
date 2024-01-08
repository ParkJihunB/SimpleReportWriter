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
        if not(self.selected_project in self.dataM.GetProejct()):
            self.cb_SelectProject(list(self.dataM.GetProejct().keys())[0])

    def btn_Write(self): pass
        # project_suffix = self.writer.GetRandomValue(self.dataM.GetProejct()[self.selected_project])
        # content_prefix = self.writer.GetRandomValue(self.dataM.GetContentPrefix())
        # content = self.writer.GetRandomValue(self.dataM.GetContent())
        # act = self.writer.GetRandomValue(self.dataM.GetAct())
        # act_suffix = self.writer.GetRandomValue(self.dataM.GetActSuffix())
        # result = self.writer.LookOverResult(self.selected_project+" "+project_suffix+content_prefix+content+act+act_suffix)
        # return result

    def cb_SelectProject(self, selected:str):
        self.selected_project = selected
        self.dataM.SaveSelectedProject(selected)

    def GetProjectList(self) -> list:
        return self.dataM.data[self.dataM.PROJECT]
    
    def GetSubProjectList(self, selected_project="")->list:
        return self.dataM.data[self.dataM.PROJECT][selected_project]