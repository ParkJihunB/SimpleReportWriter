import json




class JsonManager:
    PROJECT = "Project"
    CONTENT_PREFIX = "Content_Prefix"
    CONTENT = "Content"
    ACT = "Act"
    ACT_SUFFIX = "Act_Suffix"
    data: None

    def __init__(self):
        self.LoadData()

    def LoadData(self):
        with open('realdata.json',encoding='UTF8') as f:
            self.data = json.load(f)

    def SaveData(self):
        pass

    #TODO: 프로젝트 관리(수정/추가/삭제)
    def AddProject(self, project):
        pass
    def DeleteProject(self, project):
        pass
    def EditProject(self, project):
        pass

    def PrintData(self):
        print(self.data)