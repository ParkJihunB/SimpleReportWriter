import json

class JsonManager:
    PROJECT = "Project"
    CONTENT_PREFIX = "Content_Prefix"
    CONTENT = "Content"
    ACT = "Act"
    ACT_SUFFIX = "Act_Suffix"

    data: None
    setting: None

    def __init__(self):
        self.LoadData()

    def LoadData(self):
        with open('data_.json',encoding='UTF8') as f:
            self.data = json.load(f)
        with open('setting.json',encoding='UTF8') as f:
            self.setting = json.load(f)

    def SaveSelectedProject(self, selected):
        self.setting["selected_project"] = selected
        with open("setting.json",'w',encoding='UTF8') as f:
            json.dump(self.setting, f, ensure_ascii=False)
    
    def GetSelectedProejct(self): return self.setting["selected_project"]
    def GetProject(self): return self.data[self.PROJECT]
    def GetContentPrefix(self): return self.data[self.CONTENT_PREFIX]
    def GetContent(self): return self.data[self.CONTENT]
    def GetAct(self): return self.data[self.ACT]
    def GetActSuffix(self): return self.data[self.ACT_SUFFIX]

    def PrintData(self):
        print(self.data)