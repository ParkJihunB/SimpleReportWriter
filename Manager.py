from JsonManager import JsonManager
from Writer import Writer

#gui 와 Writer 프로그램을 이어주는 메인 프로그램
class Manager:
    dataM: JsonManager
    writer: Writer
    selected_project = ""
    
    def __init__(self) -> None:
        self.dataM = JsonManager()
        self.writer = Writer()
        self.selected_project = self.dataM.GetSelectedProejct()

    def btn_Write(self): #TODO: 나중에 Writer에 멤버 변수로 있는 dataM 없애버릴것
        project_suffix = self.writer.GetRandomValue(self.dataM.GetProejct()[self.selected_project])
        content_prefix = self.writer.GetRandomValue(self.dataM.GetContentPrefix())
        content = self.writer.GetRandomValue(self.dataM.GetContent())
        act = self.writer.GetRandomValue(self.dataM.GetAct())
        act_suffix = self.writer.GetRandomValue(self.dataM.GetActSuffix())
        result = self.writer.LookOverResult(self.selected_project+" "+project_suffix+content_prefix+content+act+act_suffix)
        return result

    def cb_SelectProject(self, selected:str):
        self.selected_project = selected
        self.dataM.SaveSelectedProject(selected)

    def btn_CreateProejct(self,new_project:str): pass
    def btn_EditProejct(self, project: str, new_project): pass
    def btn_DeleteProejct(self,project:str): pass

    def GetProjectList(self) -> list:
        return self.dataM.data[self.dataM.PROJECT]
    
    def GetSubProjectList(self, selected_project="")->list:
        #if selected_project == "": selected_project = list(self.dataM.data[self.dataM.PROJECT].keys())[0]
        return self.dataM.data[self.dataM.PROJECT][selected_project]