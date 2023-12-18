import json

PROJECT = "Project"
CONTENT = "Content"
ACT = "Act"
ADDITIONAL = "Additional"

class JsonManager:
    data: None

    def __init__(self):
        self.LoadData()
        self.PrintData()

    def LoadData(self):
        with open('data.json',encoding='UTF8') as f:
            self.data = json.load(f)

    def SaveData(self):
        pass

    def Get

    #TODO: 프로젝트 관리(수정/추가/삭제)
    def AddProject(self, project):
        pass
    def DeleteProject(self, project):
        pass
    def EditProject(self, project):
        pass

    def PrintData(self):
        print(self.data)