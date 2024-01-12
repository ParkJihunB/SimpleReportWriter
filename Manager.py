from JsonManager import JsonManager
from Project import Project
from Content import Content
from Act import Act

#gui 와 Writer 프로그램을 이어주는 메인 프로그램
class Manager:
    dataM: JsonManager
    selected_project = ""
    
    def __init__(self) -> None:
        self.dataM = JsonManager()
        #기존 데이터에서 이전에 선택했던 프로젝트를 가져온다
        self.selected_project = self.dataM.GetSelectedProejct()
        #데이터가 없을 경우(현재와 다를 경우) 가장 첫번째 프로젝트 가져온다
        if not(self.selected_project in self.dataM.GetProject()):
            self.cb_SelectProject(list(self.dataM.GetProject().keys())[0])

        self.project = Project(self.dataM.GetProject())
        self.content = Content(self.dataM.GetContentPrefix(),self.dataM.GetContent(),None)
        self.act = Act(None, self.dataM.GetAct(),self.dataM.GetActSuffix())

    def btn_Write(self):
        result = self.project.GetRandomData(self.selected_project)+" "
        result += self.content.GetRandomData()+" "
        result +=self.act.GetRandomData(self.content.current_belong)
        result = self.LookOverResult(result)
        return result

    #선택된 프로젝트 변경시 변경 내용 반영하고 json 데이터에 저장
    def cb_SelectProject(self, selected:str):
        self.selected_project = selected
        self.dataM.SaveSelectedProject(selected)

    def GetProjectList(self) -> list:
        return self.dataM.data[self.dataM.PROJECT]
    
    def GetSubProjectList(self, selected_project="")->list:
        return self.dataM.data[self.dataM.PROJECT][selected_project]

    #문장 점검(공백 없애기 등..)
    def LookOverResult(self, result: str):
        result = result.rstrip()
        result += "."
        return result.replace("  ", " ")

m = Manager()
m.btn_Write()